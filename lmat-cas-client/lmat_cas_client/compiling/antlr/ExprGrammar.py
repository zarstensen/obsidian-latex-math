# Generated from ExprGrammar.g4 by ANTLR 4.13.2
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
        4,1,54,11,2,0,7,0,1,0,5,0,4,8,0,10,0,12,0,7,9,0,1,0,1,0,1,0,1,5,
        0,1,0,0,0,10,0,5,1,0,0,0,2,4,9,0,0,0,3,2,1,0,0,0,4,7,1,0,0,0,5,6,
        1,0,0,0,5,3,1,0,0,0,6,8,1,0,0,0,7,5,1,0,0,0,8,9,5,0,0,1,9,1,1,0,
        0,0,1,5
    ]

class ExprGrammar ( Parser ):

    grammarFileName = "ExprGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "<INVALID>", "<INVALID>", "'\\times'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\\sqrt'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\\lim'", "'\\sum'", "'\\prod'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'\\{'", "'\\}'", "'\\['", "'\\]'", "'\\lceil'", 
                     "'\\rceil'", "'\\lfloor'", "'\\rfloor'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'&'", "'\\\\'" ]

    symbolicNames = [ "<INVALID>", "FUNCTION", "IGNORE", "PLUS", "MINUS", 
                      "MULT", "DIV", "TIMES", "CROSS_PROD", "DOT_PROD", 
                      "FRAC", "BINOM", "FUNC_SQRT", "CONJUGATE", "MOD", 
                      "INT", "DIFFERENTIAL", "PHYS_PARTIAL_DERIVATIVE", 
                      "LIMIT", "SUM", "PRODUCT", "VEC_UNIT", "SYMBOL", "COMMAND", 
                      "NUMBER", "BIN_NUMBER", "OCT_NUMBER", "HEX_NUMBER", 
                      "LBRACE", "RBRACE", "LPAREN", "RPAREN", "LBRACE_LITERAL", 
                      "RBRACE_LITERAL", "LBRACKET", "RBRACKET", "LCEIL", 
                      "RCEIL", "LFLOOR", "RFLOOR", "LANGLE", "RANGLE", "BAR", 
                      "DOUBLE_BAR", "BEGIN_MATRIX", "END_MATRIX", "BEGIN_V_MATRIX", 
                      "END_V_MATRIX", "BEGIN_ARRAY", "END_ARRAY", "BEGIN_ENV", 
                      "END_ENV", "ENV_EL_SEP", "ENV_ROW_SEP", "ARG_WS" ]

    RULE_debug = 0

    ruleNames =  [ "debug" ]

    EOF = Token.EOF
    FUNCTION=1
    IGNORE=2
    PLUS=3
    MINUS=4
    MULT=5
    DIV=6
    TIMES=7
    CROSS_PROD=8
    DOT_PROD=9
    FRAC=10
    BINOM=11
    FUNC_SQRT=12
    CONJUGATE=13
    MOD=14
    INT=15
    DIFFERENTIAL=16
    PHYS_PARTIAL_DERIVATIVE=17
    LIMIT=18
    SUM=19
    PRODUCT=20
    VEC_UNIT=21
    SYMBOL=22
    COMMAND=23
    NUMBER=24
    BIN_NUMBER=25
    OCT_NUMBER=26
    HEX_NUMBER=27
    LBRACE=28
    RBRACE=29
    LPAREN=30
    RPAREN=31
    LBRACE_LITERAL=32
    RBRACE_LITERAL=33
    LBRACKET=34
    RBRACKET=35
    LCEIL=36
    RCEIL=37
    LFLOOR=38
    RFLOOR=39
    LANGLE=40
    RANGLE=41
    BAR=42
    DOUBLE_BAR=43
    BEGIN_MATRIX=44
    END_MATRIX=45
    BEGIN_V_MATRIX=46
    END_V_MATRIX=47
    BEGIN_ARRAY=48
    END_ARRAY=49
    BEGIN_ENV=50
    END_ENV=51
    ENV_EL_SEP=52
    ENV_ROW_SEP=53
    ARG_WS=54

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DebugContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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




    def debug(self):

        localctx = ExprGrammar.DebugContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_debug)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 2
                    self.matchWildcard() 
                self.state = 7
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 8
            self.match(ExprGrammar.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





