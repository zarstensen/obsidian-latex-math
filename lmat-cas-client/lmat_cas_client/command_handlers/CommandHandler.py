from abc import ABC, abstractmethod
from typing import Any, override


# The CommandResult represents an arbitrary result returned by a CommandHandler.
# It contains the result data and a method for converting this data into a message payload.
class CommandResult(ABC):

    @abstractmethod
    def getPayload(self) -> tuple[str, dict]:
        pass

    # helper method for producing a common result payload.
    @staticmethod
    def result(value) -> tuple[str, dict]:
        return ("result", value)

# THis should not be a thing?
class ErrorResult(CommandResult):

    def __init__(self, dev_msg: str, usr_msg: str | None = None):
        super().__init__()
        self.dev_msg = dev_msg
        self.usr_msg = usr_msg if usr_msg is not None else dev_msg

    @override
    def getPayload(self) -> tuple[str, dict]:
        return "error", { dict(usr_message=self.usr_msg, dev_message=self.dev_msg) }

# CommandHandler should be inherited by objects wanting to implement a handler.
# The handle method returns a CommandResult for the implemented command.
class CommandHandler(ABC):
    @abstractmethod
    def handle(self, message: Any) -> CommandResult:
        pass
