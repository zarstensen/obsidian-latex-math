from typing import override

from pydantic import BaseModel
from sympy import *

from lmat_cas_client.compiling.Compiler import (
    lmat_env_to_definition_store,
)
from lmat_cas_client.LmatEnvironment import LmatEnvironment

from .CommandHandler import CommandResult, CompilingCommandHandler


class ConvertSympyModeMessage(BaseModel):
    expression: str
    environment: LmatEnvironment


class ConvertSympyResult(CommandResult):
    def __init__(self, sympy_expr):
        super().__init__()
        self.sympy_expr = sympy_expr

    @override
    def getResponsePayload(self) -> dict:
        return CommandResult.result(dict(code=str(sympify(self.sympy_expr))))


class ConvertSympyHandler(CompilingCommandHandler):
    @override
    def handle(self, message: ConvertSympyModeMessage):
        message = ConvertSympyModeMessage.model_validate(message)
        # TODO: how should multiple expressions be handled?
        return ConvertSympyResult(
            self._cas_expr_compiler.compile(
                message.expression,
                lmat_env_to_definition_store(
                    message.environment, self._def_store_compiler
                ),
            ).get_expr(-1)
        )
