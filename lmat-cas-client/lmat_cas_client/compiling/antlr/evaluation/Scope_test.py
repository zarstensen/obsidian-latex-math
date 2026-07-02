from typing import Self
import sympy as sp

from lmat_cas_client.compiling.antlr import Ast, ExprLexer
from lmat_cas_client.compiling.antlr.evaluation.CasExprTransformer import (
    a_expr_2_sympy,
)
from lmat_cas_client.compiling.antlr.ExprGrammar import ExprGrammar
from lmat_cas_client.compiling.antlr.evaluation.Scope import (
    BoundParam,
    LiteralParam,
    Scope,
    Signature,
)


class TestScope:
    def test_scope(self: Self) -> None:
        s: Scope = Scope()

        s.register_single(
            (
                Signature(
                    head_id="x",
                    index_params=(LiteralParam(Ast.Symbol(None, "i")),),
                ),
                ExprGrammar(ExprLexer.stream_from_src("42")).a_expr().res,
            )
        )

        expr = ExprGrammar(ExprLexer.stream_from_src("x_i")).a_expr().res

        tsp = a_expr_2_sympy(expr, s)
        assert tsp == 42

    def test_scope_more(self: Self) -> None:
        s: Scope = Scope()

        s.register(
            (
                (
                    Signature(
                        head_id="x",
                        index_params=(BoundParam(Signature(head_id="i")),),
                    ),
                    ExprGrammar(ExprLexer.stream_from_src("x_{i - 1}")).a_expr().res,
                ),
                (
                    Signature(
                        head_id="x",
                        index_params=(LiteralParam(Ast.Number(None, "0")),),
                    ),
                    ExprGrammar(ExprLexer.stream_from_src("0")).a_expr().res,
                ),
            )
        )

        expr = ExprGrammar(ExprLexer.stream_from_src("x_{10}")).a_expr().res

        tsp = a_expr_2_sympy(expr, s)
        assert tsp == sum(range(11))
