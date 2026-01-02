from typing import Iterable, override
from lark import Tree
from sympy import Basic, Expr, Function
from .DefinitionStore import Definition, DefinitionStore, FunctionDefinition
from lmat_cas_client.compiling.transforming.TransformerRunner import TransformerRunner
from lmat_cas_client.compiling.transforming.cas_expr.CasExprTransformer import CasExpr


type AstExprTransformer = TransformerRunner[[DefinitionStore], CasExpr]
type AstDepsTransformer = TransformerRunner[[], set[str]]


class AstDefinition(Definition):
    """
    Definition holding an abstract syntax tree (AST), which needs to be transformed in order to retreivieve its defined value.
    """

    def __init__(
        self,
        expr_transformer: AstExprTransformer,
        dependencies_transformer: AstDepsTransformer,
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
    def defined_value(self, definition_store: DefinitionStore) -> Basic:
        return self._transformer.transform(
            self._ast_definition, definition_store
        ).get_expr(-1)

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
        expr_transformer: AstExprTransformer,
        dependencies_transformer: AstDepsTransformer,
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
    ) -> Basic:
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
        ).get_expr(-1)

    @override
    def dependencies(self) -> set[str]:
        return self._dependencies_transformer.transform(self._ast_body).difference(
            self._variables
        )
