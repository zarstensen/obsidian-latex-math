import itertools
from enum import Enum
from typing import Iterable, Iterator, NamedTuple, cast

from lark import Token, Transformer, v_args
from lark.tree import Meta
from lmat_cas_client.compiling.definition.Resolver import (
    DefinitionResolver,
)
from lmat_cas_client.compiling.transforming.cas_expr.ConstantsTransformer import (
    ConstantsTransformer,
)
from lmat_cas_client.compiling.transforming.cas_expr.FunctionsTransformer import (
    BuiltInFunctionsTransformer,
    ImplicitMulStrategy,
    implicit_mul_strategy,
)
from lmat_cas_client.compiling.transforming.cas_expr.UndefinedAtomsTransformer import (
    UndefinedAtomsTransformer,
)
from lmat_cas_client.compiling.transforming.ComposeTransformers import (
    compose_transformers,
)
from lmat_cas_client.compiling.transforming.TransformerRunner import TransformerRunner
from lmat_cas_client.math_lib import MatrixUtils
from sympy import *
from sympy import Basic, Expr
from sympy.core.numbers import Float, Integer
from sympy.logic.boolalg import *

from ..LatexMatrix import LatexMatrix


class CasExpr(NamedTuple):
    """
    The CasExpr class represents a series of sympy expressions and their original locations in some source text.
    """

    expressions: tuple[tuple[Basic, Meta], ...]

    @staticmethod
    def from_cas_exprs(
        systems: Iterable["CasExpr"],
    ) -> "CasExpr":
        expressions: list[tuple[Basic, Meta]] = []

        for system in systems:
            expressions.extend(system.expressions)

        return CasExpr(tuple(expressions))

    # retreive number of expressions in the system
    def __len__(self):
        return len(self.expressions)

    # retreive the expression at the given index
    def get_expr(self, expression_index: int) -> Basic:
        (expr, _) = self.expressions[expression_index]
        return expr

    # retreive all expressions
    def get_all_expr(self) -> Iterator[Basic]:
        return map(self.get_expr, range(len(self)))

    # retreive location information about the given expression
    def get_location(self, expression_index: int) -> Meta:
        (_, meta) = self.expressions[expression_index]
        return meta

    # retreive all location information.
    def get_all_locations(self) -> Iterator[Meta]:
        return map(self.get_location, range(len(self)))


class CasExprTransformer(Transformer):
    """
    The SympyTransformer class provides functions for transforming
    rules defined in latex_math_grammar.lark into sympy expressions.
    """

    class Delim(Enum):
        MatDelim = 1

    @v_args(inline=True)
    def NUMERIC_DIGIT(self, digit: Token):
        return Integer(str(digit))

    @v_args(inline=True)
    def BASE_10_NUMBER(self, number: Token):
        number_str = str(number)

        if "." in number_str:
            return Float(number_str)

        return Integer(number_str)

    @v_args(inline=True)
    def HEXADECIMAL_NUMBER(self, number):
        hex_number_str = str(number).replace("\\mathrm{", "").replace("}", "").lower()

        return Integer(int(hex_number_str, 16))

    @v_args(inline=True)
    def OCTAL_NUMBER(self, number):
        octal_number_str = str(number).replace("\\mathrm{", "").replace("}", "")

        return Integer(int(octal_number_str, 8))

    @v_args(inline=True)
    def BINARY_NUMBER(self, number):
        binary_number_str = str(number).replace("\\mathrm{", "").replace("}", "")

        return Integer(int(binary_number_str, 2))

    @v_args(meta=True, inline=True)
    def cas_expression(
        self, meta: Meta, cas_expr: CasExpr | list[CasExpr] | Basic
    ) -> CasExpr:
        match cas_expr:
            case CasExpr():
                return cas_expr  # nothing to do, input is already CasExpr
            case list() as cas_exprs:
                return CasExpr.from_cas_exprs(cas_exprs)
            case sympy_expr:
                return CasExpr(tuple([(cast(Basic, sympy_expr), meta)]))

    def sor_env(self, relations: list[CasExpr | Delim]) -> CasExpr:
        return CasExpr.from_cas_exprs([
            cast(CasExpr, next(row))  # the row iterator should only contain 1 element
            for is_delim, row in itertools.groupby(
                relations, lambda t: t == self.Delim.MatDelim
            )
            if not is_delim
        ])

    def sor_and_chain(self, relations: list[CasExpr]) -> CasExpr:
        return CasExpr.from_cas_exprs(relations)

    @v_args(meta=True)
    def relation(self, meta: Meta, tokens: list[Expr | Token]) -> CasExpr:
        if len(tokens) == 1:
            return CasExpr(tuple([(cast(Expr, tokens[0]), meta)]))
        # construct a list of relations which later will be used to construct
        # a chained relation object.
        # a = b = c should produce [a = b, b = c],
        # that way when we chain them with and's (a = b & b = c),
        # it should be logically equivalent to a = b = c
        prev_expr: Expr = Dummy()
        relation_type = None

        relations = []

        for token in tokens:
            if isinstance(token, Token):
                relation_type = token.type
            else:
                if relation_type is not None:
                    relations.append(
                        self._create_relation(prev_expr, token, relation_type)
                    )
                    relation_type = None
                prev_expr = token

        if relation_type is not None:
            relations.append(self._create_relation(prev_expr, Dummy(), relation_type))

        return CasExpr(tuple((relation, meta) for relation in relations))

    def expression(self, tokens: list[Expr | Token]) -> Expr:
        # construct a sum between the given sympy expressions,
        # with the sign that separates them in the tokens list.

        signs = [self.SIGN_DICT[t.type] for t in tokens if isinstance(t, Token)]
        values = list(filter(lambda t: not isinstance(t, Token), tokens))

        # if no first sign was specified, it is implicitly '+'.
        if len(signs) < len(values):
            signs.insert(0, self.SIGN_DICT["ADD"])

        if len(signs) != len(values):
            raise RuntimeError(
                f"Error, too few signs were present in expression, expected {len(values) - 1} - {len(values)} got {len(signs)}"
            )

        result: Expr = (
            signs[0] * values[0] if signs[0] != S.One else cast(Expr, values[0])
        )

        # TODO: perhaps scalars should be autoconverted to 0d matrices here,
        # if it is attempted to sum a matrix and a scalar.
        for sign, value in zip(signs[1:], values[1:]):
            result += sign * value if sign != S.One else value

        return result

    def term(self, tokens: list[Expr | Token]) -> Expr:
        # multiply / divide a series of factor together.
        # tokens is a list of sympy expressions, representing factors,
        # separated by a multiplication / division token.

        result: Expr = cast(Expr, tokens[0])

        i = 1
        while i < len(tokens):
            operator: Token = cast(Token, tokens[i])

            i += 1

            sign: Integer = S.One

            if isinstance(tokens[i], Token):
                sign = self.SIGN_DICT[cast(Token, tokens[i]).type]
                i += 1

            factor: Expr = cast(Expr, tokens[i])
            i += 1

            if operator.type == "OPERATOR_CROSS" and MatrixUtils.is_matrix(result):
                result = cast(MatrixBase, result).cross(sign * factor)
            elif operator.type in ("OPERATOR_CROSS", "OPERATOR_MUL"):
                result *= sign * factor
            elif operator.type == "OPERATOR_DIV":
                result /= sign * factor
            else:
                raise RuntimeError(f"Unknown term operator '{operator.type}'")

        return result

    @v_args(inline=True)
    @implicit_mul_strategy(ImplicitMulStrategy.MULT)
    def implicit_multiplication(self, *factors: Expr) -> Expr:
        result = factors[0]

        for factor in factors[1:]:
            result *= factor

        return result

    @v_args(inline=True)
    @implicit_mul_strategy(ImplicitMulStrategy.RHS)
    def exponentiation(self, base: Expr, exponent: Expr) -> Expr:
        # special matrix notation.
        if isinstance(exponent, Symbol) and MatrixUtils.is_matrix(base):
            if str(exponent) == "T":
                return base.transpose()
            elif str(exponent) == "H":
                return base.adjoint()

        return pow(base, exponent)

    @v_args(inline=True)
    def matrix_body(self, *body: Expr | Token) -> list[list[Expr]]:
        return [
            list(cast(Iterator[Expr], row))
            for is_delim, row in itertools.groupby(
                body, lambda t: t == self.Delim.MatDelim
            )
            if not is_delim
        ]

    @v_args(inline=True)
    def matrix(self, matrix_begin_cmd, matrix_body, matrix_end_cmd) -> LatexMatrix:
        return LatexMatrix(
            matrix_body, env_begin=str(matrix_begin_cmd), env_end=str(matrix_end_cmd)
        )

    @v_args(inline=True)
    def array_matrix(
        self, matrix_begin_cmd, array_options, matrix_body, matrix_end_cmd
    ) -> LatexMatrix:
        return LatexMatrix(
            matrix_body,
            env_begin=f"{matrix_begin_cmd}{array_options}",
            env_end=str(matrix_end_cmd),
        )

    @v_args(inline=True)
    def det_matrix(self, begin, matrix_body, end) -> LatexMatrix:
        return self.matrix(begin, matrix_body, end).det()

    def matrix_like_delim(self, _: Iterator[Token]):
        return self.Delim.MatDelim

    SIGN_DICT = {"ADD": S.One, "SUB": S.NegativeOne}

    def _create_relation(self, left: Expr, right: Expr, relation_type: str) -> Rel:
        with evaluate(False):
            match relation_type:
                case "EQUAL":
                    return Eq(left, right, evaluate=False)
                case "NOT_EQUAL":
                    return Ne(left, right)
                case "LT":
                    return Lt(left, right)
                case "LTE":
                    return Le(left, right)
                case "GT":
                    return Gt(left, right)
                case "GTE":
                    return Ge(left, right)
                case _:
                    raise RuntimeError(
                        f"Unknown relation type '{relation_type}' between {left} and {right}"
                    )

    def list_of_expressions(self, tokens: Iterator[Expr]) -> list[Expr]:
        return list(
            filter(lambda x: not isinstance(x, Token) or x.type != "COMMA", tokens)
        )


def cas_expr_transformer(resolver: DefinitionResolver):
    return compose_transformers(
        UndefinedAtomsTransformer(resolver),
        ConstantsTransformer(),
        BuiltInFunctionsTransformer(resolver),
        CasExprTransformer(),
    )


cas_expr_transformer_runner: TransformerRunner[[DefinitionResolver], CasExpr] = (
    TransformerRunner(cas_expr_transformer)
)


__all__ = ["cas_expr_transformer_runner"]
