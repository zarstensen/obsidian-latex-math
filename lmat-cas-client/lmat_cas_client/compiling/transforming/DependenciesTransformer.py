# mypy: disable-error-code="override"
from itertools import chain
from typing import Any, Iterable, Optional, override

from lark import Discard, v_args
from sympy import Symbol
from sympy.physics.units import Quantity

from lmat_cas_client.compiling.definition.EmptyResolver import EmptyResolver
from lmat_cas_client.compiling.transforming.cas_expr.UndefinedAtomsTransformer import (
    UndefinedAtomsTransformer,
)
from lmat_cas_client.compiling.transforming.TransformerRunner import TransformerRunner


@v_args(inline=True)
class DependenciesTransformer(UndefinedAtomsTransformer):
    """
    Transforms an AST produced from latex_math_grammar.lark into a set of undefined symbol and function names present in the AST.
    This set of symbols and functions can be interpreted as the dependencies of the equation the AST represents.
    """

    def __init__(self):
        UndefinedAtomsTransformer.__init__(self, EmptyResolver())

    @override
    def __default__(self, _data, children, _meta) -> set[str]:
        symbols = set()

        for child in children:
            match child:
                case str() if type(child) is str:
                    symbols.add(child)
                case set() if all(isinstance(e, str) for e in child):
                    symbols.update(child)

        return symbols

    @override
    def substitute_symbol(self, symbol: Symbol) -> set[str]:
        return set((symbol.name,))

    @override
    def unit(self, unit_symbol: Symbol) -> set[str]:
        unit: Any | Quantity = super().unit(unit_symbol)

        if isinstance(unit, Quantity):
            return Discard  # type: ignore[return-value]

        return set((unit_symbol.name,))

    @override
    def maybe_function_application(
        self, func_name: Symbol, func_args: Iterable[str]
    ) -> set[str]:
        # include both the function itself, and all arguments to the function as dependencies.
        # e.g. f(x, 1, y) should produce { 'f', 'x', 'y' }

        return set((func_name.name, *func_args))

    @v_args(inline=False)
    def list_of_expressions(self, tokens: Iterable[set[str]]) -> set[str]:
        return set(chain.from_iterable(tokens))

    @override
    def index_range(self, beg: Optional[set[str]], end: Optional[set[str]]) -> set[str]:
        return (beg or set()).union(end or set())

    @override
    def index_all(self) -> set[str]:
        return set()

    @override
    def index_singular(self, index: set[str]) -> set[str]:
        return index

    @override
    @UndefinedAtomsTransformer._index_symbol_prime
    def complement_2d_indexing(self, index_str: str, *_args):
        return set()

    @override
    @UndefinedAtomsTransformer._index_symbol_prime
    def standard_2d_indexing(self, index_str: str, *_args):
        return set()

    @override
    @UndefinedAtomsTransformer._index_symbol_prime
    def standard_1d_indexing(
        self, index_str: set[str], index_target: set[str], index: set[str]
    ):
        # this depends on both the indexed symbol + the non indexed version, and all the indexes as individual symbols.
        return set()


type DepsTransformer = TransformerRunner[[], set[str]]

dependencies_transformer_runner = TransformerRunner[[], set[str]](
    DependenciesTransformer
)

__all__ = ["dependencies_transformer_runner"]
