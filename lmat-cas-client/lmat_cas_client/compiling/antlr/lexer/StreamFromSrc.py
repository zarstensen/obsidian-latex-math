
from antlr4 import Lexer
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream


def stream_from_src(lex_cls: type[Lexer], src: str) -> CommonTokenStream:
    return CommonTokenStream(lex_cls(InputStream(src)))

