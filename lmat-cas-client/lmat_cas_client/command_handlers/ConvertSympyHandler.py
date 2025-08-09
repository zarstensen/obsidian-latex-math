from typing import override

from pydantic import BaseModel
from sympy import *

from lmat_cas_client.compiling.CompilerCore import Compiler
from lmat_cas_client.LmatEnvironment import LmatEnvironment

from .CommandHandler import CommandHandler, CommandResult


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

class ConvertSympyHandler(CommandHandler):
    def __init__(self, compiler: Compiler):
        super().__init__()
        self._compiler = compiler

    @override
    def handle(self, message: ConvertSympyModeMessage):
        message = ConvertSympyModeMessage.model_validate(message)

        return ConvertSympyResult(
            self._compiler.compile(message.expression, LmatEnvironment.create_definition_store(message.environment))
        )
