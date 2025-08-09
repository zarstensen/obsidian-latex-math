from typing import override

from sympy import *

from .EvalHandlerBase import EvalHandlerBase, EvaluateMessage


class FactorHandler(EvalHandlerBase):
    @override
    def evaluate(self, sympy_expr: Expr, _message: EvaluateMessage) -> Expr:
        return factor(simplify(sympy_expr.doit()))
