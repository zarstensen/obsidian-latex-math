from lmat_cas_client.command_handlers.ConvertSympyHandler import *
from lmat_cas_client.compiling.Compiler import (
    LatexToCasExprCompiler,
    LatexToDefStoreCompiler,
)
from sympy import *


## Tests the conver to sympy mode.
class TestConvertSympy:
    expr_compiler = LatexToCasExprCompiler()
    store_compiler = LatexToDefStoreCompiler()

    def test_convert_simple(self):
        a, b = symbols("a b")

        handler = ConvertSympyHandler(self.expr_compiler, self.store_compiler)

        result = handler.handle({"expression": "a + b", "environment": {}})

        assert result.sympy_expr == a + b
