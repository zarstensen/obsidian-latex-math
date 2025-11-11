from abc import ABC, abstractmethod
from typing import override

from pydantic import BaseModel
from sympy import *
from sympy.core.relational import Relational
from sympy.physics.units.unitsystem import UnitSystem

import lmat_cas_client.math_lib.units.UnitUtils as UnitUtils
from lmat_cas_client.compiling.Compiler import Compiler
from lmat_cas_client.compiling.DefinitionStore import DefinitionStore
from lmat_cas_client.compiling.transforming.PropositionsTransformer import (
    PropositionExpr,
)
from lmat_cas_client.compiling.transforming.SystemOfExpr import SystemOfExpr
from lmat_cas_client.LmatEnvironment import LmatEnvironment
from lmat_cas_client.LmatLatexPrinter import lmat_latex

from .CommandHandler import CommandHandler, CommandResult


class EvaluateMessage(BaseModel):
    expression: str
    environment: LmatEnvironment


class EvaluateResult(CommandResult, ABC):
    def __init__(
        self, sympy_expr: Expr, expr_separator: str, expr_lines: list[int] | None
    ):
        super().__init__()
        self.sympy_expr = sympy_expr
        self.expr_separator = expr_separator
        self.expr_lines = expr_lines

    @override
    def getResponsePayload(self):
        metadata = dict(separator=self.expr_separator)

        if self.expr_lines is not None and self.expr_lines[0] != self.expr_lines[1]:
            metadata = dict(
                **metadata, start_line=self.expr_lines[0], end_line=self.expr_lines[1]
            )

        return CommandResult.result(
            dict(evaluated_expression=lmat_latex(self.sympy_expr), metadata=metadata)
        )


class EvalHandlerBase(CommandHandler, ABC):
    def __init__(self, compiler: Compiler[[DefinitionStore], Expr]):
        super().__init__()
        self._compiler = compiler

    @abstractmethod
    def evaluate(self, sympy_expr: Expr, message: EvaluateMessage) -> Expr:
        pass

    @override
    def handle(self, message: EvaluateMessage) -> EvaluateResult:
        message = EvaluateMessage.model_validate(message)

        definitions_store = LmatEnvironment.create_definition_store(message.environment)
        sympy_expr = self._compiler.compile(message.expression, definitions_store)
        expr_lines = None

        # choose bottom / right most evaluatable expression.
        while isinstance(sympy_expr, SystemOfExpr) or isinstance(
            sympy_expr, Relational
        ):
            # for system of expressions, take the last one
            if isinstance(sympy_expr, SystemOfExpr):
                expr_lines = (
                    sympy_expr.get_location(-1).line,
                    sympy_expr.get_location(-1).end_line,
                )

                if expr_lines[1] is None:
                    expr_lines = (expr_lines[0], len(message.expression.splitlines()))

                sympy_expr = sympy_expr.get_expr(-1)

            # for equalities, take the right hand side.
            if isinstance(sympy_expr, Relational):
                sympy_expr = sympy_expr.rhs

        if isinstance(sympy_expr, PropositionExpr):
            separator = r"\equiv"
        else:
            separator = "="

        sympy_expr = self.evaluate(sympify(sympy_expr), message)

        unit_system = message.environment.unit_system

        if unit_system is not None:
            sympy_expr = UnitUtils.auto_convert(
                sympy_expr, UnitSystem.get_unit_system(unit_system)
            )
        else:
            sympy_expr = UnitUtils.auto_convert(sympy_expr)

        return EvaluateResult(sympy_expr, separator, expr_lines)
