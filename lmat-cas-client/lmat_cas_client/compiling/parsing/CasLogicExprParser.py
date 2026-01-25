import os

from lark import Lark

from lmat_cas_client.compiling.parsing.CasExprParser import latex_comment_remover
from lmat_cas_client.compiling.parsing.Parser import Parser, lark_parser_defaults
from lmat_cas_client.compiling.transforming.ComposeTransformers import (
    AstNamespacesRemover,
)
from lmat_cas_client.compiling.transforming.cas_expr.UndefinedAtomsTransformer import IndexInjector

GRAMMAR_FILE = "cas_logic_expr.lark"

cas_logic_expr_parser = Parser(
    Lark.open(
        os.path.join(os.path.dirname(__file__), GRAMMAR_FILE),
        rel_to=os.path.dirname(__file__),
        start="cas_logic_expression",
        **lark_parser_defaults,
    ),
    pre_processor=latex_comment_remover,
    post_processor=lambda s, t: IndexInjector(s).visit(
        AstNamespacesRemover("cas_expr").visit(t)
    ),
)

"""
PrettyParser instance capable of parsing a latex cas expr string.
"""
__all__ = [
    "cas_logic_expr_parser",
]
