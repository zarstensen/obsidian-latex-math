from collections.abc import Iterable
from typing import Iterator, Optional, override

from lark import Token, Transformer, Tree, Visitor
from regex import Regex


class AstNamespacesRemover(Visitor):
    def __init__(self, *namespaces: str):
        self._rem_regex = Regex(
            rf"^(_)?(?:{'|'.join(namespace for namespace in namespaces)})__(.*)$"
        )

    def __default__(self, node: Tree):
        node.data = self._rem_regex.sub(r"\1\2", node.data)

        new_children = []

        for child in node.children:
            match child:
                case Tree():
                    new_children.append(child)
                case Token():
                    new_children.append(
                        child.update(self._rem_regex.sub(r"\1\2", child.type))
                    )

        node.children = new_children
        return node


def compose_transformers(*transformers: Iterator[Transformer]):
    composed_transformer = Transformer()

    for transformer in transformers:
        for method_name in dir(transformer):
            method = getattr(transformer, method_name)

            if not callable(method):
                continue

            if method_name.startswith("_") or method_name == "transform":
                continue

            setattr(composed_transformer, method_name, method)

    return composed_transformer
