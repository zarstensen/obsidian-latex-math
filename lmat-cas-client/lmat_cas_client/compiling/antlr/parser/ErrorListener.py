from antlr4 import Lexer
from attrs import frozen
from typing import Self
from antlr4 import Parser
from typing import override

from antlr4 import Token
from antlr4.Recognizer import Recognizer
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import RecognitionException

class ParseError(Exception):
    pass

@frozen
class ErrorEntry:
    start: int
    end: int
    msg: str
    
    def build_msg(self, src_txt: str, span: int) -> str:

        ctx_start = max(self.start - span, 0)
        ctx_end = self.start + span

        before = src_txt[ctx_start:self.start].rsplit('\n', 1)[-1]
        after = src_txt[self.start:ctx_end].split('\n', 1)[0]

        highlight_span = min(ctx_end, self.end) - self.start


        return f"{before}{after}\n{' ' * len(before.expandtabs())}^{'~' * highlight_span}\n{self.msg}\n"

class ParseErrorListener(ErrorListener):

    def __init__(self: Self):
        self._errors: list[ErrorEntry] | None = None
        self._ctx_span = 40

    def has_errors(self) -> bool:
        return self._errors is not None

    def build_parse_error(self, src_txt: str) -> ParseError:
        if not self.has_errors():
            raise ValueError("Can only build ParseError if listener got errors")

        assert self._errors is not None

        return ParseError("\n".join(err.build_msg(src_txt, self._ctx_span) for err in self._errors))

    @override
    def syntaxError(
        self,
        recognizer: Recognizer,
        offendingSymbol: Token | None,
        line: int,
        column: int,
        msg: str,
        e: RecognitionException | None,
    ) -> None:
        self._errors = self._errors or []

        if offendingSymbol is not None:
            start = offendingSymbol.start
            stop = offendingSymbol.stop
        else:
            match recognizer:
                case Lexer():
                    start = recognizer.inputStream.index
                case _:
                    start = 0

            stop = start

        self._errors.append(ErrorEntry(start, stop, msg))

