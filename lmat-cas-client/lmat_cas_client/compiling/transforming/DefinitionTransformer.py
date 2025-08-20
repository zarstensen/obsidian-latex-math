
from lark import Token, v_args
from sympy import Symbol
from sympy.core.function import AppliedUndef

from lmat_cas_client.compiling.transforming.SympyTransformer import SympyTransformer


class DefinitionTransformer(SympyTransformer):
    @v_args(inline=True)
    def latex_math_definition_string(self, lhs: Symbol | AppliedUndef, rhs: Token):
        return lhs, rhs.value
