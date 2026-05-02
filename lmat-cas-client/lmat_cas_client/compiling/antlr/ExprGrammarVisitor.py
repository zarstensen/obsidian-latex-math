# Generated from ExprGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprGrammar import ExprGrammar
else:
    from ExprGrammar import ExprGrammar

import lmat_cas_client.compiling.antlr.Ast as Ast


# This class defines a complete generic visitor for a parse tree produced by ExprGrammar.

class ExprGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprGrammar#debug.
    def visitDebug(self, ctx:ExprGrammar.DebugContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Function.
    def visitFunction(self, ctx:ExprGrammar.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Series.
    def visitSeries(self, ctx:ExprGrammar.SeriesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#MultiplicativeOp.
    def visitMultiplicativeOp(self, ctx:ExprGrammar.MultiplicativeOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#UAdditiveOp.
    def visitUAdditiveOp(self, ctx:ExprGrammar.UAdditiveOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#AdditiveOp.
    def visitAdditiveOp(self, ctx:ExprGrammar.AdditiveOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Stub.
    def visitStub(self, ctx:ExprGrammar.StubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#ExponentialOp.
    def visitExponentialOp(self, ctx:ExprGrammar.ExponentialOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Limit.
    def visitLimit(self, ctx:ExprGrammar.LimitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Prefix.
    def visitPrefix(self, ctx:ExprGrammar.PrefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Int.
    def visitInt(self, ctx:ExprGrammar.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#atom.
    def visitAtom(self, ctx:ExprGrammar.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#latex_cmd_arg.
    def visitLatex_cmd_arg(self, ctx:ExprGrammar.Latex_cmd_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#limit_dir.
    def visitLimit_dir(self, ctx:ExprGrammar.Limit_dirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#series_range_args.
    def visitSeries_range_args(self, ctx:ExprGrammar.Series_range_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#hard_func.
    def visitHard_func(self, ctx:ExprGrammar.Hard_funcContext):
        return self.visitChildren(ctx)



del ExprGrammar