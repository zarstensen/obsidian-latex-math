from lark import Transformer, v_args
from sympy import *


# This transformer is responsible for providing the values of various un-redefinable (cannot ':=' them) mathematical constants.
@v_args(inline=True)
class ConstantsTransformer(Transformer):
    def digit(self, digit_val: Expr) -> Expr:
        return digit_val

    def CONST_INFINITY(self, _) -> Expr:
        return oo
