from abc import ABC, abstractmethod
from typing import Any, override

from lmat_cas_client.compiling.definition.DefinitionStore import (
    DefinitionStore,
    assert_acyclic_dependencies,
)
from lmat_cas_client.compiling.definition.DefinitionStoreResolver import (
    DefinitionStoreResolver,
)
from lmat_cas_client.compiling.parsing.CasExprParser import (
    cas_expr_parser,
)
from lmat_cas_client.compiling.parsing.DefinitionsParser import cas_expr_def_parser
from lmat_cas_client.compiling.transforming.cas_expr.CasExprTransformer import (
    CasExpr,
    CasExprTransformer,
    cas_expr_transformer_runner,
)
from lmat_cas_client.compiling.transforming.DefinitionsTransformer import (
    definitions_transformer_runner,
)
from lmat_cas_client.compiling.transforming.DependenciesTransformer import (
    DependenciesTransformer,
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

        assert_acyclic_dependencies(def_store, dependencies)

        return cas_expr_transformer_runner.transform(
            ast, DefinitionStoreResolver(def_store, cas_expr_transformer_runner)
        )


class LatexToDefinitionCompiler(Compiler[[], Any]):
    def __init__(
        self,
        expr_transformer: CasExprTransformer,
        deps_transformer: DependenciesTransformer,
    ):
        super().__init__()
        self._expr_transformer = expr_transformer
        self._deps_transformer = deps_transformer

    @override
    def compile(self, latex_str: str) -> Any:
        ast = cas_expr_def_parser.parse(latex_str)
        return definitions_transformer_runner.transform(
            ast, self._expr_transformer, self._deps_transformer
        )
