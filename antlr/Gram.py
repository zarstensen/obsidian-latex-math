# Generated from d:/DTU/School/.obsidian/plugins/obsidian-latex-math/antlr/Gram.g4 by ANTLR 4.13.1
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
        4,1,14,59,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,1,1,1,1,1,1,
        1,1,1,1,3,1,32,8,1,1,1,1,1,1,1,3,1,37,8,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,46,8,1,1,1,1,1,1,1,1,1,5,1,52,8,1,10,1,12,1,55,9,1,1,2,
        1,2,1,2,0,1,2,3,0,2,4,0,2,1,0,8,9,1,0,11,13,67,0,6,1,0,0,0,2,36,
        1,0,0,0,4,56,1,0,0,0,6,7,3,2,1,0,7,8,5,0,0,1,8,1,1,0,0,0,9,10,6,
        1,-1,0,10,11,5,1,0,0,11,12,3,2,1,0,12,13,5,2,0,0,13,37,1,0,0,0,14,
        15,5,3,0,0,15,16,3,2,1,0,16,17,5,4,0,0,17,37,1,0,0,0,18,24,5,10,
        0,0,19,20,5,3,0,0,20,21,3,2,1,0,21,22,5,4,0,0,22,25,1,0,0,0,23,25,
        3,4,2,0,24,19,1,0,0,0,24,23,1,0,0,0,25,31,1,0,0,0,26,27,5,3,0,0,
        27,28,3,2,1,0,28,29,5,4,0,0,29,32,1,0,0,0,30,32,3,4,2,0,31,26,1,
        0,0,0,31,30,1,0,0,0,32,37,1,0,0,0,33,37,5,13,0,0,34,37,5,11,0,0,
        35,37,5,12,0,0,36,9,1,0,0,0,36,14,1,0,0,0,36,18,1,0,0,0,36,33,1,
        0,0,0,36,34,1,0,0,0,36,35,1,0,0,0,37,53,1,0,0,0,38,39,10,7,0,0,39,
        40,5,5,0,0,40,52,3,2,1,8,41,45,10,6,0,0,42,46,5,6,0,0,43,46,5,7,
        0,0,44,46,1,0,0,0,45,42,1,0,0,0,45,43,1,0,0,0,45,44,1,0,0,0,46,47,
        1,0,0,0,47,52,3,2,1,7,48,49,10,5,0,0,49,50,7,0,0,0,50,52,3,2,1,6,
        51,38,1,0,0,0,51,41,1,0,0,0,51,48,1,0,0,0,52,55,1,0,0,0,53,51,1,
        0,0,0,53,54,1,0,0,0,54,3,1,0,0,0,55,53,1,0,0,0,56,57,7,1,0,0,57,
        5,1,0,0,0,6,24,31,36,45,51,53
    ]

class Gram ( Parser ):

    grammarFileName = "Gram.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "'}'", "'^'", 
                     "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "POW", "MUL", "DIV", "PLUS", "MINUS", "FRAC", "NUMBER", 
                      "WORD", "COMM", "WS" ]

    RULE_debug = 0
    RULE_expr = 1
    RULE_atom = 2

    ruleNames =  [ "debug", "expr", "atom" ]

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
    NUMBER=11
    WORD=12
    COMM=13
    WS=14

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
            self.state = 6
            self.expr(0)
            self.state = 7
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

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(Gram.LBRACE)
            else:
                return self.getToken(Gram.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(Gram.RBRACE)
            else:
                return self.getToken(Gram.RBRACE, i)

        def FRAC(self):
            return self.getToken(Gram.FRAC, 0)

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Gram.AtomContext)
            else:
                return self.getTypedRuleContext(Gram.AtomContext,i)


        def COMM(self):
            return self.getToken(Gram.COMM, 0)

        def NUMBER(self):
            return self.getToken(Gram.NUMBER, 0)

        def WORD(self):
            return self.getToken(Gram.WORD, 0)

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
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 10
                self.match(Gram.LPAREN)
                self.state = 11
                self.expr(0)
                self.state = 12
                self.match(Gram.RPAREN)
                pass
            elif token in [3]:
                self.state = 14
                self.match(Gram.LBRACE)
                self.state = 15
                self.expr(0)
                self.state = 16
                self.match(Gram.RBRACE)
                pass
            elif token in [10]:
                self.state = 18
                self.match(Gram.FRAC)
                self.state = 24
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 19
                    self.match(Gram.LBRACE)
                    self.state = 20
                    self.expr(0)
                    self.state = 21
                    self.match(Gram.RBRACE)
                    pass
                elif token in [11, 12, 13]:
                    self.state = 23
                    self.atom()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 31
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 26
                    self.match(Gram.LBRACE)
                    self.state = 27
                    self.expr(0)
                    self.state = 28
                    self.match(Gram.RBRACE)
                    pass
                elif token in [11, 12, 13]:
                    self.state = 30
                    self.atom()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [13]:
                self.state = 33
                self.match(Gram.COMM)
                pass
            elif token in [11]:
                self.state = 34
                self.match(Gram.NUMBER)
                pass
            elif token in [12]:
                self.state = 35
                self.match(Gram.WORD)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 51
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = Gram.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 39
                        self.match(Gram.POW)
                        self.state = 40
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = Gram.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 45
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [6]:
                            self.state = 42
                            self.match(Gram.MUL)
                            pass
                        elif token in [7]:
                            self.state = 43
                            self.match(Gram.DIV)
                            pass
                        elif token in [1, 3, 10, 11, 12, 13]:
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 47
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = Gram.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 48
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 49
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 50
                        self.expr(6)
                        pass

             
                self.state = 55
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
        self.enterRule(localctx, 4, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
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
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         




