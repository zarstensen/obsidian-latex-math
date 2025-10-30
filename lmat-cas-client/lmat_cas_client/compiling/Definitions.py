from typing import Iterable, override

from lark import Tree
from sympy import Expr, Function, Symbol
from sympy.core.function import AppliedUndef

from lmat_cas_client.compiling.transforming.TransformerRunner import TransformerRunner

from .DefinitionStore import (
    Definition,
    DefinitionStore,
    FunctionDefinition,
)


class SympyDefinition(Definition):
    """
    SympyDefinition simply holds a sympy expression as its defined value.
    """

    def __init__(self, sympy_expr):
        self._sympy_expr = sympy_expr

    @override
    def defined_value(self, _definition_store: DefinitionStore):
        # TODO: Currently does not use a definition store for anything as it is never needed,
        # but should probably be added in the future
        return self._sympy_expr

    @override
    def dependencies(self) -> set[str]:
        # return all free symbol names and applied undefined function names as dependencies.
        return set(
            map(
                lambda d: d.name,
                self._sympy_expr.free_symbols | self._sympy_expr.atoms(AppliedUndef),
            )
        )


class AssumptionDefinition(SympyDefinition):
    """
    Specialized SympyDefinition for sympy Symbols-
    """

    def __init__(self, symbol_assumption: Symbol):
        super().__init__(symbol_assumption)

    @override
    def dependencies(self) -> set[str]:
        # assumptions have no dependencies, butSympyDefinition would return the symbol itself as such,
        # so we need to explicitly return an empty set here.
        return set()


class AstDefinition(Definition):
    """
    Definition holding an abstract syntax tree (AST), which needs to be transformed in order to retreivieve its defined value.
    """

    def __init__(
        self,
        expr_transformer: TransformerRunner[[DefinitionStore], Expr],
        dependencies_transformer: TransformerRunner[[], set[str]],
        ast_definition: Tree,
    ):
        """
        Args:
            expr_transformer (TransformerRunner[[DefinitionStore], Expr]): transformer for producing the defined value
            dependencies_transformer (TransformerRunner[[], set[str]]): transformer for producing the dependencies of the AST
            ast_definition (Tree): AST to transform
        """
        self._ast_definition = ast_definition
        self._transformer = expr_transformer
        self._dependencies_transformer = dependencies_transformer

    @override
    def defined_value(self, definition_store: DefinitionStore):
        return self._transformer.transform(self._ast_definition, definition_store)

    @override
    def dependencies(self) -> set[str]:
        return self._dependencies_transformer.transform(self._ast_definition)


#
class AstFunctionDefinition(FunctionDefinition):
    """
    Like SerializedDefinition, but with FunctionDefinition as a base
    """

    def __init__(
        self,
        expr_transformer: TransformerRunner[[DefinitionStore], Expr],
        dependencies_transformer: TransformerRunner[[], set[str]],
        func_name: str,
        ast_body: Tree,
        variables: Iterable[str],
    ):
        super().__init__(variables)
        self._func_name = func_name
        self._ast_body = ast_body
        self._transformer = expr_transformer
        self._dependencies_transformer = dependencies_transformer

    @override
    def defined_value(self, _definition_store: DefinitionStore) -> Function:
        return Function(self._func_name)

    @override
    def applied_value(
        self,
        definition_store: DefinitionStore,
        args: Iterable[Definition] | None = None,
    ) -> Expr:
        if args is None:
            args = tuple()
        else:
            args = tuple(args)

            if len(args) != len(self.variables):
                raise ValueError(
                    f"Incorrect number of function args provided.\nExpected {len(self.variables)} ({', '.join(self.variables)}) got {len(self.args)}"
                )

        args_definitions = {}

        for variable_name, argument_definition in zip(self.variables, args):
            args_definitions[variable_name] = argument_definition

        return self._transformer.transform(
            self._ast_body, definition_store.override(args_definitions)
        )

    @override
    def dependencies(self) -> set[str]:
        return self._dependencies_transformer.transform(self._ast_body).difference(
            self._variables
        )
