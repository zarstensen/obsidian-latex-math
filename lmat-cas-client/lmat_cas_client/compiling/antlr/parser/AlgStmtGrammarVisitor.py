# Generated from AlgStmtGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AlgStmtGrammar import AlgStmtGrammar
else:
    from AlgStmtGrammar import AlgStmtGrammar

from lmat_cas_client.compiling.antlr.ast import AlgStmtAst as Ast
from typing import cast, Type, Callable

def rule_t[T](_t: Type[T], v: T | None = None) -> T:
	return cast(T, v)


# This class defines a complete generic visitor for a parse tree produced by AlgStmtGrammar.

class AlgStmtGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AlgStmtGrammar#debug.
    def visitDebug(self, ctx:AlgStmtGrammar.DebugContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#alg_statement.
    def visitAlg_statement(self, ctx:AlgStmtGrammar.Alg_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#system_el.
    def visitSystem_el(self, ctx:AlgStmtGrammar.System_elContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#system_body.
    def visitSystem_body(self, ctx:AlgStmtGrammar.System_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#system_env.
    def visitSystem_env(self, ctx:AlgStmtGrammar.System_envContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#system_and_chain.
    def visitSystem_and_chain(self, ctx:AlgStmtGrammar.System_and_chainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#system.
    def visitSystem(self, ctx:AlgStmtGrammar.SystemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#rel_op.
    def visitRel_op(self, ctx:AlgStmtGrammar.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#relation.
    def visitRelation(self, ctx:AlgStmtGrammar.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#a_expr.
    def visitA_expr(self, ctx:AlgStmtGrammar.A_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#mult_expr.
    def visitMult_expr(self, ctx:AlgStmtGrammar.Mult_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#primary_a_expr.
    def visitPrimary_a_expr(self, ctx:AlgStmtGrammar.Primary_a_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#integral.
    def visitIntegral(self, ctx:AlgStmtGrammar.IntegralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#derivative.
    def visitDerivative(self, ctx:AlgStmtGrammar.DerivativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#limit.
    def visitLimit(self, ctx:AlgStmtGrammar.LimitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#series.
    def visitSeries(self, ctx:AlgStmtGrammar.SeriesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#eval_at.
    def visitEval_at(self, ctx:AlgStmtGrammar.Eval_atContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#atom.
    def visitAtom(self, ctx:AlgStmtGrammar.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#latex_cmd_arg.
    def visitLatex_cmd_arg(self, ctx:AlgStmtGrammar.Latex_cmd_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#pow_arg.
    def visitPow_arg(self, ctx:AlgStmtGrammar.Pow_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#postfix_op.
    def visitPostfix_op(self, ctx:AlgStmtGrammar.Postfix_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#func_args.
    def visitFunc_args(self, ctx:AlgStmtGrammar.Func_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#range_slot.
    def visitRange_slot(self, ctx:AlgStmtGrammar.Range_slotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#all_slot.
    def visitAll_slot(self, ctx:AlgStmtGrammar.All_slotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#slot_entry.
    def visitSlot_entry(self, ctx:AlgStmtGrammar.Slot_entryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#subscript_arg.
    def visitSubscript_arg(self, ctx:AlgStmtGrammar.Subscript_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#int_bounds.
    def visitInt_bounds(self, ctx:AlgStmtGrammar.Int_boundsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#diff_var.
    def visitDiff_var(self, ctx:AlgStmtGrammar.Diff_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#diff_vars.
    def visitDiff_vars(self, ctx:AlgStmtGrammar.Diff_varsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#limit_dir.
    def visitLimit_dir(self, ctx:AlgStmtGrammar.Limit_dirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#series_range_args.
    def visitSeries_range_args(self, ctx:AlgStmtGrammar.Series_range_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#eval_at_sub_vars.
    def visitEval_at_sub_vars(self, ctx:AlgStmtGrammar.Eval_at_sub_varsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#eval_at_arg.
    def visitEval_at_arg(self, ctx:AlgStmtGrammar.Eval_at_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#primary_symbol.
    def visitPrimary_symbol(self, ctx:AlgStmtGrammar.Primary_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#delta_symbol.
    def visitDelta_symbol(self, ctx:AlgStmtGrammar.Delta_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#symbol.
    def visitSymbol(self, ctx:AlgStmtGrammar.SymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#delim_expr.
    def visitDelim_expr(self, ctx:AlgStmtGrammar.Delim_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#combinatorial.
    def visitCombinatorial(self, ctx:AlgStmtGrammar.CombinatorialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#cmd_func.
    def visitCmd_func(self, ctx:AlgStmtGrammar.Cmd_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#matrix_row.
    def visitMatrix_row(self, ctx:AlgStmtGrammar.Matrix_rowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#matrix_body.
    def visitMatrix_body(self, ctx:AlgStmtGrammar.Matrix_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#matrix.
    def visitMatrix(self, ctx:AlgStmtGrammar.MatrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgStmtGrammar#det_matrix.
    def visitDet_matrix(self, ctx:AlgStmtGrammar.Det_matrixContext):
        return self.visitChildren(ctx)



del AlgStmtGrammar