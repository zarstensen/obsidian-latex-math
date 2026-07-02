# mypy: disable-error-code=operator
import bisect
from enum import Enum
from functools import total_ordering
from typing import Any, Callable, Mapping, Self, cast

import attrs
import sympy as sp
from antlr4 import ParserRuleContext
from attrs import frozen

from lmat_cas_client.compiling.antlr.evaluation.Scope import (
    LiteralParam,
    Scope,
    Signature,
)
from lmat_cas_client.compiling.transforming.LatexMatrix import (
    MutableLatexMatrix,
)
from lmat_cas_client.math_lib import Functions, MatrixUtils

from .. import Ast

LocRange = tuple[int, int]

ExprEntry = tuple[sp.Basic | sp.MatrixBase, LocRange]

# TODO: rename to CasExpr when old one is no longer needed
CasExprV2 = tuple[ExprEntry, ...]


def ctx_to_loc(ctx: ParserRuleContext) -> LocRange:
    start_token = ctx.start
    end_token = ctx.stop

    assert start_token is not None and end_token is not None

    return (start_token.start, end_token.stop)


def get_ast_nodes(
    node: Ast.AlgStmt,
) -> dict[str, Ast.AlgStmt | tuple[Ast.AlgStmt, ...]]:
    fields = cast(tuple[attrs.Attribute], attrs.fields(type(node)))

    alg_stmts: dict[str, Ast.AlgStmt | tuple[Ast.AlgStmt, ...]] = {}

    for field in fields:
        field_val = getattr(node, field.name)

        if isinstance(field_val, Ast.AlgStmt):
            alg_stmts[field.name] = field_val
        elif isinstance(field_val, tuple) and all(
            isinstance(v, Ast.AlgStmt) for v in field_val
        ):
            alg_stmts[field.name] = field_val

    return alg_stmts


class AmbigCallResolveStrat(Enum):
    BubbleUp = 0
    Mul = 1


# implementing this in the grammar is sort of a lost cause?
# this is really close to working though, all i need is some way to know what to do with the result of a_expr_resolve_ir, also this should probably be specificallyf or resolving the ambiguous call only, so dont mix any other stuff in it.
# but thats jujs
def a_expr_resolve_ir(
    expr: Ast.AlgStmt, scope: Scope
) -> tuple[Ast.AlgStmt, AmbigCallResolveStrat]:
    match expr:
        case Ast.AmbigApplyFunc(ctx, Ast.ApplyFunc(_, func, args), _, _):
            assert len(args) == 1
            return (Ast.MultOp(ctx, func, args[0]), AmbigCallResolveStrat.Mul)
        case Ast.SubscriptOp(_, val, _):
            new_val, strat = a_expr_resolve_ir(val, scope)
            assert isinstance(new_val, Ast.AExpr)

            match strat:
                case AmbigCallResolveStrat.BubbleUp:
                    return (
                        attrs.evolve(expr, val=new_val),
                        AmbigCallResolveStrat.BubbleUp,
                    )
                case AmbigCallResolveStrat.Mul:
                    assert isinstance(new_val, Ast.MultOp)
                    return (
                        Ast.MultOp(
                            expr.ctx, new_val.lhs, attrs.evolve(expr, val=new_val.rhs)
                        ),
                        AmbigCallResolveStrat.Mul,
                    )

        case Ast.ExpOp(_, base, _):
            new_base, strat = a_expr_resolve_ir(base, scope)

            assert isinstance(new_base, Ast.AExpr)

            match strat:
                case AmbigCallResolveStrat.BubbleUp:
                    return (
                        attrs.evolve(
                            visit_children(
                                expr,
                                lambda c: a_expr_resolve_ir(c, scope)[0],
                                {attrs.fields(Ast.ExpOp).base},
                            ),
                            base=new_base,
                        ),
                        AmbigCallResolveStrat.BubbleUp,
                    )
                case AmbigCallResolveStrat.Mul:
                    assert isinstance(new_base, Ast.MultOp)
                    return (
                        Ast.MultOp(
                            expr.ctx,
                            new_base.lhs,
                            attrs.evolve(
                                visit_children(
                                    expr,
                                    lambda c: a_expr_resolve_ir(c, scope)[0],
                                    {attrs.fields(Ast.ExpOp).base},
                                ),
                                base=new_base.rhs,
                            ),
                        ),
                        AmbigCallResolveStrat.BubbleUp,
                    )

        case Ast.Factorial(_, o) | Ast.Percent(_, o) | Ast.Permille(_, o):
            new_o, strat = a_expr_resolve_ir(o, scope)
            assert isinstance(new_o, Ast.AExpr)

            match strat:
                case AmbigCallResolveStrat.BubbleUp:
                    # this could be whatever, but there is an apply func down there somehwere.
                    # the important bit is that we do the following.
                    return (
                        attrs.evolve(expr, operand=new_o),
                        AmbigCallResolveStrat.BubbleUp,
                    )
                case AmbigCallResolveStrat.Mul:
                    assert isinstance(new_o, Ast.MultOp)
                    return (
                        Ast.MultOp(
                            expr.ctx, new_o.lhs, attrs.evolve(expr, operand=new_o.rhs)
                        ),
                        AmbigCallResolveStrat.Mul,
                    )

            pass
        case Ast.AstNode(_) as node:
            return (
                visit_children(node, lambda c: a_expr_resolve_ir(c, scope)[0]),
                AmbigCallResolveStrat.BubbleUp,
            )


def visit_children[TNode: Ast.AstNode, TChild: Ast.AstNode](
    node: TNode,
    visitor: Callable[[TChild], TChild],
    exclude_children: set[attrs.Attribute] | None = None,
):
    exclude_children = exclude_children or set()

    node_fields = cast(tuple[attrs.Attribute[TNode]], attrs.fields(type(node)))

    new_children: dict[str, TChild | tuple[TChild, ...]] = {}

    for field in node_fields:
        field_val = getattr(node, field.name)

        if field.name in exclude_children:
            continue

        match field_val:
            case Ast.AstNode() as child:
                new_children[field.name] = visitor(cast(TChild, child))
            case tuple() as children if all(
                isinstance(child, Ast.AstNode) for child in children
            ):
                new_children[field.name] = tuple(
                    visitor(cast(TChild, child)) for child in children
                )
            case _:
                pass

    return attrs.evolve(node, **new_children)


# Transform an Ast.AlgStmt into a CasExpr,
# this is basically a wrapper around the 3 main transformers (a_expr_2_cas_expr, rel_2_cas_expr, system_2_cas_rel_2_cas_expr, system_2_cas_expr),
# and picks the correct function to call, based on the type of expr.
def alg_stmt_2_cas_expr(expr: Ast.AlgStmt, scope: Scope) -> CasExprV2:
    match expr:
        case _ if isinstance(expr, Ast.AExpr):
            return a_expr_2_cas_expr(expr, scope)
        case _ if isinstance(expr, Ast.Rel):
            return rel_2_cas_expr(expr, scope)
        case _ if isinstance(expr, Ast.System):
            return system_2_cas_expr(expr, scope)


# Transform an Ast.System into a CasExpr
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


# Transform an Ast.Rel into a CasExpr,
# The CasExpr may contain multiple sympy relations, in the c that rel,
# contains chained relations (e.g. a < b < c becomes, a < b and b < c in the CasExpr)
def rel_2_cas_expr(rel: Ast.Rel, scope: Scope) -> CasExprV2:
    ev = a_expr_2_sympy

    remaining_rels = None

    # A relation may have another relation
    # as its rhs argument (e.g. when chaining relations: a < (b < c))
    # in this case, the relation should be seen as 2 relations, of the form a < b and b < c, in the same system.
    # we keep track of this scenario here.
    if isinstance(rel.rhs, Ast.Rel):
        remaining_rels = rel.rhs
        # new rhs is the lhs of the rhs relation.
        rhs = rel.rhs.lhs
    else:
        rhs = rel.rhs

    sp_rel: sp.Basic

    match rel:
        case Ast.Eq(_, lhs, _):
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


# Transform an Ast.AExpr into a CasExpr
def a_expr_2_cas_expr(expr: Ast.AExpr, scope: Scope) -> CasExprV2:
    return ((a_expr_2_sympy(expr, scope), ctx_to_loc(expr.ctx)),)


def try_substitute(
    expr: Ast.AExpr,
    s: Scope,
    transformer: Callable[[Ast.AExpr, Scope], sp.Basic | sp.MatrixBase],
) -> sp.Basic | sp.MatrixBase:
    head_id = None
    subscript_form = Ast.SubscriptForm((None, None), ())
    index_params: tuple[Ast.AExpr, ...] = ()
    arg_params: tuple[Ast.AExpr, ...] = ()

    match expr:
        # x
        case Ast.Symbol(_, symbol_name):
            head_id = symbol_name
            pass
        # x_i
        case Ast.SubscriptOp(_, Ast.Symbol(_, symbol_name), subscript) if all(
            isinstance(slot, Ast.AExpr) for slot in subscript.slots
        ):
            head_id = symbol_name
            subscript_form = subscript.form
            index_params = cast(tuple[Ast.AExpr, ...], subscript.slots)
        # f(x)
        case Ast.ApplyFunc(_, Ast.Symbol(_, symbol_name), args):
            head_id = symbol_name
            arg_params = args
        # f_i(x)
        case Ast.ApplyFunc(
            _, Ast.SubscriptOp(_, Ast.Symbol(_, symbol_name), subscript), args
        ) if all(isinstance(slot, Ast.AExpr) for slot in subscript.slots):
            head_id = symbol_name
            subscript_form = subscript.form
            index_params = cast(tuple[Ast.AExpr, ...], subscript.slots)
            arg_params = args
        case _:
            return transformer(expr, s)

    sig = Signature(
        head_id,
        subscript_form,
        tuple(LiteralParam(e) for e in index_params),
        tuple(LiteralParam(e) for e in arg_params),
    )

    resolve_result = s.resolve(
        sig, lambda la, lb: transformer(la.value, s) == transformer(lb.value, s)
    )

    if resolve_result is not None:
        expr, defs = resolve_result
        s.register(defs)

        transformed_expr = try_substitute(expr, s, transformer)

        s.unregister(defs)

        return transformed_expr

    return transformer(expr, s)


def a_expr_2_sympy(expr: Ast.AExpr, s: Scope) -> sp.Basic | sp.MatrixBase:
    return try_substitute(expr, s, _a_expr_2_sympy)


# Transform an Ast.AExpr into a sympy expression,
# Substituting variables defined in the given scope along the way.
def _a_expr_2_sympy(expr: Ast.AExpr, s: Scope) -> sp.Basic | sp.MatrixBase:
    ev = lambda e, s: try_substitute(e, s, a_expr_2_sympy)
    match expr:
        case Ast.ApplyFunc(_, _, _):
            assert False, "Cannot handle ApplyFunc without definitions"

        case Ast.SubscriptOp(_, Ast.Symbol(_, name), subscript) if (
            name,
            None,
        ) not in s:
            lbrack, rbrack = subscript.form.brackets
            return sp.Symbol(f"{name}_{{{lbrack}WHAAAAAT{rbrack}}}")

        case Ast.SubscriptOp(_, expr, subscript):
            # TODO: check if expr is indexable, if not raise / assert
            # wait no...
            return None

        case Ast.Symbol(_, name):
            return sp.Symbol(name)

        case Ast.Number(_, n_str):
            if "." in n_str:
                return sp.Float(n_str)
            else:
                return sp.Integer(n_str)

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

        case Ast.Parens(_, expr):
            return ev(expr, s)

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
            return sp.Mul(cast(sp.Expr, ev(expr, s)), 100**-1)

        case Ast.Permille(_, expr):
            return sp.Mul(cast(sp.Expr, ev(expr, s)), 1000**-1)

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
            return None

        case Ast.Root(_, expr, None):
            return sp.sqrt(ev(expr, s))

        case Ast.Root(_, expr, index):
            assert index is not None
            return sp.root(ev(expr, s), ev(index, s))

        case ir if isinstance(ir, Ast.Ir):
            assert "Cannot evaluate if Ir object is present in AST"
            return None
