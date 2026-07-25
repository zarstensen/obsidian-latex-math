from abc import ABC, abstractmethod
from typing import cast, override

from pydantic import BaseModel
from sympy import Expr, sympify
from sympy.core.relational import Relational
from sympy.physics.units.unitsystem import UnitSystem

import lmat_cas_client.math_lib.units.UnitUtils as UnitUtils
from lmat_cas_client.compiling.antlr.evaluation.AlgStmtTransformer import LocRange
from lmat_cas_client.compiling.Compiler import (
    lmat_env_to_scope,
)
from lmat_cas_client.LmatEnvironment import LmatEnvironment
from lmat_cas_client.LmatLatexPrinter import lmat_latex

from .CommandHandler import CommandResult, CompilingCommandHandler, MessageLike


class EvaluateMessage(BaseModel):
    expression: str
    environment: LmatEnvironment


class EvaluateResult(CommandResult, ABC):
    def __init__(
        self, sympy_expr: Expr, expr_separator: str, expr_loc: LocRange
    ):
        super().__init__()
        self.sympy_expr = sympy_expr
        self.expr_separator = expr_separator
        self.expr_loc = expr_loc

    @override
    def getResponsePayload(self) -> tuple[str, dict]:
        _, expr_end_pos = self.expr_loc
        metadata: dict[str, str | int] = dict(separator=self.expr_separator, end_pos = expr_end_pos)

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
    def handle(self, message: EvaluateMessage | MessageLike) -> EvaluateResult:
        message = EvaluateMessage.model_validate(message)

        scope = lmat_env_to_scope(
            message.environment, self._def_store_compiler
        )

        [*_, (sympy_expr, expr_loc)] = self._cas_expr_compiler.compile(
            message.expression, scope
        )

        # choose  right most evaluatable expression.
        # TODO: technically this can only happen once?
        while isinstance(sympy_expr, Relational):
            sympy_expr = sympy_expr.rhs

        # We must end up with an expr type after this loop.
        sympy_expr = cast(Expr, sympy_expr)

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

        return EvaluateResult(sympy_expr, separator, expr_loc)
