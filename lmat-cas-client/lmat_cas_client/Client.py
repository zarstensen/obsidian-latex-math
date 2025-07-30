import asyncio
import ctypes
import traceback
from threading import Thread
from typing import *

import jsonpickle
import websockets

from .command_handlers.CommandHandler import CommandHandler


class ThreadKill(Exception):
    pass

class KillableThread(Thread):

    # ignore thread kill exceptions.
    def run(self):
        try:
            super().run()
        except ThreadKill:
            pass

    def kill(self):
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(self.ident), ctypes.py_object(ThreadKill))

class HandlerError(Exception):
    pass

#
# The LmatCasClient class manages a connection and message parsing + encoding between an active Latex Math plugin.
# The connection works based on 'handle keys', which act like message types.
# A handle key is simply a string indicating what sort of data is sent as the payload, and how it should be handled.
# The payload is always a json object decoded into a python object.
#
# Each handle key has a handler registered, which is called with the received payload.
#
class LmatCasClient:

    SUCCESS_STATUS = "success"
    ERR_STATUS = "error"
    INTERRUPT_STATUS = "interrupted"

    def __init__(self):
        self.command_handlers: dict[str, CommandHandler] = {}
        self.command_handler_threads: dict[str, Thread] = {}
        self.connection = None

    # Connect to a Latex Math plugin currently hosting on the local host at the given port.
    async def connect(self, port: int):
        self.connection = await websockets.connect(f"ws://localhost:{port}")

    # Register a message handler.
    def register_handler(self, handler_key: str, handler_factory: CommandHandler):
        self.command_handlers[handler_key] = handler_factory

    # Start the message loop, this is required to run, before any handlers will be called.
    async def run_message_loop(self):
        while True:
            message = jsonpickle.decode(await self.connection.recv())

            uid = message["uid"]
            message_type = message["type"]
            payload = message["payload"]

            match message_type:
                case "exit":
                    await self._send("exit", uid, {})
                    break
                case "start":
                    await self._start_handler(payload, uid)
                case "interrupt":
                    await self._interrupt_handler(payload["target_uid"], uid)
                case _:
                    # If we get here in a release build, then either the cas client or the plugin source is not the same version.
                    # A plugin reinstall should (hopefully) install a cas client and plugin source with the same version.
                    await self._send_error(
                        uid,
                        dev_message=f"Unsupported message type: {message.type}",
                        usr_message="Message type is not supported, please try reinstalling the plugin."
                    )

    async def _start_handler(self, payload: dict, uid: str):
        if payload["command_type"] not in self.command_handlers:
            await self._send_error(
                uid,
                dev_message=f"Unsupported command type: {payload["command_type"]}",
                usr_message="Command type is not supported, please try reinstalling the plugin."
            )
            return

        try:
            self.command_handler_threads[uid] = KillableThread(
                target=self._async_target,
                args=(
                    self._handle_command,
                    payload["command_type"],
                    uid,
                    payload["start_args"],
                ),
                daemon=True
            )
            self.command_handler_threads[uid].start()
        except Exception as e:
            await self._send_error(
                uid,
                dev_message=str(e) + "\n" + traceback.format_exc(),
                usr_message=str(e)
            )

    async def _handle_command(self, command: str, uid: str, payload: dict):
        command_response = self.command_handlers[command].handle(payload)
        response_type, response_value = command_response.getResponsePayload()
        await self._send_success(uid, response_type, response_value)

    async def _interrupt_handler(self, target_uid: str, uid: str):
        if target_uid in self.command_handler_threads:
            self.command_handler_threads[target_uid].kill()
            del self.command_handler_threads[target_uid]

        await self._send_interrupt(uid, {})

    def _async_target(self, coro, *args, **kwargs):
        return asyncio.run(coro(*args, **kwargs))

    # Send the given json dumpable object back to the plugin.
    async def _send(self, status: str, uid: str, message: dict):
        await self.connection.send(
            jsonpickle.encode(dict(status=status, uid=uid, payload=message))
        )

    async def _send_success(self, uid: str, type: str, value: dict):
        await self._send(self.SUCCESS_STATUS, uid, dict(type=type, value=value))

    async def _send_interrupt(self, uid):
        await self._send(self.INTERRUPT_STATUS, uid, { })

    async def _send_error(self, uid: str, dev_message: str, usr_message: str | None = None):
        usr_message = dev_message if usr_message is None else usr_message

        await self._send(self.ERR_STATUS, uid, dict(
            dev_message = dev_message,
            usr_message = usr_message
        ))
