# mypy: disable-error-code=operator
from typing import Mapping, cast

import sympy as sp
from antlr4 import ParserRuleContext
from attrs import frozen

from lmat_cas_client.compiling.transforming.LatexMatrix import (
    MutableLatexMatrix,
)
from lmat_cas_client.math_lib import Functions, MatrixUtils

from .. import Ast


# @frozen
# class SymbolAstDef:
#     ast: Ast.AExpr
#
# @frozen
# class SymbolSympyDef:
#     sp_expr: sp.Basic
#
# SymbolDef = SymbolAstDef | SymbolSympyDef
#
# @frozen
# class FuncAstDef:
#     body: Ast.AExpr
#
# @frozen
# class FuncSympyDef:
#     body: sp.Basic
#
# FuncBody = FuncAstDef | FuncSympyDef
#
# # instead of unapplied bubbeling up,
# # just handle lone unapplied funcs directly in functions
# # which need to do it.
# # then also have a first pass which decides whether an index op should be an actual index op, or just a symbol / function.
# @frozen
# class FuncDef:
#     body: FuncBody
#     params: tuple[str]
#     index_params: dict[int, str]
#
#
# # why is this one special again?
# @frozen
# class UndefFuncDef:
#     func: sp.core.function.UndefinedFunction
#
# @frozen
# class EmptyDef:
#     pass
#
# Definition = SymbolDef | FuncDef | UndefFuncDef | EmptyDef
#
# @frozen
# class DefId:
#     id: str
#     subscript: frozenset[tuple[int, str]]


# so in overrides, bound slots are replaced with fixed slots
@frozen
class FixedSlot:
	ast: Ast.AExpr
	canon: sp.Basic

@frozen
class BoundSlot:
	ast: Ast.AExpr
	canon: sp.Basic

Slot = FixedSlot | BoundSlot

@frozen
class SubscriptSpec:
	subscript_delims: tuple[str | None, str | None]
	slot_seps: tuple[str, ...]

# TODO: in the future, this could also differentiate between separators,
# like the subscript spec.
@frozen
class CallSpec:
	arg_count: int
	subscript_spec: SubscriptSpec | None

# no, also a sympy expression maybe? definetly
# or maybe this is where we have some custom objects
Override = tuple[CallSpec, Ast.AExpr]

# so this should be like
@frozen
class Definition:
	overrides: dict[CallSpec | None, tuple[Override, ...]]

@frozen
class HeadKey:
	id: str
	call_spec: CallSpec | None

# maps to a list of overrides?
# but how does this work for symbol v.s. function and so on.
# makes sense its just pr. override i think?
# that way x can be the default value (i.e. symbol) and x_1 is actually a function.
# so everything is a function, they just get called in different ways i guess?
Scope = Mapping[HeadKey, Definition]

# maybe there shoud be like a main type?
#
# So how should
# x := 5
# x_{i} := 10
#
# be seen? because right now it would be that x_{i} is an override to x? or not? because the call spec is different?
# guess that makes sense. So, when you reset a definition, it resets the call spec only i guess?
# that makes sense
#
# So...
# f(x) := x^2
# f(0) := 100
#
# then f(x) := ...
# removes all overrides for specifically f(..) for all |..| = 1
# 333333333333333333333333333333

LocRange = tuple[int, int]

ExprEntry = tuple[sp.Basic | sp.MatrixBase, LocRange]

CasExprV2 = tuple[ExprEntry, ...]

def ctx_to_loc(ctx: ParserRuleContext) -> LocRange:
    start_token = ctx.start
    end_token = ctx.stop

    assert start_token is not None and end_token is not None

    return (start_token.start, end_token.stop)

def alg_stmt_2_cas_expr(expr: Ast.AlgStmt, scope: Scope) -> CasExprV2:
    match expr:
        case _ if isinstance(expr, Ast.AExpr):
            return a_expr_2_cas_expr(expr, scope)
        case _ if isinstance(expr, Ast.Rel):
            return rel_2_cas_expr(expr, scope)
        case _ if isinstance(expr, Ast.System):
            return system_2_cas_expr(expr, scope)

def system_2_cas_expr(sys: Ast.System, scope: Scope) -> CasExprV2:
    def ev(elems: list[Ast.SystemEntry], scope: Scope) -> CasExprV2:
        if len(elems) == 0:
            return ()

        e: CasExprV2

        match elems[0]:
            case Ast.RelEntry(_, rel):
                e = rel_2_cas_expr(rel, scope)
            case Ast.AExprEntry(_, a_expr):
                e = a_expr_2_cas_expr(a_expr, scope)

        return (*e, *ev(elems[1:], scope))

    return ev(sys.elems, scope)


def rel_2_cas_expr(rel: Ast.Rel, scope: Scope) -> CasExprV2:
    ev = a_expr_2_sympy

    remaining_rels = None

    if isinstance(rel.rhs, Ast.Rel):
        remaining_rels = rel.rhs
        rhs = rel.rhs.lhs
    else:
        rhs = rel.rhs

    sp_rel: sp.Basic

    match rel:
        case Ast.Eq(_, lhs, _):
            print(sp.Eq(ev(lhs, scope), ev(rhs, scope)))
            print(ev(lhs, scope), ev(rhs, scope))
            sp_rel = sp.Eq(ev(lhs, scope), ev(rhs, scope))
        case Ast.Neq(_, lhs, _):
            sp_rel = sp.Ne(ev(lhs, scope), ev(rhs, scope))
        case Ast.Lt(_, lhs, _):
            sp_rel = sp.Lt(ev(lhs, scope), ev(rhs, scope))
        case Ast.Lte(_, lhs, _):
            sp_rel = sp.Le(ev(lhs, scope), ev(rhs, scope))
        case Ast.Gt(_, lhs, _):
            sp_rel = sp.Gt(ev(lhs, scope), ev(rhs, scope))
        case Ast.Gte(_, lhs, _):
            sp_rel = sp.Ge(ev(lhs, scope), ev(rhs, scope))

    entry = (sp_rel, ctx_to_loc(rel.ctx))

    if remaining_rels is not None:
        return (entry, *rel_2_cas_expr(remaining_rels, scope))
    else:
        return (entry,)

def a_expr_2_cas_expr(expr: Ast.AExpr, scope: Scope) -> CasExprV2:

    return ((a_expr_2_sympy(expr, scope), ctx_to_loc(expr.ctx)),)

def a_expr_2_sympy(expr: Ast.AExpr, s: Scope) -> sp.Basic | sp.MatrixBase:
    ev = a_expr_2_sympy
    match expr:
        case Ast.ApplyFunc(_, Ast.Function(_, func), args):
            assert func in s
            assert False

        case Ast.SubscriptOp(_, _, _):
            assert False

        case Ast.Symbol(_, name):
            # nothing special for this one right?
            if name in s:
                # we could mark that it is currently being resolved here?
                return resolve_def(s[name], s)
            else:
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
            evd_expr = ev(expr, s)

            if MatrixUtils.is_matrix(evd_expr):
                return cast(sp.MatrixBase, evd_expr).det()

            return sp.Abs(evd_expr)

        case Ast.Norm(_, expr):
            return MatrixUtils.ensure_matrix(ev(expr, s)).norm()

        case Ast.UnitVec(_, expr):
            return MatrixUtils.ensure_matrix(ev(expr, s)).normalized()

        case Ast.Floor(_, expr):
            return sp.floor(ev(expr, s))

        case Ast.Ceil(_, expr):
            return sp.ceiling(ev(expr, s))

        case Ast.Conjugate(_, expr):
            return sp.conjugate(ev(expr, s))

        case Ast.Conjugate(_, expr):
            return sp.conjugate(ev(expr, s))

        case Ast.Binom(_, n, k):
            return sp.binomial(ev(n, s), ev(k, s))

        case Ast.Permutations(_, n, r):
            return Functions.permutations(
                cast(sp.Expr, ev(n, s)), cast(sp.Expr, ev(r, s))
            )

        case Ast.Derangements(_, n):
            return Functions.derangements(cast(sp.Expr, ev(n, s)))

        case Ast.Factorial(_, expr):
            return sp.factorial(expr)

        case Ast.Percent(_, expr):
            return sp.Mul(cast(sp.Expr, expr), 100**-1)

        case Ast.Permille(_, expr):
            return sp.Mul(cast(sp.Expr, expr), 1000**-1)

        case Ast.Sum(_, expr, var, bounds):
            start, end = bounds
            return sp.Sum(ev(expr, s), (ev(var, {}), ev(start, s), ev(end, s)))

        case Ast.Product(_, expr, var, bounds):
            start, end = bounds
            return sp.Product(
                ev(expr, s), (ev(var, {}), ev(start, s), ev(end, s))
            )

        case Ast.Integral(_, expr, diff, None):
            return sp.integrate(ev(expr, s), ev(diff, {}))

        case Ast.Integral(_, expr, diff, bounds):
            assert bounds is not None
            start, end = bounds
            return sp.integrate(
                ev(expr, s), (ev(diff, {}), ev(start, s), ev(end, s))
            )

        case Ast.Differential(_, expr, diffs):
            return sp.diff(
                ev(expr, s),
                (
                    (ev(diff, {}), ev(deg, s) if deg is not None else 1)
                    for diff, deg in diffs
                ),
            )

        case Ast.Limit(_, expr, var, point_of_approach, dir):
            return sp.limit(
                ev(expr, s), ev(var, {}), ev(point_of_approach, s), dir.value
            )

        case Ast.EvalAt(_, _, _, _):
            assert False

        case Ast.Root(_, expr, None):
            return sp.sqrt(ev(expr, s))

        case Ast.Root(_, expr, index):
            assert index is not None
            return sp.root(ev(expr, s), ev(index, s))

