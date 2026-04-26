# Generated from d:/DTU/School/.obsidian/plugins/obsidian-latex-math/lmat-cas-client/lmat_cas_client/compiling/antlr/grammar/ExprGrammar.g4 by ANTLR 4.13.1
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
        4,1,59,75,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,3,1,33,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,3,1,50,8,1,1,1,1,1,5,1,54,8,1,10,1,12,1,57,9,1,1,
        2,1,2,1,3,1,3,1,3,1,3,1,3,5,3,66,8,3,10,3,12,3,69,9,3,3,3,71,8,3,
        1,3,1,3,1,3,0,1,2,4,0,2,4,6,0,4,1,0,3,4,1,0,5,6,1,0,23,25,1,0,26,
        28,84,0,8,1,0,0,0,2,32,1,0,0,0,4,58,1,0,0,0,6,60,1,0,0,0,8,9,3,2,
        1,0,9,10,5,0,0,1,10,1,1,0,0,0,11,12,6,1,-1,0,12,13,5,27,0,0,13,14,
        5,35,0,0,14,15,3,2,1,0,15,16,5,36,0,0,16,33,1,0,0,0,17,18,5,27,0,
        0,18,19,5,33,0,0,19,20,3,2,1,0,20,21,5,34,0,0,21,33,1,0,0,0,22,23,
        5,27,0,0,23,33,3,2,1,8,24,25,7,0,0,0,25,33,3,2,1,5,26,27,5,35,0,
        0,27,28,3,2,1,0,28,29,5,36,0,0,29,33,1,0,0,0,30,33,3,6,3,0,31,33,
        3,4,2,0,32,11,1,0,0,0,32,17,1,0,0,0,32,22,1,0,0,0,32,24,1,0,0,0,
        32,26,1,0,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,55,1,0,0,0,34,35,10,
        7,0,0,35,36,7,1,0,0,36,54,3,2,1,8,37,38,10,6,0,0,38,39,7,0,0,0,39,
        54,3,2,1,7,40,41,10,4,0,0,41,54,3,2,1,5,42,43,10,12,0,0,43,49,5,
        7,0,0,44,50,3,4,2,0,45,46,5,33,0,0,46,47,3,2,1,0,47,48,5,34,0,0,
        48,50,1,0,0,0,49,44,1,0,0,0,49,45,1,0,0,0,50,54,1,0,0,0,51,52,10,
        11,0,0,52,54,7,2,0,0,53,34,1,0,0,0,53,37,1,0,0,0,53,40,1,0,0,0,53,
        42,1,0,0,0,53,51,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,
        0,56,3,1,0,0,0,57,55,1,0,0,0,58,59,7,3,0,0,59,5,1,0,0,0,60,61,5,
        1,0,0,61,70,5,35,0,0,62,67,3,2,1,0,63,64,5,32,0,0,64,66,3,2,1,0,
        65,63,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,71,1,
        0,0,0,69,67,1,0,0,0,70,62,1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,
        73,5,36,0,0,73,7,1,0,0,0,6,32,49,53,55,67,70
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
                     "<INVALID>", "'\\lim'", "'\\sum'", "'\\prod'", "<INVALID>", 
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
                      "FRAC", "BINOM", "FUNC_SQRT", "CONJUGATE", "MOD", 
                      "INT", "DIFFERENTIAL", "PHYS_PARTIAL_DERIVATIVE", 
                      "LIMIT", "SUM", "PRODUCT", "VEC_UNIT", "BANG", "PERCENT", 
                      "PERMILLE", "SYMBOL", "COMMAND", "NUMBER", "BIN_NUMBER", 
                      "OCT_NUMBER", "HEX_NUMBER", "COMMA", "LBRACE", "RBRACE", 
                      "LPAREN", "RPAREN", "LBRACE_LITERAL", "RBRACE_LITERAL", 
                      "LBRACKET", "RBRACKET", "LCEIL", "RCEIL", "LFLOOR", 
                      "RFLOOR", "LANGLE", "RANGLE", "BAR", "DOUBLE_BAR", 
                      "BEGIN_MATRIX", "END_MATRIX", "BEGIN_V_MATRIX", "END_V_MATRIX", 
                      "BEGIN_ARRAY", "END_ARRAY", "BEGIN_ENV", "END_ENV", 
                      "ENV_EL_SEP", "ENV_ROW_SEP", "ARG_WS" ]

    RULE_debug = 0
    RULE_expr = 1
    RULE_atom = 2
    RULE_function = 3

    ruleNames =  [ "debug", "expr", "atom", "function" ]

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
    FUNC_SQRT=13
    CONJUGATE=14
    MOD=15
    INT=16
    DIFFERENTIAL=17
    PHYS_PARTIAL_DERIVATIVE=18
    LIMIT=19
    SUM=20
    PRODUCT=21
    VEC_UNIT=22
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


        def getRuleIndex(self):
            return ExprGrammar.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class CommandContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COMMAND(self):
            return self.getToken(ExprGrammar.COMMAND, 0)
        def LPAREN(self):
            return self.getToken(ExprGrammar.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprGrammar.ExprContext,0)

        def RPAREN(self):
            return self.getToken(ExprGrammar.RPAREN, 0)
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


    class PrimaryContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ExprGrammar.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprGrammar.ExprContext,0)

        def RPAREN(self):
            return self.getToken(ExprGrammar.RPAREN, 0)
        def function(self):
            return self.getTypedRuleContext(ExprGrammar.FunctionContext,0)

        def atom(self):
            return self.getTypedRuleContext(ExprGrammar.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)


    class AdditiveOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
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


    class ExponentialOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprGrammar.ExprContext
            super().__init__(parser)
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
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = ExprGrammar.CommandContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 12
                self.match(ExprGrammar.COMMAND)
                self.state = 13
                self.match(ExprGrammar.LPAREN)
                self.state = 14
                self.expr(0)
                self.state = 15
                self.match(ExprGrammar.RPAREN)
                pass

            elif la_ == 2:
                localctx = ExprGrammar.CommandContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.match(ExprGrammar.COMMAND)
                self.state = 18
                self.match(ExprGrammar.LBRACE)
                self.state = 19
                self.expr(0)
                self.state = 20
                self.match(ExprGrammar.RBRACE)
                pass

            elif la_ == 3:
                localctx = ExprGrammar.CommandContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(ExprGrammar.COMMAND)
                self.state = 23
                self.expr(8)
                pass

            elif la_ == 4:
                localctx = ExprGrammar.UAdditiveOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 25
                self.expr(5)
                pass

            elif la_ == 5:
                localctx = ExprGrammar.PrimaryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(ExprGrammar.LPAREN)
                self.state = 27
                self.expr(0)
                self.state = 28
                self.match(ExprGrammar.RPAREN)
                pass

            elif la_ == 6:
                localctx = ExprGrammar.PrimaryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self.function()
                pass

            elif la_ == 7:
                localctx = ExprGrammar.PrimaryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self.atom()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 55
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 53
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = ExprGrammar.MultiplicativeOpContext(self, ExprGrammar.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 35
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 36
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = ExprGrammar.AdditiveOpContext(self, ExprGrammar.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 38
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 39
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = ExprGrammar.MultiplicativeOpContext(self, ExprGrammar.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 41
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = ExprGrammar.ExponentialOpContext(self, ExprGrammar.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 43
                        self.match(ExprGrammar.POW)
                        self.state = 49
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [26, 27, 28]:
                            self.state = 44
                            self.atom()
                            pass
                        elif token in [33]:
                            self.state = 45
                            self.match(ExprGrammar.LBRACE)
                            self.state = 46
                            self.expr(0)
                            self.state = 47
                            self.match(ExprGrammar.RBRACE)
                            pass
                        else:
                            raise NoViableAltException(self)

                        pass

                    elif la_ == 5:
                        localctx = ExprGrammar.PrefixContext(self, ExprGrammar.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 51
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 52
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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

        def getRuleIndex(self):
            return ExprGrammar.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = ExprGrammar.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(ExprGrammar.FUNCTION)
            self.state = 61
            self.match(ExprGrammar.LPAREN)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34829500442) != 0):
                self.state = 62
                self.expr(0)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==32:
                    self.state = 63
                    self.match(ExprGrammar.COMMA)
                    self.state = 64
                    self.expr(0)
                    self.state = 69
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 72
            self.match(ExprGrammar.RPAREN)
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
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         




