# Generated from ExprGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprGrammar import ExprGrammar
else:
    from ExprGrammar import ExprGrammar

import lmat_cas_client.compiling.antlr.Ast as Ast
from typing import cast, Type

def rule_t[T](t: Type[T], v: T | None = None) -> T:
	return cast(T, v)


# This class defines a complete listener for a parse tree produced by ExprGrammar.
class ExprGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by ExprGrammar#debug.
    def enterDebug(self, ctx:ExprGrammar.DebugContext):
        pass

    # Exit a parse tree produced by ExprGrammar#debug.
    def exitDebug(self, ctx:ExprGrammar.DebugContext):
        pass


    # Enter a parse tree produced by ExprGrammar#a_lmat_expr.
    def enterA_lmat_expr(self, ctx:ExprGrammar.A_lmat_exprContext):
        pass

    # Exit a parse tree produced by ExprGrammar#a_lmat_expr.
    def exitA_lmat_expr(self, ctx:ExprGrammar.A_lmat_exprContext):
        pass


    # Enter a parse tree produced by ExprGrammar#system_el.
    def enterSystem_el(self, ctx:ExprGrammar.System_elContext):
        pass

    # Exit a parse tree produced by ExprGrammar#system_el.
    def exitSystem_el(self, ctx:ExprGrammar.System_elContext):
        pass


    # Enter a parse tree produced by ExprGrammar#system_body.
    def enterSystem_body(self, ctx:ExprGrammar.System_bodyContext):
        pass

    # Exit a parse tree produced by ExprGrammar#system_body.
    def exitSystem_body(self, ctx:ExprGrammar.System_bodyContext):
        pass


    # Enter a parse tree produced by ExprGrammar#system.
    def enterSystem(self, ctx:ExprGrammar.SystemContext):
        pass

    # Exit a parse tree produced by ExprGrammar#system.
    def exitSystem(self, ctx:ExprGrammar.SystemContext):
        pass


    # Enter a parse tree produced by ExprGrammar#relation.
    def enterRelation(self, ctx:ExprGrammar.RelationContext):
        pass

    # Exit a parse tree produced by ExprGrammar#relation.
    def exitRelation(self, ctx:ExprGrammar.RelationContext):
        pass


    # Enter a parse tree produced by ExprGrammar#Comb.
    def enterComb(self, ctx:ExprGrammar.CombContext):
        pass

    # Exit a parse tree produced by ExprGrammar#Comb.
    def exitComb(self, ctx:ExprGrammar.CombContext):
        pass


    # Enter a parse tree produced by ExprGrammar#DelimitedExpr.
    def enterDelimitedExpr(self, ctx:ExprGrammar.DelimitedExprContext):
        pass

    # Exit a parse tree produced by ExprGrammar#DelimitedExpr.
    def exitDelimitedExpr(self, ctx:ExprGrammar.DelimitedExprContext):
        pass


    # Enter a parse tree produced by ExprGrammar#EvalAt.
    def enterEvalAt(self, ctx:ExprGrammar.EvalAtContext):
        pass

    # Exit a parse tree produced by ExprGrammar#EvalAt.
    def exitEvalAt(self, ctx:ExprGrammar.EvalAtContext):
        pass


    # Enter a parse tree produced by ExprGrammar#MultiplicativeOp.
    def enterMultiplicativeOp(self, ctx:ExprGrammar.MultiplicativeOpContext):
        pass

    # Exit a parse tree produced by ExprGrammar#MultiplicativeOp.
    def exitMultiplicativeOp(self, ctx:ExprGrammar.MultiplicativeOpContext):
        pass


    # Enter a parse tree produced by ExprGrammar#UAdditiveOp.
    def enterUAdditiveOp(self, ctx:ExprGrammar.UAdditiveOpContext):
        pass

    # Exit a parse tree produced by ExprGrammar#UAdditiveOp.
    def exitUAdditiveOp(self, ctx:ExprGrammar.UAdditiveOpContext):
        pass


    # Enter a parse tree produced by ExprGrammar#IndexPow.
    def enterIndexPow(self, ctx:ExprGrammar.IndexPowContext):
        pass

    # Exit a parse tree produced by ExprGrammar#IndexPow.
    def exitIndexPow(self, ctx:ExprGrammar.IndexPowContext):
        pass


    # Enter a parse tree produced by ExprGrammar#Stub.
    def enterStub(self, ctx:ExprGrammar.StubContext):
        pass

    # Exit a parse tree produced by ExprGrammar#Stub.
    def exitStub(self, ctx:ExprGrammar.StubContext):
        pass


    # Enter a parse tree produced by ExprGrammar#Index.
    def enterIndex(self, ctx:ExprGrammar.IndexContext):
        pass

    # Exit a parse tree produced by ExprGrammar#Index.
    def exitIndex(self, ctx:ExprGrammar.IndexContext):
        pass


    # Enter a parse tree produced by ExprGrammar#Prefix.
    def enterPrefix(self, ctx:ExprGrammar.PrefixContext):
        pass

    # Exit a parse tree produced by ExprGrammar#Prefix.
    def exitPrefix(self, ctx:ExprGrammar.PrefixContext):
        pass


    # Enter a parse tree produced by ExprGrammar#Int.
    def enterInt(self, ctx:ExprGrammar.IntContext):
        pass

    # Exit a parse tree produced by ExprGrammar#Int.
    def exitInt(self, ctx:ExprGrammar.IntContext):
        pass


    # Enter a parse tree produced by ExprGrammar#Function.
    def enterFunction(self, ctx:ExprGrammar.FunctionContext):
        pass

    # Exit a parse tree produced by ExprGrammar#Function.
    def exitFunction(self, ctx:ExprGrammar.FunctionContext):
        pass


    # Enter a parse tree produced by ExprGrammar#Series.
    def enterSeries(self, ctx:ExprGrammar.SeriesContext):
        pass

    # Exit a parse tree produced by ExprGrammar#Series.
    def exitSeries(self, ctx:ExprGrammar.SeriesContext):
        pass


    # Enter a parse tree produced by ExprGrammar#Deriv.
    def enterDeriv(self, ctx:ExprGrammar.DerivContext):
        pass

    # Exit a parse tree produced by ExprGrammar#Deriv.
    def exitDeriv(self, ctx:ExprGrammar.DerivContext):
        pass


    # Enter a parse tree produced by ExprGrammar#AdditiveOp.
    def enterAdditiveOp(self, ctx:ExprGrammar.AdditiveOpContext):
        pass

    # Exit a parse tree produced by ExprGrammar#AdditiveOp.
    def exitAdditiveOp(self, ctx:ExprGrammar.AdditiveOpContext):
        pass


    # Enter a parse tree produced by ExprGrammar#Pow.
    def enterPow(self, ctx:ExprGrammar.PowContext):
        pass

    # Exit a parse tree produced by ExprGrammar#Pow.
    def exitPow(self, ctx:ExprGrammar.PowContext):
        pass


    # Enter a parse tree produced by ExprGrammar#Limit.
    def enterLimit(self, ctx:ExprGrammar.LimitContext):
        pass

    # Exit a parse tree produced by ExprGrammar#Limit.
    def exitLimit(self, ctx:ExprGrammar.LimitContext):
        pass


    # Enter a parse tree produced by ExprGrammar#rel_op.
    def enterRel_op(self, ctx:ExprGrammar.Rel_opContext):
        pass

    # Exit a parse tree produced by ExprGrammar#rel_op.
    def exitRel_op(self, ctx:ExprGrammar.Rel_opContext):
        pass


    # Enter a parse tree produced by ExprGrammar#atom.
    def enterAtom(self, ctx:ExprGrammar.AtomContext):
        pass

    # Exit a parse tree produced by ExprGrammar#atom.
    def exitAtom(self, ctx:ExprGrammar.AtomContext):
        pass


    # Enter a parse tree produced by ExprGrammar#latex_cmd_arg.
    def enterLatex_cmd_arg(self, ctx:ExprGrammar.Latex_cmd_argContext):
        pass

    # Exit a parse tree produced by ExprGrammar#latex_cmd_arg.
    def exitLatex_cmd_arg(self, ctx:ExprGrammar.Latex_cmd_argContext):
        pass


    # Enter a parse tree produced by ExprGrammar#pow_arg.
    def enterPow_arg(self, ctx:ExprGrammar.Pow_argContext):
        pass

    # Exit a parse tree produced by ExprGrammar#pow_arg.
    def exitPow_arg(self, ctx:ExprGrammar.Pow_argContext):
        pass


    # Enter a parse tree produced by ExprGrammar#range_index.
    def enterRange_index(self, ctx:ExprGrammar.Range_indexContext):
        pass

    # Exit a parse tree produced by ExprGrammar#range_index.
    def exitRange_index(self, ctx:ExprGrammar.Range_indexContext):
        pass


    # Enter a parse tree produced by ExprGrammar#all_index.
    def enterAll_index(self, ctx:ExprGrammar.All_indexContext):
        pass

    # Exit a parse tree produced by ExprGrammar#all_index.
    def exitAll_index(self, ctx:ExprGrammar.All_indexContext):
        pass


    # Enter a parse tree produced by ExprGrammar#index_entry.
    def enterIndex_entry(self, ctx:ExprGrammar.Index_entryContext):
        pass

    # Exit a parse tree produced by ExprGrammar#index_entry.
    def exitIndex_entry(self, ctx:ExprGrammar.Index_entryContext):
        pass


    # Enter a parse tree produced by ExprGrammar#index_arg.
    def enterIndex_arg(self, ctx:ExprGrammar.Index_argContext):
        pass

    # Exit a parse tree produced by ExprGrammar#index_arg.
    def exitIndex_arg(self, ctx:ExprGrammar.Index_argContext):
        pass


    # Enter a parse tree produced by ExprGrammar#int_bounds.
    def enterInt_bounds(self, ctx:ExprGrammar.Int_boundsContext):
        pass

    # Exit a parse tree produced by ExprGrammar#int_bounds.
    def exitInt_bounds(self, ctx:ExprGrammar.Int_boundsContext):
        pass


    # Enter a parse tree produced by ExprGrammar#diff_var.
    def enterDiff_var(self, ctx:ExprGrammar.Diff_varContext):
        pass

    # Exit a parse tree produced by ExprGrammar#diff_var.
    def exitDiff_var(self, ctx:ExprGrammar.Diff_varContext):
        pass


    # Enter a parse tree produced by ExprGrammar#diff_vars.
    def enterDiff_vars(self, ctx:ExprGrammar.Diff_varsContext):
        pass

    # Exit a parse tree produced by ExprGrammar#diff_vars.
    def exitDiff_vars(self, ctx:ExprGrammar.Diff_varsContext):
        pass


    # Enter a parse tree produced by ExprGrammar#limit_dir.
    def enterLimit_dir(self, ctx:ExprGrammar.Limit_dirContext):
        pass

    # Exit a parse tree produced by ExprGrammar#limit_dir.
    def exitLimit_dir(self, ctx:ExprGrammar.Limit_dirContext):
        pass


    # Enter a parse tree produced by ExprGrammar#series_range_args.
    def enterSeries_range_args(self, ctx:ExprGrammar.Series_range_argsContext):
        pass

    # Exit a parse tree produced by ExprGrammar#series_range_args.
    def exitSeries_range_args(self, ctx:ExprGrammar.Series_range_argsContext):
        pass


    # Enter a parse tree produced by ExprGrammar#eval_at_sub_vars.
    def enterEval_at_sub_vars(self, ctx:ExprGrammar.Eval_at_sub_varsContext):
        pass

    # Exit a parse tree produced by ExprGrammar#eval_at_sub_vars.
    def exitEval_at_sub_vars(self, ctx:ExprGrammar.Eval_at_sub_varsContext):
        pass


    # Enter a parse tree produced by ExprGrammar#eval_at_arg.
    def enterEval_at_arg(self, ctx:ExprGrammar.Eval_at_argContext):
        pass

    # Exit a parse tree produced by ExprGrammar#eval_at_arg.
    def exitEval_at_arg(self, ctx:ExprGrammar.Eval_at_argContext):
        pass


    # Enter a parse tree produced by ExprGrammar#primary_symbol.
    def enterPrimary_symbol(self, ctx:ExprGrammar.Primary_symbolContext):
        pass

    # Exit a parse tree produced by ExprGrammar#primary_symbol.
    def exitPrimary_symbol(self, ctx:ExprGrammar.Primary_symbolContext):
        pass


    # Enter a parse tree produced by ExprGrammar#delta_symbol.
    def enterDelta_symbol(self, ctx:ExprGrammar.Delta_symbolContext):
        pass

    # Exit a parse tree produced by ExprGrammar#delta_symbol.
    def exitDelta_symbol(self, ctx:ExprGrammar.Delta_symbolContext):
        pass


    # Enter a parse tree produced by ExprGrammar#symbol.
    def enterSymbol(self, ctx:ExprGrammar.SymbolContext):
        pass

    # Exit a parse tree produced by ExprGrammar#symbol.
    def exitSymbol(self, ctx:ExprGrammar.SymbolContext):
        pass


    # Enter a parse tree produced by ExprGrammar#delim_expr.
    def enterDelim_expr(self, ctx:ExprGrammar.Delim_exprContext):
        pass

    # Exit a parse tree produced by ExprGrammar#delim_expr.
    def exitDelim_expr(self, ctx:ExprGrammar.Delim_exprContext):
        pass


    # Enter a parse tree produced by ExprGrammar#combinatorial.
    def enterCombinatorial(self, ctx:ExprGrammar.CombinatorialContext):
        pass

    # Exit a parse tree produced by ExprGrammar#combinatorial.
    def exitCombinatorial(self, ctx:ExprGrammar.CombinatorialContext):
        pass


    # Enter a parse tree produced by ExprGrammar#cmd_func.
    def enterCmd_func(self, ctx:ExprGrammar.Cmd_funcContext):
        pass

    # Exit a parse tree produced by ExprGrammar#cmd_func.
    def exitCmd_func(self, ctx:ExprGrammar.Cmd_funcContext):
        pass


    # Enter a parse tree produced by ExprGrammar#matrix_row.
    def enterMatrix_row(self, ctx:ExprGrammar.Matrix_rowContext):
        pass

    # Exit a parse tree produced by ExprGrammar#matrix_row.
    def exitMatrix_row(self, ctx:ExprGrammar.Matrix_rowContext):
        pass


    # Enter a parse tree produced by ExprGrammar#matrix_body.
    def enterMatrix_body(self, ctx:ExprGrammar.Matrix_bodyContext):
        pass

    # Exit a parse tree produced by ExprGrammar#matrix_body.
    def exitMatrix_body(self, ctx:ExprGrammar.Matrix_bodyContext):
        pass


    # Enter a parse tree produced by ExprGrammar#matrix.
    def enterMatrix(self, ctx:ExprGrammar.MatrixContext):
        pass

    # Exit a parse tree produced by ExprGrammar#matrix.
    def exitMatrix(self, ctx:ExprGrammar.MatrixContext):
        pass


    # Enter a parse tree produced by ExprGrammar#det_matrix.
    def enterDet_matrix(self, ctx:ExprGrammar.Det_matrixContext):
        pass

    # Exit a parse tree produced by ExprGrammar#det_matrix.
    def exitDet_matrix(self, ctx:ExprGrammar.Det_matrixContext):
        pass



del ExprGrammar