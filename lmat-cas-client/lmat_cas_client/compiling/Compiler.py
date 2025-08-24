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

    @abstractmethod
    def compile(self, input_str: str, *args: PTransform.args, **kwargs: PTransform.kwargs) -> TRes:
        pass

class LatexToSympyCompiler(Compiler[[DefinitionStore], Expr]):

    @override
    def compile(self, latex_str: str, def_store: DefinitionStore) -> Expr:
        ast = latex_parser.parse(latex_str)

        dependencies = dependencies_transformer_runner.transform(ast)

        def_store.assert_acyclic_dependencies(dependencies)

        return sympy_transformer_runner.transform(ast, def_store)
