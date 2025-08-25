from typing import override

from sympy import *

from .EvalHandlerBase import EvalHandlerBase, EvaluateMessage


class ExpandHandler(EvalHandlerBase):
    @override
    def evaluate(self, sympy_expr: Expr, _message: EvaluateMessage) -> Expr:
        return expand(simplify(sympy_expr.doit()))
