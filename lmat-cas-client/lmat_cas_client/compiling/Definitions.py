from typing import Iterable, override

from lark import Tree
from sympy import Expr, Function, Symbol
from sympy.core.function import AppliedUndef

from lmat_cas_client.compiling.transforming.TransformerRunner import TransformerRunner
from lmat_cas_client.compiling.transforming.cas_expr.CasExprTransformer import CasExpr

from .definitions.DefinitionStore import (
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


class SympyFunctionDefinition(FunctionDefinition):
    def __init__(self, func_name: str, variables=...):
        super().__init__(variables)
        self._func_name = func_name

    @override
    def defined_value(self, _definition_store):
        return Function(self._func_name)


class AssumptionDefinition(SympyDefinition):
    """
    Specialized SympyDefinition for sympy Symbols-
    """

    def __init__(self, symbol_assumption: Symbol):
        super().__init__(symbol_assumption)

    @override
    def dependencies(self) -> set[str]:
        # assumptions have no dependencies, but SympyDefinition would return the symbol itself as such,
        # so we need to explicitly return an empty set here.
        return set()
