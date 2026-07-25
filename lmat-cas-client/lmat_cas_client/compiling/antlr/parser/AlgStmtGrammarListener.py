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


# This class defines a complete listener for a parse tree produced by AlgStmtGrammar.
class AlgStmtGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by AlgStmtGrammar#debug.
    def enterDebug(self, ctx:AlgStmtGrammar.DebugContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#debug.
    def exitDebug(self, ctx:AlgStmtGrammar.DebugContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#alg_statement.
    def enterAlg_statement(self, ctx:AlgStmtGrammar.Alg_statementContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#alg_statement.
    def exitAlg_statement(self, ctx:AlgStmtGrammar.Alg_statementContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#system_el.
    def enterSystem_el(self, ctx:AlgStmtGrammar.System_elContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#system_el.
    def exitSystem_el(self, ctx:AlgStmtGrammar.System_elContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#system_body.
    def enterSystem_body(self, ctx:AlgStmtGrammar.System_bodyContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#system_body.
    def exitSystem_body(self, ctx:AlgStmtGrammar.System_bodyContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#system_env.
    def enterSystem_env(self, ctx:AlgStmtGrammar.System_envContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#system_env.
    def exitSystem_env(self, ctx:AlgStmtGrammar.System_envContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#system_and_chain.
    def enterSystem_and_chain(self, ctx:AlgStmtGrammar.System_and_chainContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#system_and_chain.
    def exitSystem_and_chain(self, ctx:AlgStmtGrammar.System_and_chainContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#system.
    def enterSystem(self, ctx:AlgStmtGrammar.SystemContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#system.
    def exitSystem(self, ctx:AlgStmtGrammar.SystemContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#rel_op.
    def enterRel_op(self, ctx:AlgStmtGrammar.Rel_opContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#rel_op.
    def exitRel_op(self, ctx:AlgStmtGrammar.Rel_opContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#relation.
    def enterRelation(self, ctx:AlgStmtGrammar.RelationContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#relation.
    def exitRelation(self, ctx:AlgStmtGrammar.RelationContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#a_expr.
    def enterA_expr(self, ctx:AlgStmtGrammar.A_exprContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#a_expr.
    def exitA_expr(self, ctx:AlgStmtGrammar.A_exprContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#mult_expr.
    def enterMult_expr(self, ctx:AlgStmtGrammar.Mult_exprContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#mult_expr.
    def exitMult_expr(self, ctx:AlgStmtGrammar.Mult_exprContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#primary_a_expr.
    def enterPrimary_a_expr(self, ctx:AlgStmtGrammar.Primary_a_exprContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#primary_a_expr.
    def exitPrimary_a_expr(self, ctx:AlgStmtGrammar.Primary_a_exprContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#integral.
    def enterIntegral(self, ctx:AlgStmtGrammar.IntegralContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#integral.
    def exitIntegral(self, ctx:AlgStmtGrammar.IntegralContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#derivative.
    def enterDerivative(self, ctx:AlgStmtGrammar.DerivativeContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#derivative.
    def exitDerivative(self, ctx:AlgStmtGrammar.DerivativeContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#limit.
    def enterLimit(self, ctx:AlgStmtGrammar.LimitContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#limit.
    def exitLimit(self, ctx:AlgStmtGrammar.LimitContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#series.
    def enterSeries(self, ctx:AlgStmtGrammar.SeriesContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#series.
    def exitSeries(self, ctx:AlgStmtGrammar.SeriesContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#eval_at.
    def enterEval_at(self, ctx:AlgStmtGrammar.Eval_atContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#eval_at.
    def exitEval_at(self, ctx:AlgStmtGrammar.Eval_atContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#atom.
    def enterAtom(self, ctx:AlgStmtGrammar.AtomContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#atom.
    def exitAtom(self, ctx:AlgStmtGrammar.AtomContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#latex_cmd_arg.
    def enterLatex_cmd_arg(self, ctx:AlgStmtGrammar.Latex_cmd_argContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#latex_cmd_arg.
    def exitLatex_cmd_arg(self, ctx:AlgStmtGrammar.Latex_cmd_argContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#pow_arg.
    def enterPow_arg(self, ctx:AlgStmtGrammar.Pow_argContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#pow_arg.
    def exitPow_arg(self, ctx:AlgStmtGrammar.Pow_argContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#postfix_op.
    def enterPostfix_op(self, ctx:AlgStmtGrammar.Postfix_opContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#postfix_op.
    def exitPostfix_op(self, ctx:AlgStmtGrammar.Postfix_opContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#func_args.
    def enterFunc_args(self, ctx:AlgStmtGrammar.Func_argsContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#func_args.
    def exitFunc_args(self, ctx:AlgStmtGrammar.Func_argsContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#range_slot.
    def enterRange_slot(self, ctx:AlgStmtGrammar.Range_slotContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#range_slot.
    def exitRange_slot(self, ctx:AlgStmtGrammar.Range_slotContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#all_slot.
    def enterAll_slot(self, ctx:AlgStmtGrammar.All_slotContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#all_slot.
    def exitAll_slot(self, ctx:AlgStmtGrammar.All_slotContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#slot_entry.
    def enterSlot_entry(self, ctx:AlgStmtGrammar.Slot_entryContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#slot_entry.
    def exitSlot_entry(self, ctx:AlgStmtGrammar.Slot_entryContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#subscript_arg.
    def enterSubscript_arg(self, ctx:AlgStmtGrammar.Subscript_argContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#subscript_arg.
    def exitSubscript_arg(self, ctx:AlgStmtGrammar.Subscript_argContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#int_bounds.
    def enterInt_bounds(self, ctx:AlgStmtGrammar.Int_boundsContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#int_bounds.
    def exitInt_bounds(self, ctx:AlgStmtGrammar.Int_boundsContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#diff_var.
    def enterDiff_var(self, ctx:AlgStmtGrammar.Diff_varContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#diff_var.
    def exitDiff_var(self, ctx:AlgStmtGrammar.Diff_varContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#diff_vars.
    def enterDiff_vars(self, ctx:AlgStmtGrammar.Diff_varsContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#diff_vars.
    def exitDiff_vars(self, ctx:AlgStmtGrammar.Diff_varsContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#limit_dir.
    def enterLimit_dir(self, ctx:AlgStmtGrammar.Limit_dirContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#limit_dir.
    def exitLimit_dir(self, ctx:AlgStmtGrammar.Limit_dirContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#series_range_args.
    def enterSeries_range_args(self, ctx:AlgStmtGrammar.Series_range_argsContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#series_range_args.
    def exitSeries_range_args(self, ctx:AlgStmtGrammar.Series_range_argsContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#eval_at_sub_vars.
    def enterEval_at_sub_vars(self, ctx:AlgStmtGrammar.Eval_at_sub_varsContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#eval_at_sub_vars.
    def exitEval_at_sub_vars(self, ctx:AlgStmtGrammar.Eval_at_sub_varsContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#eval_at_arg.
    def enterEval_at_arg(self, ctx:AlgStmtGrammar.Eval_at_argContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#eval_at_arg.
    def exitEval_at_arg(self, ctx:AlgStmtGrammar.Eval_at_argContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#primary_symbol.
    def enterPrimary_symbol(self, ctx:AlgStmtGrammar.Primary_symbolContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#primary_symbol.
    def exitPrimary_symbol(self, ctx:AlgStmtGrammar.Primary_symbolContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#delta_symbol.
    def enterDelta_symbol(self, ctx:AlgStmtGrammar.Delta_symbolContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#delta_symbol.
    def exitDelta_symbol(self, ctx:AlgStmtGrammar.Delta_symbolContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#symbol.
    def enterSymbol(self, ctx:AlgStmtGrammar.SymbolContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#symbol.
    def exitSymbol(self, ctx:AlgStmtGrammar.SymbolContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#delim_expr.
    def enterDelim_expr(self, ctx:AlgStmtGrammar.Delim_exprContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#delim_expr.
    def exitDelim_expr(self, ctx:AlgStmtGrammar.Delim_exprContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#combinatorial.
    def enterCombinatorial(self, ctx:AlgStmtGrammar.CombinatorialContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#combinatorial.
    def exitCombinatorial(self, ctx:AlgStmtGrammar.CombinatorialContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#cmd_func.
    def enterCmd_func(self, ctx:AlgStmtGrammar.Cmd_funcContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#cmd_func.
    def exitCmd_func(self, ctx:AlgStmtGrammar.Cmd_funcContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#matrix_row.
    def enterMatrix_row(self, ctx:AlgStmtGrammar.Matrix_rowContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#matrix_row.
    def exitMatrix_row(self, ctx:AlgStmtGrammar.Matrix_rowContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#matrix_body.
    def enterMatrix_body(self, ctx:AlgStmtGrammar.Matrix_bodyContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#matrix_body.
    def exitMatrix_body(self, ctx:AlgStmtGrammar.Matrix_bodyContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#matrix.
    def enterMatrix(self, ctx:AlgStmtGrammar.MatrixContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#matrix.
    def exitMatrix(self, ctx:AlgStmtGrammar.MatrixContext):
        pass


    # Enter a parse tree produced by AlgStmtGrammar#det_matrix.
    def enterDet_matrix(self, ctx:AlgStmtGrammar.Det_matrixContext):
        pass

    # Exit a parse tree produced by AlgStmtGrammar#det_matrix.
    def exitDet_matrix(self, ctx:AlgStmtGrammar.Det_matrixContext):
        pass



del AlgStmtGrammar