# Generated from d:/DTU/School/.obsidian/plugins/obsidian-latex-math/lmat-cas-client/lmat_cas_client/compiling/antlr/ExprGrammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,32,6,2,0,7,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,4,0,2,1,0,0,0,2,3,5,
        1,0,0,3,4,5,0,0,1,4,1,1,0,0,0,0
    ]

class ExprGrammar ( Parser ):

    grammarFileName = "ExprGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'+'", "'-'", "<INVALID>", 
                     "<INVALID>", "'\\times'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'}'", "'('", "')'", "'\\{'", "'\\}'", 
                     "'\\['", "'\\]'", "'\\lceil'", "'\\rceil'", "'\\lfloor'", 
                     "'\\rfloor'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'int'" ]

    symbolicNames = [ "<INVALID>", "IGNORE", "PLUS", "MINUS", "MULT", "DIV", 
                      "TIMES", "CROSS_PROD", "DOT_PROD", "LBRACE", "RBRACE", 
                      "LPAREN", "RPAREN", "LBRACE_LITERAL", "RBRACE_LITERAL", 
                      "LBRACKET", "RBRACKET", "LCEIL", "RCEIL", "LFLOOR", 
                      "RFLOOR", "LANGLE", "RANGLE", "BAR", "DOUBLE_BAR", 
                      "FRAC", "INT", "DX", "NUMBER", "WORD", "COMM", "WS", 
                      "ARG_WS" ]

    RULE_debug = 0

    ruleNames =  [ "debug" ]

    EOF = Token.EOF
    IGNORE=1
    PLUS=2
    MINUS=3
    MULT=4
    DIV=5
    TIMES=6
    CROSS_PROD=7
    DOT_PROD=8
    LBRACE=9
    RBRACE=10
    LPAREN=11
    RPAREN=12
    LBRACE_LITERAL=13
    RBRACE_LITERAL=14
    LBRACKET=15
    RBRACKET=16
    LCEIL=17
    RCEIL=18
    LFLOOR=19
    RFLOOR=20
    LANGLE=21
    RANGLE=22
    BAR=23
    DOUBLE_BAR=24
    FRAC=25
    INT=26
    DX=27
    NUMBER=28
    WORD=29
    COMM=30
    WS=31
    ARG_WS=32

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DebugContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IGNORE(self):
            return self.getToken(ExprGrammar.IGNORE, 0)

        def EOF(self):
            return self.getToken(ExprGrammar.EOF, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_debug

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDebug" ):
                listener.enterDebug(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDebug" ):
                listener.exitDebug(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDebug" ):
                return visitor.visitDebug(self)
            else:
                return visitor.visitChildren(self)




    def debug(self):

        localctx = ExprGrammar.DebugContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_debug)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(ExprGrammar.IGNORE)
            self.state = 3
            self.match(ExprGrammar.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





