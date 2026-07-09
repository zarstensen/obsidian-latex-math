# Generated from AlgExprGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AlgExprGrammar import AlgExprGrammar
else:
    from AlgExprGrammar import AlgExprGrammar

import lmat_cas_client.compiling.antlr.Ast as Ast
from typing import cast, Type, Callable

def rule_t[T](_t: Type[T], v: T | None = None) -> T:
	return cast(T, v)


# This class defines a complete listener for a parse tree produced by AlgExprGrammar.
class AlgExprGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by AlgExprGrammar#debug.
    def enterDebug(self, ctx:AlgExprGrammar.DebugContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#debug.
    def exitDebug(self, ctx:AlgExprGrammar.DebugContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#alg_statement.
    def enterAlg_statement(self, ctx:AlgExprGrammar.Alg_statementContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#alg_statement.
    def exitAlg_statement(self, ctx:AlgExprGrammar.Alg_statementContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#system_el.
    def enterSystem_el(self, ctx:AlgExprGrammar.System_elContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#system_el.
    def exitSystem_el(self, ctx:AlgExprGrammar.System_elContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#system_body.
    def enterSystem_body(self, ctx:AlgExprGrammar.System_bodyContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#system_body.
    def exitSystem_body(self, ctx:AlgExprGrammar.System_bodyContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#system_env.
    def enterSystem_env(self, ctx:AlgExprGrammar.System_envContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#system_env.
    def exitSystem_env(self, ctx:AlgExprGrammar.System_envContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#system_and_chain.
    def enterSystem_and_chain(self, ctx:AlgExprGrammar.System_and_chainContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#system_and_chain.
    def exitSystem_and_chain(self, ctx:AlgExprGrammar.System_and_chainContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#system.
    def enterSystem(self, ctx:AlgExprGrammar.SystemContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#system.
    def exitSystem(self, ctx:AlgExprGrammar.SystemContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#rel_op.
    def enterRel_op(self, ctx:AlgExprGrammar.Rel_opContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#rel_op.
    def exitRel_op(self, ctx:AlgExprGrammar.Rel_opContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#relation.
    def enterRelation(self, ctx:AlgExprGrammar.RelationContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#relation.
    def exitRelation(self, ctx:AlgExprGrammar.RelationContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#a_expr.
    def enterA_expr(self, ctx:AlgExprGrammar.A_exprContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#a_expr.
    def exitA_expr(self, ctx:AlgExprGrammar.A_exprContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#atom.
    def enterAtom(self, ctx:AlgExprGrammar.AtomContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#atom.
    def exitAtom(self, ctx:AlgExprGrammar.AtomContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#latex_cmd_arg.
    def enterLatex_cmd_arg(self, ctx:AlgExprGrammar.Latex_cmd_argContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#latex_cmd_arg.
    def exitLatex_cmd_arg(self, ctx:AlgExprGrammar.Latex_cmd_argContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#pow_arg.
    def enterPow_arg(self, ctx:AlgExprGrammar.Pow_argContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#pow_arg.
    def exitPow_arg(self, ctx:AlgExprGrammar.Pow_argContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#postfix_op.
    def enterPostfix_op(self, ctx:AlgExprGrammar.Postfix_opContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#postfix_op.
    def exitPostfix_op(self, ctx:AlgExprGrammar.Postfix_opContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#func_args.
    def enterFunc_args(self, ctx:AlgExprGrammar.Func_argsContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#func_args.
    def exitFunc_args(self, ctx:AlgExprGrammar.Func_argsContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#range_slot.
    def enterRange_slot(self, ctx:AlgExprGrammar.Range_slotContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#range_slot.
    def exitRange_slot(self, ctx:AlgExprGrammar.Range_slotContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#all_slot.
    def enterAll_slot(self, ctx:AlgExprGrammar.All_slotContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#all_slot.
    def exitAll_slot(self, ctx:AlgExprGrammar.All_slotContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#slot_entry.
    def enterSlot_entry(self, ctx:AlgExprGrammar.Slot_entryContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#slot_entry.
    def exitSlot_entry(self, ctx:AlgExprGrammar.Slot_entryContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#subscript_arg.
    def enterSubscript_arg(self, ctx:AlgExprGrammar.Subscript_argContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#subscript_arg.
    def exitSubscript_arg(self, ctx:AlgExprGrammar.Subscript_argContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#int_bounds.
    def enterInt_bounds(self, ctx:AlgExprGrammar.Int_boundsContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#int_bounds.
    def exitInt_bounds(self, ctx:AlgExprGrammar.Int_boundsContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#diff_var.
    def enterDiff_var(self, ctx:AlgExprGrammar.Diff_varContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#diff_var.
    def exitDiff_var(self, ctx:AlgExprGrammar.Diff_varContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#diff_vars.
    def enterDiff_vars(self, ctx:AlgExprGrammar.Diff_varsContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#diff_vars.
    def exitDiff_vars(self, ctx:AlgExprGrammar.Diff_varsContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#limit_dir.
    def enterLimit_dir(self, ctx:AlgExprGrammar.Limit_dirContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#limit_dir.
    def exitLimit_dir(self, ctx:AlgExprGrammar.Limit_dirContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#series_range_args.
    def enterSeries_range_args(self, ctx:AlgExprGrammar.Series_range_argsContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#series_range_args.
    def exitSeries_range_args(self, ctx:AlgExprGrammar.Series_range_argsContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#eval_at_sub_vars.
    def enterEval_at_sub_vars(self, ctx:AlgExprGrammar.Eval_at_sub_varsContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#eval_at_sub_vars.
    def exitEval_at_sub_vars(self, ctx:AlgExprGrammar.Eval_at_sub_varsContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#eval_at_arg.
    def enterEval_at_arg(self, ctx:AlgExprGrammar.Eval_at_argContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#eval_at_arg.
    def exitEval_at_arg(self, ctx:AlgExprGrammar.Eval_at_argContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#primary_symbol.
    def enterPrimary_symbol(self, ctx:AlgExprGrammar.Primary_symbolContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#primary_symbol.
    def exitPrimary_symbol(self, ctx:AlgExprGrammar.Primary_symbolContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#delta_symbol.
    def enterDelta_symbol(self, ctx:AlgExprGrammar.Delta_symbolContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#delta_symbol.
    def exitDelta_symbol(self, ctx:AlgExprGrammar.Delta_symbolContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#symbol.
    def enterSymbol(self, ctx:AlgExprGrammar.SymbolContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#symbol.
    def exitSymbol(self, ctx:AlgExprGrammar.SymbolContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#delim_expr.
    def enterDelim_expr(self, ctx:AlgExprGrammar.Delim_exprContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#delim_expr.
    def exitDelim_expr(self, ctx:AlgExprGrammar.Delim_exprContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#combinatorial.
    def enterCombinatorial(self, ctx:AlgExprGrammar.CombinatorialContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#combinatorial.
    def exitCombinatorial(self, ctx:AlgExprGrammar.CombinatorialContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#cmd_func.
    def enterCmd_func(self, ctx:AlgExprGrammar.Cmd_funcContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#cmd_func.
    def exitCmd_func(self, ctx:AlgExprGrammar.Cmd_funcContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#matrix_row.
    def enterMatrix_row(self, ctx:AlgExprGrammar.Matrix_rowContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#matrix_row.
    def exitMatrix_row(self, ctx:AlgExprGrammar.Matrix_rowContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#matrix_body.
    def enterMatrix_body(self, ctx:AlgExprGrammar.Matrix_bodyContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#matrix_body.
    def exitMatrix_body(self, ctx:AlgExprGrammar.Matrix_bodyContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#matrix.
    def enterMatrix(self, ctx:AlgExprGrammar.MatrixContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#matrix.
    def exitMatrix(self, ctx:AlgExprGrammar.MatrixContext):
        pass


    # Enter a parse tree produced by AlgExprGrammar#det_matrix.
    def enterDet_matrix(self, ctx:AlgExprGrammar.Det_matrixContext):
        pass

    # Exit a parse tree produced by AlgExprGrammar#det_matrix.
    def exitDet_matrix(self, ctx:AlgExprGrammar.Det_matrixContext):
        pass



del AlgExprGrammar