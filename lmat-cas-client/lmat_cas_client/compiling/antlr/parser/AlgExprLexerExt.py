from typing import override

from antlr4 import Token

from lmat_cas_client.compiling.antlr.lexer.AddModes import AddModes
from lmat_cas_client.compiling.antlr.lexer.SepInjector import SepInjector
from lmat_cas_client.compiling.antlr.parser.AlgExprLexer import AlgExprLexer


class AlgExprLexerExt(AddModes, AlgExprLexer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sep_injector = SepInjector()
        self._sep_injector.set_adj_tokens(self.ADJ_TOKENS)

    @override
    def nextToken(self) -> Token:
        return self._sep_injector.next_token(
            super(),
            self.ADJ_OP,
        )
