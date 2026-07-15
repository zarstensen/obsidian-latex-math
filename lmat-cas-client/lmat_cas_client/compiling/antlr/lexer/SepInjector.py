
from typing import Iterable

from antlr4 import Lexer
from antlr4.CommonTokenFactory import CommonTokenFactory


class SepInjector:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._prev_token_type = None
        self._token_buffer = []
        self._illegal_lhs_tokens = set()
        self._illegal_rhs_tokens = set()

    def set_adj_tokens(self, adj_tokens: Iterable[tuple[int | None, int | None] | int]):
        for e in adj_tokens:
            match e:
                case int():
                    self._illegal_lhs_tokens.add(e)
                    self._illegal_rhs_tokens.add(e)
                case (l, r):
                    if l is not None:
                        self._illegal_lhs_tokens.add(l)
                    if r is not None:
                        self._illegal_rhs_tokens.add(r)

    def next_token(self, lexer: Lexer, sep_token_type: int):
        return lexer.nextToken()
        if len(self._token_buffer) > 0:
            next_token = self._token_buffer.pop()
        else:
            next_token = lexer.nextToken()

        assert next_token is not None

        if next_token.type in self._illegal_rhs_tokens and self._prev_token_type in self._illegal_lhs_tokens:
            self._token_buffer.append(next_token)
            next_token = CommonTokenFactory.DEFAULT.createThin(sep_token_type, "")

        self._prev_token_type = next_token.type
        return next_token

