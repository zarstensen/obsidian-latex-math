#
# The Compiler module defines a bunch of pre-initialized compilers used throughout the codebase.
#
from typing import override

from sympy import Expr

from lmat_cas_client.compiling.DefinitionStore import DefinitionStore
from lmat_cas_client.compiling.parsing.LatexParser import latex_parser
from lmat_cas_client.compiling.transforming.DependenciesTransformer import (
    DependenciesTransformer,
)
from lmat_cas_client.compiling.transforming.SympyTransformer import (
    SympyTransformer,
)

from .CompilerCore import Compiler

# A latex source code to sympy expression compiler which does NOT check for cyclic dependencies in the latex source string.
# this is intended for compiling after the dependencies have been checked in some other form.
latex_to_sympy_compiler_no_deps_assert = Compiler[Expr](latex_parser, SympyTransformer)
# A latex source code to dependency name's compiler.
# Takes a latex string and compiles it to a set of string, containing the names of all symbols and undefined functions this expression contains,
# and thus depends on.
latex_to_dependencies_compiler = Compiler[set[str]](latex_parser, DependenciesTransformer)

class LatexToSympyCompiler(Compiler[Expr]):
    def __init__(self):
        super().__init__(latex_parser, SympyTransformer)

    @override
    def compile(self, input_str: str, def_store: DefinitionStore):
        dependencies = latex_to_dependencies_compiler.compile(input_str, DefinitionStore())

        def_store.assert_acyclic_dependencies(dependencies)

        return super().compile(input_str, def_store)

# A latex source code to sympy expression compiler.
# Takes a latex string and compiles it to a sympy expression.
# Also checks for any cyclic dependencies in the latex input and passed definition store.
latex_to_sympy_compiler = LatexToSympyCompiler()
