# Generated from ExprGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprGrammar import ExprGrammar
else:
    from ExprGrammar import ExprGrammar

import lmat_cas_client.compiling.antlr.Ast as Ast
from typing import cast


# This class defines a complete generic visitor for a parse tree produced by ExprGrammar.

class ExprGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprGrammar#debug.
    def visitDebug(self, ctx:ExprGrammar.DebugContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#relation.
    def visitRelation(self, ctx:ExprGrammar.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Comb.
    def visitComb(self, ctx:ExprGrammar.CombContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#DelimitedExpr.
    def visitDelimitedExpr(self, ctx:ExprGrammar.DelimitedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#MultiplicativeOp.
    def visitMultiplicativeOp(self, ctx:ExprGrammar.MultiplicativeOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#UAdditiveOp.
    def visitUAdditiveOp(self, ctx:ExprGrammar.UAdditiveOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#IndexPow.
    def visitIndexPow(self, ctx:ExprGrammar.IndexPowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Stub.
    def visitStub(self, ctx:ExprGrammar.StubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Index.
    def visitIndex(self, ctx:ExprGrammar.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Prefix.
    def visitPrefix(self, ctx:ExprGrammar.PrefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Int.
    def visitInt(self, ctx:ExprGrammar.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Function.
    def visitFunction(self, ctx:ExprGrammar.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Series.
    def visitSeries(self, ctx:ExprGrammar.SeriesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Deriv.
    def visitDeriv(self, ctx:ExprGrammar.DerivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#AdditiveOp.
    def visitAdditiveOp(self, ctx:ExprGrammar.AdditiveOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Pow.
    def visitPow(self, ctx:ExprGrammar.PowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Limit.
    def visitLimit(self, ctx:ExprGrammar.LimitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#rel_op.
    def visitRel_op(self, ctx:ExprGrammar.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#atom.
    def visitAtom(self, ctx:ExprGrammar.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#latex_cmd_arg.
    def visitLatex_cmd_arg(self, ctx:ExprGrammar.Latex_cmd_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#pow_arg.
    def visitPow_arg(self, ctx:ExprGrammar.Pow_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#int_bounds.
    def visitInt_bounds(self, ctx:ExprGrammar.Int_boundsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#diff_var.
    def visitDiff_var(self, ctx:ExprGrammar.Diff_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#diff_vars.
    def visitDiff_vars(self, ctx:ExprGrammar.Diff_varsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#limit_dir.
    def visitLimit_dir(self, ctx:ExprGrammar.Limit_dirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#series_range_args.
    def visitSeries_range_args(self, ctx:ExprGrammar.Series_range_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#primary_symbol.
    def visitPrimary_symbol(self, ctx:ExprGrammar.Primary_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#delta_symbol.
    def visitDelta_symbol(self, ctx:ExprGrammar.Delta_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#symbol.
    def visitSymbol(self, ctx:ExprGrammar.SymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#delim_expr.
    def visitDelim_expr(self, ctx:ExprGrammar.Delim_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#combinatorial.
    def visitCombinatorial(self, ctx:ExprGrammar.CombinatorialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#singular_index.
    def visitSingular_index(self, ctx:ExprGrammar.Singular_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#range_index.
    def visitRange_index(self, ctx:ExprGrammar.Range_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#all_index.
    def visitAll_index(self, ctx:ExprGrammar.All_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#index_entry.
    def visitIndex_entry(self, ctx:ExprGrammar.Index_entryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#index_arg.
    def visitIndex_arg(self, ctx:ExprGrammar.Index_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#builtin_func.
    def visitBuiltin_func(self, ctx:ExprGrammar.Builtin_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#matrix_row.
    def visitMatrix_row(self, ctx:ExprGrammar.Matrix_rowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#matrix_body.
    def visitMatrix_body(self, ctx:ExprGrammar.Matrix_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#matrix.
    def visitMatrix(self, ctx:ExprGrammar.MatrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#expr_system_expr.
    def visitExpr_system_expr(self, ctx:ExprGrammar.Expr_system_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#expr_system_body.
    def visitExpr_system_body(self, ctx:ExprGrammar.Expr_system_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#expr_system.
    def visitExpr_system(self, ctx:ExprGrammar.Expr_systemContext):
        return self.visitChildren(ctx)



del ExprGrammar