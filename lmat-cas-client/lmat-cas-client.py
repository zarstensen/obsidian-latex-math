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
from lmat_cas_client.command_handlers.TruthTableHandler import TruthTableHandler
from lmat_cas_client.grammar.LatexParser import LatexParser

if len(sys.argv) < 2:
    print("Usage:"
            f"\npython {os.path.basename(__file__)} [port]"
            "\n\tport - port number on local host the plugin server is listening at.")
    sys.exit(1)

port = int(sys.argv[1])

latex_parser = LatexParser()

client = LmatCasClient()

client.register_handler("eval", EvalHandler(latex_parser))
client.register_handler("evalf", EvalfHandler(latex_parser))
client.register_handler("expand", ExpandHandler(latex_parser))
client.register_handler("factor", FactorHandler(latex_parser))
client.register_handler("apart", ApartHandler(latex_parser))
client.register_handler("solve", SolveHandler(latex_parser))
client.register_handler("solve-info", SolveInfoHandler(latex_parser))
client.register_handler("symbolsets", SymbolSetHandler(latex_parser))
client.register_handler("convert-sympy", ConvertSympyHandler(latex_parser))
client.register_handler("convert-units", ConvertUnitsHandler(latex_parser))
client.register_handler("truth-table", TruthTableHandler(latex_parser))

async def main():
    await client.connect(port)
    await client.run_message_loop()

# set this policy so async functions work in threads on windows.
# otherwise exceptions randomly occur when async loops terminate.
if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.run(main())
