import os

from lark import Lark

from lmat_cas_client.compiling.parsing.CasExprParser import (
    CasExprPostLexer,
    latex_comment_remover,
)
from lmat_cas_client.compiling.parsing.Parser import Parser, lark_parser_defaults

GRAMMAR_FILE = "definition_grammar.lark"


# there should be 2 of these.
cas_expr_def_parser = Parser(
    Lark.open(
        os.path.join(os.path.dirname(__file__), GRAMMAR_FILE),
        rel_to=os.path.dirname(__file__),
        postlex=CasExprPostLexer("cas_expr__"),
        start="cas_expr_def",  # and also one for cas_logic_def_expression
        **lark_parser_defaults,
    ),
    pre_processor=latex_comment_remover,
)

# there should be 2 of these.
# cas_logic_expr_def_parser = Parser(
#     Lark.open(
#         os.path.join(os.path.dirname(__file__), GRAMMAR_FILE),
#         rel_to=os.path.dirname(__file__),
#         postlex=CasExprPostLexer("cas_expr__"),
#         start="cas_logic_expr_def",  # and also one for cas_logic_def_expression
#         **lark_parser_defaults,
#     ),
#     pre_processor=latex_comment_remover,
# )

"""
PrettyParser instance capable of parsing a latex math string.
"""

__all__ = ["cas_expr_def_parser"]
