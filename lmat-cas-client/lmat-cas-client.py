import asyncio
import os
import sys

from lmat_cas_client.Client import LmatCasClient
from lmat_cas_client.command_handlers.ApartHandler import ApartHandler
from lmat_cas_client.command_handlers.ConvertSympyHandler import ConvertSympyHandler
from lmat_cas_client.command_handlers.ConvertUnitsHandler import ConvertUnitsHandler
from lmat_cas_client.command_handlers.EvalfHandler import EvalfHandler
from lmat_cas_client.command_handlers.EvalHandler import EvalHandler
from lmat_cas_client.command_handlers.ExpandHandler import ExpandHandler
from lmat_cas_client.command_handlers.FactorHandler import FactorHandler
from lmat_cas_client.command_handlers.SolveHandler import SolveHandler, SolveInfoHandler
from lmat_cas_client.command_handlers.SymbolSetHandler import SymbolSetHandler
from lmat_cas_client.command_handlers.test_handlers.TestHangHandler import (
    TestHangHandler,
)
from lmat_cas_client.command_handlers.TruthTableHandler import TruthTableHandler
from lmat_cas_client.compiling.Compiler import LatexToSympyCompiler

if len(sys.argv) != 2:
    print("Usage:"
            f"\npython {os.path.basename(__file__)} [port]"
            "\n\tport - port number on local host the plugin server is listening at."
            )
    sys.exit(1)

port = int(sys.argv[1])


client = LmatCasClient()

client.register_handler("eval", EvalHandler(LatexToSympyCompiler()))
client.register_handler("evalf", EvalfHandler(LatexToSympyCompiler()))
client.register_handler("expand", ExpandHandler(LatexToSympyCompiler()))
client.register_handler("factor", FactorHandler(LatexToSympyCompiler()))
client.register_handler("apart", ApartHandler(LatexToSympyCompiler()))
client.register_handler("solve", SolveHandler(LatexToSympyCompiler()))
client.register_handler("solve-info", SolveInfoHandler(LatexToSympyCompiler()))
client.register_handler("symbolsets", SymbolSetHandler(LatexToSympyCompiler()))
client.register_handler("convert-sympy", ConvertSympyHandler(LatexToSympyCompiler()))
client.register_handler("convert-units", ConvertUnitsHandler(LatexToSympyCompiler()))
client.register_handler("truth-table", TruthTableHandler(LatexToSympyCompiler()))

# test specific handlers

client.register_handler("test-hang", TestHangHandler())

async def main():
    await client.connect(port)
    await client.run_message_loop()

# set this policy so async functions work in threads on windows.
# otherwise exceptions randomly occur when async loops terminate.
if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.run(main())
