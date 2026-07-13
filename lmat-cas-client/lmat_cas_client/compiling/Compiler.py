from lmat_cas_client.compiling.antlr.parser.ErrorListener import ParseError
from abc import ABC, abstractmethod
from typing import Any, override

from lmat_cas_client.compiling.antlr.evaluation.CasExprTransformer import (
    CasExprV2,
    alg_stmt_2_cas_expr,
)
from lmat_cas_client.compiling.antlr.evaluation.DefExprTransformer import (
    binding_stmts_2_bindings,
)
from lmat_cas_client.compiling.antlr.evaluation.Scope import OptBinding, Scope
from lmat_cas_client.compiling.antlr.parser.AlgExprGrammar import AlgExprGrammar
from lmat_cas_client.compiling.antlr.parser.AlgExprLexer import AlgExprLexer
from lmat_cas_client.compiling.antlr.parser.DefExprGrammar import DefExprGrammar
from lmat_cas_client.compiling.antlr.parser.DefExprLexer import DefExprLexer
from lmat_cas_client.compiling.antlr.parser.ErrorListener import ParseErrorListener
from lmat_cas_client.LmatEnvironment import LmatEnvironment


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


CasExprCompiler = Compiler[[Scope], CasExprV2]


class CompileError(Exception):
    pass


class LatexToCasExprCompiler(CasExprCompiler):
    """
    Combines a latex parser and a sympy transformer to provide a latex to sympy compiler.
    Symbol assumptions + definitions and function definitions may be supplied in a DefinitionStore passed as an argument to the compile() function.
    """

    @override
    def compile(self, latex_str: str, scope: Scope) -> CasExprV2:
        """
        Compile the given latex string to a sympy expression.
        Args:
            latex_str (str): input latex math string
            scope (DefinitionStore): DefinitionStore to take substitution values from.

        Returns:
            Expr: compiled sympy expression.
        """

        err_listener = ParseErrorListener()

        stream = AlgExprLexer.stream_from_src(latex_str)
        stream.tokenSource.removeErrorListeners()
        stream.tokenSource.addErrorListener(err_listener)

        parser = AlgExprGrammar(stream)

        parser.removeErrorListeners()
        parser.addErrorListener(err_listener)

        ast = parser.alg_statement().res

        if err_listener.has_errors():
            raise err_listener.build_parse_error(latex_str)

        return alg_stmt_2_cas_expr(ast, scope)


class LatexToLogicCasExprCompiler(CasExprCompiler):
    """
    Same as LatexToCasExprCompiler, except input string is expected to
    conform to cas_logic_expr.lark.
    """

    @override
    def compile(self, latex_str: str, scope: Scope) -> CasExprV2:
        return ()
        # ast = cas_logic_expr_parser.parse(latex_str)
        #
        # dependencies = dependencies_transformer_runner.transform(ast)
        #
        # assert_acyclic_dependencies(scope, dependencies)
        #
        # return cas_logic_expr_transformer_runner.transform(
        #     ast, DefinitionStoreResolver(scope, cas_logic_expr_transformer_runner)
        # )


BindingsCompiler = Compiler[[], tuple[OptBinding, ...]]


class LatexToDefStoreCompiler(BindingsCompiler):
    """
    Produces a DefinitionStore from a latex string, according to the cas_def.lark grammar.
    These definition stores can be chained to combine multiple such definitions into a singular definition store.
    """

    @override
    def compile(self, latex_str: str) -> tuple[OptBinding, ...]:
        # TODO: error handling
        err_listener = ParseErrorListener()

        stream = DefExprLexer.stream_from_src(latex_str)
        stream.tokenSource.removeErrorListeners()
        stream.tokenSource.addErrorListener(err_listener)

        parser = DefExprGrammar(stream)

        parser.removeErrorListeners()
        parser.addErrorListener(err_listener)

        ast = parser.bindings().res

        if err_listener.has_errors():
            raise err_listener.build_parse_error(latex_str)

        return binding_stmts_2_bindings(ast)


class LatexToLogicDefStoreCompiler(BindingsCompiler):
    """
    Same as LatexToDefStoreCompiler but expects logic definitions (i.e. right hand side of symbol definitions are cas logic expressions)
    """

    @override
    def compile(self, latex_str: str) -> Any:
        return ()
        # ast = cas_logic_expr_def_parser.parse(latex_str)
        # return definitions_transformer_runner.transform(
        #     ast, cas_logic_expr_transformer_runner, dependencies_transformer_runner
        # )


def lmat_env_to_scope(env: LmatEnvironment, compiler: BindingsCompiler) -> Scope:
    """
    Constructs a definition store from the given LmatEnvironment
    and definition compiler, by going through all definition strings
    in the environment, compiling them, and chaining them into a singular
    definition store.
    """
    env = LmatEnvironment.model_validate(env)

    # TODO: standard bindings here
    bindings: list[OptBinding] = []

    for i, definition_str in enumerate(env.definitionsv2):
        try:
            bindings.extend(compiler.compile(definition_str))
        except ParseError as e:
            raise RuntimeError(f"Error whilst parsing definition {i}:\n{e}") from e

    scope = Scope()
    scope.register(bindings)

    return scope
