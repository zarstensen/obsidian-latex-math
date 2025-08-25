from lmat_cas_client.command_handlers.ConvertSympyHandler import *
from lmat_cas_client.compiling.Compiler import LatexToSympyCompiler
from sympy import *


## Tests the conver to sympy mode.
class TestConvertSympy:
    compiler = LatexToSympyCompiler()

    def test_convert_simple(self):
        a, b = symbols("a b")

        handler = ConvertSympyHandler(self.compiler)

        result = handler.handle({"expression": "a + b", "environment": {}})

        assert result.sympy_expr == a + b
