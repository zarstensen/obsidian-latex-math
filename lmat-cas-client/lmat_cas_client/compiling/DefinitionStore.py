from abc import ABC, abstractmethod
from collections import deque
from copy import copy
from typing import Iterable, Optional, Self

from sympy import Expr


class Definition(ABC):
    """
    The abstract Definition class serves as a base class for all definition types managable by a DefinitionStore.
    A definition must at the very least provide a defined value in the context of a definition store,
    as well as being able to produce a set of dependencies, which this definition requires before it's defined value can be computed.

    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
    def dependencies(self) -> set[str]:
        """
        return a list of definition names which the current definition depends on.
        """
        pass

    @abstractmethod
    def defined_value(self, definition_store: 'DefinitionStore') -> Expr:
        """
        return the value this symbol has been defined to be,
        pulling values of dependencies from the given definition store.
        """
        pass


class FunctionDefinition(Definition):
    """
    The FunctionDefinition class is a specialized Definition,
    which allows a definition to define some variables, which arguemnts may be applied to, producing unique values.
    defined_value should in this case return a value representing the unapplied function itself,
    and applied_value should produce the output of the applied function.
    """
    def __init__(self, variables: Iterable[str] = [ ]):
        super().__init__()
        self._variables = tuple(variables)

    @property
    def variables(self) -> tuple[str]:
        """
        set of definition names, which will be replaced with the 'args' passed in applied_value.
        these should in most cases **NOT** be a part of the dependencies method output.
        """
        return self._variables


    @abstractmethod
    def applied_value(self, definition_store: 'DefinitionStore', args: Iterable[Definition] | None = None) -> Expr:
        """
        compute the output of the applied function given some args and a DefinitionStore to pull definitions from.
        args should be equal in length to variables, and variables[n] should be replaced with args[n] when computing the applied function.

        Args:
            definition_store (DefinitionStore): DefinitionStore to retreive dependent values from
            args (Iterable[Definition] | None, optional): args to be passed to the function. If None, args are set equal to variables. Defaults to None.

        Returns:
            Expr: applied value
        """
        pass


class CyclicDependencyError(Exception):
    """
    Error thrown when a DefinitionStore has detected a cyclic dependency between a subset of Definitions.
    The problematic definitions are stored in the cyclic_dependencies field.
    """
    def __init__(self, cyclic_dependencies: set[str], *args):
        super().__init__(*args)
        self.cyclic_dependencies = cyclic_dependencies

class DefinitionStore:
    """
    The DefinitionStore is responsible for storing a series of definitions, identifying them by a string key, known as a 'definition name'.
    """

    def __init__(self, definitions: dict[str, Definition] = { }):
        """
        Construct a DefinitionStore from the given map of definition names to their corresponding Definition objects

        Args:
            definitions (dict[str, Definition], optional): Defaults to { }.
        """
        self._definitions = dict()
        self._expr_cache = dict()

        for def_key, def_value in definitions.items():
            self.set_definition(def_key, def_value)

    def clone(self) -> Self:
        return DefinitionStore(self.get_definitions())

    def override(self, new_definitions: dict[str, Definition]) -> Self:
        """_summary_
        clone the current DefinitionStore and add the new definitions to the existing definitions in the old DefinitionStore.

        Args:
            new_definitions (dict[str, Definition]): definitions to override / add in the new DefinitionStore

        Returns:
            DefinitionStore
        """
        new_def_store = self.clone()

        for new_def_name, new_def in new_definitions.items():
            new_def_store.set_definition(new_def_name, new_def)

        return new_def_store

    def set_definition(self, definition_name: str, definition: Definition):
        self._definitions[definition_name] = definition
        # also clear cache here.
        self._expr_cache[definition_name] = dict()

    def get_definition(self, definition_name: str, *, default: Optional[Definition] = None) -> Optional[Definition]:
        return self._definitions.get(definition_name, default)

    def get_definitions(self) -> dict[str, Definition]:
        """
        creates a COPY of all definitions, only use to create new definition stores.

        Returns:
            dict[str, Definition]
        """
        return copy(self._definitions)

    def get_definition_names(self) -> set[str]:
        """
        retreive a set of all definition names currently tied to a definition in the DefinitionStore.

        Returns:
            set[str]
        """
        return set(self._definitions.keys())


    def resolve_dependencies(self, definition_names: Iterable[str]) -> tuple[bool, tuple[str]]:
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
            tuple[bool, tuple[str]]
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

        dependency_graph: dict[str, set[str]] = { }
        in_deg_table: dict[int, str] = { }

        marked_definitions = set({ })

        # construct 'G' by performing BFS from each name in definition_names,
        # this visits the connected subcomponent which 'G' should equal.

        for definition_name in definition_names:

            if definition_name in marked_definitions:
                continue

            dependency_graph[definition_name] = set()
            in_deg_table[definition_name] = 0
            marked_definitions.add(definition_name)

            visit_queue = deque({ definition_name })

            while len(visit_queue) > 0:

                definition_name_vertex = visit_queue.popleft()

                definition_node = self.get_definition(definition_name_vertex)

                if definition_node is None:
                    continue

                neighbours = definition_node.dependencies()

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

        topological_ordering = [ ]

        source_definitions = deque(filter(lambda s: in_deg_table[s] == 0, dependency_graph))

        while len(source_definitions) > 0:
            source_definition = source_definitions.popleft()

            topological_ordering.append(source_definition)

            for neighbour_name in dependency_graph[source_definition]:
                in_deg_table[neighbour_name] -= 1

                if in_deg_table[neighbour_name] == 0:
                    source_definitions.append(neighbour_name)

            del in_deg_table[source_definition]

        if in_deg_table != { }:
            # in_deg_table is not empty <==> graph is not a DAG <==> there is a cyclic dependency in the remaining vertices in the graph.
            return False, tuple(in_deg_table.keys())

        return True, tuple(topological_ordering)

    def assert_acyclic_dependencies(self, definition_names: Iterable[str]) -> tuple[str]:
        """
        same as resolve_dependencies, but throws an exception if dependencies are cyclic.

        Args:
            definition_names (Iterable[str])

        Raises:
            CyclicDependencyError

        Returns:
            tuple[str]
        """
        success, result = self.resolve_dependencies(definition_names)

        if success:
            return result

        raise CyclicDependencyError(result, f"There is a cyclic dependency between the following definitions: {', '.join(result)}")
