from typing import cast

from lark import Token, Transformer, v_args
from lark.tree import Meta
from lmat_cas_client.compiling.definition.Resolver import DefinitionResolver
from lmat_cas_client.compiling.transforming.cas_expr.CasExprTransformer import (
    CasExpr,
    cas_expr_transformer,
)
from lmat_cas_client.compiling.transforming.ComposeTransformers import (
    compose_transformers,
)
from lmat_cas_client.compiling.transforming.Ir import ir_strat
from lmat_cas_client.compiling.transforming.TransformerRunner import TransformerRunner
from sympy import *
from sympy.logic.boolalg import *


@v_args(inline=True)
class CasLogicTransformer(Transformer):
    """
    The FucntionsTransformer holds the implementation of various mathematical function rules,
    defined in the latex math grammar.
    """

    def CMD_TAUTOLOGY(self, _) -> Expr:
        return S.true

    def CMD_FALSUM(self, _) -> Expr:
        return S.false

    @v_args(meta=True, inline=True)
    def cas_logic_expression(self, meta: Meta, *props: Basic) -> CasExpr:
        return CasExpr(tuple([(prop, meta) for prop in props]))

    @ir_strat()
    def prop_iff(self, *args: tuple[Expr]) -> Basic:
        return Equivalent(*args)

    @ir_strat()
    def prop_negated_iff(self, *args: tuple[Expr]) -> BooleanFunction:
        return Not(Equivalent(*args))

    @ir_strat()
    def prop_implies(self, *args: Expr | Token) -> Expr:
        reversed_args = list(reversed(args))

        while len(reversed_args) > 1:
            left: Expr = cast(Expr, reversed_args.pop())
            op_token: Token = cast(Token, reversed_args.pop())
            right: Expr = cast(Expr, reversed_args.pop())

            match op_token.type:
                case "_LR_IMPLICATION":
                    implication = Implies(left, right, evaluate=False)
                case "_NEG_LR_IMPLICATION":
                    implication = Not(
                        Implies(left, right, evaluate=False), evaluate=False
                    )
                case "_RL_IMPLICATION":
                    implication = Implies(right, left, evaluate=False)
                case "_NEG_RL_IMPLICATION":
                    implication = Not(
                        Implies(right, left, evaluate=False), evaluate=False
                    )
                case _:
                    raise ValueError(f"Unexpected token: {repr(op_token)}")

            reversed_args.append(implication)

        return cast(Expr, reversed_args[0])

    @ir_strat()
    def prop_or(self, *args: Boolean) -> BooleanFunction:
        return Or(*args)

    @ir_strat()
    def prop_nand(self, *args: Boolean) -> BooleanFunction:
        return Nand(*args)

    @ir_strat()
    def prop_and(self, *args: Boolean) -> BooleanFunction:
        return And(*args)

    @ir_strat()
    def prop_nor(self, *args: Boolean) -> BooleanFunction:
        return Nor(*args)

    @ir_strat()
    def prop_xor(self, *args: Boolean) -> BooleanFunction:
        return Xor(*args)

    @ir_strat()
    def prop_xnor(self, *args: Boolean) -> BooleanFunction:
        return Xnor(*args)

    @ir_strat()
    def prop_not(self, arg: Boolean) -> BooleanFunction:
        return Not(arg)


cas_logic_expr_transformer_runner = TransformerRunner[[DefinitionResolver], CasExpr](
    lambda drs: compose_transformers(
        CasLogicTransformer(),
        cas_expr_transformer(drs),
    )
)

__all__ = ["cas_logic_expr_transformer_runner"]
