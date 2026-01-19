from abc import ABC, abstractmethod
from typing import Any, ChainMap, override

from lark import LarkError

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
from lmat_cas_client.compiling.parsing.CasLogicExprParser import cas_logic_expr_parser
from lmat_cas_client.compiling.parsing.DefinitionsParser import (
    cas_expr_def_parser,
    cas_logic_expr_def_parser,
)
from lmat_cas_client.compiling.transforming.cas_expr.CasExprTransformer import (
    CasExpr,
    cas_expr_transformer_runner,
)
from lmat_cas_client.compiling.transforming.cas_logic_expr.PropositionsTransformer import (
    cas_logic_expr_transformer_runner,
)
from lmat_cas_client.compiling.transforming.DefinitionsTransformer import (
    definitions_transformer_runner,
)
from lmat_cas_client.compiling.transforming.DependenciesTransformer import (
    dependencies_transformer_runner,
)
from lmat_cas_client.LmatEnvironment import LmatEnvironment
from lmat_cas_client.math_lib.StandardDefinitionStore import StandardDefinitionStore


class Compiler[**PTransform, TRes](ABC):
    """
    Interface providing a compile function taking an input string as well as PTransform args,
    and produces TRes from the given args.
    """

    @abstractmethod
    def compile(
        self, input_str: str, *args: PTransform.args, **kwargs: PTransform.kwargs
    ) -> TRes:
        pass


CasExprCompiler = Compiler[[DefinitionStore], CasExpr]


class LatexToCasExprCompiler(CasExprCompiler):
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


class LatexToLogicCasExprCompiler(CasExprCompiler):
    """
    Same as LatexToCasExprCompiler, except input string is expected to
    conform to cas_logic_expr.lark.
    """

    @override
    def compile(self, latex_str: str, def_store: DefinitionStore) -> CasExpr:
        ast = cas_logic_expr_parser.parse(latex_str)

        dependencies = dependencies_transformer_runner.transform(ast)

        assert_acyclic_dependencies(def_store, dependencies)

        return cas_logic_expr_transformer_runner.transform(
            ast, DefinitionStoreResolver(def_store, cas_logic_expr_transformer_runner)
        )


DefStoreCompiler = Compiler[[], DefinitionStore]


class LatexToDefStoreCompiler(DefStoreCompiler):
    """
    Produces a DefinitionStore from a latex string, according to the cas_def.lark grammar.
    These definition stores can be chained to combine multiple such definitions into a singular definition store.
    """

    @override
    def compile(self, latex_str: str) -> Any:
        ast = cas_expr_def_parser.parse(latex_str)
        return definitions_transformer_runner.transform(
            ast, cas_expr_transformer_runner, dependencies_transformer_runner
        )


class LatexToLogicDefStoreCompiler(DefStoreCompiler):
    """
    Same as LatexToDefStoreCompiler but expects logic definitions (i.e. right hand side of symbol definitions are cas logic expressions)
    """

    @override
    def compile(self, latex_str: str) -> Any:
        ast = cas_logic_expr_def_parser.parse(latex_str)
        return definitions_transformer_runner.transform(
            ast, cas_logic_expr_transformer_runner, dependencies_transformer_runner
        )


def lmat_env_to_definition_store(
    env: LmatEnvironment, compiler: DefStoreCompiler
) -> DefinitionStore:
    """
    Constructs a definition store from the given LmatEnvironment
    and definition compiler, by going through all definition strings
    in the environment, compiling them, and chaining them into a singular
    definition store.
    """
    env = LmatEnvironment.model_validate(env)
    stores = [StandardDefinitionStore]

    for definition_str in env.definitionsv2:
        try:
            stores.append(compiler.compile(definition_str))
        except LarkError:
            # TODO: how can we distinguish between not-a-definition latex and definition with error latex?
            # right now we just assume that any latex which produces a parse error is not intended to be a definition.
            pass

    return ChainMap(*reversed(stores))
