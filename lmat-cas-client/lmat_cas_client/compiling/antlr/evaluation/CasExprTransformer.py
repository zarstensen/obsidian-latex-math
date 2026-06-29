# mypy: disable-error-code=operator
import bisect
from enum import Enum
from functools import total_ordering
from typing import Any, Callable, Mapping, Self, cast

import attrs
import sympy as sp
from antlr4 import ParserRuleContext
from attrs import frozen

from lmat_cas_client.compiling.transforming.LatexMatrix import (
    MutableLatexMatrix,
)
from lmat_cas_client.math_lib import Functions, MatrixUtils

from .. import Ast


@frozen
class FixedParam:
    """
    Represents a parameter to a definition,
    which is a part of the definition symbol itself.
    FixedParam is *not* substituted into the value of the definition.
    """

    ast: Ast.Symbol | Ast.SubscriptOp

    def inject_definition(scope: Scope):
        match ast:
            case Ast.Symbol(_, name):
                scope[(name, None)].add()
        pass


@frozen
class BoundParam:
    """
    Represents a parameter to a definition,
    which is not a part of the definition symbol, but is instead a parameter to the definitions value,
    which is substituted with another value when the definition is resolved.
    """

    ast: Ast.AExpr


type Param = FixedParam | BoundParam

type Params = tuple[Param, ...]


@frozen
@total_ordering
class OverrideSpec:
    """
    Represents the requirements a symbol / function call must uphold,
    for some override to be considered.
    Specifically, each parameter in the subscripts and call arguments
    of some resolve target must uphold httetehthethethethehth
    """

    subscript_slots: Params
    call_params: Params

    def __lt__(self, other: Self) -> bool:
        """
        OverrideSpec's are ordered first by their no. BoundParam in subscript_slots,
        and secondly by their no. BoundParam in call_params.
        """

        def bound_count(params: Params) -> int:
            return sum(1 for p in params if isinstance(p, BoundParam))

        if bound_count(self.subscript_slots) < bound_count(other.subscript_slots):
            return True

        return bound_count(self.call_params) < bound_count(other.call_params)


type Override = tuple[OverrideSpec, Ast.AExpr]


class Overrides:
    def __init__(self, slot_count: int) -> None:
        assert slot_count >= 0, "slout_count must be non-negative"

        self.slot_count = slot_count
        self.overrides: list[tuple[OverrideSpec, Any]] = []

    def add(self, override: Override) -> Self:
        call_spec, _ = override

        assert len(call_spec.subscript_slots) == self.slot_count

        bisect.insort_left(self.overrides, override, key=lambda x: x[0])

        return self

    # this should also return the scope which the expr should be evaluated in...
    # feels like it makes sense its created here.
    # some logic may need to be shared for the definition grammar transformer,
    # but thats fine...
    def resolve(
        self, args: tuple[sp.Basic, ...], slots: tuple[sp.Basic, ...]
    ) -> Ast.AExpr | None:
        if self.slot_count != len(slots):
            return None

        for override, defi in self.overrides:
            valid_override = True

            if len(override.call_params) != len(args):
                valid_override = False
            else:
                for param, ss in zip(
                    (*override.subscript_slots, *override.call_params), (*slots, *args)
                ):
                    match param:
                        case BoundParam(_):
                            pass
                        case FixedParam(param_ast):
                            # so why can it not just be sympy all the way down?
                            # i mean, we already now the definition id, do we actually?
                            if not a_expr_2_sympy(param_ast, {}).equals(ss):
                                valid_override = False
                                break

            if valid_override:
                return defi

        return None

    def __repr__(self) -> str:
        return f"Overrides({self.overrides!r})"

    def __str__(self) -> str:
        return self.__repr__()


type HeadId = str

# IT HAS BEEN DECIDED this should be a CLASS, that way it can also handle merging multiple scopes cleanly
# would be messy otherwise, so...
type DefId = tuple[HeadId, Ast.SubscriptForm | None]
type ScopeMap = Mapping[DefId, Overrides]


class Scope:
    def __init__(self, scope_map: ScopeMap):
        self.scope_map = dict(scope_map)

    @staticmethod
    def empty() -> "Scope":
        return Scope({})

    def add_override(self, id: DefId, override: Override) -> Self:
        _, sub_form = id
        if id not in self.scope_map:
            self.scope_map[id] = Overrides(
                len(sub_form.slot_seps) if sub_form is not None else 0
            )
        self.scope_map[id].add(override)
        return self


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
    subscript_form = None
    call_args: tuple[Ast.AExpr, ...] = ()
    subscript_slots: tuple[Ast.AExpr, ...] = ()

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
            subscript_slots = cast(tuple[Ast.AExpr, ...], subscript.slots)
        # f(x)
        case Ast.ApplyFunc(_, Ast.Symbol(_, symbol_name), args):
            head_id = symbol_name
            call_args = args
        # f_i(x)
        case Ast.ApplyFunc(
            _, Ast.SubscriptOp(_, Ast.Symbol(_, symbol_name), subscript), args
        ) if all(isinstance(slot, Ast.AExpr) for slot in subscript.slots):
            head_id = symbol_name
            subscript_form = subscript.form
            subscript_slots = cast(tuple[Ast.AExpr, ...], subscript.slots)
            call_args = args
        case _:
            return transformer(expr, s)

    def_id = (head_id, subscript_form)

    resolved_val = None

    if def_id in s:
        resolved_val = s[def_id].resolve(call_args, subscript_slots)

    if resolved_val is not None:
        # so here, we need to inject variables to substitute
        # is call_args and subscript_slots... shomehow...
        # but again, a function is needed for this anyways, so not really that bad...
        return transformer(resolved_val, s)

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
