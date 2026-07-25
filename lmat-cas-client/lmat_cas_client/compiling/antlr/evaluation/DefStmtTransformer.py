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
from lmat_cas_client.compiling.antlr.evaluation.AlgStmtTransformer import symbol_2_str
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

    assert False, "unreachable"


def extract_symbols(expr: AlgStmtAst.AExpr) -> set[AlgStmtAst.AExpr]:
    symbols: set[AlgStmtAst.AExpr] = set()

    def combine_child(c: AlgStmtAst.AExpr):
        symbols.update(extract_symbols(c))
        return c

    match expr:
        case AlgStmtAst.SubscriptOp(_, AlgStmtAst.Symbol(), subscript):
            symbols.add(expr)

            for slot in subscript.slots:
                if isinstance(slot, AlgStmtAst.AExpr) and Signature.from_a_expr(slot) is not None:
                        pass
                elif isinstance(slot, AlgStmtAst.AExpr):
                        combine_child(slot)
                elif isinstance(slot, tuple):
                    for e in slot:
                        if e is not None:
                            combine_child(e)
        case AlgStmtAst.Symbol():
            symbols.add(expr)
        case _:
            visit_children(expr, combine_child)

    return symbols


def definition_2_binding(definition: Definition) -> OptBinding:
    subscript_form = SubscriptForm()
    index_params: Params = ()

    if definition.signature.subscript is not None:
        symbols_in_body = (
            extract_symbols(definition.body) if definition.body is not None else {}
        )

        assert all(
            isinstance(slot, AlgStmtAst.AExpr)
            for slot in definition.signature.subscript.slots
        )
        subscript_form = definition.signature.subscript.form

        for slot in definition.signature.subscript.slots:
            assert isinstance(slot, AlgStmtAst.AExpr)
            if slot in symbols_in_body:
                signature = Signature.from_a_expr(slot)
                assert signature is not None

                index_params = (*index_params, BoundParam(signature))
            else:
                index_params = (*index_params, LiteralParam(slot))

    arg_params: Params = ()

    if definition.signature.func_args is not None:

        for arg in definition.signature.func_args:
            arg_sig = Signature.from_a_expr(arg)

            if arg_sig is not None:
                arg_params = (*arg_params, BoundParam(arg_sig))
            else:
                arg_params = (*arg_params, LiteralParam(arg))

    signature = Signature(
        definition.signature.head.name, subscript_form, index_params, arg_params
    )

    return (signature, definition.body)


def assumption_2_binding(assumption: Assumption) -> OptBinding:
    subscript_form = SubscriptForm()
    index_params: Params = ()

    if assumption.signature.subscript is not None:
        assert all(
            isinstance(slot, AlgStmtAst.AExpr)
            for slot in assumption.signature.subscript.slots
        )
        subscript_form = assumption.signature.subscript.form
        index_params = tuple(map(LiteralParam, assumption.signature.subscript.slots))  # type: ignore[arg-type]

    arg_params: Params = ()

    if assumption.signature.func_args is not None:
        arg_params = tuple(map(LiteralParam, assumption.signature.func_args))

    signature = Signature(
        assumption.signature.head.name, subscript_form, index_params, arg_params
    )

    match assumption.set:
        case None:
            return (signature, None)
        case s:
            if assumption.signature.func_args is None:
                return (
                    signature,
                    sp.Symbol(
                        symbol_2_str(assumption.signature.head, assumption.signature.subscript),
                        **set_2_assumptions(s),
                    ),
                )
            else:
                return (
                    signature,
                    sp.Function(
                        symbol_2_str(assumption.signature.head, assumption.signature.subscript),
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
