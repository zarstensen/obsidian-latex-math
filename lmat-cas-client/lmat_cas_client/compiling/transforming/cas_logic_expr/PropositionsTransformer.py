from lark import Token, Transformer, v_args
from lmat_cas_client.compiling.definition.Resolver import DefinitionResolver
from lmat_cas_client.compiling.transforming.cas_expr.CasExprTransformer import (
    CasExpr,
    cas_expr_transformer,
)
from lmat_cas_client.compiling.transforming.ComposeTransformers import (
    compose_transformers,
)
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
    def cas_logic_expression(self, meta, *props: Expr) -> CasExpr:
        return CasExpr([(prop, meta) for prop in props])

    def prop_iff(self, *args: tuple[Expr]) -> Expr:
        return Equivalent(*args)

    def prop_negated_iff(self, *args: tuple[Expr]) -> Expr:
        return Not(Equivalent(*args))

    def prop_implies(self, *args: tuple[Expr | Token]) -> Expr:
        args = list(reversed(args))

        while len(args) > 1:
            left = args.pop()
            op_token = args.pop()
            right = args.pop()

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

            args.append(implication)

        return args[0]

    def prop_or(self, *args: tuple[Expr]) -> Expr:
        return Or(*args, evaluate=False)

    def prop_nand(self, *args: tuple[Expr]) -> Expr:
        return Nand(*args, evaluate=False)

    def prop_and(self, *args: tuple[Expr]) -> Expr:
        return And(*args, evaluate=False)

    def prop_nor(self, *args: tuple[Expr]) -> Expr:
        return Nor(*args, evaluate=False)

    def prop_xor(self, *args: tuple[Expr]) -> Expr:
        return Xor(*args, evaluate=False)

    def prop_xnor(self, *args: tuple[Expr]) -> Expr:
        return Xnor(*args, evaluate=False)

    def prop_not(self, arg: Expr) -> Expr:
        return Not(arg, evaluate=False)


cas_logic_expr_transformer_runner = TransformerRunner[[DefinitionResolver], CasExpr](
    lambda drs: compose_transformers(
        CasLogicTransformer(),
        cas_expr_transformer(drs),
    )
)

__all__ = ["cas_logic_expr_transformer_runner"]
