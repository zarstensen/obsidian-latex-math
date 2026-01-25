import os

from lark import Lark

from lmat_cas_client.compiling.parsing.CasExprParser import (
    CasExprPostLexer,
    latex_comment_remover,
)
from lmat_cas_client.compiling.parsing.Parser import Parser, lark_parser_defaults
from lmat_cas_client.compiling.transforming.ComposeTransformers import (
    AstNamespacesRemover,
)
from lmat_cas_client.compiling.transforming.cas_expr.UndefinedAtomsTransformer import IndexInjector

GRAMMAR_FILE = "cas_def.lark"


cas_expr_def_parser = Parser(
    Lark.open(
        os.path.join(os.path.dirname(__file__), GRAMMAR_FILE),
        rel_to=os.path.dirname(__file__),
        postlex=CasExprPostLexer("cas_expr__"),
        start="cas_expr_def",
        **lark_parser_defaults,
    ),
    pre_processor=latex_comment_remover,
    post_processor=lambda s, t: IndexInjector(s).visit(
        AstNamespacesRemover("cas_expr").visit(t)
    ),  # remove the cas_expr namespace from the ast,
    # so the ast's present in the Definition's do not contain a cas_expr__ prefix.
)
"""
Parser instance for parsing a latex string into a DefinitionStore.
"""

cas_logic_expr_def_parser = Parser(
    Lark.open(
        os.path.join(os.path.dirname(__file__), GRAMMAR_FILE),
        rel_to=os.path.dirname(__file__),
        postlex=CasExprPostLexer("cas_expr__"),
        start="cas_logic_expr_def",
        **lark_parser_defaults,
    ),
    pre_processor=latex_comment_remover,
    post_processor=lambda _, t: AstNamespacesRemover(
        "cas_expr", "cas_logic_expr"
    ).visit(t),
    # same as for cas_expr_def_parser, except we also need to remove the logic namespace.
)

"""
Parser instance for parsing a latex string into a DefinitionStore.
The latex string is expected to be logic expressions.
"""

__all__ = ["cas_expr_def_parser", "cas_logic_expr_def_parser"]
