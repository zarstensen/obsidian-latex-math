from typing import Any

from lark import Token, Transformer, Tree, Visitor, v_args
from regex import Regex
from sympy import Basic

from lmat_cas_client.compiling.definitions.DefinitionStore import DefinitionStore
from lmat_cas_client.compiling.Definitions import AstDefinition
from lmat_cas_client.compiling.transforming.DependenciesTransformer import (
    dependencies_transformer_runner,
)
from lmat_cas_client.compiling.transforming.TransformerRunner import TransformerRunner
from lmat_cas_client.compiling.transforming.cas_expr.CasExprTransformer import (
    CasExpr,
    cas_expr_transformer_runner,
)


class AstNamespaceRemover(Visitor):
    def __init__(self, namespace: str):
        self._rem_regex = Regex(rf"^(_)?{namespace}(.*)$")

    def __default__(self, node: Tree):
        node.data = self._rem_regex.sub(r"\1\2", node.data)

        new_children = []

        for child in node.children:
            match child:
                case Tree():
                    new_children.append(child)
                case Token():
                    new_children.append(
                        child.update(self._rem_regex.sub(r"\1\2", child.type))
                    )

        node.children = new_children
        return node


@v_args(inline=True)
class DefinitionsTransformer(Transformer):

    def __init__(
        self,
        expr_transformer: TransformerRunner[[DefinitionStore], CasExpr],
        dependencies_transformer: TransformerRunner[[], set[str]],
    ):
        self._expr_transformer = expr_transformer
        self._dependencies_transformer = dependencies_transformer
        pass
        # super().__init__(visit_tokens)

    def value_def_expr(self, def_ast: Tree, value_ast: Tree):
        def_ast = AstNamespaceRemover("cas_expr__").visit(def_ast)
        value_ast = AstNamespaceRemover("cas_expr__").visit(value_ast)

        def_val = cas_expr_transformer_runner.transform(
            def_ast, DefinitionStore.empty()
        )

        if len(def_val) != 1 or not hasattr(def_val.get_expr(-1), "name"):
            return ValueError("AAAAAA PANIC AAAAAAAAA")

        return def_val.get_expr(-1).name, AstDefinition(
            cas_expr_transformer_runner, dependencies_transformer_runner, value_ast
        )


definitions_transformer_runner = TransformerRunner[
    [TransformerRunner[[DefinitionStore], CasExpr], TransformerRunner[[], set[str]]],
    Any,
](DefinitionsTransformer)

__all__ = ["definitions_transformer_runner"]
