from typing import Iterator

from lark import Transformer


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
