import time
from abc import ABC
from typing import override

from lmat_cas_client.command_handlers.CommandHandler import (
    CommandHandler,
    CommandResult,
)
from lmat_cas_client.command_handlers.EvalHandlerBase import EvaluateResult
from pydantic import BaseModel


class TestHangMessage(BaseModel):
    hang_time: float

class TestHangResult(CommandResult, ABC):
    @override
    def getResponsePayload(self):
        return CommandResult.result(dict())

class TestHangHandler(CommandHandler, ABC):
    """
    Command handler only to be used for test purposes.
    Hangs for TestHangMEssage.hang_time and completes immediatly after
    """

    def __init__(self):
        super().__init__()

    @override
    def handle(self, message: TestHangMessage) -> EvaluateResult:
        message = TestHangMessage.model_validate(message)
        time.sleep(message.hang_time * 1000)
