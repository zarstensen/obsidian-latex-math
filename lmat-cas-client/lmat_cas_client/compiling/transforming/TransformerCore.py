from typing import Callable

from lark import Transformer, Tree


class TransformerRunner[**PTransform, TRes: Transformer]:
    def __init__(self, transformer_factory: Callable[PTransform, TRes]):
        self._transformer_factory = transformer_factory

    def transform(self, tree: Tree, *args: PTransform.args, **kwargs: PTransform.kwargs) -> TRes:
        return self._transformer_factory(*args, **kwargs).transform(tree)
