from typing import TypedDict, override

from sympy import *

from lmat_cas_client.grammar.LmatEnvDefStore import LmatEnvDefStore
from lmat_cas_client.grammar.SympyParser import SympyParser
from lmat_cas_client.LmatEnvironment import LmatEnvironment

from .CommandHandler import CommandHandler, CommandResult


class ConvertSympyModeMessage(TypedDict):
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
    def __init__(self, parser: SympyParser):
        super().__init__()
        self._parser = parser

    @override
    def handle(self, message: ConvertSympyModeMessage):
        return ConvertSympyResult(
            self._parser.parse(message['expression'], LmatEnvDefStore(self._parser, message['environment']))
        )
