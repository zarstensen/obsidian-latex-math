# Generated from ExprGrammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


import Ast

def serializedATN():
    return [
        4,1,63,194,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,5,1,25,8,1,10,1,12,1,28,
        9,1,3,1,30,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,3,1,48,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,67,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,84,8,1,1,1,1,1,1,1,1,1,1,1,
        3,1,91,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,106,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,123,8,1,1,1,5,1,126,8,1,10,1,12,1,129,9,1,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,137,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,147,
        8,3,1,4,1,4,1,4,1,4,1,4,3,4,154,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,176,8,5,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,192,
        8,6,1,6,0,1,2,7,0,2,4,6,8,10,12,0,2,1,0,23,24,1,0,4,5,218,0,14,1,
        0,0,0,2,83,1,0,0,0,4,136,1,0,0,0,6,146,1,0,0,0,8,153,1,0,0,0,10,
        175,1,0,0,0,12,191,1,0,0,0,14,15,3,2,1,0,15,16,5,0,0,1,16,17,6,0,
        -1,0,17,1,1,0,0,0,18,19,6,1,-1,0,19,20,5,1,0,0,20,29,5,39,0,0,21,
        26,3,2,1,0,22,23,5,34,0,0,23,25,3,2,1,0,24,22,1,0,0,0,25,28,1,0,
        0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,30,1,0,0,0,28,26,1,0,0,0,29,21,
        1,0,0,0,29,30,1,0,0,0,30,31,1,0,0,0,31,84,5,40,0,0,32,33,5,1,0,0,
        33,34,5,37,0,0,34,35,3,2,1,0,35,36,5,38,0,0,36,84,1,0,0,0,37,38,
        5,1,0,0,38,84,3,2,1,11,39,40,5,21,0,0,40,41,5,35,0,0,41,42,5,37,
        0,0,42,43,5,28,0,0,43,44,5,22,0,0,44,47,3,2,1,0,45,46,5,8,0,0,46,
        48,3,8,4,0,47,45,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,49,50,5,38,
        0,0,50,51,3,2,1,10,51,84,1,0,0,0,52,53,7,0,0,0,53,54,3,10,5,0,54,
        55,5,39,0,0,55,56,3,2,1,0,56,57,5,40,0,0,57,84,1,0,0,0,58,59,7,0,
        0,0,59,60,3,10,5,0,60,61,3,2,1,6,61,84,1,0,0,0,62,63,5,4,0,0,63,
        67,6,1,-1,0,64,65,5,5,0,0,65,67,6,1,-1,0,66,62,1,0,0,0,66,64,1,0,
        0,0,67,68,1,0,0,0,68,69,3,2,1,4,69,70,6,1,-1,0,70,84,1,0,0,0,71,
        72,5,18,0,0,72,73,3,2,1,0,73,74,5,19,0,0,74,84,1,0,0,0,75,76,5,39,
        0,0,76,77,3,2,1,0,77,78,5,40,0,0,78,79,6,1,-1,0,79,84,1,0,0,0,80,
        81,3,4,2,0,81,82,6,1,-1,0,82,84,1,0,0,0,83,18,1,0,0,0,83,32,1,0,
        0,0,83,37,1,0,0,0,83,39,1,0,0,0,83,52,1,0,0,0,83,58,1,0,0,0,83,66,
        1,0,0,0,83,71,1,0,0,0,83,75,1,0,0,0,83,80,1,0,0,0,84,127,1,0,0,0,
        85,90,10,9,0,0,86,87,5,6,0,0,87,91,6,1,-1,0,88,89,5,7,0,0,89,91,
        6,1,-1,0,90,86,1,0,0,0,90,88,1,0,0,0,91,92,1,0,0,0,92,93,3,2,1,10,
        93,94,6,1,-1,0,94,126,1,0,0,0,95,96,10,8,0,0,96,97,4,1,2,0,97,98,
        3,2,1,9,98,99,6,1,-1,0,99,126,1,0,0,0,100,105,10,5,0,0,101,102,5,
        4,0,0,102,106,6,1,-1,0,103,104,5,5,0,0,104,106,6,1,-1,0,105,101,
        1,0,0,0,105,103,1,0,0,0,106,107,1,0,0,0,107,108,3,2,1,6,108,109,
        6,1,-1,0,109,126,1,0,0,0,110,111,10,15,0,0,111,112,5,8,0,0,112,113,
        3,6,3,0,113,114,6,1,-1,0,114,126,1,0,0,0,115,122,10,14,0,0,116,117,
        5,25,0,0,117,123,6,1,-1,0,118,119,5,26,0,0,119,123,6,1,-1,0,120,
        121,5,27,0,0,121,123,6,1,-1,0,122,116,1,0,0,0,122,118,1,0,0,0,122,
        120,1,0,0,0,123,124,1,0,0,0,124,126,6,1,-1,0,125,85,1,0,0,0,125,
        95,1,0,0,0,125,100,1,0,0,0,125,110,1,0,0,0,125,115,1,0,0,0,126,129,
        1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,3,1,0,0,0,129,127,1,
        0,0,0,130,131,5,28,0,0,131,137,6,2,-1,0,132,133,5,29,0,0,133,137,
        6,2,-1,0,134,135,5,30,0,0,135,137,6,2,-1,0,136,130,1,0,0,0,136,132,
        1,0,0,0,136,134,1,0,0,0,137,5,1,0,0,0,138,139,3,4,2,0,139,140,6,
        3,-1,0,140,147,1,0,0,0,141,142,5,37,0,0,142,143,3,2,1,0,143,144,
        5,38,0,0,144,145,6,3,-1,0,145,147,1,0,0,0,146,138,1,0,0,0,146,141,
        1,0,0,0,147,7,1,0,0,0,148,149,5,37,0,0,149,150,7,1,0,0,150,154,5,
        38,0,0,151,154,5,4,0,0,152,154,5,5,0,0,153,148,1,0,0,0,153,151,1,
        0,0,0,153,152,1,0,0,0,154,9,1,0,0,0,155,156,5,35,0,0,156,157,5,37,
        0,0,157,158,5,28,0,0,158,159,5,36,0,0,159,160,3,2,1,0,160,161,5,
        38,0,0,161,162,5,8,0,0,162,163,3,6,3,0,163,164,6,5,-1,0,164,176,
        1,0,0,0,165,166,5,8,0,0,166,167,3,6,3,0,167,168,5,35,0,0,168,169,
        5,37,0,0,169,170,5,28,0,0,170,171,5,36,0,0,171,172,3,2,1,0,172,173,
        5,38,0,0,173,174,6,5,-1,0,174,176,1,0,0,0,175,155,1,0,0,0,175,165,
        1,0,0,0,176,11,1,0,0,0,177,178,5,12,0,0,178,179,3,6,3,0,179,180,
        3,6,3,0,180,192,1,0,0,0,181,182,5,13,0,0,182,183,3,6,3,0,183,184,
        3,6,3,0,184,192,1,0,0,0,185,186,5,14,0,0,186,192,3,6,3,0,187,188,
        5,15,0,0,188,192,3,6,3,0,189,190,5,16,0,0,190,192,3,6,3,0,191,177,
        1,0,0,0,191,181,1,0,0,0,191,185,1,0,0,0,191,187,1,0,0,0,191,189,
        1,0,0,0,192,13,1,0,0,0,15,26,29,47,66,83,90,105,122,125,127,136,
        146,153,175,191
    ]

class ExprGrammar ( Parser ):

    grammarFileName = "ExprGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "<INVALID>", "<INVALID>", "'^'", "'\\times'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\\sqrt'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\\lim'", "<INVALID>", 
                     "'\\sum'", "'\\prod'", "'!'", "'\\%'", "'\\textperthousand'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "','", "'_'", "'='", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'\\{'", "'\\}'", "'\\['", 
                     "'\\]'", "'\\lceil'", "'\\rceil'", "'\\lfloor'", "'\\rfloor'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'&'", "'\\\\'" ]

    symbolicNames = [ "<INVALID>", "FUNCTION", "CMD_FUNCTION", "IGNORE", 
                      "PLUS", "MINUS", "MULT", "DIV", "POW", "TIMES", "CROSS_PROD", 
                      "DOT_PROD", "FRAC", "BINOM", "SQRT", "CONJUGATE", 
                      "VEC_UNIT", "MOD", "INT", "DIFFERENTIAL", "PHYS_PARTIAL_DERIVATIVE", 
                      "LIMIT", "LIMIT_ARROW", "SUM", "PRODUCT", "BANG", 
                      "PERCENT", "PERMILLE", "SYMBOL", "COMMAND", "NUMBER", 
                      "BIN_NUMBER", "OCT_NUMBER", "HEX_NUMBER", "COMMA", 
                      "UNDERSCORE", "EQUAL", "LBRACE", "RBRACE", "LPAREN", 
                      "RPAREN", "LBRACE_LITERAL", "RBRACE_LITERAL", "LBRACKET", 
                      "RBRACKET", "LCEIL", "RCEIL", "LFLOOR", "RFLOOR", 
                      "LANGLE", "RANGLE", "BAR", "DOUBLE_BAR", "BEGIN_MATRIX", 
                      "END_MATRIX", "BEGIN_V_MATRIX", "END_V_MATRIX", "BEGIN_ARRAY", 
                      "END_ARRAY", "BEGIN_ENV", "END_ENV", "ENV_EL_SEP", 
                      "ENV_ROW_SEP", "ARG_WS" ]

    RULE_debug = 0
    RULE_expr = 1
    RULE_atom = 2
    RULE_latex_cmd_arg = 3
    RULE_limit_dir = 4
    RULE_series_range_args = 5
    RULE_hard_func = 6

    ruleNames =  [ "debug", "expr", "atom", "latex_cmd_arg", "limit_dir", 
                   "series_range_args", "hard_func" ]

    EOF = Token.EOF
    FUNCTION=1
    CMD_FUNCTION=2
    IGNORE=3
    PLUS=4
    MINUS=5
    MULT=6
    DIV=7
    POW=8
    TIMES=9
    CROSS_PROD=10
    DOT_PROD=11
    FRAC=12
    BINOM=13
    SQRT=14
    CONJUGATE=15
    VEC_UNIT=16
    MOD=17
    INT=18
    DIFFERENTIAL=19
    PHYS_PARTIAL_DERIVATIVE=20
    LIMIT=21
    LIMIT_ARROW=22
    SUM=23
    PRODUCT=24
    BANG=25
    PERCENT=26
    PERMILLE=27
    SYMBOL=28
    COMMAND=29
    NUMBER=30
    BIN_NUMBER=31
    OCT_NUMBER=32
    HEX_NUMBER=33
    COMMA=34
    UNDERSCORE=35
    EQUAL=36
    LBRACE=37
    RBRACE=38
    LPAREN=39
    RPAREN=40
    LBRACE_LITERAL=41
    RBRACE_LITERAL=42
    LBRACKET=43
    RBRACKET=44
    LCEIL=45
    RCEIL=46
    LFLOOR=47
    RFLOOR=48
    LANGLE=49
    RANGLE=50
    BAR=51
    DOUBLE_BAR=52
    BEGIN_MATRIX=53
    END_MATRIX=54
    BEGIN_V_MATRIX=55
    END_V_MATRIX=56
    BEGIN_ARRAY=57
    END_ARRAY=58
    BEGIN_ENV=59
    END_ENV=60
    ENV_EL_SEP=61
    ENV_ROW_SEP=62
    ARG_WS=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    func_set: set[str] = set()



    class DebugContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(ExprGrammar.ExprContext,0)


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
            self.state = 14
            localctx._expr = self.expr(0)
            self.state = 15
            self.match(ExprGrammar.EOF)
            localctx.res = localctx._expr.res
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.node_t = None


        def getRuleIndex(self):
            return ExprGrammar.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.res = ctx.res
            self.node_t = ctx.node_t


    class FunctionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
            self._expr = None # ExprContext
            self.copyFrom(ctx)

        def FUNCTION(self):
            return self.getToken(ExprGrammar.FUNCTION, 0)
        def LPAREN(self):
            return self.getToken(ExprGrammar.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(ExprGrammar.RPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.ExprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.COMMA)
            else:
                return self.getToken(ExprGrammar.COMMA, i)
        def LBRACE(self):
            return self.getToken(ExprGrammar.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(ExprGrammar.RBRACE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)


    class SeriesContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
            self._expr = None # ExprContext
            self.copyFrom(ctx)

        def series_range_args(self):
            return self.getTypedRuleContext(ExprGrammar.Series_range_argsContext,0)

        def LPAREN(self):
            return self.getToken(ExprGrammar.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprGrammar.ExprContext,0)

        def RPAREN(self):
            return self.getToken(ExprGrammar.RPAREN, 0)
        def SUM(self):
            return self.getToken(ExprGrammar.SUM, 0)
        def PRODUCT(self):
            return self.getToken(ExprGrammar.PRODUCT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeries" ):
                listener.enterSeries(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeries" ):
                listener.exitSeries(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeries" ):
                return visitor.visitSeries(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicativeOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
            self.lhs = None # ExprContext
            self.rhs = None # ExprContext
            self._expr = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.ExprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.ExprContext,i)

        def MULT(self):
            return self.getToken(ExprGrammar.MULT, 0)
        def DIV(self):
            return self.getToken(ExprGrammar.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeOp" ):
                listener.enterMultiplicativeOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeOp" ):
                listener.exitMultiplicativeOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeOp" ):
                return visitor.visitMultiplicativeOp(self)
            else:
                return visitor.visitChildren(self)


    class UAdditiveOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
            self._expr = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprGrammar.ExprContext,0)

        def PLUS(self):
            return self.getToken(ExprGrammar.PLUS, 0)
        def MINUS(self):
            return self.getToken(ExprGrammar.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUAdditiveOp" ):
                listener.enterUAdditiveOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUAdditiveOp" ):
                listener.exitUAdditiveOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUAdditiveOp" ):
                return visitor.visitUAdditiveOp(self)
            else:
                return visitor.visitChildren(self)


    class AdditiveOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
            self.lhs = None # ExprContext
            self.rhs = None # ExprContext
            self._expr = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.ExprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.ExprContext,i)

        def PLUS(self):
            return self.getToken(ExprGrammar.PLUS, 0)
        def MINUS(self):
            return self.getToken(ExprGrammar.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveOp" ):
                listener.enterAdditiveOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveOp" ):
                listener.exitAdditiveOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveOp" ):
                return visitor.visitAdditiveOp(self)
            else:
                return visitor.visitChildren(self)


    class StubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
            self._expr = None # ExprContext
            self._atom = None # AtomContext
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ExprGrammar.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprGrammar.ExprContext,0)

        def RPAREN(self):
            return self.getToken(ExprGrammar.RPAREN, 0)
        def atom(self):
            return self.getTypedRuleContext(ExprGrammar.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStub" ):
                listener.enterStub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStub" ):
                listener.exitStub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStub" ):
                return visitor.visitStub(self)
            else:
                return visitor.visitChildren(self)


    class ExponentialOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
            self.base = None # ExprContext
            self.exp = None # Latex_cmd_argContext
            self.copyFrom(ctx)

        def POW(self):
            return self.getToken(ExprGrammar.POW, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprGrammar.ExprContext,0)

        def latex_cmd_arg(self):
            return self.getTypedRuleContext(ExprGrammar.Latex_cmd_argContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponentialOp" ):
                listener.enterExponentialOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponentialOp" ):
                listener.exitExponentialOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponentialOp" ):
                return visitor.visitExponentialOp(self)
            else:
                return visitor.visitChildren(self)


    class LimitContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
            self._expr = None # ExprContext
            self.copyFrom(ctx)

        def LIMIT(self):
            return self.getToken(ExprGrammar.LIMIT, 0)
        def UNDERSCORE(self):
            return self.getToken(ExprGrammar.UNDERSCORE, 0)
        def LBRACE(self):
            return self.getToken(ExprGrammar.LBRACE, 0)
        def SYMBOL(self):
            return self.getToken(ExprGrammar.SYMBOL, 0)
        def LIMIT_ARROW(self):
            return self.getToken(ExprGrammar.LIMIT_ARROW, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.ExprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.ExprContext,i)

        def RBRACE(self):
            return self.getToken(ExprGrammar.RBRACE, 0)
        def POW(self):
            return self.getToken(ExprGrammar.POW, 0)
        def limit_dir(self):
            return self.getTypedRuleContext(ExprGrammar.Limit_dirContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimit" ):
                listener.enterLimit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimit" ):
                listener.exitLimit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLimit" ):
                return visitor.visitLimit(self)
            else:
                return visitor.visitChildren(self)


    class PrefixContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
            self.op = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprGrammar.ExprContext,0)

        def BANG(self):
            return self.getToken(ExprGrammar.BANG, 0)
        def PERCENT(self):
            return self.getToken(ExprGrammar.PERCENT, 0)
        def PERMILLE(self):
            return self.getToken(ExprGrammar.PERMILLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefix" ):
                listener.enterPrefix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefix" ):
                listener.exitPrefix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrefix" ):
                return visitor.visitPrefix(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
            self._expr = None # ExprContext
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ExprGrammar.INT, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprGrammar.ExprContext,0)

        def DIFFERENTIAL(self):
            return self.getToken(ExprGrammar.DIFFERENTIAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprGrammar.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = ExprGrammar.FunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 19
                self.match(ExprGrammar.FUNCTION)
                self.state = 20
                self.match(ExprGrammar.LPAREN)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 551662387250) != 0):
                    self.state = 21
                    localctx._expr = self.expr(0)
                    self.state = 26
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==34:
                        self.state = 22
                        self.match(ExprGrammar.COMMA)
                        self.state = 23
                        localctx._expr = self.expr(0)
                        self.state = 28
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 31
                self.match(ExprGrammar.RPAREN)
                pass

            elif la_ == 2:
                localctx = ExprGrammar.FunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 32
                self.match(ExprGrammar.FUNCTION)
                self.state = 33
                self.match(ExprGrammar.LBRACE)
                self.state = 34
                localctx._expr = self.expr(0)
                self.state = 35
                self.match(ExprGrammar.RBRACE)
                pass

            elif la_ == 3:
                localctx = ExprGrammar.FunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 37
                self.match(ExprGrammar.FUNCTION)
                self.state = 38
                localctx._expr = self.expr(11)
                pass

            elif la_ == 4:
                localctx = ExprGrammar.LimitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                self.match(ExprGrammar.LIMIT)
                self.state = 40
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 41
                self.match(ExprGrammar.LBRACE)
                self.state = 42
                self.match(ExprGrammar.SYMBOL)
                self.state = 43
                self.match(ExprGrammar.LIMIT_ARROW)
                self.state = 44
                localctx._expr = self.expr(0)
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==8:
                    self.state = 45
                    self.match(ExprGrammar.POW)
                    self.state = 46
                    self.limit_dir()


                self.state = 49
                self.match(ExprGrammar.RBRACE)
                self.state = 50
                localctx._expr = self.expr(10)
                pass

            elif la_ == 5:
                localctx = ExprGrammar.SeriesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 53
                self.series_range_args()
                self.state = 54
                self.match(ExprGrammar.LPAREN)
                self.state = 55
                localctx._expr = self.expr(0)
                self.state = 56
                self.match(ExprGrammar.RPAREN)
                pass

            elif la_ == 6:
                localctx = ExprGrammar.SeriesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 58
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 59
                self.series_range_args()
                self.state = 60
                localctx._expr = self.expr(6)
                pass

            elif la_ == 7:
                localctx = ExprGrammar.UAdditiveOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 66
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [4]:
                    self.state = 62
                    self.match(ExprGrammar.PLUS)
                    localctx.node_t = Ast.UPlusOp
                    pass
                elif token in [5]:
                    self.state = 64
                    self.match(ExprGrammar.MINUS)
                    localctx.node_t = Ast.UMinusOp
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 68
                localctx._expr = self.expr(4)
                localctx.res = localctx.node_t(localctx, localctx._expr.res)
                pass

            elif la_ == 8:
                localctx = ExprGrammar.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 71
                self.match(ExprGrammar.INT)
                self.state = 72
                localctx._expr = self.expr(0)
                self.state = 73
                self.match(ExprGrammar.DIFFERENTIAL)
                pass

            elif la_ == 9:
                localctx = ExprGrammar.StubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 75
                self.match(ExprGrammar.LPAREN)
                self.state = 76
                localctx._expr = self.expr(0)
                self.state = 77
                self.match(ExprGrammar.RPAREN)
                localctx.res = localctx._expr.res
                pass

            elif la_ == 10:
                localctx = ExprGrammar.StubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 80
                localctx._atom = self.atom()
                localctx.res = localctx._atom.res 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 125
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = ExprGrammar.MultiplicativeOpContext(self, ExprGrammar.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 85
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 90
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [6]:
                            self.state = 86
                            self.match(ExprGrammar.MULT)
                            localctx.node_t = Ast.MultOp
                            pass
                        elif token in [7]:
                            self.state = 88
                            self.match(ExprGrammar.DIV)
                            localctx.node_t = Ast.DivOp
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 92
                        localctx.rhs = localctx._expr = self.expr(10)
                        localctx.res = localctx.node_t(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 2:
                        localctx = ExprGrammar.MultiplicativeOpContext(self, ExprGrammar.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 95
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 96
                        if not self._input.LA(1) not in (self.PLUS, self.MINUS, self.NUMBER):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self._input.LA(1) not in (self.PLUS, self.MINUS, self.NUMBER)")
                        self.state = 97
                        localctx.rhs = localctx._expr = self.expr(9)
                        localctx.res = Ast.MultOp(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 3:
                        localctx = ExprGrammar.AdditiveOpContext(self, ExprGrammar.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 100
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 105
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [4]:
                            self.state = 101
                            self.match(ExprGrammar.PLUS)
                            localctx.node_t = Ast.AddOp
                            pass
                        elif token in [5]:
                            self.state = 103
                            self.match(ExprGrammar.MINUS)
                            localctx.node_t = Ast.SubOp
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 107
                        localctx.rhs = localctx._expr = self.expr(6)
                        localctx.res = localctx.node_t(localctx, localctx.lhs.res, localctx.rhs.res)
                        pass

                    elif la_ == 4:
                        localctx = ExprGrammar.ExponentialOpContext(self, ExprGrammar.ExprContext(self, _parentctx, _parentState))
                        localctx.base = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 110
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 111
                        self.match(ExprGrammar.POW)
                        self.state = 112
                        localctx.exp = self.latex_cmd_arg()
                        localctx.res=Ast.ExpOp(localctx, localctx.base.res, localctx.exp.res)
                        pass

                    elif la_ == 5:
                        localctx = ExprGrammar.PrefixContext(self, ExprGrammar.ExprContext(self, _parentctx, _parentState))
                        localctx.op = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 115
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 122
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [25]:
                            self.state = 116
                            self.match(ExprGrammar.BANG)
                            localctx.node_t = Ast.Factorial
                            pass
                        elif token in [26]:
                            self.state = 118
                            self.match(ExprGrammar.PERCENT)
                            localctx.node_t = Ast.Percent
                            pass
                        elif token in [27]:
                            self.state = 120
                            self.match(ExprGrammar.PERMILLE)
                            localctx.node_t = Ast.Permille
                            pass
                        else:
                            raise NoViableAltException(self)

                        localctx.res = localctx.node_t(localctx, localctx.op.res)
                        pass

             
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self._SYMBOL = None # Token
            self._COMMAND = None # Token
            self._NUMBER = None # Token

        def SYMBOL(self):
            return self.getToken(ExprGrammar.SYMBOL, 0)

        def COMMAND(self):
            return self.getToken(ExprGrammar.COMMAND, 0)

        def NUMBER(self):
            return self.getToken(ExprGrammar.NUMBER, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = ExprGrammar.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atom)
        try:
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                localctx._SYMBOL = self.match(ExprGrammar.SYMBOL)
                localctx.res = Ast.Symbol(localctx, (None if localctx._SYMBOL is None else localctx._SYMBOL.text))
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                localctx._COMMAND = self.match(ExprGrammar.COMMAND)
                localctx.res = Ast.Symbol(localctx, (None if localctx._COMMAND is None else localctx._COMMAND.text))
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                localctx._NUMBER = self.match(ExprGrammar.NUMBER)
                localctx.res = Ast.Number(localctx, (None if localctx._NUMBER is None else localctx._NUMBER.text))
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Latex_cmd_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self._atom = None # AtomContext
            self._expr = None # ExprContext

        def atom(self):
            return self.getTypedRuleContext(ExprGrammar.AtomContext,0)


        def LBRACE(self):
            return self.getToken(ExprGrammar.LBRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprGrammar.ExprContext,0)


        def RBRACE(self):
            return self.getToken(ExprGrammar.RBRACE, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_latex_cmd_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLatex_cmd_arg" ):
                listener.enterLatex_cmd_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLatex_cmd_arg" ):
                listener.exitLatex_cmd_arg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLatex_cmd_arg" ):
                return visitor.visitLatex_cmd_arg(self)
            else:
                return visitor.visitChildren(self)




    def latex_cmd_arg(self):

        localctx = ExprGrammar.Latex_cmd_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_latex_cmd_arg)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28, 29, 30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138
                localctx._atom = self.atom()
                localctx.res = localctx._atom.res 
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(ExprGrammar.LBRACE)
                self.state = 142
                localctx._expr = self.expr(0)
                self.state = 143
                self.match(ExprGrammar.RBRACE)
                localctx.res = localctx._expr.res
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Limit_dirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(ExprGrammar.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ExprGrammar.RBRACE, 0)

        def PLUS(self):
            return self.getToken(ExprGrammar.PLUS, 0)

        def MINUS(self):
            return self.getToken(ExprGrammar.MINUS, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_limit_dir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimit_dir" ):
                listener.enterLimit_dir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimit_dir" ):
                listener.exitLimit_dir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLimit_dir" ):
                return visitor.visitLimit_dir(self)
            else:
                return visitor.visitChildren(self)




    def limit_dir(self):

        localctx = ExprGrammar.Limit_dirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_limit_dir)
        self._la = 0 # Token type
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.match(ExprGrammar.LBRACE)
                self.state = 149
                _la = self._input.LA(1)
                if not(_la==4 or _la==5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 150
                self.match(ExprGrammar.RBRACE)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.match(ExprGrammar.PLUS)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 152
                self.match(ExprGrammar.MINUS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Series_range_argsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.symb = None
            self.start = None
            self.end = None
            self._SYMBOL = None # Token
            self._expr = None # ExprContext
            self._latex_cmd_arg = None # Latex_cmd_argContext

        def UNDERSCORE(self):
            return self.getToken(ExprGrammar.UNDERSCORE, 0)

        def LBRACE(self):
            return self.getToken(ExprGrammar.LBRACE, 0)

        def SYMBOL(self):
            return self.getToken(ExprGrammar.SYMBOL, 0)

        def EQUAL(self):
            return self.getToken(ExprGrammar.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprGrammar.ExprContext,0)


        def RBRACE(self):
            return self.getToken(ExprGrammar.RBRACE, 0)

        def POW(self):
            return self.getToken(ExprGrammar.POW, 0)

        def latex_cmd_arg(self):
            return self.getTypedRuleContext(ExprGrammar.Latex_cmd_argContext,0)


        def getRuleIndex(self):
            return ExprGrammar.RULE_series_range_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeries_range_args" ):
                listener.enterSeries_range_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeries_range_args" ):
                listener.exitSeries_range_args(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeries_range_args" ):
                return visitor.visitSeries_range_args(self)
            else:
                return visitor.visitChildren(self)




    def series_range_args(self):

        localctx = ExprGrammar.Series_range_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_series_range_args)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 156
                self.match(ExprGrammar.LBRACE)
                self.state = 157
                localctx._SYMBOL = self.match(ExprGrammar.SYMBOL)
                self.state = 158
                self.match(ExprGrammar.EQUAL)
                self.state = 159
                localctx._expr = self.expr(0)
                self.state = 160
                self.match(ExprGrammar.RBRACE)
                self.state = 161
                self.match(ExprGrammar.POW)
                self.state = 162
                localctx._latex_cmd_arg = self.latex_cmd_arg()

                localctx.symb = Ast.Symbol(localctx, (None if localctx._SYMBOL is None else localctx._SYMBOL.text))
                localctx.start = localctx._expr.res
                localctx.end = localctx._latex_cmd_arg.res

                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.match(ExprGrammar.POW)
                self.state = 166
                localctx._latex_cmd_arg = self.latex_cmd_arg()
                self.state = 167
                self.match(ExprGrammar.UNDERSCORE)
                self.state = 168
                self.match(ExprGrammar.LBRACE)
                self.state = 169
                localctx._SYMBOL = self.match(ExprGrammar.SYMBOL)
                self.state = 170
                self.match(ExprGrammar.EQUAL)
                self.state = 171
                localctx._expr = self.expr(0)
                self.state = 172
                self.match(ExprGrammar.RBRACE)

                localctx.symb = Ast.Symbol(localctx, (None if localctx._SYMBOL is None else localctx._SYMBOL.text))
                localctx.start = localctx._expr.res
                localctx.end = localctx._latex_cmd_arg.res

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Hard_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None

        def FRAC(self):
            return self.getToken(ExprGrammar.FRAC, 0)

        def latex_cmd_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.Latex_cmd_argContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.Latex_cmd_argContext,i)


        def BINOM(self):
            return self.getToken(ExprGrammar.BINOM, 0)

        def SQRT(self):
            return self.getToken(ExprGrammar.SQRT, 0)

        def CONJUGATE(self):
            return self.getToken(ExprGrammar.CONJUGATE, 0)

        def VEC_UNIT(self):
            return self.getToken(ExprGrammar.VEC_UNIT, 0)

        def getRuleIndex(self):
            return ExprGrammar.RULE_hard_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHard_func" ):
                listener.enterHard_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHard_func" ):
                listener.exitHard_func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHard_func" ):
                return visitor.visitHard_func(self)
            else:
                return visitor.visitChildren(self)




    def hard_func(self):

        localctx = ExprGrammar.Hard_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_hard_func)
        try:
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(ExprGrammar.FRAC)
                self.state = 178
                self.latex_cmd_arg()
                self.state = 179
                self.latex_cmd_arg()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(ExprGrammar.BINOM)
                self.state = 182
                self.latex_cmd_arg()
                self.state = 183
                self.latex_cmd_arg()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.match(ExprGrammar.SQRT)
                self.state = 186
                self.latex_cmd_arg()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 187
                self.match(ExprGrammar.CONJUGATE)
                self.state = 188
                self.latex_cmd_arg()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 5)
                self.state = 189
                self.match(ExprGrammar.VEC_UNIT)
                self.state = 190
                self.latex_cmd_arg()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self._input.LA(1) not in (self.PLUS, self.MINUS, self.NUMBER)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 14)
         




