import sympy as sp

from lmat_cas_client.compiling.antlr.ast import AlgStmtAst
from lmat_cas_client.compiling.antlr.ast.AlgStmtAst import SubscriptForm
from lmat_cas_client.compiling.antlr.ast.AstNode import visit_children
from lmat_cas_client.compiling.antlr.ast.DefStmtAst import (
    Assumption,
    BindingStmt,
    BindingStmts,
    Definition,
    Set,
    SetBound,
    SetType,
)
from lmat_cas_client.compiling.antlr.evaluation.CasExprTransformer import symbol_2_str
from lmat_cas_client.compiling.antlr.evaluation.Scope import (
    BoundParam,
    LiteralParam,
    OptBinding,
    Params,
    Signature,
)


def binding_stmts_2_bindings(stmts: BindingStmts) -> tuple[OptBinding, ...]:
    return tuple(map(binding_stmt_2_binding, stmts))


def binding_stmt_2_binding(stmt: BindingStmt) -> OptBinding:
    match stmt:
        case Definition():
            return definition_2_binding(stmt)
        case Assumption():
            return assumption_2_binding(stmt)


def extract_symbols(expr: AlgStmtAst.AExpr) -> set[AlgStmtAst.AExpr]:
    match expr:
        case AlgStmtAst.Symbol() | AlgStmtAst.SubscriptOp(_, AlgStmtAst.Symbol(), _):
            return {expr}
        case _:
            symbols: set[AlgStmtAst.AExpr] = set()

            def combine_child(c: AlgStmtAst.AExpr):
                symbols.update(extract_symbols(c))

                return c

            visit_children(expr, combine_child)

            return symbols


def definition_2_binding(definition: Definition) -> OptBinding:
    print("DEFINITION: ", definition, flush=True)
    subscript_form = SubscriptForm()
    index_params: Params = ()

    if definition.subscript is not None:
        symbols_in_body = (
            extract_symbols(definition.body) if definition.body is not None else {}
        )

        assert all(
            isinstance(slot, AlgStmtAst.AExpr)
            for slot in definition.subscript.slots
        )
        subscript_form = definition.subscript.form

        for slot in definition.subscript.slots:
            assert isinstance(slot, AlgStmtAst.AExpr)
            if slot in symbols_in_body:
                signature = Signature.from_a_expr(slot)
                assert signature is not None

                index_params = (*index_params, BoundParam(signature))
            else:
                index_params = (*index_params, LiteralParam(slot))

    arg_params: Params = ()

    if definition.func_args is not None:
        arg_params = tuple(map(LiteralParam, definition.func_args))

    signature = Signature(
        definition.head.name, subscript_form, index_params, arg_params
    )

    return (signature, definition.body)


def assumption_2_binding(assumption: Assumption) -> OptBinding:
    subscript_form = SubscriptForm()
    index_params: Params = ()

    if assumption.subscript is not None:
        assert all(
            isinstance(slot, AlgStmtAst.AExpr)
            for slot in assumption.subscript.slots
        )
        subscript_form = assumption.subscript.form
        index_params = tuple(map(LiteralParam, assumption.subscript.slots))  # type: ignore[arg-type]

    arg_params: Params = ()

    if assumption.func_args is not None:
        arg_params = tuple(map(LiteralParam, assumption.func_args))

    signature = Signature(
        assumption.head.name, subscript_form, index_params, arg_params
    )

    match assumption.set:
        case None:
            return (signature, None)
        case s:
            if assumption.func_args is None:
                return (
                    signature,
                    sp.Symbol(
                        symbol_2_str(assumption.head, assumption.subscript),
                        **set_2_assumptions(s),
                    ),
                )
            else:
                return (
                    signature,
                    sp.Function(
                        symbol_2_str(assumption.head, assumption.subscript),
                        **set_2_assumptions(s),
                    ),
                )


def set_2_assumptions(set: Set) -> dict[str, bool]:
    assumptions: dict[str, bool] = {}

    match set.set_type:
        case SetType.COMPLEX:
            assumptions = {"complex": True}
        case SetType.REAL:
            assumptions = {"real": True}
        case SetType.IMAGINARY:
            assumptions = {"imaginary": True}
        case SetType.RATIONAL:
            assumptions = {"rational": True}
        case SetType.INTEGER:
            assumptions = {"integer": True}
        case SetType.NATURAL:
            assumptions = {"integer": True, "positive": True, "nonzero": True}
        case SetType.EVEN:
            assumptions = {"even": True}
        case SetType.ODD:
            assumptions = {"odd": True}
        case SetType.PRIME:
            assumptions = {"prime": True}
        case SetType.EXT_REAL:
            assumptions = {"extended_real": True}
        case SetType.ALGEBRAIC:
            assumptions = {"algebraic": True}

    match set.set_bound:
        case SetBound.POSITIVE:
            assumptions = {**assumptions, "positive": True}
        case SetBound.NONNEGATIVE:
            assumptions = {**assumptions, "nonnegative": True}
        case SetBound.NEGATIVE:
            assumptions = {**assumptions, "negative": True}
        case SetBound.NONPOSITIVE:
            assumptions = {**assumptions, "nonpositive": True}
        case SetBound.NONZERO:
            assumptions = {**assumptions, "nonzero": True}
        case SetBound.NONE:
            pass

    return assumptions
