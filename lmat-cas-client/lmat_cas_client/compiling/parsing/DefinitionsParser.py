import os

from lark import Lark

from lmat_cas_client.compiling.parsing.CasExprParser import (
    CasExprPostLexer,
    latex_comment_remover,
)
from lmat_cas_client.compiling.parsing.Parser import Parser

GRAMMAR_FILE = "definition_grammar.lark"


definition_parser = Parser(
    Lark.open(
        os.path.join(os.path.dirname(__file__), GRAMMAR_FILE),
        rel_to=os.path.dirname(__file__),
        parser="lalr",
        start="def_expr",
        lexer="contextual",
        debug=False,
        cache=True,
        propagate_positions=True,
        maybe_placeholders=True,
        regex=True,
        postlex=CasExprPostLexer("latex_math_grammar__"),
    ),
    pre_processor=latex_comment_remover,
)
"""
PrettyParser instance capable of parsing a latex math string.
"""

__all__ = ["definition_parser"]
