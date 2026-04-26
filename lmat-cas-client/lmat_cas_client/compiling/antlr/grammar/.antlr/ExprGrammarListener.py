# Generated from d:/DTU/School/.obsidian/plugins/obsidian-latex-math/lmat-cas-client/lmat_cas_client/compiling/antlr/grammar/ExprGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprGrammar import ExprGrammar
else:
    from ExprGrammar import ExprGrammar

# This class defines a complete listener for a parse tree produced by ExprGrammar.
class ExprGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by ExprGrammar#debug.
    def enterDebug(self, ctx:ExprGrammar.DebugContext):
        pass

    # Exit a parse tree produced by ExprGrammar#debug.
    def exitDebug(self, ctx:ExprGrammar.DebugContext):
        pass


    # Enter a parse tree produced by ExprGrammar#Command.
    def enterCommand(self, ctx:ExprGrammar.CommandContext):
        pass

    # Exit a parse tree produced by ExprGrammar#Command.
    def exitCommand(self, ctx:ExprGrammar.CommandContext):
        pass


    # Enter a parse tree produced by ExprGrammar#MultiplicativeOp.
    def enterMultiplicativeOp(self, ctx:ExprGrammar.MultiplicativeOpContext):
        pass

    # Exit a parse tree produced by ExprGrammar#MultiplicativeOp.
    def exitMultiplicativeOp(self, ctx:ExprGrammar.MultiplicativeOpContext):
        pass


    # Enter a parse tree produced by ExprGrammar#UAdditiveOp.
    def enterUAdditiveOp(self, ctx:ExprGrammar.UAdditiveOpContext):
        pass

    # Exit a parse tree produced by ExprGrammar#UAdditiveOp.
    def exitUAdditiveOp(self, ctx:ExprGrammar.UAdditiveOpContext):
        pass


    # Enter a parse tree produced by ExprGrammar#Primary.
    def enterPrimary(self, ctx:ExprGrammar.PrimaryContext):
        pass

    # Exit a parse tree produced by ExprGrammar#Primary.
    def exitPrimary(self, ctx:ExprGrammar.PrimaryContext):
        pass


    # Enter a parse tree produced by ExprGrammar#AdditiveOp.
    def enterAdditiveOp(self, ctx:ExprGrammar.AdditiveOpContext):
        pass

    # Exit a parse tree produced by ExprGrammar#AdditiveOp.
    def exitAdditiveOp(self, ctx:ExprGrammar.AdditiveOpContext):
        pass


    # Enter a parse tree produced by ExprGrammar#ExponentialOp.
    def enterExponentialOp(self, ctx:ExprGrammar.ExponentialOpContext):
        pass

    # Exit a parse tree produced by ExprGrammar#ExponentialOp.
    def exitExponentialOp(self, ctx:ExprGrammar.ExponentialOpContext):
        pass


    # Enter a parse tree produced by ExprGrammar#Prefix.
    def enterPrefix(self, ctx:ExprGrammar.PrefixContext):
        pass

    # Exit a parse tree produced by ExprGrammar#Prefix.
    def exitPrefix(self, ctx:ExprGrammar.PrefixContext):
        pass


    # Enter a parse tree produced by ExprGrammar#atom.
    def enterAtom(self, ctx:ExprGrammar.AtomContext):
        pass

    # Exit a parse tree produced by ExprGrammar#atom.
    def exitAtom(self, ctx:ExprGrammar.AtomContext):
        pass


    # Enter a parse tree produced by ExprGrammar#function.
    def enterFunction(self, ctx:ExprGrammar.FunctionContext):
        pass

    # Exit a parse tree produced by ExprGrammar#function.
    def exitFunction(self, ctx:ExprGrammar.FunctionContext):
        pass



del ExprGrammar