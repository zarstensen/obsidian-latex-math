from abc import ABC, abstractmethod
from ast import Expr
from typing import override

from lmat_cas_client.compiling.DefinitionStore import DefinitionStore
from lmat_cas_client.compiling.parsing.LatexParser import (
    latex_parser,
)
from lmat_cas_client.compiling.transforming.DependenciesTransformer import (
    dependencies_transformer_runner,
)
from lmat_cas_client.compiling.transforming.SympyTransformer import (
    sympy_transformer_runner,
)


class Compiler[**PTransform, TRes](ABC):
    """
    Interface providing a compile function taking an input string as wella s PTransform args,
    and produces TRes from the given args.
    """
    @abstractmethod
    def compile(self, input_str: str, *args: PTransform.args, **kwargs: PTransform.kwargs) -> TRes:
        pass

class LatexToSympyCompiler(Compiler[[DefinitionStore], Expr]):
    """
    Combines a latex parser and a sympy transformer to provide a latex to sympy compiler.
    Symbol assumptions + definitions and function definitions may be supplied in a DefinitionStore passed as an argument to the compile() function.
    """

    @override
    def compile(self, latex_str: str, def_store: DefinitionStore) -> Expr:
        """
        Compile the given latex string to a sympy expression.
        Args:
            latex_str (str): input latex math string
            def_store (DefinitionStore): DefinitionStore to take substitution values from.

        Returns:
            Expr: compiled sympy expression.
        """
        ast = latex_parser.parse(latex_str)

        dependencies = dependencies_transformer_runner.transform(ast)

        def_store.assert_acyclic_dependencies(dependencies)

        return sympy_transformer_runner.transform(ast, def_store)
