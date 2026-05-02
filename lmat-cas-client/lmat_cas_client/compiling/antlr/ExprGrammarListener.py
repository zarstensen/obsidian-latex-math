# Generated from ExprGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprGrammar import ExprGrammar
else:
    from ExprGrammar import ExprGrammar

import lmat_cas_client.compiling.antlr.Ast as Ast


# This class defines a complete listener for a parse tree produced by ExprGrammar.
class ExprGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by ExprGrammar#debug.
    def enterDebug(self, ctx:ExprGrammar.DebugContext):
        pass

    # Exit a parse tree produced by ExprGrammar#debug.
    def exitDebug(self, ctx:ExprGrammar.DebugContext):
        pass


    # Enter a parse tree produced by ExprGrammar#Function.
    def enterFunction(self, ctx:ExprGrammar.FunctionContext):
        pass

    # Exit a parse tree produced by ExprGrammar#Function.
    def exitFunction(self, ctx:ExprGrammar.FunctionContext):
        pass


    # Enter a parse tree produced by ExprGrammar#Series.
    def enterSeries(self, ctx:ExprGrammar.SeriesContext):
        pass

    # Exit a parse tree produced by ExprGrammar#Series.
    def exitSeries(self, ctx:ExprGrammar.SeriesContext):
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


    # Enter a parse tree produced by ExprGrammar#AdditiveOp.
    def enterAdditiveOp(self, ctx:ExprGrammar.AdditiveOpContext):
        pass

    # Exit a parse tree produced by ExprGrammar#AdditiveOp.
    def exitAdditiveOp(self, ctx:ExprGrammar.AdditiveOpContext):
        pass


    # Enter a parse tree produced by ExprGrammar#Stub.
    def enterStub(self, ctx:ExprGrammar.StubContext):
        pass

    # Exit a parse tree produced by ExprGrammar#Stub.
    def exitStub(self, ctx:ExprGrammar.StubContext):
        pass


    # Enter a parse tree produced by ExprGrammar#ExponentialOp.
    def enterExponentialOp(self, ctx:ExprGrammar.ExponentialOpContext):
        pass

    # Exit a parse tree produced by ExprGrammar#ExponentialOp.
    def exitExponentialOp(self, ctx:ExprGrammar.ExponentialOpContext):
        pass


    # Enter a parse tree produced by ExprGrammar#Limit.
    def enterLimit(self, ctx:ExprGrammar.LimitContext):
        pass

    # Exit a parse tree produced by ExprGrammar#Limit.
    def exitLimit(self, ctx:ExprGrammar.LimitContext):
        pass


    # Enter a parse tree produced by ExprGrammar#Prefix.
    def enterPrefix(self, ctx:ExprGrammar.PrefixContext):
        pass

    # Exit a parse tree produced by ExprGrammar#Prefix.
    def exitPrefix(self, ctx:ExprGrammar.PrefixContext):
        pass


    # Enter a parse tree produced by ExprGrammar#Int.
    def enterInt(self, ctx:ExprGrammar.IntContext):
        pass

    # Exit a parse tree produced by ExprGrammar#Int.
    def exitInt(self, ctx:ExprGrammar.IntContext):
        pass


    # Enter a parse tree produced by ExprGrammar#atom.
    def enterAtom(self, ctx:ExprGrammar.AtomContext):
        pass

    # Exit a parse tree produced by ExprGrammar#atom.
    def exitAtom(self, ctx:ExprGrammar.AtomContext):
        pass


    # Enter a parse tree produced by ExprGrammar#latex_cmd_arg.
    def enterLatex_cmd_arg(self, ctx:ExprGrammar.Latex_cmd_argContext):
        pass

    # Exit a parse tree produced by ExprGrammar#latex_cmd_arg.
    def exitLatex_cmd_arg(self, ctx:ExprGrammar.Latex_cmd_argContext):
        pass


    # Enter a parse tree produced by ExprGrammar#limit_dir.
    def enterLimit_dir(self, ctx:ExprGrammar.Limit_dirContext):
        pass

    # Exit a parse tree produced by ExprGrammar#limit_dir.
    def exitLimit_dir(self, ctx:ExprGrammar.Limit_dirContext):
        pass


    # Enter a parse tree produced by ExprGrammar#series_range_args.
    def enterSeries_range_args(self, ctx:ExprGrammar.Series_range_argsContext):
        pass

    # Exit a parse tree produced by ExprGrammar#series_range_args.
    def exitSeries_range_args(self, ctx:ExprGrammar.Series_range_argsContext):
        pass


    # Enter a parse tree produced by ExprGrammar#hard_func.
    def enterHard_func(self, ctx:ExprGrammar.Hard_funcContext):
        pass

    # Exit a parse tree produced by ExprGrammar#hard_func.
    def exitHard_func(self, ctx:ExprGrammar.Hard_funcContext):
        pass



del ExprGrammar