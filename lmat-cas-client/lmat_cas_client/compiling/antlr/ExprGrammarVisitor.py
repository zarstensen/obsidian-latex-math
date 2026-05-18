# Generated from ExprGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprGrammar import ExprGrammar
else:
    from ExprGrammar import ExprGrammar

import lmat_cas_client.compiling.antlr.Ast as Ast
from typing import cast, Type

def rule_t[T](_t: Type[T], v: T | None = None) -> T:
	return cast(T, v)


# This class defines a complete generic visitor for a parse tree produced by ExprGrammar.

class ExprGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprGrammar#debug.
    def visitDebug(self, ctx:ExprGrammar.DebugContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#a_lmat_expr.
    def visitA_lmat_expr(self, ctx:ExprGrammar.A_lmat_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#system_el.
    def visitSystem_el(self, ctx:ExprGrammar.System_elContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#system_body.
    def visitSystem_body(self, ctx:ExprGrammar.System_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#system_env.
    def visitSystem_env(self, ctx:ExprGrammar.System_envContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#system_and_chain.
    def visitSystem_and_chain(self, ctx:ExprGrammar.System_and_chainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#system.
    def visitSystem(self, ctx:ExprGrammar.SystemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#rel_op.
    def visitRel_op(self, ctx:ExprGrammar.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#relation.
    def visitRelation(self, ctx:ExprGrammar.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#a_expr.
    def visitA_expr(self, ctx:ExprGrammar.A_exprContext):
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


    # Visit a parse tree produced by ExprGrammar#eval_at_sub_vars.
    def visitEval_at_sub_vars(self, ctx:ExprGrammar.Eval_at_sub_varsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#eval_at_arg.
    def visitEval_at_arg(self, ctx:ExprGrammar.Eval_at_argContext):
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


    # Visit a parse tree produced by ExprGrammar#function.
    def visitFunction(self, ctx:ExprGrammar.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#delim_expr.
    def visitDelim_expr(self, ctx:ExprGrammar.Delim_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#combinatorial.
    def visitCombinatorial(self, ctx:ExprGrammar.CombinatorialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#cmd_func.
    def visitCmd_func(self, ctx:ExprGrammar.Cmd_funcContext):
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


    # Visit a parse tree produced by ExprGrammar#det_matrix.
    def visitDet_matrix(self, ctx:ExprGrammar.Det_matrixContext):
        return self.visitChildren(ctx)



del ExprGrammar