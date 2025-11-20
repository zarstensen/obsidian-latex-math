from typing import Any

from lark import Transformer, v_args

from lmat_cas_client.compiling.transforming.TransformerRunner import TransformerRunner


@v_args(inline=True)
class DefinitionsTransformer(Transformer):
    # in addition to defenition stuff,
    # also traverse latex math AST, and remove all (_)?latex_math_grammar__ strings in trees and terminals.

    pass


definitions_transformer_runner = TransformerRunner[[], Any](DefinitionsTransformer)

__all__ = ["definitions_transformer_runner"]
