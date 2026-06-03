# mypy: disable-error-code=operator
from sortedcontainers import SortedDict
import bisect
from functools import total_ordering
from typing import Any, Mapping, Self, cast

import sympy as sp
from antlr4 import ParserRuleContext
from attrs import frozen
from sortedcontainers import SortedList

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
class FixedParam:
    ast: Ast.AExpr
    canon: sp.Basic


@frozen
class BoundParam:
    ast: Ast.AExpr
    canon: sp.Basic


Param = FixedParam | BoundParam

Params = tuple[Param, ...]


@frozen
class SubscriptId:
    subscript_delims: tuple[str | None, str | None]
    slot_seps: tuple[str, ...]


@frozen
@total_ordering
class CallSpec:
    subscript_slots: Params | None
    call_params: Params | None

    def __lt__(self, other: Self) -> bool:
        def bound_count(params: Params) -> int:
            return sum(1 for p in params if isinstance(p, BoundParam))

        match self.subscript_slots, other.subscript_slots:
            case None, None:
                pass
            case None, _:
                return False
            case _, None:
                return True
            case s_slots, o_slots:
                assert s_slots is not None and o_slots is not None
                s_slots_count = bound_count(s_slots)
                o_slots_count = bound_count(o_slots)
                if s_slots_count < o_slots_count:
                    return True

        match self.call_params, other.call_params:
            case None, None:
                return False
            case None, _:
                return False
            case _, None:
                return True
            case s_params, o_params:
                assert s_params is not None and o_params is not None
                return bound_count(s_params) < bound_count(o_params)

        return False


# None, for no subscript.
# None, for not a typical function definition? as in no () needed.
# so, crucially for this, the 2'nd (or first idk) slot will always have same length / None value
Overrides = list[tuple[CallSpec, Any]]

Override = tuple[CallSpec, Any]


class OverridesV2:
    def __init__(self) -> None:
        self.overrides: list[tuple[CallSpec, Any]] = []

    def add(self, override: Override) -> Self:
        call_spec, _ = override

        bisect.insort_left(self.overrides, override, key=lambda x: x[0])
        return self


OverridesV3 = SortedDict[CallSpec, Any]

# no, also a sympy expression maybe? definetly
# or maybe this is where we have some custom objects
# so... we map call spec to something, but should there be multiple layers to this?
# i mean we can probably binary search through it? then it could just be a simple list?
# then it just has to be ordered in a particular way, but thats just something which is defined i guess.
# but does this even matter, does it not make sense that a definition has an arg count? maybe not?
# like should it even be possible to do f(x) := ..., f(x, y) := ...
# it makes stuff like \dv ambiguous so probably not?
# but, it *should* be allowed for indexes, so f_{x} := ..., f_{x, y} := ... is allowed.
# because it would not be ambituous for \dv.
# so the only top level thing which makes sense to have is slot count somehow?, well slot count + delimiters + separators,
# which i guess would be the subscript id? that would make sense
SubDefinitions = Mapping[SubscriptId | None, OverridesV3]

HeadId = str

# maps to a list of overrides?
# but how does this work for symbol v.s. function and so on.
# makes sense its just pr. override i think?
# that way x can be the default value (i.e. symbol) and x_1 is actually a function.
# so everything is a function, they just get called in different ways i guess?
Scope = Mapping[HeadId, SubDefinitions]

s: Scope = {
    "f": {
        # this specific one, or the list to the right, should be a class, instead of just a list
        # it needs to maintain additional rules about its structure, which a simple list cannot help with.
        # call arg check should be higher up, only the subscript check should be here.
        # because call args must be the same for the symbol? no they must not, nvm...
        # but then the call args should not be restricted here either...
        # becuase
        # f_{a}(x, y) :=...
        # f_{b}(x) := ...
        # would not be allowed right now...
        None: SortedList([])
    }
}

print(s)

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
            return sp.Product(ev(expr, s), (ev(var, {}), ev(start, s), ev(end, s)))

        case Ast.Integral(_, expr, diff, None):
            return sp.integrate(ev(expr, s), ev(diff, {}))

        case Ast.Integral(_, expr, diff, bounds):
            assert bounds is not None
            start, end = bounds
            return sp.integrate(ev(expr, s), (ev(diff, {}), ev(start, s), ev(end, s)))

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
