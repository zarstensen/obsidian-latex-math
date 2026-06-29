from typing import Self

from lmat_cas_client.compiling.antlr import Ast, ExprLexer
from lmat_cas_client.compiling.antlr.evaluation.CasExprTransformer import (
    FixedParam,
    Overrides,
    OverrideSpec,
    Scope,
    a_expr_2_sympy,
)
from lmat_cas_client.compiling.antlr.ExprGrammar import ExprGrammar


class TestScope:
    def test_scope(self: Self) -> None:
        s: Scope = {
            ("x", None): Overrides(0).add(
                (
                    OverrideSpec((), ()),
                    ExprGrammar(ExprLexer.stream_from_src("42")).a_expr().res,
                )
            ),
            ("x", Ast.SubscriptForm((None, None), ())): Overrides(1).add(
                (
                    OverrideSpec(
                        (
                            FixedParam(
                                ExprGrammar(ExprLexer.stream_from_src("i")).a_expr().res
                            )
                        ),
                        (),
                    ),
                    ExprGrammar(ExprLexer.stream_from_src("11")).a_expr().res,
                )
            ),
        }

        expr = ExprGrammar(ExprLexer.stream_from_src("x_i")).a_expr().res

        tsp = a_expr_2_sympy(expr, s)
        assert tsp == 11
