from typing import Callable

from lark import Transformer, Tree


class TransformerRunner[**PTransform, TRes: Transformer]:
    """
    Wrapper class for a lark Transformer factory taking PTransform arguments and returning TRes as a transform result.
    Constructs a new Transformer instance from the given Transformer factory, and transforms a given tree with the newly constructed instance.
    """
    def __init__(self, transformer_factory: Callable[PTransform, TRes]):
        self._transformer_factory = transformer_factory

    def transform(self, tree: Tree, *args: PTransform.args, **kwargs: PTransform.kwargs) -> TRes:
        """
        Transform given tree with Transformer build from transformer_factory.
        Args:
            tree (Tree): tree to transform

        Returns:
            TRes: transformed result
        """
        return self._transformer_factory(*args, **kwargs).transform(tree)
