from antlr4 import Lexer
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream


class BaseLexer(Lexer):

    @classmethod
    def stream_from_src(cls, src: str) -> CommonTokenStream:
    	return CommonTokenStream(cls(InputStream(src)))
