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


# This class defines a complete generic visitor for a parse tree produced by DefExprGrammar.

class DefExprGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DefExprGrammar#debug.
    def visitDebug(self, ctx:DefExprGrammar.DebugContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#bindings.
    def visitBindings(self, ctx:DefExprGrammar.BindingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#binding.
    def visitBinding(self, ctx:DefExprGrammar.BindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#definition.
    def visitDefinition(self, ctx:DefExprGrammar.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#def_body.
    def visitDef_body(self, ctx:DefExprGrammar.Def_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#symbol_assumption.
    def visitSymbol_assumption(self, ctx:DefExprGrammar.Symbol_assumptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#function_assumption.
    def visitFunction_assumption(self, ctx:DefExprGrammar.Function_assumptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#assum_body.
    def visitAssum_body(self, ctx:DefExprGrammar.Assum_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#set.
    def visitSet(self, ctx:DefExprGrammar.SetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#set_complex.
    def visitSet_complex(self, ctx:DefExprGrammar.Set_complexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#set_real.
    def visitSet_real(self, ctx:DefExprGrammar.Set_realContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#set_imaginary.
    def visitSet_imaginary(self, ctx:DefExprGrammar.Set_imaginaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#set_rational.
    def visitSet_rational(self, ctx:DefExprGrammar.Set_rationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#set_integer.
    def visitSet_integer(self, ctx:DefExprGrammar.Set_integerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#set_natural.
    def visitSet_natural(self, ctx:DefExprGrammar.Set_naturalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#set_even.
    def visitSet_even(self, ctx:DefExprGrammar.Set_evenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#set_odd.
    def visitSet_odd(self, ctx:DefExprGrammar.Set_oddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#set_prime.
    def visitSet_prime(self, ctx:DefExprGrammar.Set_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#algebraic_set.
    def visitAlgebraic_set(self, ctx:DefExprGrammar.Algebraic_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#ext_real_set.
    def visitExt_real_set(self, ctx:DefExprGrammar.Ext_real_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#unsigned_set.
    def visitUnsigned_set(self, ctx:DefExprGrammar.Unsigned_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#signed_set.
    def visitSigned_set(self, ctx:DefExprGrammar.Signed_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#positive_set.
    def visitPositive_set(self, ctx:DefExprGrammar.Positive_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#nonnegative_set.
    def visitNonnegative_set(self, ctx:DefExprGrammar.Nonnegative_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#negative_set.
    def visitNegative_set(self, ctx:DefExprGrammar.Negative_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#nonpositive_set.
    def visitNonpositive_set(self, ctx:DefExprGrammar.Nonpositive_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DefExprGrammar#natural0_set.
    def visitNatural0_set(self, ctx:DefExprGrammar.Natural0_setContext):
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