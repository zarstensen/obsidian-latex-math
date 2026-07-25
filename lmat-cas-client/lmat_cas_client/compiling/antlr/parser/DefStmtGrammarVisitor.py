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


# This class defines a complete generic visitor for a parse tree produced by DefStmtGrammar.

class DefStmtGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DefStmtGrammar#debug.
    def visitDebug(self, ctx:DefStmtGrammar.DebugContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#bindings.
    def visitBindings(self, ctx:DefStmtGrammar.BindingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#binding.
    def visitBinding(self, ctx:DefStmtGrammar.BindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#symbol_signature.
    def visitSymbol_signature(self, ctx:DefStmtGrammar.Symbol_signatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#function_signature.
    def visitFunction_signature(self, ctx:DefStmtGrammar.Function_signatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#signature.
    def visitSignature(self, ctx:DefStmtGrammar.SignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#definition.
    def visitDefinition(self, ctx:DefStmtGrammar.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#def_body.
    def visitDef_body(self, ctx:DefStmtGrammar.Def_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#symbol_assumptions.
    def visitSymbol_assumptions(self, ctx:DefStmtGrammar.Symbol_assumptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#function_assumption.
    def visitFunction_assumption(self, ctx:DefStmtGrammar.Function_assumptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#assum_body.
    def visitAssum_body(self, ctx:DefStmtGrammar.Assum_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#set.
    def visitSet(self, ctx:DefStmtGrammar.SetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#complex_set.
    def visitComplex_set(self, ctx:DefStmtGrammar.Complex_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#real_set.
    def visitReal_set(self, ctx:DefStmtGrammar.Real_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#imaginary_set.
    def visitImaginary_set(self, ctx:DefStmtGrammar.Imaginary_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#rational_set.
    def visitRational_set(self, ctx:DefStmtGrammar.Rational_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#integer_set.
    def visitInteger_set(self, ctx:DefStmtGrammar.Integer_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#natural_set.
    def visitNatural_set(self, ctx:DefStmtGrammar.Natural_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#even_set.
    def visitEven_set(self, ctx:DefStmtGrammar.Even_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#odd_set.
    def visitOdd_set(self, ctx:DefStmtGrammar.Odd_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#prime_set.
    def visitPrime_set(self, ctx:DefStmtGrammar.Prime_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#algebraic_set.
    def visitAlgebraic_set(self, ctx:DefStmtGrammar.Algebraic_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#ext_real_set.
    def visitExt_real_set(self, ctx:DefStmtGrammar.Ext_real_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#unordered_set.
    def visitUnordered_set(self, ctx:DefStmtGrammar.Unordered_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#ordered_set.
    def visitOrdered_set(self, ctx:DefStmtGrammar.Ordered_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#positive_set.
    def visitPositive_set(self, ctx:DefStmtGrammar.Positive_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#nonnegative_set.
    def visitNonnegative_set(self, ctx:DefStmtGrammar.Nonnegative_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#negative_set.
    def visitNegative_set(self, ctx:DefStmtGrammar.Negative_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#nonpositive_set.
    def visitNonpositive_set(self, ctx:DefStmtGrammar.Nonpositive_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#nonzero_natural_set.
    def visitNonzero_natural_set(self, ctx:DefStmtGrammar.Nonzero_natural_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#alg_statement.
    def visitAlg_statement(self, ctx:DefStmtGrammar.Alg_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#system_el.
    def visitSystem_el(self, ctx:DefStmtGrammar.System_elContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#system_body.
    def visitSystem_body(self, ctx:DefStmtGrammar.System_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#system_env.
    def visitSystem_env(self, ctx:DefStmtGrammar.System_envContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#system_and_chain.
    def visitSystem_and_chain(self, ctx:DefStmtGrammar.System_and_chainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#system.
    def visitSystem(self, ctx:DefStmtGrammar.SystemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#rel_op.
    def visitRel_op(self, ctx:DefStmtGrammar.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#relation.
    def visitRelation(self, ctx:DefStmtGrammar.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#a_expr.
    def visitA_expr(self, ctx:DefStmtGrammar.A_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#mult_expr.
    def visitMult_expr(self, ctx:DefStmtGrammar.Mult_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#primary_a_expr.
    def visitPrimary_a_expr(self, ctx:DefStmtGrammar.Primary_a_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#integral.
    def visitIntegral(self, ctx:DefStmtGrammar.IntegralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#derivative.
    def visitDerivative(self, ctx:DefStmtGrammar.DerivativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#limit.
    def visitLimit(self, ctx:DefStmtGrammar.LimitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#series.
    def visitSeries(self, ctx:DefStmtGrammar.SeriesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#eval_at.
    def visitEval_at(self, ctx:DefStmtGrammar.Eval_atContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#atom.
    def visitAtom(self, ctx:DefStmtGrammar.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#latex_cmd_arg.
    def visitLatex_cmd_arg(self, ctx:DefStmtGrammar.Latex_cmd_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#pow_arg.
    def visitPow_arg(self, ctx:DefStmtGrammar.Pow_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#postfix_op.
    def visitPostfix_op(self, ctx:DefStmtGrammar.Postfix_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#func_args.
    def visitFunc_args(self, ctx:DefStmtGrammar.Func_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#range_slot.
    def visitRange_slot(self, ctx:DefStmtGrammar.Range_slotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#all_slot.
    def visitAll_slot(self, ctx:DefStmtGrammar.All_slotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#slot_entry.
    def visitSlot_entry(self, ctx:DefStmtGrammar.Slot_entryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#subscript_arg.
    def visitSubscript_arg(self, ctx:DefStmtGrammar.Subscript_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#int_bounds.
    def visitInt_bounds(self, ctx:DefStmtGrammar.Int_boundsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#diff_var.
    def visitDiff_var(self, ctx:DefStmtGrammar.Diff_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#diff_vars.
    def visitDiff_vars(self, ctx:DefStmtGrammar.Diff_varsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#limit_dir.
    def visitLimit_dir(self, ctx:DefStmtGrammar.Limit_dirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#series_range_args.
    def visitSeries_range_args(self, ctx:DefStmtGrammar.Series_range_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#eval_at_sub_vars.
    def visitEval_at_sub_vars(self, ctx:DefStmtGrammar.Eval_at_sub_varsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#eval_at_arg.
    def visitEval_at_arg(self, ctx:DefStmtGrammar.Eval_at_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#primary_symbol.
    def visitPrimary_symbol(self, ctx:DefStmtGrammar.Primary_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#delta_symbol.
    def visitDelta_symbol(self, ctx:DefStmtGrammar.Delta_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#symbol.
    def visitSymbol(self, ctx:DefStmtGrammar.SymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#delim_expr.
    def visitDelim_expr(self, ctx:DefStmtGrammar.Delim_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#combinatorial.
    def visitCombinatorial(self, ctx:DefStmtGrammar.CombinatorialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#cmd_func.
    def visitCmd_func(self, ctx:DefStmtGrammar.Cmd_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#matrix_row.
    def visitMatrix_row(self, ctx:DefStmtGrammar.Matrix_rowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#matrix_body.
    def visitMatrix_body(self, ctx:DefStmtGrammar.Matrix_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#matrix.
    def visitMatrix(self, ctx:DefStmtGrammar.MatrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefStmtGrammar#det_matrix.
    def visitDet_matrix(self, ctx:DefStmtGrammar.Det_matrixContext):
        return self.visitChildren(ctx)



del DefStmtGrammar