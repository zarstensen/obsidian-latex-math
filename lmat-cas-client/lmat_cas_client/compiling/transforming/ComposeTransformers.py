from typing import override

from lark import Token, Transformer, Tree, Visitor
from lark.tree import Branch
from regex import Regex


class AstNamespacesRemover(Visitor):
    """
    Remove the given grammar namespaces from some AST.
    These namespaces are added when lark imports stuff from other files,
    e.g. %import a.rule_a is aliased to a__rule_a, however this confuses
    the parser, unless merge_transformers is used, but merge transformers
    does not allow for the transformers to cyclicly depend on each other.

    for this to work, the simplest solution is just to remove this namespace,
    ensure no collisions manually (rarely happens anyways), and combine all of the transformers
    into one big transformer, via. reflection (see compose_transformers).
    """

    def __init__(self, *namespaces: str):
        self._rem_regex = Regex(
            rf"^(_)?(?:(?:{'|'.join(namespace for namespace in namespaces)})__)+(.*)$"
        )

    @override
    def __default__(self, node: Tree):
        node.data = self._rem_regex.sub(r"\1\2", node.data)

        new_children: list[Branch] = []

        for child in node.children:
            match child:
                case Token():
                    new_children.append(
                        child.update(self._rem_regex.sub(r"\1\2", child.type))
                    )
                case _:
                    new_children.append(child)

        node.children = new_children
        return node


def compose_transformers(*transformers: Transformer):
    """
    Compose a series of transformers into a singular transformer,
    no namespaces are added to any of the transformers.

    rule handlers are prioritized from right to left,
    so if 2 rule handlers of the same name exists in the transformers list,
    the one in the transformer furthest to the right, is picked.
    """
    composed_transformer: Transformer = Transformer()

    for transformer in transformers:
        for method_name in dir(transformer):
            method = getattr(transformer, method_name)

            if not callable(method):
                continue

            if method_name.startswith("_") or method_name == "transform":
                continue

            setattr(composed_transformer, method_name, method)

    return composed_transformer
