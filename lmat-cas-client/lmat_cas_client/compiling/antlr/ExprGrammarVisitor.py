# Generated from ExprGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprGrammar import ExprGrammar
else:
    from ExprGrammar import ExprGrammar

import lmat_cas_client.compiling.antlr.Ast as Ast


# This class defines a complete generic visitor for a parse tree produced by ExprGrammar.

class ExprGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprGrammar#debug.
    def visitDebug(self, ctx:ExprGrammar.DebugContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#rel_op.
    def visitRel_op(self, ctx:ExprGrammar.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#relation.
    def visitRelation(self, ctx:ExprGrammar.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#deriv_arg.
    def visitDeriv_arg(self, ctx:ExprGrammar.Deriv_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#deriv_args.
    def visitDeriv_args(self, ctx:ExprGrammar.Deriv_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#int_bounds.
    def visitInt_bounds(self, ctx:ExprGrammar.Int_boundsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Comb.
    def visitComb(self, ctx:ExprGrammar.CombContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#MultiplicativeOp.
    def visitMultiplicativeOp(self, ctx:ExprGrammar.MultiplicativeOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#UAdditiveOp.
    def visitUAdditiveOp(self, ctx:ExprGrammar.UAdditiveOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Stub.
    def visitStub(self, ctx:ExprGrammar.StubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#ExponentialOp.
    def visitExponentialOp(self, ctx:ExprGrammar.ExponentialOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Prefix.
    def visitPrefix(self, ctx:ExprGrammar.PrefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Int.
    def visitInt(self, ctx:ExprGrammar.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Function.
    def visitFunction(self, ctx:ExprGrammar.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Series.
    def visitSeries(self, ctx:ExprGrammar.SeriesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Deriv.
    def visitDeriv(self, ctx:ExprGrammar.DerivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Abs.
    def visitAbs(self, ctx:ExprGrammar.AbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#AdditiveOp.
    def visitAdditiveOp(self, ctx:ExprGrammar.AdditiveOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Limit.
    def visitLimit(self, ctx:ExprGrammar.LimitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#atom.
    def visitAtom(self, ctx:ExprGrammar.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#symbol.
    def visitSymbol(self, ctx:ExprGrammar.SymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#subscript_arg.
    def visitSubscript_arg(self, ctx:ExprGrammar.Subscript_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#subscript_symbol.
    def visitSubscript_symbol(self, ctx:ExprGrammar.Subscript_symbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#latex_cmd_arg.
    def visitLatex_cmd_arg(self, ctx:ExprGrammar.Latex_cmd_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#pow_arg.
    def visitPow_arg(self, ctx:ExprGrammar.Pow_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#limit_dir.
    def visitLimit_dir(self, ctx:ExprGrammar.Limit_dirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#series_range_args.
    def visitSeries_range_args(self, ctx:ExprGrammar.Series_range_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#builtin_func.
    def visitBuiltin_func(self, ctx:ExprGrammar.Builtin_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#matrix_el.
    def visitMatrix_el(self, ctx:ExprGrammar.Matrix_elContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#matrix_row.
    def visitMatrix_row(self, ctx:ExprGrammar.Matrix_rowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#matrix_body.
    def visitMatrix_body(self, ctx:ExprGrammar.Matrix_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#matrix.
    def visitMatrix(self, ctx:ExprGrammar.MatrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#expr_system_expr.
    def visitExpr_system_expr(self, ctx:ExprGrammar.Expr_system_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#expr_system_body.
    def visitExpr_system_body(self, ctx:ExprGrammar.Expr_system_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#expr_system.
    def visitExpr_system(self, ctx:ExprGrammar.Expr_systemContext):
        return self.visitChildren(ctx)



del ExprGrammar