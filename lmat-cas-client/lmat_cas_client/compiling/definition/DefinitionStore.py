from abc import ABC
from collections import deque
from collections.abc import Iterable
from typing import MutableMapping

from attr import field, frozen
from lark import Tree
from sympy import Basic, Expr
from sympy.core.function import UndefinedFunction


@frozen
class AstDef:
    """
    Definition entry for a definition,
    which can be resolved from some parsed string (latex prob.) represented as the stored ast.
    """

    ast: Tree


@frozen
class SympyDef:
    """
    Definition entry for values defined as singular sympy expressions.
    """

    expr: Basic


@frozen
class AstFunDef:
    """
    Like AstDef but for an appliable function with a body and an uneavluated value.
    e.g. f(x) = x^2
          ^      ^
        unappl.  |
                body
    """

    body: Tree
    unapplied: Basic


@frozen
class SympyFunDef:
    """
    Like AstFunDef but for sympy Expr objects, instead of Lark trees.
    """

    body: Expr


@frozen
class SympyUndefFunDef:
    undef_fun: UndefinedFunction


type SymDefVal = AstDef | SympyDef
"""
UnionType representing all symbol-like definitions definable in a DefinitionStore
"""

type FunDefVal = AstFunDef | SympyFunDef | SympyUndefFunDef
"""
UnionType representing all function-like definitions definable in a DefinitionStore
"""


@frozen(slots=False)
class Definition(ABC):
    """
    Base "class" for all types storable in a DefinitionStore.
    All definitions must hold a set of dependencies they must need to be resolved,
    before their own value can be safely resolved.
    Note that extending this class, also requires implementing / extending an already existing Resolver,
    for the definition to be resolvable.
    """

    deps: frozenset[str] = field(kw_only=True, factory=frozenset, converter=frozenset)


@frozen
class SymbolDefinition(Definition):
    """
    Stores a symbol-like definition.
    i.e.
    x := ... some expression ...

    where 'some expression' can be resolved from value.
    """

    value: SymDefVal


@frozen
class FunctionDefinition(Definition):
    """
    Stores a function-like definition.
    i.e.
    f(x, y) := ... some expression ...

    where 'some expression' can be resolved from value,
    and (x, y) is stored in params.
    """

    value: FunDefVal
    params: tuple[str]


@frozen
class EmptyDefinition(Definition):
    """
    Stores an empty definition, which SHOULD NOT be resolvable.
    This is usefull for stuff like undefining already defined values.
    """

    pass


type DefinitionStore = MutableMapping[str, Definition]
"""
The DefinitionStore is any mapping between a set of definition id's (str keys) and a corresponding Definition type.
"""


class CyclicDependencyError(Exception):
    """
    Error thrown when a DefinitionStore has detected a cyclic dependency between a subset of Definitions.
    The problematic definitions are stored in the cyclic_dependencies field.
    """

    def __init__(self, cyclic_dependencies: frozenset[str], *args):
        super().__init__(*args)
        self.cyclic_dependencies = cyclic_dependencies


@frozen
class OrderedDeps:
    deps: tuple[str, ...]


@frozen
class CyclicDeps:
    deps: frozenset[str]


type DepsResolveResult = OrderedDeps | CyclicDeps


def resolve_dependencies(
    def_store: DefinitionStore, definition_names: Iterable[str]
) -> OrderedDeps | CyclicDeps:
    """
    produce a list containing all elements of 'definition_names', as well as their dependencies such that
    every name in the list, only depends on definitions to the left of it self.
    e.g.
    'x' depends on 'y' and 'z'
    'y' depends on 'z'
    'z' depends on nothing

    resolve_dependencies(('x', 'y', 'z')) produces ('z', 'y', 'x')

    first result is the status of the function call, True for success, False for failure.
    if True, the list returned is described above.
    if False, the list returned is a list of definition names, which have cyclic dependencies between eachother.

    Args:
        definition_names (Iterable[str])

    Returns:
        OrderedDeps | CyclicDeps: OrderedDeps on success, CyclicDeps on failure.
    """

    # The general strategy here is to first build a digraph 'G = (N, D)', where each node 'n E N' is a definition,
    # and each directed edge 'd E D', between two nodes, represents a dependency between those nodes.
    # 'G' is a subgraph of the entire digraph representing all definitions in the DefinitionStore.
    # The 'G' subgraph should be the connected subcomponent of this larger graph, which contains all definitions passed in 'definition_names'.
    # any edge 'd' in the graph 'G' points from the dependant node to the dependency node.
    # e.g.
    # 'x' depends on 'y' ==> ('n_y', 'n_x') E D
    #
    # this graph structure ensures the LR topological ordering of all nodes in 'G' corresponds with the
    # order required for definitions only to depend on other definitions to the left of itself.

    # build the dependency digraph 'G' (connected subcomponent) which contains all entries in the passed symbols list.
    # the graph is represented as an adjacency map.
    # an in-degree table, keeping track of the in-degrees of all nodes in 'G',
    # is also constructed, as it is needed later for constructing the topological ordering.

    definition_names = tuple(definition_names)

    dependency_graph: dict[str, set[str]] = {}
    in_deg_table: dict[str, int] = {}

    marked_definitions = set({})

    # construct 'G' by performing BFS from each name in definition_names,
    # this visits the connected subcomponent which 'G' should equal.

    for definition_name in definition_names:
        if definition_name in marked_definitions:
            continue

        dependency_graph[definition_name] = set()
        in_deg_table[definition_name] = 0
        marked_definitions.add(definition_name)

        visit_queue = deque({definition_name})

        while len(visit_queue) > 0:
            definition_name_vertex = visit_queue.popleft()

            if definition_name_vertex not in def_store:
                continue

            definition_node = def_store[definition_name_vertex]

            neighbours = definition_node.deps

            for neighbour_name in neighbours:
                if neighbour_name not in marked_definitions:
                    marked_definitions.add(neighbour_name)
                    dependency_graph[neighbour_name] = set()
                    in_deg_table[neighbour_name] = 0
                    visit_queue.append(neighbour_name)

                dependency_graph[neighbour_name].add(definition_name_vertex)
                in_deg_table[definition_name_vertex] += 1

    # construct topological order from 'G' by iteratively removing a source node (in-degree = 0)
    # from 'G' and placing it in topological_ordering, until 'G' is empty.

    topological_ordering = []

    source_definitions = deque(filter(lambda s: in_deg_table[s] == 0, dependency_graph))

    while len(source_definitions) > 0:
        source_definition = source_definitions.popleft()

        topological_ordering.append(source_definition)

        for neighbour_name in dependency_graph[source_definition]:
            in_deg_table[neighbour_name] -= 1

            if in_deg_table[neighbour_name] == 0:
                source_definitions.append(neighbour_name)

        del in_deg_table[source_definition]

    if in_deg_table != {}:
        # in_deg_table is not empty <==> graph is not a DAG <==> there is a cyclic dependency in the remaining vertices in the graph.
        return CyclicDeps(frozenset(in_deg_table.keys()))

    return OrderedDeps(tuple(topological_ordering))


def assert_acyclic_dependencies(
    def_store: DefinitionStore, definition_names: Iterable[str]
) -> tuple[str, ...]:
    """
    same as resolve_dependencies, but throws an exception if dependencies are cyclic.

    Args:
        definition_names (Iterable[str])

    Raises:
        CyclicDependencyError

    Returns:
        tuple[str]
    """
    match resolve_dependencies(def_store, definition_names):
        case OrderedDeps(deps):
            return deps
        case CyclicDeps(deps):
            raise CyclicDependencyError(
                deps,
                f"There is a cyclic dependency between the following definitions: {', '.join(deps)}",
            )
