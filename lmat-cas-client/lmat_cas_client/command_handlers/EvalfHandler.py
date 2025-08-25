from typing import override

from sympy import *

from .EvalHandlerBase import EvalHandlerBase, EvaluateMessage


class EvalfHandler(EvalHandlerBase):
    @override
    def evaluate(self, sympy_expr: Expr, _message: EvaluateMessage) -> Expr:
        return sympy_expr.evalf()
