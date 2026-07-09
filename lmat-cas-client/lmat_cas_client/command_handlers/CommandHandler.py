from abc import ABC, abstractmethod
from typing import Any, Mapping

from lmat_cas_client.compiling.Compiler import CasExprCompiler, BindingsCompiler


class CommandResult(ABC):
    """
    The CommandResult represents an arbitrary result returned by a CommandHandler.
    It contains the result data and a method for converting this data into a message payload.    Args:
    """

    # return response payload type as 1'st element, and serializable response dict payload as 2'nd element.
    @abstractmethod
    def getResponsePayload(self) -> tuple[str, dict]:
        pass

    # helper method for producing a common result payload.
    @staticmethod
    def result(value: dict) -> tuple[str, dict]:
        return ("result", value)


MessageLike = Mapping[str, Any]


class CommandHandler(ABC):
    """
    CommandHandler should be inherited by objects wanting to implement a handler.
    The handle method returns a CommandResult for the implemented command.
    """

    @abstractmethod
    def handle(self, message: Any | MessageLike) -> CommandResult:
        pass


class CompilingCommandHandler(CommandHandler, ABC):
    """
    Base class for all command handlers which require compiling some form of string (latex) input.
    This is mainly a utility class for reducing repeat constructors.
    """

    def __init__(
        self, cas_expr_compiler: CasExprCompiler, def_store_compiler: BindingsCompiler
    ):
        super().__init__()
        self._cas_expr_compiler = cas_expr_compiler
        self._def_store_compiler = def_store_compiler
