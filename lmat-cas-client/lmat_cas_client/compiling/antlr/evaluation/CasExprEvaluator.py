from typing import cast

import sympy as sp

from lmat_cas_client.compiling.transforming.LatexMatrix import (
    LatexMatrix,
    MutableLatexMatrix,
)
from lmat_cas_client.math_lib import Functions, MatrixUtils

from .. import Ast

LocRange = tuple[int, int]

ExprEntry = tuple[sp.Basic, LocRange]

CasExprV2 = tuple[ExprEntry, ...]


def a_expr_2_sympy(expr: Ast.AExpr, scope: None) -> ExprEntry:
    def ev(expr: Ast.AExpr, s: None):
        match expr:
            case Ast.ApplyFunc(_, _, _):
                assert False

            case Ast.IndexOp(_, _, _):
                assert False

            case Ast.Symbol(_, name):
                return sp.Symbol(name)

            case Ast.Number(_, n_str):
                if "." in n_str:
                    return sp.Float(n_str)
                else:
                    return sp.Integer(n_str)

            case Ast.Function(_, name):
                return sp.Function(name)

            case Ast.Matrix(_, elems, beg_cmd, end_cmd):
                return MutableLatexMatrix(
                    [[ev(e, s) for e in r] for r in elems],
                    env_begin=beg_cmd,
                    env_end=end_cmd,
                )

            case Ast.DetMatrix(_, elems):
                return sp.Matrix([[ev(e, s) for e in r] for r in elems]).det()

            case Ast.ExpOp(_, base, exp):
                return ev(base, s) ** ev(exp, s)

            case Ast.MultOp(_, lhs, rhs):
                return ev(lhs, s) * ev(rhs, s)

            case Ast.XProdOp(_, lhs, rhs):
                return MatrixUtils.ensure_matrix(ev(lhs, s)).cross(ev(rhs, s))

            case Ast.DotProd(_, lhs, rhs):
                return MatrixUtils.ensure_matrix(ev(lhs, s)).dot(
                    ev(rhs, s), conjugate_convention="right"
                )

            case Ast.DivOp(_, lhs, rhs):
                return ev(lhs, s) / ev(rhs, s)

            case Ast.ModOp(_, lhs, rhs):
                return sp.Mod(ev(lhs, s), ev(rhs, s))

            case Ast.AddOp(_, lhs, rhs):
                return ev(lhs, s) + ev(rhs, s)

            case Ast.SubOp(_, lhs, rhs):
                return ev(lhs, s) - ev(rhs, s)

            case Ast.UPlusOp(_, op):
                return +ev(op, s)

            case Ast.UMinusOp(_, op):
                return -ev(op, s)

            case Ast.Abs(_, expr):
                expr = ev(expr, s)

                if MatrixUtils.is_matrix(expr):
                    return cast(sp.MatrixBase, expr).det()

                return sp.Abs(expr)

            case Ast.Norm(_, expr):
                return MatrixUtils.ensure_matrix(ev(expr, s)).norm()

            case Ast.UnitVec(_, expr):
                return MatrixUtils.ensure_matrix(ev(expr, s)).normalized()

            case Ast.Floor(_, expr):
                return sp.Floor(ev(expr, s))

            case Ast.Ceil(_, expr):
                return sp.Ceil(ev(expr, s))

            case Ast.Conjugate(_, expr):
                return sp.conjugate(ev(expr, s))

            case Ast.Conjugate(_, expr):
                return sp.conjugate(ev(expr, s))

            case Ast.Binom(_, n, k):
                return sp.binomial(ev(n, s), ev(k, s))

            case Ast.Permutations(_, n, r):
                return Functions.permutations(ev(n, s), ev(r, s))

            case Ast.Derangements(_, n):
                return Functions.derangements(ev(n, s))

            case Ast.Factorial(_, expr):
                return sp.factorial(expr)

            case Ast.Percent(_, expr):
                return sp.Mul(expr, 100**-1)

            case Ast.Permille(_, expr):
                return sp.Mul(expr, 1000**-1)

            case Ast.Sum(_, expr, var, bounds):
                start, end = bounds
                return sp.Sum(ev(expr, s), (ev(var, None), ev(start, s), ev(end, s)))

            case Ast.Product(_, expr, var, bounds):
                start, end = bounds
                return sp.Product(
                    ev(expr, s), (ev(var, None), ev(start, s), ev(end, s))
                )

            case Ast.Integral(_, expr, diff, None):
                return sp.integrate(ev(expr, s), ev(diff, None))

            case Ast.Integral(_, expr, diff, bounds):
                assert bounds is not None
                start, end = bounds
                return sp.integrate(
                    ev(expr, s), (ev(diff, None), ev(start, s), ev(end, s))
                )

            case Ast.Differential(_, expr, diffs):
                return sp.diff(
                    ev(expr, s),
                    (
                        (ev(diff, None), ev(deg, s) if deg is not None else 1)
                        for diff, deg in diffs
                    ),
                )

            case Ast.Limit(_, expr, var, point_of_approach, dir):
                return sp.limit(
                    ev(expr, s), ev(var, None), ev(point_of_approach, s), dir.value
                )

            case Ast.EvalAt(_, _, _, _):
                pass

            case Ast.Root(_, expr, None):
                return sp.sqrt(ev(expr, s))

            case Ast.Root(_, expr, index):
                assert index is not None
                return sp.root(ev(expr, s), ev(index, s))

    match expr:
        case Ast.AstNode(ctx):
            start_token = ctx.start
            end_token = ctx.stop

            assert start_token is not None and end_token is not None

            return (ev(expr, scope), (start_token.start, end_token.stop))

    # TODO: what to do here...
    assert False
