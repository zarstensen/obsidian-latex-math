# Generated from AlgExprGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AlgExprGrammar import AlgExprGrammar
else:
    from AlgExprGrammar import AlgExprGrammar

from lmat_cas_client.compiling.antlr.ast import AlgStmtAst as Ast
from typing import cast, Type, Callable

def rule_t[T](_t: Type[T], v: T | None = None) -> T:
	return cast(T, v)


# This class defines a complete generic visitor for a parse tree produced by AlgExprGrammar.

class AlgExprGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AlgExprGrammar#debug.
    def visitDebug(self, ctx:AlgExprGrammar.DebugContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#alg_statement.
    def visitAlg_statement(self, ctx:AlgExprGrammar.Alg_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#system_el.
    def visitSystem_el(self, ctx:AlgExprGrammar.System_elContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#system_body.
    def visitSystem_body(self, ctx:AlgExprGrammar.System_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#system_env.
    def visitSystem_env(self, ctx:AlgExprGrammar.System_envContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#system_and_chain.
    def visitSystem_and_chain(self, ctx:AlgExprGrammar.System_and_chainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#system.
    def visitSystem(self, ctx:AlgExprGrammar.SystemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#rel_op.
    def visitRel_op(self, ctx:AlgExprGrammar.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#relation.
    def visitRelation(self, ctx:AlgExprGrammar.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#a_expr.
    def visitA_expr(self, ctx:AlgExprGrammar.A_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#atom_v2.
    def visitAtom_v2(self, ctx:AlgExprGrammar.Atom_v2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#integral.
    def visitIntegral(self, ctx:AlgExprGrammar.IntegralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#derivative.
    def visitDerivative(self, ctx:AlgExprGrammar.DerivativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#limit_expr.
    def visitLimit_expr(self, ctx:AlgExprGrammar.Limit_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#series_expr.
    def visitSeries_expr(self, ctx:AlgExprGrammar.Series_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#atom.
    def visitAtom(self, ctx:AlgExprGrammar.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#latex_cmd_arg.
    def visitLatex_cmd_arg(self, ctx:AlgExprGrammar.Latex_cmd_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#pow_arg.
    def visitPow_arg(self, ctx:AlgExprGrammar.Pow_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#postfix_op.
    def visitPostfix_op(self, ctx:AlgExprGrammar.Postfix_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#func_args.
    def visitFunc_args(self, ctx:AlgExprGrammar.Func_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#range_slot.
    def visitRange_slot(self, ctx:AlgExprGrammar.Range_slotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#all_slot.
    def visitAll_slot(self, ctx:AlgExprGrammar.All_slotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#slot_entry.
    def visitSlot_entry(self, ctx:AlgExprGrammar.Slot_entryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#subscript_arg.
    def visitSubscript_arg(self, ctx:AlgExprGrammar.Subscript_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#int_bounds.
    def visitInt_bounds(self, ctx:AlgExprGrammar.Int_boundsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#diff_var.
    def visitDiff_var(self, ctx:AlgExprGrammar.Diff_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#diff_vars.
    def visitDiff_vars(self, ctx:AlgExprGrammar.Diff_varsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#limit_dir.
    def visitLimit_dir(self, ctx:AlgExprGrammar.Limit_dirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#series_range_args.
    def visitSeries_range_args(self, ctx:AlgExprGrammar.Series_range_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#eval_at_sub_vars.
    def visitEval_at_sub_vars(self, ctx:AlgExprGrammar.Eval_at_sub_varsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#eval_at_arg.
    def visitEval_at_arg(self, ctx:AlgExprGrammar.Eval_at_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#primary_symbol.
    def visitPrimary_symbol(self, ctx:AlgExprGrammar.Primary_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#delta_symbol.
    def visitDelta_symbol(self, ctx:AlgExprGrammar.Delta_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#symbol.
    def visitSymbol(self, ctx:AlgExprGrammar.SymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#delim_expr.
    def visitDelim_expr(self, ctx:AlgExprGrammar.Delim_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#combinatorial.
    def visitCombinatorial(self, ctx:AlgExprGrammar.CombinatorialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#cmd_func.
    def visitCmd_func(self, ctx:AlgExprGrammar.Cmd_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#matrix_row.
    def visitMatrix_row(self, ctx:AlgExprGrammar.Matrix_rowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#matrix_body.
    def visitMatrix_body(self, ctx:AlgExprGrammar.Matrix_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#matrix.
    def visitMatrix(self, ctx:AlgExprGrammar.MatrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgExprGrammar#det_matrix.
    def visitDet_matrix(self, ctx:AlgExprGrammar.Det_matrixContext):
        return self.visitChildren(ctx)



del AlgExprGrammar