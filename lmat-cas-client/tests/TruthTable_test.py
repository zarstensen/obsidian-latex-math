from lmat_cas_client.command_handlers.TruthTableHandler import TruthTableHandler
from lmat_cas_client.compiling.Compiler import LatexToSympyCompiler
from sympy import *


class TestTruthTable:
    handler = TruthTableHandler(LatexToSympyCompiler())

    def test_truth_table(self):
        p, q, r = symbols('P Q R')

        result = self.handler.handle({ 'expression': r"P \wedge Q",
                             'environment': {},
                             'truth_table_format': "md"
                             })

        assert result.columns == [p, q]
        assert result.truth_table == [
            [True,  True,  True],
            [True,  False, False],
            [False, True,  False],
            [False, False, False],
        ]
