from typing import cast

import sympy as sp
from sympy import Matrix
from lmat_cas_client.math_lib import MatrixUtils

from .. import Ast


def evalExprToSympy(expr: Ast.Expr, scope: None) -> sp.Expr:
    ev = evalExprToSympy
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


def evalAppliedBuiltingFuncToSympy(f: Ast.BuiltinFunc, scope: None) -> sp.Expr:
    ev = evalExprToSympy
    match f:
        case Ast.Factorial(_, op):
            return sp.factorial(ev(op, scope))
        case Ast.Percent(_, op):
            return sp.Mul(ev(op, scope), 100**-1)
        case Ast.Permille(_, op):
            return sp.Mul(ev(op, scope), 1000**-1)
        case Ast.Binom(_, n, k):
            return sp.binomial(ev(n, scope), ev(k, scope))
        case Ast.Sqrt(_, op):
            return cast(sp.Expr, sp.sqrt(ev(op, scope)))
        case Ast.Conjugate(_, op):
            return sp.conjugate(ev(op, scope))
        case Ast.UnitVec(_, op):
            return cast(
                sp.Expr,
                MatrixUtils.ensure_matrix(
                    cast(sp.Basic, cast(object, op))
                ).normalized(),
            )
