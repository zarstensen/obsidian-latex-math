from typing import override

from sympy import *

from .EvalHandlerBase import EvalHandlerBase, EvaluateMessage


class EvalHandler(EvalHandlerBase):
    @override
    def evaluate(self, sympy_expr: Expr, _message: EvaluateMessage) -> Expr:
        return simplify(sympy_expr.doit())
