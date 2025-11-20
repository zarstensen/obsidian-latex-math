from abc import ABC, abstractmethod
from typing import Any, override

from lmat_cas_client.compiling.DefinitionStore import DefinitionStore
from lmat_cas_client.compiling.parsing.CasExprParser import (
    cas_expr_parser,
)
from lmat_cas_client.compiling.parsing.DefinitionsParser import definition_parser
from lmat_cas_client.compiling.transforming.CasExprTransformer import (
    CasExpr,
    cas_expr_tansformer_runner,
)
from lmat_cas_client.compiling.transforming.DefinitionsTransformer import (
    definitions_transformer_runner,
)
from lmat_cas_client.compiling.transforming.DependenciesTransformer import (
    dependencies_transformer_runner,
)


class Compiler[**PTransform, TRes](ABC):
    """
    Interface providing a compile function taking an input string as wella s PTransform args,
    and produces TRes from the given args.
    """

    @abstractmethod
    def compile(
        self, input_str: str, *args: PTransform.args, **kwargs: PTransform.kwargs
    ) -> TRes:
        pass


class LatexToCasExprCompiler(Compiler[[DefinitionStore], CasExpr]):
    """
    Combines a latex parser and a sympy transformer to provide a latex to sympy compiler.
    Symbol assumptions + definitions and function definitions may be supplied in a DefinitionStore passed as an argument to the compile() function.
    """

    @override
    def compile(self, latex_str: str, def_store: DefinitionStore) -> CasExpr:
        """
        Compile the given latex string to a sympy expression.
        Args:
            latex_str (str): input latex math string
            def_store (DefinitionStore): DefinitionStore to take substitution values from.

        Returns:
            Expr: compiled sympy expression.
        """
        ast = cas_expr_parser.parse(latex_str)

        dependencies = dependencies_transformer_runner.transform(ast)

        def_store.assert_acyclic_dependencies(dependencies)

        return cas_expr_tansformer_runner.transform(ast, def_store)


class LatexToDefinitionCompiler(Compiler[[], Any]):
    @override
    def compile(self, latex_str: str) -> Any:
        ast = definition_parser.parse(latex_str)
        return definitions_transformer_runner.transform(ast)
