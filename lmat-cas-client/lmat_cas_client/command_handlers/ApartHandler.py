from typing import override

from sympy import *

from .EvalHandlerBase import EvalHandlerBase, EvaluateMessage


class ApartHandler(EvalHandlerBase):
    @override
    def evaluate(self, sympy_expr: Expr, _message: EvaluateMessage) -> Expr:
        return apart(simplify(sympy_expr.doit()))
