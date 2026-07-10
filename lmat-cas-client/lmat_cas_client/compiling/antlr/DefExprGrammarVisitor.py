# Generated from DefExprGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DefExprGrammar import DefExprGrammar
else:
    from DefExprGrammar import DefExprGrammar

import lmat_cas_client.compiling.antlr.Ast as Ast
from typing import cast, Type, Callable

def rule_t[T](_t: Type[T], v: T | None = None) -> T:
	return cast(T, v)


# This class defines a complete generic visitor for a parse tree produced by DefExprGrammar.

class DefExprGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DefExprGrammar#debug.
    def visitDebug(self, ctx:DefExprGrammar.DebugContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#alg_statement.
    def visitAlg_statement(self, ctx:DefExprGrammar.Alg_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#system_el.
    def visitSystem_el(self, ctx:DefExprGrammar.System_elContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#system_body.
    def visitSystem_body(self, ctx:DefExprGrammar.System_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#system_env.
    def visitSystem_env(self, ctx:DefExprGrammar.System_envContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#system_and_chain.
    def visitSystem_and_chain(self, ctx:DefExprGrammar.System_and_chainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#system.
    def visitSystem(self, ctx:DefExprGrammar.SystemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#rel_op.
    def visitRel_op(self, ctx:DefExprGrammar.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#relation.
    def visitRelation(self, ctx:DefExprGrammar.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#a_expr.
    def visitA_expr(self, ctx:DefExprGrammar.A_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#atom.
    def visitAtom(self, ctx:DefExprGrammar.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#latex_cmd_arg.
    def visitLatex_cmd_arg(self, ctx:DefExprGrammar.Latex_cmd_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#pow_arg.
    def visitPow_arg(self, ctx:DefExprGrammar.Pow_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#postfix_op.
    def visitPostfix_op(self, ctx:DefExprGrammar.Postfix_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#func_args.
    def visitFunc_args(self, ctx:DefExprGrammar.Func_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#range_slot.
    def visitRange_slot(self, ctx:DefExprGrammar.Range_slotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#all_slot.
    def visitAll_slot(self, ctx:DefExprGrammar.All_slotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#slot_entry.
    def visitSlot_entry(self, ctx:DefExprGrammar.Slot_entryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#subscript_arg.
    def visitSubscript_arg(self, ctx:DefExprGrammar.Subscript_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#int_bounds.
    def visitInt_bounds(self, ctx:DefExprGrammar.Int_boundsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#diff_var.
    def visitDiff_var(self, ctx:DefExprGrammar.Diff_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#diff_vars.
    def visitDiff_vars(self, ctx:DefExprGrammar.Diff_varsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#limit_dir.
    def visitLimit_dir(self, ctx:DefExprGrammar.Limit_dirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#series_range_args.
    def visitSeries_range_args(self, ctx:DefExprGrammar.Series_range_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#eval_at_sub_vars.
    def visitEval_at_sub_vars(self, ctx:DefExprGrammar.Eval_at_sub_varsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#eval_at_arg.
    def visitEval_at_arg(self, ctx:DefExprGrammar.Eval_at_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#primary_symbol.
    def visitPrimary_symbol(self, ctx:DefExprGrammar.Primary_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#delta_symbol.
    def visitDelta_symbol(self, ctx:DefExprGrammar.Delta_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#symbol.
    def visitSymbol(self, ctx:DefExprGrammar.SymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#delim_expr.
    def visitDelim_expr(self, ctx:DefExprGrammar.Delim_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#combinatorial.
    def visitCombinatorial(self, ctx:DefExprGrammar.CombinatorialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#cmd_func.
    def visitCmd_func(self, ctx:DefExprGrammar.Cmd_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#matrix_row.
    def visitMatrix_row(self, ctx:DefExprGrammar.Matrix_rowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#matrix_body.
    def visitMatrix_body(self, ctx:DefExprGrammar.Matrix_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#matrix.
    def visitMatrix(self, ctx:DefExprGrammar.MatrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#det_matrix.
    def visitDet_matrix(self, ctx:DefExprGrammar.Det_matrixContext):
        return self.visitChildren(ctx)



del DefExprGrammar