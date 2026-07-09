# mypy: disable-error-code=operator
from enum import Enum
from typing import Callable, cast

import attrs
import sympy as sp
from antlr4 import ParserRuleContext

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


def literal_sp_comparer(scope: Scope) -> LiteralParam.EqChecker:
    """
    Check if 2 literal parameters are considered equal, in the context of the given scope.
    This checks if their transformed sympy values are equal.
    """
    return lambda la, lb: a_expr_2_sympy(la.literal, scope) == a_expr_2_sympy(
        lb.literal, scope
    )


def ctx_to_loc(ctx: ParserRuleContext) -> LocRange:
    """
    Extract location information from a ParserRuleContext object into a LocRange.
    """
    start_token = ctx.start
    end_token = ctx.stop

    assert start_token is not None and end_token is not None

    return (start_token.start, end_token.stop)


def visit_children[TNode: Ast.AstNode, TChild: Ast.AstNode](
    node: TNode,
    visitor: Callable[[TChild], TChild],
    exclude_children: set[attrs.Attribute] | None = None,
):
    """
    Call visitor on all fields of node which extend AstNode.
    This also includes all AstNode's in pure AstNode tuples.

    the visitor returns a new child node which the previous child is replaced with.
    returns a new version of node, which contains the newly replaced children.

    visitor is not invoked for fields present in exclude_children.
    """
    exclude_children = exclude_children or set()

    node_fields: tuple[attrs.Attribute[TNode]] = attrs.fields(type(node))

    new_children: dict[str, TChild | tuple[TChild | None, ...]] = {}

    for field in node_fields:
        field_val = getattr(node, field.name)

        if field in exclude_children:
            continue

        match field_val:
            case Ast.AstNode() as child:
                new_children[field.name] = visitor(cast(TChild, child))
            # TODO: this should just be any nested iterable here...
            case tuple() as children if all(
                isinstance(child, Ast.AstNode) or child is None for child in children
            ):
                new_children[field.name] = tuple(
                    visitor(cast(TChild, child)) if child is not None else None
                    for child in children
                )
            case _:
                pass

    return attrs.evolve(node, **new_children)


class AmbigCallResolution(Enum):
    """
    TEST
    """

    BubbleUp = 0
    """
    TEST2
    """

    ImplicitMult = 1
    """
    TEST3
    """


def a_expr_resolve_ambig_calls(
    expr: Ast.AlgStmt, scope: Scope
) -> tuple[Ast.AlgStmt, AmbigCallResolution]:
    """
    Given an AlgStmt AST and a Scope which it should be transformed in,
    this function recursively resolves all AmbigApplyFunc nodes in the AST.
    """
    match expr:
        # handle case where we actually need to resolve an ambiguity.
        case Ast.AmbigApplyFunc(ctx, Ast.ApplyFunc(_, func, args)):
            # first check if func is an AExpr whic could potentially have a definition
            signature = Signature.from_a_expr(expr.apply_func_candidate)

            if signature is not None:

                # now check if it has a definition and that definition is a function.
                resolved_binding_id = scope.resolve(
                    signature, literal_sp_comparer(scope)
                )

                if (
                    resolved_binding_id is not None
                    and len(scope.get_binding(resolved_binding_id)[0].arg_params) >= 1
                ):
                    # it is, so resolve it to an ApplyFunc
                    return (
                        Ast.ApplyFunc(ctx, func, args),
                        AmbigCallResolution.BubbleUp,
                    )

            # the func expr could not be resolved to a function definition,
            # so it is resolved to a multipication instead.
            # i.e. (1 + 1)(x) becomes (1 + 1) * x and f(x) becomes f * x
            assert len(args) == 1
            return (Ast.MultOp(ctx, func, args[0]), AmbigCallResolution.ImplicitMult)

        # handle case where a postfix operator is appled to an ambiguous expression.
        # the operator should be applied to the right most side of a potential multiplication resolution.
        # e.x.
        # f(x)_i
        # ImplicitMult -> f * (x)_i
        # BubbleUp -> (f(x))_i
        case (
            Ast.ExpOp(_, val, _)
            | Ast.SubscriptOp(_, val, _)
            | Ast.Factorial(_, val)
            | Ast.Percent(_, val)
            | Ast.Permille(_, val)
        ):

            # select which field we need to pick the AmbigCallResolution from.
            # e.g. in ExpOp its base, as this is the field which is ambiguous (e.g. f(x)^y is ambig where as y^{f(x)} is not )
            match expr:
                case Ast.ExpOp():
                    ambig_field = attrs.fields(Ast.ExpOp).base
                case Ast.SubscriptOp():
                    ambig_field = attrs.fields(Ast.SubscriptOp).val
                case Ast.Factorial() | Ast.Percent() | Ast.Permille():
                    ambig_field = attrs.fields(type(expr)).operand

            # resolve ambiguity and keep the resolution enum
            unambig_val, strat = a_expr_resolve_ambig_calls(val, scope)
            assert isinstance(unambig_val, Ast.AExpr)

            # resolve ambiguities in the rest of the expr
            unambig_expr = visit_children(
                expr, lambda c: a_expr_resolve_ambig_calls(c, scope)[0], {ambig_field}
            )

            match strat:
                case AmbigCallResolution.BubbleUp:
                    # in this case, the operand should be applied to the entire unambig_expr,
                    # as it was resolved to not be a binary expr (implicit multiplication)
                    # so we just inject the resolved value into the unambig_expr
                    return (
                        attrs.evolve(
                            unambig_expr,
                            **{ambig_field.name: unambig_val},
                        ),
                        AmbigCallResolution.BubbleUp,
                    )
                case AmbigCallResolution.ImplicitMult:
                    # in this case, the operand should be applied to the rhs of unambig_expr,
                    # as it was resolved to be a binary expr (implicit multiplication)
                    assert isinstance(unambig_val, Ast.MultOp)
                    return (
                        Ast.MultOp(
                            expr.ctx,
                            unambig_val.lhs,
                            attrs.evolve(
                                unambig_expr,
                                **{ambig_field.name: unambig_val.rhs},
                            ),
                        ),
                        AmbigCallResolution.BubbleUp,
                    )

        case Ast.AstNode(_) as node:
            return (
                visit_children(node, lambda c: a_expr_resolve_ambig_calls(c, scope)[0]),
                AmbigCallResolution.BubbleUp,
            )


def a_expr_sub_bindings(
    expr: Ast.AExpr, scope: Scope, lit_eq_checker: LiteralParam.EqChecker
) -> Ast.AExpr:
    """
    Goes through the given expr and substitutes values in the AST, based on bindings in the provided scope.
    """

    # get the signature for the potential substitution target
    signature = Signature.from_a_expr(expr)

    if signature is not None:
        resolved_binding_id = scope.resolve(signature, lit_eq_checker)

        if resolved_binding_id is not None:
            # a binding has been found for the expression at this point
            # now we need to transform its bound value, and introduce new bindings in the scope,
            # coming from binding the signature to the resolved binding.
            binding_signature, bound_val = scope.get_binding(resolved_binding_id)

            bindings = binding_signature.bind(signature, lit_eq_checker)

            # also make sure bindings are resolved in the bindings...
            bindings = tuple(
                (sig, a_expr_sub_bindings(val, scope, lit_eq_checker))
                for (sig, val) in bindings
            )

            binding_ids = scope.register(bindings)

            # instead of recursively calling a_expr_subs here,
            # we call a_expr_2_sympy and memoize the result instead.
            # this greatly improves performance for recursive bindings with multiple recursive variables.
            sp_expr = a_expr_2_sympy(bound_val, scope)

            scope.unregister(binding_ids)

            sp_const = Ast.SympyConstant(bound_val.ctx, sp_expr)

            scope.reregister_single((binding_signature, sp_const), resolved_binding_id)

            return sp_const

    sub = lambda c: a_expr_sub_bindings(c, scope, lit_eq_checker)

    # expression should not be substituted itself
    # there are still some special cases where scope must be modified.
    match expr:
        case (
            Ast.Sum(_, sexpr, var, _)
            | Ast.Product(_, sexpr, var, _)
            | Ast.Limit(_, sexpr, var, _, _)
        ):
            # if an AstNode introduces a variable / symbol, this symbol must be temporarily unbounded in the scope.

            # first substitute bindings in fields which should use the current scope.
            # in the above cases, its the expr field which we want to evaluate with a new scope.
            # we also dont want to try to substitute in the value of the variable itself, in the field which stores the variable.
            # e.g. \sum_{i=0}^9 i
            #            ^      ^
            #            we dont want to substitute either of these occurenses of the symbol 'i'
            subbed_expr = visit_children(
                expr,
                sub,
                {
                    attrs.fields(Ast.Sum).var,
                    attrs.fields(Ast.Sum).expr,
                    attrs.fields(Ast.Product).var,
                    attrs.fields(Ast.Product).expr,
                    attrs.fields(Ast.Limit).var,
                    attrs.fields(Ast.Limit).expr,
                },
            )

            var_signature = Signature.from_a_expr(var)
            assert var_signature is not None

            var_binding_id = scope.resolve(var_signature, lit_eq_checker)

            if var_binding_id is not None:
                var_signature, var_bound_value = scope.get_binding(var_binding_id)

                # the variable was bound to something, so bind it to None temprorarily whilst evaluating the expr field.
                scope.reregister_single((var_signature, None), var_binding_id)

            subbed_expr = attrs.evolve(
                subbed_expr, expr=a_expr_sub_bindings(sexpr, scope, lit_eq_checker)
            )

            # now reregister the original binding in the scope.
            if var_binding_id is not None:
                scope.reregister_single(
                    (var_signature, var_bound_value), var_binding_id
                )

            return subbed_expr
        case _:
            return visit_children(
                expr,
                sub,
                {
                    attrs.fields(Ast.Integral).diff,
                    attrs.fields(Ast.Differential).differentials,
                },
            )


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


def a_expr_2_sympy(expr: Ast.AExpr, s: Scope) -> sp.Basic | sp.MatrixBase:
    expr = a_expr_sub_bindings(expr, s, literal_sp_comparer(s))
    return _a_expr_2_sympy(expr)


# Transform an Ast.AExpr into a sympy expression,
# Substituting variables defined in the given scope along the way.
def _a_expr_2_sympy(expr: Ast.AExpr) -> sp.Basic | sp.MatrixBase:
    ev = _a_expr_2_sympy
    # TODO: scope should not be here, it should be in a_expr_subs
    match expr:
        case Ast.ApplyFunc(_, _, _):
            assert False, "Cannot handle ApplyFunc without definitions"

        case Ast.SubscriptOp(_, Ast.Symbol(_, name), subscript):
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
                [[ev(e) for e in r] for r in elems],
                env_begin=beg_cmd,
                env_end=end_cmd,
            )

        case Ast.DetMatrix(_, elems):
            return sp.Matrix([[ev(e) for e in r] for r in elems]).det()

        case Ast.ExpOp(_, base, exp):
            return ev(base) ** ev(exp)

        case Ast.MultOp(_, lhs, rhs):
            return ev(lhs) * ev(rhs)

        case Ast.XProdOp(_, lhs, rhs):
            return MatrixUtils.ensure_matrix(ev(lhs)).cross(ev(rhs))

        case Ast.DotProd(_, lhs, rhs):
            return MatrixUtils.ensure_matrix(ev(lhs)).dot(
                ev(rhs), conjugate_convention="right"
            )

        case Ast.DivOp(_, lhs, rhs):
            return ev(lhs) / ev(rhs)

        case Ast.ModOp(_, lhs, rhs):
            return sp.Mod(ev(lhs), ev(rhs))

        case Ast.AddOp(_, lhs, rhs):
            return ev(lhs) + ev(rhs)

        case Ast.SubOp(_, lhs, rhs):
            return ev(lhs) - ev(rhs)

        case Ast.UPlusOp(_, op):
            return +ev(op)

        case Ast.UMinusOp(_, op):
            return -ev(op)

        case Ast.Parens(_, expr):
            return ev(expr)

        case Ast.Abs(_, expr):
            evd_expr = ev(expr)

            if MatrixUtils.is_matrix(evd_expr):
                return cast(sp.MatrixBase, evd_expr).det()

            return sp.Abs(evd_expr)

        case Ast.Norm(_, expr):
            return MatrixUtils.ensure_matrix(ev(expr)).norm()

        case Ast.UnitVec(_, expr):
            return MatrixUtils.ensure_matrix(ev(expr)).normalized()

        case Ast.Floor(_, expr):
            return sp.floor(ev(expr))

        case Ast.Ceil(_, expr):
            return sp.ceiling(ev(expr))

        case Ast.Conjugate(_, expr):
            return sp.conjugate(ev(expr))

        case Ast.Binom(_, n, k):
            return sp.binomial(ev(n), ev(k))

        case Ast.Permutations(_, n, r):
            return Functions.permutations(cast(sp.Expr, ev(n)), cast(sp.Expr, ev(r)))

        case Ast.Derangements(_, n):
            return Functions.derangements(cast(sp.Expr, ev(n)))

        case Ast.Factorial(_, expr):
            return sp.factorial(expr)

        case Ast.Percent(_, expr):
            return sp.Mul(cast(sp.Expr, ev(expr)), 100**-1)

        case Ast.Permille(_, expr):
            return sp.Mul(cast(sp.Expr, ev(expr)), 1000**-1)

        case Ast.Sum(_, expr, var, bounds):
            start, end = bounds
            return sp.Sum(ev(expr), (ev(var), ev(start), ev(end)))

        case Ast.Product(_, expr, var, bounds):
            start, end = bounds
            return sp.Product(ev(expr), (ev(var), ev(start), ev(end)))

        case Ast.Integral(_, expr, diff, None):
            return sp.integrate(ev(expr), ev(diff))

        case Ast.Integral(_, expr, diff, bounds):
            assert bounds is not None
            start, end = bounds
            return sp.integrate(ev(expr), (ev(diff), ev(start), ev(end)))

        case Ast.Differential(_, expr, diffs):
            return sp.diff(
                ev(expr),
                ((ev(diff), ev(deg) if deg is not None else 1) for diff, deg in diffs),
            )

        case Ast.Limit(_, expr, var, point_of_approach, dir):
            return sp.limit(ev(expr), ev(var), ev(point_of_approach), dir.value)

        case Ast.EvalAt(_, _, _, _):
            assert False
            return None

        case Ast.Root(_, expr, None):
            return sp.sqrt(ev(expr))

        case Ast.Root(_, expr, index):
            assert index is not None
            return sp.root(ev(expr), ev(index))

        case Ast.SympyConstant(_, val):
            return val

        case ir if isinstance(ir, Ast.Ir):
            assert "Cannot evaluate if Ir object is present in AST"
            return None
