import os

from lark import Lark

from lmat_cas_client.compiling.parsing.CasExprParser import latex_comment_remover
from lmat_cas_client.compiling.parsing.Parser import Parser, lark_parser_defaults
from lmat_cas_client.compiling.transforming.ComposeTransformers import (
    AstNamespacesRemover,
)

GRAMMAR_FILE = "cas_logic_expr.lark"

cas_logic_expr_parser = Parser(
    Lark.open(
        os.path.join(os.path.dirname(__file__), GRAMMAR_FILE),
        rel_to=os.path.dirname(__file__),
        start="cas_logic_expression",
        **lark_parser_defaults,
    ),
    pre_processor=latex_comment_remover,
    post_processor=AstNamespacesRemover("cas_expr").visit,
)

"""
PrettyParser instance capable of parsing a latex cas expr string.
"""
__all__ = [
    "cas_logic_expr_parser",
]
