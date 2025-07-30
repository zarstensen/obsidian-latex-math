from abc import ABC, abstractmethod
from typing import Any


# The CommandResult represents an arbitrary result returned by a CommandHandler.
# It contains the result data and a method for converting this data into a message payload.
class CommandResult(ABC):

    # return response payload type as 1'st element, and serializable response dict payload as 2'nd element.
    @abstractmethod
    def getResponsePayload(self) -> tuple[str, dict]:
        pass

    # helper method for producing a common result payload.
    @staticmethod
    def result(value: dict) -> tuple[str, dict]:
        return ("result", value)

# CommandHandler should be inherited by objects wanting to implement a handler.
# The handle method returns a CommandResult for the implemented command.
class CommandHandler(ABC):
    @abstractmethod
    def handle(self, message: Any) -> CommandResult:
        pass
