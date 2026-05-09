# pyright: reportOperatorIssue=false, reportArgumentType=false
from typing import cast

import sympy as sp
from lmat_cas_client.math_lib import MatrixUtils

from .. import Ast

LocRange = tuple[int, int]

ExprEntry = tuple[sp.Basic, LocRange]

CasExprV2 = tuple[ExprEntry, ...]

def evalExprToSympy(expr: Ast.Expr, scope: None) -> ExprEntry:
    def ev(expr: Ast.Expr, scope: None):
        match expr:
            case Ast.Symbol(_, s):
                return sp.Symbol(s)
            case Ast.Number(_, n_str):
                if "." in n_str:
                    return sp.Float(n_str)
                else:
                    return sp.Integer(n_str)
            case Ast.ExpOp(_, base, exp):
                return ev(base, scope) ** ev(exp, scope)
            case Ast.MultOp(_, lhs, rhs):
                return ev(lhs, scope) * ev(rhs, scope)
            case Ast.DivOp(_, lhs, rhs):
                return ev(lhs, scope) / ev(rhs, scope)
            case Ast.AddOp(_, lhs, rhs):
                return ev(lhs, scope) + ev(rhs, scope)
            case Ast.SubOp(_, lhs, rhs):
                return ev(lhs, scope) - ev(rhs, scope)
            case Ast.UPlusOp(_, op):
                return +ev(op, scope)
            case Ast.UMinusOp(_, op):
                return -ev(op, scope)
            case Ast.AppliedBuiltinFunc(_, f):
                return evalAppliedBuiltingFuncToSympy(f, scope)

    match expr:
        case Ast.AstNode(ctx):
            start_token = ctx.start
            end_token = ctx.stop

            assert start_token is not None and end_token is not None

            return (ev(expr, scope)[0], (start_token.start, end_token.stop))

    # TODO: what to do here...
    assert False

def evalAppliedBuiltingFuncToSympy(f: Ast.BuiltinFunc, scope: None) -> sp.Basic:
    ev = evalExprToSympy
    match f:
        case Ast.Factorial(_, op):
            return sp.factorial(ev(op, scope))
        case Ast.Percent(_, op):
            return sp.Mul(ev(op, scope)[0], 100**-1)
        case Ast.Permille(_, op):
            return sp.Mul(ev(op, scope)[0], 1000**-1)
        case Ast.Binom(_, n, k):
            return sp.binomial(ev(n, scope), ev(k, scope))
        case Ast.Root(_, op, None):
            return sp.sqrt(ev(op, scope))
        case Ast.Root(_, op, index):
            assert index is not None
            return sp.root(ev(op, scope), ev(index, scope))
        case Ast.Conjugate(_, op):
            return sp.conjugate(ev(op, scope))
        case Ast.UnitVec(_, op):
            return MatrixUtils.ensure_matrix(
                    cast(sp.Basic, cast(object, op))
                ).normalized()
