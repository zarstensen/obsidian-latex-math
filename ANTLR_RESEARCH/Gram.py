# Generated from d:/DTU/School/.obsidian/plugins/obsidian-latex-math/ANTLR_RESEARCH/Gram.g4 by ANTLR 4.13.1
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
        4,1,17,101,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,26,8,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,35,8,1,1,1,1,1,1,1,1,1,5,1,41,8,1,10,1,12,
        1,44,9,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,52,8,2,1,2,1,2,1,2,1,2,1,2,
        3,2,59,8,2,1,2,4,2,62,8,2,11,2,12,2,63,1,2,1,2,4,2,68,8,2,11,2,12,
        2,69,1,2,4,2,73,8,2,11,2,12,2,74,1,2,1,2,1,2,4,2,80,8,2,11,2,12,
        2,81,1,2,1,2,1,2,1,2,1,2,1,2,3,2,90,8,2,1,2,4,2,93,8,2,11,2,12,2,
        94,3,2,97,8,2,1,3,1,3,1,3,0,1,2,4,0,2,4,6,0,2,1,0,8,9,1,0,13,15,
        117,0,8,1,0,0,0,2,25,1,0,0,0,4,96,1,0,0,0,6,98,1,0,0,0,8,9,3,2,1,
        0,9,10,5,0,0,1,10,1,1,0,0,0,11,12,6,1,-1,0,12,13,5,1,0,0,13,14,3,
        2,1,0,14,15,5,2,0,0,15,26,1,0,0,0,16,17,5,3,0,0,17,18,3,2,1,0,18,
        19,5,4,0,0,19,26,1,0,0,0,20,26,3,4,2,0,21,26,5,15,0,0,22,26,5,13,
        0,0,23,26,5,14,0,0,24,26,5,12,0,0,25,11,1,0,0,0,25,16,1,0,0,0,25,
        20,1,0,0,0,25,21,1,0,0,0,25,22,1,0,0,0,25,23,1,0,0,0,25,24,1,0,0,
        0,26,42,1,0,0,0,27,28,10,8,0,0,28,29,5,5,0,0,29,41,3,2,1,9,30,34,
        10,7,0,0,31,35,5,6,0,0,32,35,5,7,0,0,33,35,1,0,0,0,34,31,1,0,0,0,
        34,32,1,0,0,0,34,33,1,0,0,0,35,36,1,0,0,0,36,41,3,2,1,8,37,38,10,
        6,0,0,38,39,7,0,0,0,39,41,3,2,1,7,40,27,1,0,0,0,40,30,1,0,0,0,40,
        37,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,3,1,0,0,
        0,44,42,1,0,0,0,45,51,5,10,0,0,46,47,5,3,0,0,47,48,3,2,1,0,48,49,
        5,4,0,0,49,52,1,0,0,0,50,52,3,6,3,0,51,46,1,0,0,0,51,50,1,0,0,0,
        52,58,1,0,0,0,53,54,5,3,0,0,54,55,3,2,1,0,55,56,5,4,0,0,56,59,1,
        0,0,0,57,59,3,6,3,0,58,53,1,0,0,0,58,57,1,0,0,0,59,97,1,0,0,0,60,
        62,5,11,0,0,61,60,1,0,0,0,62,63,1,0,0,0,63,61,1,0,0,0,63,64,1,0,
        0,0,64,65,1,0,0,0,65,67,3,2,1,0,66,68,5,12,0,0,67,66,1,0,0,0,68,
        69,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,97,1,0,0,0,71,73,5,11,
        0,0,72,71,1,0,0,0,73,74,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,76,
        1,0,0,0,76,77,5,10,0,0,77,79,5,3,0,0,78,80,5,12,0,0,79,78,1,0,0,
        0,80,81,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,83,1,0,0,0,83,89,
        5,4,0,0,84,85,5,3,0,0,85,86,3,2,1,0,86,87,5,4,0,0,87,90,1,0,0,0,
        88,90,3,6,3,0,89,84,1,0,0,0,89,88,1,0,0,0,90,92,1,0,0,0,91,93,5,
        12,0,0,92,91,1,0,0,0,93,94,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,
        97,1,0,0,0,96,45,1,0,0,0,96,61,1,0,0,0,96,72,1,0,0,0,97,5,1,0,0,
        0,98,99,7,1,0,0,99,7,1,0,0,0,13,25,34,40,42,51,58,63,69,74,81,89,
        94,96
    ]

class Gram ( Parser ):

    grammarFileName = "Gram.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "'}'", "'^'", 
                     "'*'", "'/'", "'+'", "'-'", "<INVALID>", "'int'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "POW", "MUL", "DIV", "PLUS", "MINUS", "FRAC", "INT", 
                      "DX", "NUMBER", "WORD", "COMM", "WS", "ARG_WS" ]

    RULE_debug = 0
    RULE_expr = 1
    RULE_function = 2
    RULE_atom = 3

    ruleNames =  [ "debug", "expr", "function", "atom" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    LBRACE=3
    RBRACE=4
    POW=5
    MUL=6
    DIV=7
    PLUS=8
    MINUS=9
    FRAC=10
    INT=11
    DX=12
    NUMBER=13
    WORD=14
    COMM=15
    WS=16
    ARG_WS=17

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
            return self.getTypedRuleContext(Gram.ExprContext,0)


        def EOF(self):
            return self.getToken(Gram.EOF, 0)

        def getRuleIndex(self):
            return Gram.RULE_debug

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

        localctx = Gram.DebugContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_debug)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expr(0)
            self.state = 9
            self.match(Gram.EOF)
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

        def LPAREN(self):
            return self.getToken(Gram.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Gram.ExprContext)
            else:
                return self.getTypedRuleContext(Gram.ExprContext,i)


        def RPAREN(self):
            return self.getToken(Gram.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(Gram.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(Gram.RBRACE, 0)

        def function(self):
            return self.getTypedRuleContext(Gram.FunctionContext,0)


        def COMM(self):
            return self.getToken(Gram.COMM, 0)

        def NUMBER(self):
            return self.getToken(Gram.NUMBER, 0)

        def WORD(self):
            return self.getToken(Gram.WORD, 0)

        def DX(self):
            return self.getToken(Gram.DX, 0)

        def POW(self):
            return self.getToken(Gram.POW, 0)

        def MUL(self):
            return self.getToken(Gram.MUL, 0)

        def DIV(self):
            return self.getToken(Gram.DIV, 0)

        def PLUS(self):
            return self.getToken(Gram.PLUS, 0)

        def MINUS(self):
            return self.getToken(Gram.MINUS, 0)

        def getRuleIndex(self):
            return Gram.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Gram.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 12
                self.match(Gram.LPAREN)
                self.state = 13
                self.expr(0)
                self.state = 14
                self.match(Gram.RPAREN)
                pass
            elif token in [3]:
                self.state = 16
                self.match(Gram.LBRACE)
                self.state = 17
                self.expr(0)
                self.state = 18
                self.match(Gram.RBRACE)
                pass
            elif token in [10, 11]:
                self.state = 20
                self.function()
                pass
            elif token in [15]:
                self.state = 21
                self.match(Gram.COMM)
                pass
            elif token in [13]:
                self.state = 22
                self.match(Gram.NUMBER)
                pass
            elif token in [14]:
                self.state = 23
                self.match(Gram.WORD)
                pass
            elif token in [12]:
                self.state = 24
                self.match(Gram.DX)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 40
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = Gram.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 27
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 28
                        self.match(Gram.POW)
                        self.state = 29
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = Gram.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 34
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [6]:
                            self.state = 31
                            self.match(Gram.MUL)
                            pass
                        elif token in [7]:
                            self.state = 32
                            self.match(Gram.DIV)
                            pass
                        elif token in [1, 3, 10, 11, 12, 13, 14, 15]:
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 36
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = Gram.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 38
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 39
                        self.expr(7)
                        pass

             
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FRAC(self):
            return self.getToken(Gram.FRAC, 0)

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(Gram.LBRACE)
            else:
                return self.getToken(Gram.LBRACE, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Gram.ExprContext)
            else:
                return self.getTypedRuleContext(Gram.ExprContext,i)


        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(Gram.RBRACE)
            else:
                return self.getToken(Gram.RBRACE, i)

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Gram.AtomContext)
            else:
                return self.getTypedRuleContext(Gram.AtomContext,i)


        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(Gram.INT)
            else:
                return self.getToken(Gram.INT, i)

        def DX(self, i:int=None):
            if i is None:
                return self.getTokens(Gram.DX)
            else:
                return self.getToken(Gram.DX, i)

        def getRuleIndex(self):
            return Gram.RULE_function

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




    def function(self):

        localctx = Gram.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.match(Gram.FRAC)
                self.state = 51
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 46
                    self.match(Gram.LBRACE)
                    self.state = 47
                    self.expr(0)
                    self.state = 48
                    self.match(Gram.RBRACE)
                    pass
                elif token in [13, 14, 15]:
                    self.state = 50
                    self.atom()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 58
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 53
                    self.match(Gram.LBRACE)
                    self.state = 54
                    self.expr(0)
                    self.state = 55
                    self.match(Gram.RBRACE)
                    pass
                elif token in [13, 14, 15]:
                    self.state = 57
                    self.atom()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 60
                        self.match(Gram.INT)

                    else:
                        raise NoViableAltException(self)
                    self.state = 63 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                self.state = 65
                self.expr(0)
                self.state = 67 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 66
                        self.match(Gram.DX)

                    else:
                        raise NoViableAltException(self)
                    self.state = 69 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 71
                    self.match(Gram.INT)
                    self.state = 74 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==11):
                        break

                self.state = 76
                self.match(Gram.FRAC)
                self.state = 77
                self.match(Gram.LBRACE)
                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 78
                    self.match(Gram.DX)
                    self.state = 81 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==12):
                        break

                self.state = 83
                self.match(Gram.RBRACE)
                self.state = 89
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 84
                    self.match(Gram.LBRACE)
                    self.state = 85
                    self.expr(0)
                    self.state = 86
                    self.match(Gram.RBRACE)
                    pass
                elif token in [13, 14, 15]:
                    self.state = 88
                    self.atom()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 92 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 91
                        self.match(Gram.DX)

                    else:
                        raise NoViableAltException(self)
                    self.state = 94 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(Gram.NUMBER, 0)

        def WORD(self):
            return self.getToken(Gram.WORD, 0)

        def COMM(self):
            return self.getToken(Gram.COMM, 0)

        def getRuleIndex(self):
            return Gram.RULE_atom

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

        localctx = Gram.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0)):
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
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         




