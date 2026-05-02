# mypy: disable-error-code="attr-defined"
from typing import Any

import pytest
from lmat_cas_client.compiling.Compiler import (
    LatexToCasExprCompiler,
    LatexToDefStoreCompiler,
    LatexToLogicCasExprCompiler,
    LatexToLogicDefStoreCompiler,
    lmat_env_to_definition_store,
)
from lmat_cas_client.compiling.definition.DefinitionStore import CyclicDependencyError
from lmat_cas_client.compiling.parsing import PrettyParserError
from lmat_cas_client.compiling.transforming.cas_expr.CasExprTransformer import CasExpr
from lmat_cas_client.compiling.transforming.LatexMatrix import LatexMatrix
from lmat_cas_client.LmatEnvironment import LmatEnvironment
from sympy import *
from sympy import Expr
from sympy.logic.boolalg import *

class TestAntlr:

	def test_test(self):
		comp = LatexToCasExprCompiler()
		ce = comp.compile("1 + 1^2 - \\frac12", {})
		pass
