from abc import ABC, abstractmethod
from typing import override

from pydantic import BaseModel
from sympy import *
from sympy.core.relational import Relational
from sympy.physics.units.unitsystem import UnitSystem

import lmat_cas_client.math_lib.units.UnitUtils as UnitUtils
from lmat_cas_client.compiling.Compiler import (
    lmat_env_to_definition_store,
)
from lmat_cas_client.LmatEnvironment import LmatEnvironment
from lmat_cas_client.LmatLatexPrinter import lmat_latex

from .CommandHandler import CommandResult, CompilingCommandHandler


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


class EvalHandlerBase(CompilingCommandHandler, ABC):
    """
    Base class command handler for all the evaluate suite command handlers.
    All implementing classes need to implement an evaluate method,
    this base class takes rest of all of the remaining logic.
    """

    @abstractmethod
    def evaluate(self, sympy_expr: Expr, message: EvaluateMessage) -> Expr:
        pass

    @override
    def handle(self, message: EvaluateMessage) -> EvaluateResult:
        message = EvaluateMessage.model_validate(message)

        definitions_store = lmat_env_to_definition_store(
            message.environment, self._def_store_compiler
        )

        [*_, (sympy_expr, expr_meta)] = self._cas_expr_compiler.compile(
            message.expression, definitions_store
        ).expressions

        expr_lines = (
            expr_meta.line,
            expr_meta.end_line,
        )

        if expr_lines[1] is None:
            expr_lines = (expr_lines[0], len(message.expression.splitlines()))

        # choose  right most evaluatable expression.
        while isinstance(sympy_expr, Relational):
            sympy_expr = sympy_expr.rhs

        # TODO: the separator stuff should no longer be a thing?
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
