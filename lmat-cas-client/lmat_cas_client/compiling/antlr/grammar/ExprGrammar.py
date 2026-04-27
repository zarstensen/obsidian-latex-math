# Generated from c:/Users/sblso/Downloads/school/.obsidian/plugins/obsidian-latex-math/lmat-cas-client/lmat_cas_client/compiling/antlr/grammar/ExprGrammar.g4 by ANTLR 4.13.1
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
        4,1,59,143,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,5,1,18,8,1,10,1,12,1,21,9,1,3,1,23,8,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,53,8,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,70,8,1,1,1,1,1,5,1,
        74,8,1,10,1,12,1,77,9,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,85,8,2,1,3,1,
        3,1,3,1,3,1,3,1,3,3,3,93,8,3,1,3,1,3,1,3,1,3,1,3,3,3,100,8,3,1,3,
        1,3,1,3,1,3,1,3,1,3,3,3,108,8,3,1,3,1,3,1,3,1,3,1,3,3,3,115,8,3,
        1,3,1,3,1,3,1,3,1,3,1,3,3,3,123,8,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,
        131,8,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,139,8,3,3,3,141,8,3,1,3,0,1,
        2,4,0,2,4,6,0,4,1,0,3,4,1,0,20,22,1,0,5,6,1,0,23,25,167,0,8,1,0,
        0,0,2,52,1,0,0,0,4,84,1,0,0,0,6,140,1,0,0,0,8,9,3,2,1,0,9,10,5,0,
        0,1,10,1,1,0,0,0,11,12,6,1,-1,0,12,13,5,1,0,0,13,22,5,35,0,0,14,
        19,3,2,1,0,15,16,5,32,0,0,16,18,3,2,1,0,17,15,1,0,0,0,18,21,1,0,
        0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,22,14,
        1,0,0,0,22,23,1,0,0,0,23,24,1,0,0,0,24,53,5,36,0,0,25,26,5,1,0,0,
        26,27,5,33,0,0,27,28,3,2,1,0,28,29,5,34,0,0,29,53,1,0,0,0,30,31,
        5,1,0,0,31,53,3,2,1,10,32,33,7,0,0,0,33,53,3,2,1,7,34,35,7,1,0,0,
        35,36,5,35,0,0,36,37,3,2,1,0,37,38,5,36,0,0,38,53,1,0,0,0,39,40,
        7,1,0,0,40,53,3,2,1,4,41,42,5,17,0,0,42,43,3,2,1,0,43,44,5,18,0,
        0,44,53,1,0,0,0,45,46,5,35,0,0,46,47,3,2,1,0,47,48,5,36,0,0,48,53,
        1,0,0,0,49,50,3,4,2,0,50,51,6,1,-1,0,51,53,1,0,0,0,52,11,1,0,0,0,
        52,25,1,0,0,0,52,30,1,0,0,0,52,32,1,0,0,0,52,34,1,0,0,0,52,39,1,
        0,0,0,52,41,1,0,0,0,52,45,1,0,0,0,52,49,1,0,0,0,53,75,1,0,0,0,54,
        55,10,9,0,0,55,56,7,2,0,0,56,74,3,2,1,10,57,58,10,8,0,0,58,59,7,
        0,0,0,59,74,3,2,1,9,60,61,10,6,0,0,61,74,3,2,1,7,62,63,10,14,0,0,
        63,69,5,7,0,0,64,70,3,4,2,0,65,66,5,33,0,0,66,67,3,2,1,0,67,68,5,
        34,0,0,68,70,1,0,0,0,69,64,1,0,0,0,69,65,1,0,0,0,70,74,1,0,0,0,71,
        72,10,13,0,0,72,74,7,3,0,0,73,54,1,0,0,0,73,57,1,0,0,0,73,60,1,0,
        0,0,73,62,1,0,0,0,73,71,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,
        1,0,0,0,76,3,1,0,0,0,77,75,1,0,0,0,78,79,5,26,0,0,79,85,6,2,-1,0,
        80,81,5,27,0,0,81,85,6,2,-1,0,82,83,5,28,0,0,83,85,6,2,-1,0,84,78,
        1,0,0,0,84,80,1,0,0,0,84,82,1,0,0,0,85,5,1,0,0,0,86,92,5,11,0,0,
        87,93,3,4,2,0,88,89,5,33,0,0,89,90,3,2,1,0,90,91,5,34,0,0,91,93,
        1,0,0,0,92,87,1,0,0,0,92,88,1,0,0,0,93,99,1,0,0,0,94,100,3,4,2,0,
        95,96,5,33,0,0,96,97,3,2,1,0,97,98,5,34,0,0,98,100,1,0,0,0,99,94,
        1,0,0,0,99,95,1,0,0,0,100,141,1,0,0,0,101,107,5,12,0,0,102,108,3,
        4,2,0,103,104,5,33,0,0,104,105,3,2,1,0,105,106,5,34,0,0,106,108,
        1,0,0,0,107,102,1,0,0,0,107,103,1,0,0,0,108,114,1,0,0,0,109,115,
        3,4,2,0,110,111,5,33,0,0,111,112,3,2,1,0,112,113,5,34,0,0,113,115,
        1,0,0,0,114,109,1,0,0,0,114,110,1,0,0,0,115,141,1,0,0,0,116,122,
        5,13,0,0,117,123,3,4,2,0,118,119,5,33,0,0,119,120,3,2,1,0,120,121,
        5,34,0,0,121,123,1,0,0,0,122,117,1,0,0,0,122,118,1,0,0,0,123,141,
        1,0,0,0,124,130,5,14,0,0,125,131,3,4,2,0,126,127,5,33,0,0,127,128,
        3,2,1,0,128,129,5,34,0,0,129,131,1,0,0,0,130,125,1,0,0,0,130,126,
        1,0,0,0,131,141,1,0,0,0,132,138,5,15,0,0,133,139,3,4,2,0,134,135,
        5,33,0,0,135,136,3,2,1,0,136,137,5,34,0,0,137,139,1,0,0,0,138,133,
        1,0,0,0,138,134,1,0,0,0,139,141,1,0,0,0,140,86,1,0,0,0,140,101,1,
        0,0,0,140,116,1,0,0,0,140,124,1,0,0,0,140,132,1,0,0,0,141,7,1,0,
        0,0,15,19,22,52,69,73,75,84,92,99,107,114,122,130,138,140
    ]

class ExprGrammar ( Parser ):

    grammarFileName = "ExprGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "<INVALID>", "<INVALID>", "'^'", "'\\times'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\\sqrt'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\\lim'", "'\\sum'", "'\\prod'", 
                     "'!'", "'\\%'", "'\\textperthousand'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "','", "<INVALID>", "<INVALID>", "'('", 
                     "')'", "'\\{'", "'\\}'", "'\\['", "'\\]'", "'\\lceil'", 
                     "'\\rceil'", "'\\lfloor'", "'\\rfloor'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'&'", "'\\\\'" ]

    symbolicNames = [ "<INVALID>", "FUNCTION", "IGNORE", "PLUS", "MINUS", 
                      "MULT", "DIV", "POW", "TIMES", "CROSS_PROD", "DOT_PROD", 
                      "FRAC", "BINOM", "SQRT", "CONJUGATE", "VEC_UNIT", 
                      "MOD", "INT", "DIFFERENTIAL", "PHYS_PARTIAL_DERIVATIVE", 
                      "LIMIT", "SUM", "PRODUCT", "BANG", "PERCENT", "PERMILLE", 
                      "SYMBOL", "COMMAND", "NUMBER", "BIN_NUMBER", "OCT_NUMBER", 
                      "HEX_NUMBER", "COMMA", "LBRACE", "RBRACE", "LPAREN", 
                      "RPAREN", "LBRACE_LITERAL", "RBRACE_LITERAL", "LBRACKET", 
                      "RBRACKET", "LCEIL", "RCEIL", "LFLOOR", "RFLOOR", 
                      "LANGLE", "RANGLE", "BAR", "DOUBLE_BAR", "BEGIN_MATRIX", 
                      "END_MATRIX", "BEGIN_V_MATRIX", "END_V_MATRIX", "BEGIN_ARRAY", 
                      "END_ARRAY", "BEGIN_ENV", "END_ENV", "ENV_EL_SEP", 
                      "ENV_ROW_SEP", "ARG_WS" ]

    RULE_debug = 0
    RULE_expr = 1
    RULE_atom = 2
    RULE_hard_func = 3

    ruleNames =  [ "debug", "expr", "atom", "hard_func" ]

    EOF = Token.EOF
    FUNCTION=1
    IGNORE=2
    PLUS=3
    MINUS=4
    MULT=5
    DIV=6
    POW=7
    TIMES=8
    CROSS_PROD=9
    DOT_PROD=10
    FRAC=11
    BINOM=12
    SQRT=13
    CONJUGATE=14
    VEC_UNIT=15
    MOD=16
    INT=17
    DIFFERENTIAL=18
    PHYS_PARTIAL_DERIVATIVE=19
    LIMIT=20
    SUM=21
    PRODUCT=22
    BANG=23
    PERCENT=24
    PERMILLE=25
    SYMBOL=26
    COMMAND=27
    NUMBER=28
    BIN_NUMBER=29
    OCT_NUMBER=30
    HEX_NUMBER=31
    COMMA=32
    LBRACE=33
    RBRACE=34
    LPAREN=35
    RPAREN=36
    LBRACE_LITERAL=37
    RBRACE_LITERAL=38
    LBRACKET=39
    RBRACKET=40
    LCEIL=41
    RCEIL=42
    LFLOOR=43
    RFLOOR=44
    LANGLE=45
    RANGLE=46
    BAR=47
    DOUBLE_BAR=48
    BEGIN_MATRIX=49
    END_MATRIX=50
    BEGIN_V_MATRIX=51
    END_V_MATRIX=52
    BEGIN_ARRAY=53
    END_ARRAY=54
    BEGIN_ENV=55
    END_ENV=56
    ENV_EL_SEP=57
    ENV_ROW_SEP=58
    ARG_WS=59

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




    def debug(self):

        localctx = ExprGrammar.DebugContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_debug)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expr(0)
            self.state = 9
            self.match(ExprGrammar.EOF)
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


        def getRuleIndex(self):
            return ExprGrammar.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.res = ctx.res


    class SeriesContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

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
        def LIMIT(self):
            return self.getToken(ExprGrammar.LIMIT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeries" ):
                listener.enterSeries(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeries" ):
                listener.exitSeries(self)


    class CommandContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
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
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)


    class MultiplicativeOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
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


    class UAdditiveOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
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


    class AdditiveOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
            self.lhs = None # ExprContext
            self.rhs = None # ExprContext
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


    class StubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
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


    class ExponentialOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
            self._atom = None # AtomContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.ExprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.ExprContext,i)

        def POW(self):
            return self.getToken(ExprGrammar.POW, 0)
        def atom(self):
            return self.getTypedRuleContext(ExprGrammar.AtomContext,0)

        def LBRACE(self):
            return self.getToken(ExprGrammar.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(ExprGrammar.RBRACE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponentialOp" ):
                listener.enterExponentialOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponentialOp" ):
                listener.exitExponentialOp(self)


    class PrefixContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
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


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
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
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = ExprGrammar.CommandContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 12
                self.match(ExprGrammar.FUNCTION)
                self.state = 13
                self.match(ExprGrammar.LPAREN)
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34836971546) != 0):
                    self.state = 14
                    self.expr(0)
                    self.state = 19
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==32:
                        self.state = 15
                        self.match(ExprGrammar.COMMA)
                        self.state = 16
                        self.expr(0)
                        self.state = 21
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 24
                self.match(ExprGrammar.RPAREN)
                pass

            elif la_ == 2:
                localctx = ExprGrammar.CommandContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(ExprGrammar.FUNCTION)
                self.state = 26
                self.match(ExprGrammar.LBRACE)
                self.state = 27
                self.expr(0)
                self.state = 28
                self.match(ExprGrammar.RBRACE)
                pass

            elif la_ == 3:
                localctx = ExprGrammar.CommandContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self.match(ExprGrammar.FUNCTION)
                self.state = 31
                self.expr(10)
                pass

            elif la_ == 4:
                localctx = ExprGrammar.UAdditiveOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 32
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 33
                self.expr(7)
                pass

            elif la_ == 5:
                localctx = ExprGrammar.SeriesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 34
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 35
                self.match(ExprGrammar.LPAREN)
                self.state = 36
                self.expr(0)
                self.state = 37
                self.match(ExprGrammar.RPAREN)
                pass

            elif la_ == 6:
                localctx = ExprGrammar.SeriesContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 40
                self.expr(4)
                pass

            elif la_ == 7:
                localctx = ExprGrammar.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 41
                self.match(ExprGrammar.INT)
                self.state = 42
                self.expr(0)
                self.state = 43
                self.match(ExprGrammar.DIFFERENTIAL)
                pass

            elif la_ == 8:
                localctx = ExprGrammar.StubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.match(ExprGrammar.LPAREN)
                self.state = 46
                self.expr(0)
                self.state = 47
                self.match(ExprGrammar.RPAREN)
                pass

            elif la_ == 9:
                localctx = ExprGrammar.StubContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 49
                localctx._atom = self.atom()
                localctx.res = localctx._atom.res 
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 75
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 73
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = ExprGrammar.MultiplicativeOpContext(self, ExprGrammar.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 54
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 55
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 56
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = ExprGrammar.AdditiveOpContext(self, ExprGrammar.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 57
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 58
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 59
                        localctx.rhs = self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = ExprGrammar.MultiplicativeOpContext(self, ExprGrammar.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 60
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 61
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = ExprGrammar.ExponentialOpContext(self, ExprGrammar.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 62
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 63
                        self.match(ExprGrammar.POW)
                        self.state = 69
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [26, 27, 28]:
                            self.state = 64
                            localctx._atom = self.atom()
                            pass
                        elif token in [33]:
                            self.state = 65
                            self.match(ExprGrammar.LBRACE)
                            self.state = 66
                            self.expr(0)
                            self.state = 67
                            self.match(ExprGrammar.RBRACE)
                            pass
                        else:
                            raise NoViableAltException(self)

                        pass

                    elif la_ == 5:
                        localctx = ExprGrammar.PrefixContext(self, ExprGrammar.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 71
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 72
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 77
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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




    def atom(self):

        localctx = ExprGrammar.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_atom)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                localctx._SYMBOL = self.match(ExprGrammar.SYMBOL)
                localctx.res = Ast.Symbol((None if localctx._SYMBOL is None else localctx._SYMBOL.text))
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                localctx._COMMAND = self.match(ExprGrammar.COMMAND)
                localctx.res = Ast.Symbol((None if localctx._COMMAND is None else localctx._COMMAND.text))
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                localctx._NUMBER = self.match(ExprGrammar.NUMBER)
                localctx.res = Ast.Number((None if localctx._NUMBER is None else localctx._NUMBER.text))
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

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.AtomContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.AtomContext,i)


        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.LBRACE)
            else:
                return self.getToken(ExprGrammar.LBRACE, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprGrammar.ExprContext)
            else:
                return self.getTypedRuleContext(ExprGrammar.ExprContext,i)


        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprGrammar.RBRACE)
            else:
                return self.getToken(ExprGrammar.RBRACE, i)

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




    def hard_func(self):

        localctx = ExprGrammar.Hard_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_hard_func)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(ExprGrammar.FRAC)
                self.state = 92
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [26, 27, 28]:
                    self.state = 87
                    self.atom()
                    pass
                elif token in [33]:
                    self.state = 88
                    self.match(ExprGrammar.LBRACE)
                    self.state = 89
                    self.expr(0)
                    self.state = 90
                    self.match(ExprGrammar.RBRACE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 99
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [26, 27, 28]:
                    self.state = 94
                    self.atom()
                    pass
                elif token in [33]:
                    self.state = 95
                    self.match(ExprGrammar.LBRACE)
                    self.state = 96
                    self.expr(0)
                    self.state = 97
                    self.match(ExprGrammar.RBRACE)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.match(ExprGrammar.BINOM)
                self.state = 107
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [26, 27, 28]:
                    self.state = 102
                    self.atom()
                    pass
                elif token in [33]:
                    self.state = 103
                    self.match(ExprGrammar.LBRACE)
                    self.state = 104
                    self.expr(0)
                    self.state = 105
                    self.match(ExprGrammar.RBRACE)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 114
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [26, 27, 28]:
                    self.state = 109
                    self.atom()
                    pass
                elif token in [33]:
                    self.state = 110
                    self.match(ExprGrammar.LBRACE)
                    self.state = 111
                    self.expr(0)
                    self.state = 112
                    self.match(ExprGrammar.RBRACE)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 116
                self.match(ExprGrammar.SQRT)
                self.state = 122
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [26, 27, 28]:
                    self.state = 117
                    self.atom()
                    pass
                elif token in [33]:
                    self.state = 118
                    self.match(ExprGrammar.LBRACE)
                    self.state = 119
                    self.expr(0)
                    self.state = 120
                    self.match(ExprGrammar.RBRACE)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 124
                self.match(ExprGrammar.CONJUGATE)
                self.state = 130
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [26, 27, 28]:
                    self.state = 125
                    self.atom()
                    pass
                elif token in [33]:
                    self.state = 126
                    self.match(ExprGrammar.LBRACE)
                    self.state = 127
                    self.expr(0)
                    self.state = 128
                    self.match(ExprGrammar.RBRACE)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 5)
                self.state = 132
                self.match(ExprGrammar.VEC_UNIT)
                self.state = 138
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [26, 27, 28]:
                    self.state = 133
                    self.atom()
                    pass
                elif token in [33]:
                    self.state = 134
                    self.match(ExprGrammar.LBRACE)
                    self.state = 135
                    self.expr(0)
                    self.state = 136
                    self.match(ExprGrammar.RBRACE)
                    pass
                else:
                    raise NoViableAltException(self)

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
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 13)
         




