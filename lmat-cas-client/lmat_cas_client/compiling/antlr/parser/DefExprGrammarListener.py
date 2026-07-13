# Generated from DefExprGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DefExprGrammar import DefExprGrammar
else:
    from DefExprGrammar import DefExprGrammar

from lmat_cas_client.compiling.antlr.ast import DefStmtAst as DefAst


from lmat_cas_client.compiling.antlr.ast import AlgStmtAst as Ast
from typing import cast, Type, Callable

def rule_t[T](_t: Type[T], v: T | None = None) -> T:
	return cast(T, v)


# This class defines a complete listener for a parse tree produced by DefExprGrammar.
class DefExprGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by DefExprGrammar#debug.
    def enterDebug(self, ctx:DefExprGrammar.DebugContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#debug.
    def exitDebug(self, ctx:DefExprGrammar.DebugContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#bindings.
    def enterBindings(self, ctx:DefExprGrammar.BindingsContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#bindings.
    def exitBindings(self, ctx:DefExprGrammar.BindingsContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#binding.
    def enterBinding(self, ctx:DefExprGrammar.BindingContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#binding.
    def exitBinding(self, ctx:DefExprGrammar.BindingContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#definition.
    def enterDefinition(self, ctx:DefExprGrammar.DefinitionContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#definition.
    def exitDefinition(self, ctx:DefExprGrammar.DefinitionContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#def_body.
    def enterDef_body(self, ctx:DefExprGrammar.Def_bodyContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#def_body.
    def exitDef_body(self, ctx:DefExprGrammar.Def_bodyContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#symbol_assumption.
    def enterSymbol_assumption(self, ctx:DefExprGrammar.Symbol_assumptionContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#symbol_assumption.
    def exitSymbol_assumption(self, ctx:DefExprGrammar.Symbol_assumptionContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#function_assumption.
    def enterFunction_assumption(self, ctx:DefExprGrammar.Function_assumptionContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#function_assumption.
    def exitFunction_assumption(self, ctx:DefExprGrammar.Function_assumptionContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#assum_body.
    def enterAssum_body(self, ctx:DefExprGrammar.Assum_bodyContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#assum_body.
    def exitAssum_body(self, ctx:DefExprGrammar.Assum_bodyContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#set.
    def enterSet(self, ctx:DefExprGrammar.SetContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#set.
    def exitSet(self, ctx:DefExprGrammar.SetContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#set_complex.
    def enterSet_complex(self, ctx:DefExprGrammar.Set_complexContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#set_complex.
    def exitSet_complex(self, ctx:DefExprGrammar.Set_complexContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#set_real.
    def enterSet_real(self, ctx:DefExprGrammar.Set_realContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#set_real.
    def exitSet_real(self, ctx:DefExprGrammar.Set_realContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#set_imaginary.
    def enterSet_imaginary(self, ctx:DefExprGrammar.Set_imaginaryContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#set_imaginary.
    def exitSet_imaginary(self, ctx:DefExprGrammar.Set_imaginaryContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#set_rational.
    def enterSet_rational(self, ctx:DefExprGrammar.Set_rationalContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#set_rational.
    def exitSet_rational(self, ctx:DefExprGrammar.Set_rationalContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#set_integer.
    def enterSet_integer(self, ctx:DefExprGrammar.Set_integerContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#set_integer.
    def exitSet_integer(self, ctx:DefExprGrammar.Set_integerContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#set_natural.
    def enterSet_natural(self, ctx:DefExprGrammar.Set_naturalContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#set_natural.
    def exitSet_natural(self, ctx:DefExprGrammar.Set_naturalContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#set_even.
    def enterSet_even(self, ctx:DefExprGrammar.Set_evenContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#set_even.
    def exitSet_even(self, ctx:DefExprGrammar.Set_evenContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#set_odd.
    def enterSet_odd(self, ctx:DefExprGrammar.Set_oddContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#set_odd.
    def exitSet_odd(self, ctx:DefExprGrammar.Set_oddContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#set_prime.
    def enterSet_prime(self, ctx:DefExprGrammar.Set_primeContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#set_prime.
    def exitSet_prime(self, ctx:DefExprGrammar.Set_primeContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#algebraic_set.
    def enterAlgebraic_set(self, ctx:DefExprGrammar.Algebraic_setContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#algebraic_set.
    def exitAlgebraic_set(self, ctx:DefExprGrammar.Algebraic_setContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#ext_real_set.
    def enterExt_real_set(self, ctx:DefExprGrammar.Ext_real_setContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#ext_real_set.
    def exitExt_real_set(self, ctx:DefExprGrammar.Ext_real_setContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#unsigned_set.
    def enterUnsigned_set(self, ctx:DefExprGrammar.Unsigned_setContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#unsigned_set.
    def exitUnsigned_set(self, ctx:DefExprGrammar.Unsigned_setContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#signed_set.
    def enterSigned_set(self, ctx:DefExprGrammar.Signed_setContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#signed_set.
    def exitSigned_set(self, ctx:DefExprGrammar.Signed_setContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#positive_set.
    def enterPositive_set(self, ctx:DefExprGrammar.Positive_setContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#positive_set.
    def exitPositive_set(self, ctx:DefExprGrammar.Positive_setContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#nonnegative_set.
    def enterNonnegative_set(self, ctx:DefExprGrammar.Nonnegative_setContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#nonnegative_set.
    def exitNonnegative_set(self, ctx:DefExprGrammar.Nonnegative_setContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#negative_set.
    def enterNegative_set(self, ctx:DefExprGrammar.Negative_setContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#negative_set.
    def exitNegative_set(self, ctx:DefExprGrammar.Negative_setContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#nonpositive_set.
    def enterNonpositive_set(self, ctx:DefExprGrammar.Nonpositive_setContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#nonpositive_set.
    def exitNonpositive_set(self, ctx:DefExprGrammar.Nonpositive_setContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#natural0_set.
    def enterNatural0_set(self, ctx:DefExprGrammar.Natural0_setContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#natural0_set.
    def exitNatural0_set(self, ctx:DefExprGrammar.Natural0_setContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#alg_statement.
    def enterAlg_statement(self, ctx:DefExprGrammar.Alg_statementContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#alg_statement.
    def exitAlg_statement(self, ctx:DefExprGrammar.Alg_statementContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#system_el.
    def enterSystem_el(self, ctx:DefExprGrammar.System_elContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#system_el.
    def exitSystem_el(self, ctx:DefExprGrammar.System_elContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#system_body.
    def enterSystem_body(self, ctx:DefExprGrammar.System_bodyContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#system_body.
    def exitSystem_body(self, ctx:DefExprGrammar.System_bodyContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#system_env.
    def enterSystem_env(self, ctx:DefExprGrammar.System_envContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#system_env.
    def exitSystem_env(self, ctx:DefExprGrammar.System_envContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#system_and_chain.
    def enterSystem_and_chain(self, ctx:DefExprGrammar.System_and_chainContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#system_and_chain.
    def exitSystem_and_chain(self, ctx:DefExprGrammar.System_and_chainContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#system.
    def enterSystem(self, ctx:DefExprGrammar.SystemContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#system.
    def exitSystem(self, ctx:DefExprGrammar.SystemContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#rel_op.
    def enterRel_op(self, ctx:DefExprGrammar.Rel_opContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#rel_op.
    def exitRel_op(self, ctx:DefExprGrammar.Rel_opContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#relation.
    def enterRelation(self, ctx:DefExprGrammar.RelationContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#relation.
    def exitRelation(self, ctx:DefExprGrammar.RelationContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#a_expr.
    def enterA_expr(self, ctx:DefExprGrammar.A_exprContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#a_expr.
    def exitA_expr(self, ctx:DefExprGrammar.A_exprContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#atom.
    def enterAtom(self, ctx:DefExprGrammar.AtomContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#atom.
    def exitAtom(self, ctx:DefExprGrammar.AtomContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#latex_cmd_arg.
    def enterLatex_cmd_arg(self, ctx:DefExprGrammar.Latex_cmd_argContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#latex_cmd_arg.
    def exitLatex_cmd_arg(self, ctx:DefExprGrammar.Latex_cmd_argContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#pow_arg.
    def enterPow_arg(self, ctx:DefExprGrammar.Pow_argContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#pow_arg.
    def exitPow_arg(self, ctx:DefExprGrammar.Pow_argContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#postfix_op.
    def enterPostfix_op(self, ctx:DefExprGrammar.Postfix_opContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#postfix_op.
    def exitPostfix_op(self, ctx:DefExprGrammar.Postfix_opContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#func_args.
    def enterFunc_args(self, ctx:DefExprGrammar.Func_argsContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#func_args.
    def exitFunc_args(self, ctx:DefExprGrammar.Func_argsContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#range_slot.
    def enterRange_slot(self, ctx:DefExprGrammar.Range_slotContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#range_slot.
    def exitRange_slot(self, ctx:DefExprGrammar.Range_slotContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#all_slot.
    def enterAll_slot(self, ctx:DefExprGrammar.All_slotContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#all_slot.
    def exitAll_slot(self, ctx:DefExprGrammar.All_slotContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#slot_entry.
    def enterSlot_entry(self, ctx:DefExprGrammar.Slot_entryContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#slot_entry.
    def exitSlot_entry(self, ctx:DefExprGrammar.Slot_entryContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#subscript_arg.
    def enterSubscript_arg(self, ctx:DefExprGrammar.Subscript_argContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#subscript_arg.
    def exitSubscript_arg(self, ctx:DefExprGrammar.Subscript_argContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#int_bounds.
    def enterInt_bounds(self, ctx:DefExprGrammar.Int_boundsContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#int_bounds.
    def exitInt_bounds(self, ctx:DefExprGrammar.Int_boundsContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#diff_var.
    def enterDiff_var(self, ctx:DefExprGrammar.Diff_varContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#diff_var.
    def exitDiff_var(self, ctx:DefExprGrammar.Diff_varContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#diff_vars.
    def enterDiff_vars(self, ctx:DefExprGrammar.Diff_varsContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#diff_vars.
    def exitDiff_vars(self, ctx:DefExprGrammar.Diff_varsContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#limit_dir.
    def enterLimit_dir(self, ctx:DefExprGrammar.Limit_dirContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#limit_dir.
    def exitLimit_dir(self, ctx:DefExprGrammar.Limit_dirContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#series_range_args.
    def enterSeries_range_args(self, ctx:DefExprGrammar.Series_range_argsContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#series_range_args.
    def exitSeries_range_args(self, ctx:DefExprGrammar.Series_range_argsContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#eval_at_sub_vars.
    def enterEval_at_sub_vars(self, ctx:DefExprGrammar.Eval_at_sub_varsContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#eval_at_sub_vars.
    def exitEval_at_sub_vars(self, ctx:DefExprGrammar.Eval_at_sub_varsContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#eval_at_arg.
    def enterEval_at_arg(self, ctx:DefExprGrammar.Eval_at_argContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#eval_at_arg.
    def exitEval_at_arg(self, ctx:DefExprGrammar.Eval_at_argContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#primary_symbol.
    def enterPrimary_symbol(self, ctx:DefExprGrammar.Primary_symbolContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#primary_symbol.
    def exitPrimary_symbol(self, ctx:DefExprGrammar.Primary_symbolContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#delta_symbol.
    def enterDelta_symbol(self, ctx:DefExprGrammar.Delta_symbolContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#delta_symbol.
    def exitDelta_symbol(self, ctx:DefExprGrammar.Delta_symbolContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#symbol.
    def enterSymbol(self, ctx:DefExprGrammar.SymbolContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#symbol.
    def exitSymbol(self, ctx:DefExprGrammar.SymbolContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#delim_expr.
    def enterDelim_expr(self, ctx:DefExprGrammar.Delim_exprContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#delim_expr.
    def exitDelim_expr(self, ctx:DefExprGrammar.Delim_exprContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#combinatorial.
    def enterCombinatorial(self, ctx:DefExprGrammar.CombinatorialContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#combinatorial.
    def exitCombinatorial(self, ctx:DefExprGrammar.CombinatorialContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#cmd_func.
    def enterCmd_func(self, ctx:DefExprGrammar.Cmd_funcContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#cmd_func.
    def exitCmd_func(self, ctx:DefExprGrammar.Cmd_funcContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#matrix_row.
    def enterMatrix_row(self, ctx:DefExprGrammar.Matrix_rowContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#matrix_row.
    def exitMatrix_row(self, ctx:DefExprGrammar.Matrix_rowContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#matrix_body.
    def enterMatrix_body(self, ctx:DefExprGrammar.Matrix_bodyContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#matrix_body.
    def exitMatrix_body(self, ctx:DefExprGrammar.Matrix_bodyContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#matrix.
    def enterMatrix(self, ctx:DefExprGrammar.MatrixContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#matrix.
    def exitMatrix(self, ctx:DefExprGrammar.MatrixContext):
        pass


    # Enter a parse tree produced by DefExprGrammar#det_matrix.
    def enterDet_matrix(self, ctx:DefExprGrammar.Det_matrixContext):
        pass

    # Exit a parse tree produced by DefExprGrammar#det_matrix.
    def exitDet_matrix(self, ctx:DefExprGrammar.Det_matrixContext):
        pass



del DefExprGrammar