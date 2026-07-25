# Generated from DefStmtGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DefStmtGrammar import DefStmtGrammar
else:
    from DefStmtGrammar import DefStmtGrammar

from lmat_cas_client.compiling.antlr.ast import DefStmtAst as DefAst


from lmat_cas_client.compiling.antlr.ast import AlgStmtAst as Ast
from typing import cast, Type, Callable

def rule_t[T](_t: Type[T], v: T | None = None) -> T:
	return cast(T, v)


# This class defines a complete listener for a parse tree produced by DefStmtGrammar.
class DefStmtGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by DefStmtGrammar#debug.
    def enterDebug(self, ctx:DefStmtGrammar.DebugContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#debug.
    def exitDebug(self, ctx:DefStmtGrammar.DebugContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#bindings.
    def enterBindings(self, ctx:DefStmtGrammar.BindingsContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#bindings.
    def exitBindings(self, ctx:DefStmtGrammar.BindingsContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#binding.
    def enterBinding(self, ctx:DefStmtGrammar.BindingContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#binding.
    def exitBinding(self, ctx:DefStmtGrammar.BindingContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#symbol_signature.
    def enterSymbol_signature(self, ctx:DefStmtGrammar.Symbol_signatureContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#symbol_signature.
    def exitSymbol_signature(self, ctx:DefStmtGrammar.Symbol_signatureContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#function_signature.
    def enterFunction_signature(self, ctx:DefStmtGrammar.Function_signatureContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#function_signature.
    def exitFunction_signature(self, ctx:DefStmtGrammar.Function_signatureContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#signature.
    def enterSignature(self, ctx:DefStmtGrammar.SignatureContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#signature.
    def exitSignature(self, ctx:DefStmtGrammar.SignatureContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#definition.
    def enterDefinition(self, ctx:DefStmtGrammar.DefinitionContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#definition.
    def exitDefinition(self, ctx:DefStmtGrammar.DefinitionContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#def_body.
    def enterDef_body(self, ctx:DefStmtGrammar.Def_bodyContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#def_body.
    def exitDef_body(self, ctx:DefStmtGrammar.Def_bodyContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#symbol_assumptions.
    def enterSymbol_assumptions(self, ctx:DefStmtGrammar.Symbol_assumptionsContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#symbol_assumptions.
    def exitSymbol_assumptions(self, ctx:DefStmtGrammar.Symbol_assumptionsContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#function_assumption.
    def enterFunction_assumption(self, ctx:DefStmtGrammar.Function_assumptionContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#function_assumption.
    def exitFunction_assumption(self, ctx:DefStmtGrammar.Function_assumptionContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#assum_body.
    def enterAssum_body(self, ctx:DefStmtGrammar.Assum_bodyContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#assum_body.
    def exitAssum_body(self, ctx:DefStmtGrammar.Assum_bodyContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#set.
    def enterSet(self, ctx:DefStmtGrammar.SetContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#set.
    def exitSet(self, ctx:DefStmtGrammar.SetContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#complex_set.
    def enterComplex_set(self, ctx:DefStmtGrammar.Complex_setContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#complex_set.
    def exitComplex_set(self, ctx:DefStmtGrammar.Complex_setContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#real_set.
    def enterReal_set(self, ctx:DefStmtGrammar.Real_setContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#real_set.
    def exitReal_set(self, ctx:DefStmtGrammar.Real_setContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#imaginary_set.
    def enterImaginary_set(self, ctx:DefStmtGrammar.Imaginary_setContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#imaginary_set.
    def exitImaginary_set(self, ctx:DefStmtGrammar.Imaginary_setContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#rational_set.
    def enterRational_set(self, ctx:DefStmtGrammar.Rational_setContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#rational_set.
    def exitRational_set(self, ctx:DefStmtGrammar.Rational_setContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#integer_set.
    def enterInteger_set(self, ctx:DefStmtGrammar.Integer_setContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#integer_set.
    def exitInteger_set(self, ctx:DefStmtGrammar.Integer_setContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#natural_set.
    def enterNatural_set(self, ctx:DefStmtGrammar.Natural_setContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#natural_set.
    def exitNatural_set(self, ctx:DefStmtGrammar.Natural_setContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#even_set.
    def enterEven_set(self, ctx:DefStmtGrammar.Even_setContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#even_set.
    def exitEven_set(self, ctx:DefStmtGrammar.Even_setContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#odd_set.
    def enterOdd_set(self, ctx:DefStmtGrammar.Odd_setContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#odd_set.
    def exitOdd_set(self, ctx:DefStmtGrammar.Odd_setContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#prime_set.
    def enterPrime_set(self, ctx:DefStmtGrammar.Prime_setContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#prime_set.
    def exitPrime_set(self, ctx:DefStmtGrammar.Prime_setContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#algebraic_set.
    def enterAlgebraic_set(self, ctx:DefStmtGrammar.Algebraic_setContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#algebraic_set.
    def exitAlgebraic_set(self, ctx:DefStmtGrammar.Algebraic_setContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#ext_real_set.
    def enterExt_real_set(self, ctx:DefStmtGrammar.Ext_real_setContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#ext_real_set.
    def exitExt_real_set(self, ctx:DefStmtGrammar.Ext_real_setContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#unordered_set.
    def enterUnordered_set(self, ctx:DefStmtGrammar.Unordered_setContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#unordered_set.
    def exitUnordered_set(self, ctx:DefStmtGrammar.Unordered_setContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#ordered_set.
    def enterOrdered_set(self, ctx:DefStmtGrammar.Ordered_setContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#ordered_set.
    def exitOrdered_set(self, ctx:DefStmtGrammar.Ordered_setContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#positive_set.
    def enterPositive_set(self, ctx:DefStmtGrammar.Positive_setContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#positive_set.
    def exitPositive_set(self, ctx:DefStmtGrammar.Positive_setContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#nonnegative_set.
    def enterNonnegative_set(self, ctx:DefStmtGrammar.Nonnegative_setContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#nonnegative_set.
    def exitNonnegative_set(self, ctx:DefStmtGrammar.Nonnegative_setContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#negative_set.
    def enterNegative_set(self, ctx:DefStmtGrammar.Negative_setContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#negative_set.
    def exitNegative_set(self, ctx:DefStmtGrammar.Negative_setContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#nonpositive_set.
    def enterNonpositive_set(self, ctx:DefStmtGrammar.Nonpositive_setContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#nonpositive_set.
    def exitNonpositive_set(self, ctx:DefStmtGrammar.Nonpositive_setContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#nonzero_natural_set.
    def enterNonzero_natural_set(self, ctx:DefStmtGrammar.Nonzero_natural_setContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#nonzero_natural_set.
    def exitNonzero_natural_set(self, ctx:DefStmtGrammar.Nonzero_natural_setContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#alg_statement.
    def enterAlg_statement(self, ctx:DefStmtGrammar.Alg_statementContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#alg_statement.
    def exitAlg_statement(self, ctx:DefStmtGrammar.Alg_statementContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#system_el.
    def enterSystem_el(self, ctx:DefStmtGrammar.System_elContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#system_el.
    def exitSystem_el(self, ctx:DefStmtGrammar.System_elContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#system_body.
    def enterSystem_body(self, ctx:DefStmtGrammar.System_bodyContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#system_body.
    def exitSystem_body(self, ctx:DefStmtGrammar.System_bodyContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#system_env.
    def enterSystem_env(self, ctx:DefStmtGrammar.System_envContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#system_env.
    def exitSystem_env(self, ctx:DefStmtGrammar.System_envContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#system_and_chain.
    def enterSystem_and_chain(self, ctx:DefStmtGrammar.System_and_chainContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#system_and_chain.
    def exitSystem_and_chain(self, ctx:DefStmtGrammar.System_and_chainContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#system.
    def enterSystem(self, ctx:DefStmtGrammar.SystemContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#system.
    def exitSystem(self, ctx:DefStmtGrammar.SystemContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#rel_op.
    def enterRel_op(self, ctx:DefStmtGrammar.Rel_opContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#rel_op.
    def exitRel_op(self, ctx:DefStmtGrammar.Rel_opContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#relation.
    def enterRelation(self, ctx:DefStmtGrammar.RelationContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#relation.
    def exitRelation(self, ctx:DefStmtGrammar.RelationContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#a_expr.
    def enterA_expr(self, ctx:DefStmtGrammar.A_exprContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#a_expr.
    def exitA_expr(self, ctx:DefStmtGrammar.A_exprContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#mult_expr.
    def enterMult_expr(self, ctx:DefStmtGrammar.Mult_exprContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#mult_expr.
    def exitMult_expr(self, ctx:DefStmtGrammar.Mult_exprContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#primary_a_expr.
    def enterPrimary_a_expr(self, ctx:DefStmtGrammar.Primary_a_exprContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#primary_a_expr.
    def exitPrimary_a_expr(self, ctx:DefStmtGrammar.Primary_a_exprContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#integral.
    def enterIntegral(self, ctx:DefStmtGrammar.IntegralContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#integral.
    def exitIntegral(self, ctx:DefStmtGrammar.IntegralContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#derivative.
    def enterDerivative(self, ctx:DefStmtGrammar.DerivativeContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#derivative.
    def exitDerivative(self, ctx:DefStmtGrammar.DerivativeContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#limit.
    def enterLimit(self, ctx:DefStmtGrammar.LimitContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#limit.
    def exitLimit(self, ctx:DefStmtGrammar.LimitContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#series.
    def enterSeries(self, ctx:DefStmtGrammar.SeriesContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#series.
    def exitSeries(self, ctx:DefStmtGrammar.SeriesContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#eval_at.
    def enterEval_at(self, ctx:DefStmtGrammar.Eval_atContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#eval_at.
    def exitEval_at(self, ctx:DefStmtGrammar.Eval_atContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#atom.
    def enterAtom(self, ctx:DefStmtGrammar.AtomContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#atom.
    def exitAtom(self, ctx:DefStmtGrammar.AtomContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#latex_cmd_arg.
    def enterLatex_cmd_arg(self, ctx:DefStmtGrammar.Latex_cmd_argContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#latex_cmd_arg.
    def exitLatex_cmd_arg(self, ctx:DefStmtGrammar.Latex_cmd_argContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#pow_arg.
    def enterPow_arg(self, ctx:DefStmtGrammar.Pow_argContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#pow_arg.
    def exitPow_arg(self, ctx:DefStmtGrammar.Pow_argContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#postfix_op.
    def enterPostfix_op(self, ctx:DefStmtGrammar.Postfix_opContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#postfix_op.
    def exitPostfix_op(self, ctx:DefStmtGrammar.Postfix_opContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#func_args.
    def enterFunc_args(self, ctx:DefStmtGrammar.Func_argsContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#func_args.
    def exitFunc_args(self, ctx:DefStmtGrammar.Func_argsContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#range_slot.
    def enterRange_slot(self, ctx:DefStmtGrammar.Range_slotContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#range_slot.
    def exitRange_slot(self, ctx:DefStmtGrammar.Range_slotContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#all_slot.
    def enterAll_slot(self, ctx:DefStmtGrammar.All_slotContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#all_slot.
    def exitAll_slot(self, ctx:DefStmtGrammar.All_slotContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#slot_entry.
    def enterSlot_entry(self, ctx:DefStmtGrammar.Slot_entryContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#slot_entry.
    def exitSlot_entry(self, ctx:DefStmtGrammar.Slot_entryContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#subscript_arg.
    def enterSubscript_arg(self, ctx:DefStmtGrammar.Subscript_argContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#subscript_arg.
    def exitSubscript_arg(self, ctx:DefStmtGrammar.Subscript_argContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#int_bounds.
    def enterInt_bounds(self, ctx:DefStmtGrammar.Int_boundsContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#int_bounds.
    def exitInt_bounds(self, ctx:DefStmtGrammar.Int_boundsContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#diff_var.
    def enterDiff_var(self, ctx:DefStmtGrammar.Diff_varContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#diff_var.
    def exitDiff_var(self, ctx:DefStmtGrammar.Diff_varContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#diff_vars.
    def enterDiff_vars(self, ctx:DefStmtGrammar.Diff_varsContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#diff_vars.
    def exitDiff_vars(self, ctx:DefStmtGrammar.Diff_varsContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#limit_dir.
    def enterLimit_dir(self, ctx:DefStmtGrammar.Limit_dirContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#limit_dir.
    def exitLimit_dir(self, ctx:DefStmtGrammar.Limit_dirContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#series_range_args.
    def enterSeries_range_args(self, ctx:DefStmtGrammar.Series_range_argsContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#series_range_args.
    def exitSeries_range_args(self, ctx:DefStmtGrammar.Series_range_argsContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#eval_at_sub_vars.
    def enterEval_at_sub_vars(self, ctx:DefStmtGrammar.Eval_at_sub_varsContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#eval_at_sub_vars.
    def exitEval_at_sub_vars(self, ctx:DefStmtGrammar.Eval_at_sub_varsContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#eval_at_arg.
    def enterEval_at_arg(self, ctx:DefStmtGrammar.Eval_at_argContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#eval_at_arg.
    def exitEval_at_arg(self, ctx:DefStmtGrammar.Eval_at_argContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#primary_symbol.
    def enterPrimary_symbol(self, ctx:DefStmtGrammar.Primary_symbolContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#primary_symbol.
    def exitPrimary_symbol(self, ctx:DefStmtGrammar.Primary_symbolContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#delta_symbol.
    def enterDelta_symbol(self, ctx:DefStmtGrammar.Delta_symbolContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#delta_symbol.
    def exitDelta_symbol(self, ctx:DefStmtGrammar.Delta_symbolContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#symbol.
    def enterSymbol(self, ctx:DefStmtGrammar.SymbolContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#symbol.
    def exitSymbol(self, ctx:DefStmtGrammar.SymbolContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#delim_expr.
    def enterDelim_expr(self, ctx:DefStmtGrammar.Delim_exprContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#delim_expr.
    def exitDelim_expr(self, ctx:DefStmtGrammar.Delim_exprContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#combinatorial.
    def enterCombinatorial(self, ctx:DefStmtGrammar.CombinatorialContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#combinatorial.
    def exitCombinatorial(self, ctx:DefStmtGrammar.CombinatorialContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#cmd_func.
    def enterCmd_func(self, ctx:DefStmtGrammar.Cmd_funcContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#cmd_func.
    def exitCmd_func(self, ctx:DefStmtGrammar.Cmd_funcContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#matrix_row.
    def enterMatrix_row(self, ctx:DefStmtGrammar.Matrix_rowContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#matrix_row.
    def exitMatrix_row(self, ctx:DefStmtGrammar.Matrix_rowContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#matrix_body.
    def enterMatrix_body(self, ctx:DefStmtGrammar.Matrix_bodyContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#matrix_body.
    def exitMatrix_body(self, ctx:DefStmtGrammar.Matrix_bodyContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#matrix.
    def enterMatrix(self, ctx:DefStmtGrammar.MatrixContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#matrix.
    def exitMatrix(self, ctx:DefStmtGrammar.MatrixContext):
        pass


    # Enter a parse tree produced by DefStmtGrammar#det_matrix.
    def enterDet_matrix(self, ctx:DefStmtGrammar.Det_matrixContext):
        pass

    # Exit a parse tree produced by DefStmtGrammar#det_matrix.
    def exitDet_matrix(self, ctx:DefStmtGrammar.Det_matrixContext):
        pass



del DefStmtGrammar