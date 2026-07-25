import sys
from typing import Self

import pytest

from lmat_cas_client.compiling.antlr.ast import AlgStmtAst as Ast
from lmat_cas_client.compiling.antlr.evaluation.AlgStmtTransformer import (
    a_expr_2_sympy,
    a_expr_resolve_ambig_calls,
    literal_sp_comparer,
)
from lmat_cas_client.compiling.antlr.evaluation.Scope import (
    BoundParam,
    LiteralParam,
    Scope,
    Signature,
)
from lmat_cas_client.compiling.antlr.lexer.StreamFromSrc import stream_from_src
from lmat_cas_client.compiling.antlr.parser.AlgStmtGrammar import AlgStmtGrammar
from lmat_cas_client.compiling.antlr.parser.AlgStmtLexer import AlgStmtLexer


def parse(src: str) -> Ast.AExpr:
    return AlgStmtGrammar(stream_from_src(AlgStmtLexer, src)).a_expr().res


def lit_eq(a: LiteralParam, b: LiteralParam) -> bool:
    return literal_sp_comparer(Scope())(a, b)


# ============================================================
#  Signature unit tests
# ============================================================


class TestSignatureFromAExpr:
    @pytest.mark.parametrize(
        ("src", "expected_head", "expected_index_count", "expected_arg_count"),
        [
            ("x", "x", 0, 0),
            ("x_i", "x", 1, 0),
        ],
    )
    def test_valid(
        self, src: str, expected_head: str, expected_index_count: int, expected_arg_count: int
    ) -> None:
        sig = Signature.from_a_expr(parse(src))
        assert sig is not None
        assert sig.head_id == expected_head
        assert len(sig.index_params) == expected_index_count
        assert len(sig.arg_params) == expected_arg_count

    @pytest.mark.parametrize(
        "src",
        [
            "42",
            "a + b",
            "x_{1:2}",
        ],
    )
    def test_invalid(self, src: str) -> None:
        assert Signature.from_a_expr(parse(src)) is None

    @pytest.mark.parametrize(
        ("src", "register_sig", "expected_head", "expected_index_count", "expected_arg_count"),
        [
            (
                "f(x)",
                Signature(
                    head_id="f",
                    arg_params=(BoundParam(Signature(head_id="x")),),
                ),
                "f", 0, 1,
            ),
            (
                "f_i(x)",
                Signature(
                    head_id="f",
                    index_params=(BoundParam(Signature(head_id="i")),),
                    arg_params=(BoundParam(Signature(head_id="x")),),
                ),
                "f", 1, 1,
            ),
        ],
    )
    def test_function_call(
        self, src: str, register_sig: Signature,
        expected_head: str, expected_index_count: int, expected_arg_count: int,
    ) -> None:
        s = Scope()
        s.register_single((register_sig, parse("0")))
        resolved, _ = a_expr_resolve_ambig_calls(parse(src), s)
        assert isinstance(resolved, Ast.AExpr)
        sig = Signature.from_a_expr(resolved)
        assert sig is not None
        assert sig.head_id == expected_head
        assert len(sig.index_params) == expected_index_count
        assert len(sig.arg_params) == expected_arg_count

class TestSignatureTryBind:
    @pytest.mark.parametrize(
        ("pattern", "target", "expected_binding_count"),
        [
            (Signature(head_id="x"), Signature(head_id="x"), 0),
            (
                Signature(
                    head_id="x",
                    index_params=(BoundParam(Signature(head_id="i")),),
                ),
                Signature(
                    head_id="x",
                    index_params=(LiteralParam(parse("a")),),
                ),
                1,
            ),
            (
                Signature(
                    head_id="x",
                    index_params=(LiteralParam(parse("i")),),
                ),
                Signature(
                    head_id="x",
                    index_params=(LiteralParam(parse("i")),),
                ),
                0,
            ),
            (
                Signature(
                    head_id="f",
                    index_params=(BoundParam(Signature(head_id="i")),),
                    arg_params=(LiteralParam(parse("x")),),
                ),
                Signature(
                    head_id="f",
                    index_params=(LiteralParam(parse("a")),),
                    arg_params=(LiteralParam(parse("x")),),
                ),
                1,
            ),
        ],
    )
    def test_success(
        self, pattern: Signature, target: Signature, expected_binding_count: int
    ) -> None:
        result = pattern.try_bind(target, lit_eq)
        assert result is not None
        assert len(result) == expected_binding_count

    @pytest.mark.parametrize(
        ("pattern", "target", "reason"),
        [
            (Signature(head_id="x"), Signature(head_id="y"), "head_id mismatch"),
            (
                Signature(head_id="x", index_params=(LiteralParam(parse("i")),)),
                Signature(head_id="x"),
                "index param count mismatch",
            ),
            (
                Signature(head_id="f", arg_params=(LiteralParam(parse("x")),)),
                Signature(head_id="f"),
                "arg param count mismatch",
            ),
            (
                Signature(
                    head_id="x",
                    index_params=(LiteralParam(parse("i")),),
                ),
                Signature(
                    head_id="x",
                    index_params=(BoundParam(Signature(head_id="j")),),
                ),
                "pattern has LiteralParam where target has BoundParam",
            ),
            (
                Signature(
                    head_id="x",
                    index_params=(LiteralParam(parse("i")),),
                ),
                Signature(
                    head_id="x",
                    index_params=(LiteralParam(parse("j")),),
                ),
                "literal values differ",
            ),
        ],
    )
    def test_failure(self, pattern: Signature, target: Signature, reason: str) -> None:
        assert pattern.try_bind(target, lit_eq) is None, reason


class TestSignaturePostInit:
    @pytest.mark.parametrize(
        "sig",
        [
            Signature(head_id="x"),
            Signature(head_id="x", subscript_form=Ast.SubscriptForm()),
            Signature(
                head_id="x",
                index_params=(LiteralParam(parse("i")),),
            ),
            Signature(
                head_id="x",
                index_params=(
                    LiteralParam(parse("i")),
                    LiteralParam(parse("j")),
                ),
                subscript_form=Ast.SubscriptForm((None, None), (",",)),
            ),
        ],
    )
    def test_valid(self, sig: Signature) -> None:
        pass  # no exception means valid


# ============================================================
#  Scope unit tests
# ============================================================


class TestScopeParentChild:
    def test_unregister_parent_removes_children(self) -> None:
        s = Scope()
        parent_id = s.register_single((Signature(head_id="x"), parse("0")))
        child1_id = s.register_single((Signature(head_id="y"), parse("1")), parent=parent_id)
        child2_id = s.register_single((Signature(head_id="z"), parse("2")), parent=parent_id)

        s.unregister_single(parent_id)

        with pytest.raises(KeyError):
            s.get_binding(parent_id)
        with pytest.raises(KeyError):
            s.get_binding(child1_id)
        with pytest.raises(KeyError):
            s.get_binding(child2_id)

    def test_unregister_parent_removes_grandchildren(self) -> None:
        s = Scope()
        grandparent_id = s.register_single((Signature(head_id="a"), parse("0")))
        parent_id = s.register_single((Signature(head_id="b"), parse("1")), parent=grandparent_id)
        child_id = s.register_single((Signature(head_id="c"), parse("2")), parent=parent_id)

        s.unregister_single(grandparent_id)

        with pytest.raises(KeyError):
            s.get_binding(grandparent_id)
        with pytest.raises(KeyError):
            s.get_binding(parent_id)
        with pytest.raises(KeyError):
            s.get_binding(child_id)

    def test_unregister_child_does_not_affect_parent(self) -> None:
        s = Scope()
        parent_id = s.register_single((Signature(head_id="x"), parse("0")))
        child_id = s.register_single((Signature(head_id="y"), parse("1")), parent=parent_id)

        s.unregister_single(child_id)

        with pytest.raises(KeyError):
            s.get_binding(child_id)

        sig, body = s.get_binding(parent_id)
        assert sig.head_id == "x"

    def test_unregister_one_child_does_not_affect_siblings(self) -> None:
        s = Scope()
        parent_id = s.register_single((Signature(head_id="x"), parse("0")))
        child1_id = s.register_single((Signature(head_id="y"), parse("1")), parent=parent_id)
        child2_id = s.register_single((Signature(head_id="z"), parse("2")), parent=parent_id)

        s.unregister_single(child1_id)

        with pytest.raises(KeyError):
            s.get_binding(child1_id)

        sig, body = s.get_binding(child2_id)
        assert sig.head_id == "z"

    def test_register_with_nonexistent_parent_raises(self) -> None:
        s = Scope()
        with pytest.raises(AssertionError):
            s.register_single((Signature(head_id="x"), parse("0")), parent=999)

    def test_unregister_parent_removes_only_subtree(self) -> None:
        s = Scope()
        root_id = s.register_single((Signature(head_id="root"), parse("0")))
        branch_id = s.register_single((Signature(head_id="branch"), parse("1")), parent=root_id)
        leaf_id = s.register_single((Signature(head_id="leaf"), parse("2")), parent=branch_id)
        other_id = s.register_single((Signature(head_id="other"), parse("3")))

        s.unregister_single(branch_id)

        with pytest.raises(KeyError):
            s.get_binding(branch_id)
        with pytest.raises(KeyError):
            s.get_binding(leaf_id)

        sig, body = s.get_binding(root_id)
        assert sig.head_id == "root"

        sig, body = s.get_binding(other_id)
        assert sig.head_id == "other"


class TestScopeUnregister:

    def test_unregister(self) -> None:
        s = Scope()
        ids = s.register(
            (
                (Signature(head_id="a"), parse("0")),
                (Signature(head_id="b"), parse("1")),
                (Signature(head_id="c"), parse("2")),
            )
        )

        s.unregister((ids[0], ids[2]))

        with pytest.raises(KeyError):
            s.get_binding(ids[0])
        with pytest.raises(KeyError):
            s.get_binding(ids[2])

        sig, body = s.get_binding(ids[1])
        assert sig.head_id == "b"
        assert isinstance(body, Ast.Number) and body.number == "1"


class TestScopeGetBinding:
    def test_get_opt_binding(self) -> None:
        s = Scope()
        id0 = s.register_single((Signature(head_id="x"), parse("42")))

        sig, body = s.get_opt_binding(id0)
        assert sig.head_id == "x"
        assert isinstance(body, Ast.Number) and body.number == "42"

    def test_get_binding_raises_on_none_body(self) -> None:
        s = Scope()
        id0 = s.register_single((Signature(head_id="x"), None))
        with pytest.raises(KeyError, match="None body"):
            s.get_binding(id0)

    def test_get_binding_raises_on_missing_id(self) -> None:
        s = Scope()
        with pytest.raises(KeyError):
            s.get_binding(-1)


class TestScopeResolve:
    @pytest.mark.parametrize(
        ("register_sigs", "target"),
        [
            # single binding, exact match
            ([Signature(head_id="x")], Signature(head_id="x")),
            # multiple different head_ids
            ([Signature(head_id="x"), Signature(head_id="y")], Signature(head_id="x")),
            # subscript with matching literal
            (
                [Signature(
                    head_id="x",
                    index_params=(LiteralParam(parse("i")),),
                )],
                Signature(
                    head_id="x",
                    index_params=(LiteralParam(parse("i")),),
                ),
            ),
            # bound param pattern matches any literal
            (
                [Signature(
                    head_id="x",
                    index_params=(BoundParam(Signature(head_id="i")),),
                )],
                Signature(
                    head_id="x",
                    index_params=(LiteralParam(parse("a")),),
                ),
            ),
        ],
    )
    def test_finds_binding(
        self,
        register_sigs: list[Signature],
        target: Signature,
    ) -> None:
        s = Scope()
        for sig in register_sigs:
            s.register_single((sig, parse("0")))
        result = s.resolve(target, lit_eq)
        assert result is not None
        resolved_sig, _ = s.get_binding(result)
        assert resolved_sig.head_id == target.head_id

    @pytest.mark.parametrize(
        ("register_sigs", "target"),
        [
            ([], Signature(head_id="x")),
            ([(Signature(head_id="y"), parse("0"))], Signature(head_id="x")),
            (
                [(Signature(head_id="x", index_params=(LiteralParam(parse("i")),)), parse("0"))],
                Signature(head_id="x"),
            ),
            (
                [(Signature(head_id="f", arg_params=(LiteralParam(parse("x")),)), parse("0"))],
                Signature(head_id="f"),
            ),
            (
                [(Signature(head_id="x", index_params=(LiteralParam(parse("i")),)), parse("0"))],
                Signature(head_id="x", index_params=(LiteralParam(parse("j")),)),
            ),
            (
                [(Signature(head_id="x"), None)],
                Signature(head_id="x"),
            ),
        ],
    )
    def test_fail_resolve(
        self, register_sigs: list[tuple[Signature, Ast.AExpr | None]], target: Signature
    ) -> None:
        s = Scope()
        for sig, body in register_sigs:
            s.register_single((sig, body))
        assert s.resolve(target, lit_eq) is None

    @pytest.mark.parametrize(
        ("register_sigs", "target", "expected_body_src"),
        [
            # higher priority (LiteralParams) wins over lower (BoundParams)
            (
                [
                    (Signature(
                        head_id="x",
                        index_params=(BoundParam(Signature(head_id="i")),),
                        arg_params=(BoundParam(Signature(head_id="j")),),
                    ), parse("low")),
                    (Signature(
                        head_id="x",
                        index_params=(LiteralParam(parse("k")),),
                        arg_params=(LiteralParam(parse("v")),),
                    ), parse("high")),
                ],
                Signature(
                    head_id="x",
                    index_params=(LiteralParam(parse("k")),),
                    arg_params=(LiteralParam(parse("v")),),
                ),
                "high",
            ),
            # later registration wins for equal priority
            (
                [
                    (Signature(head_id="x"), parse("first")),
                    (Signature(head_id="x"), parse("second")),
                ],
                Signature(head_id="x"),
                "second",
            ),
        ],
    )
    def test_resolve_priority(
        self,
        register_sigs: list[tuple[Signature, Ast.AExpr]],
        target: Signature,
        expected_body_src: str,
    ) -> None:
        s = Scope()
        for sig, body in register_sigs:
            s.register_single((sig, body))
        result = s.resolve(target, lit_eq)
        assert result is not None
        _, body = s.get_binding(result)
        assert lit_eq(LiteralParam(body), LiteralParam(parse(expected_body_src)))


# ============================================================
#  Existing integration tests (unchanged)
# ============================================================


class TestScopeIntegration:
    def test_scope(self: Self) -> None:
        s = Scope()

        s.register_single(
            (
                Signature(
                    head_id="x",
                    index_params=(LiteralParam(parse("i")),),
                ),
                parse("42"),
            )
        )

        expr = parse("x_i")

        tsp = a_expr_2_sympy(expr, s)
        assert tsp == 42

    @pytest.mark.skip(reason="Unfinished — needs correct expected value")
    def test_scope_more(self: Self) -> None:
        sys.setrecursionlimit(100000)
        s = Scope()

        s.register(
            (
                (
                    Signature(
                        head_id="x",
                        index_params=(BoundParam(Signature(head_id="i")),),
                    ),
                    parse(r"x_{i - 1} + (\sum_{i=0}^{i} i^2)^i"),
                ),
                (
                    Signature(
                        head_id="x",
                        index_params=(LiteralParam(parse("0")),),
                    ),
                    parse("0"),
                ),
            )
        )

        expr = parse("x_{10}")

        tsp = a_expr_2_sympy(expr, s)
        assert tsp == sum(range(11))

    def test_fibonacci(self) -> None:
        s = Scope()

        s.register(
            (
                (
                    Signature(
                        head_id="F",
                        arg_params=(BoundParam(Signature(head_id="n")),),
                    ),
                    parse(r"F(n - 1) + F(n - 2)"),
                ),
                (
                    Signature(
                        head_id="F",
                        arg_params=(LiteralParam(parse("0")),),
                    ),
                    parse("0"),
                ),
                (
                    Signature(
                        head_id="F",
                        arg_params=(LiteralParam(parse("1")),),
                    ),
                    parse("1"),
                ),
            )
        )

        expr = parse("F(10)")

        tsp = a_expr_2_sympy(expr, s)
        assert tsp == 55
