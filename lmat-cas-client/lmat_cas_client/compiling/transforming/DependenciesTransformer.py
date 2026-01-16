from itertools import chain
from typing import Iterator, override

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
    def substitute_symbol(self, symbol: str) -> set[str]:
        return set((symbol,))

    @override
    def unit(self, unit_symbol: Symbol) -> set[str]:
        symbol_or_unit: set[str] | Quantity = super().unit(unit_symbol)

        match symbol_or_unit:
            case Quantity():
                return Discard
            case set():
                return symbol_or_unit
            case _:
                assert False

    @override
    def undefined_function(
        self, func_name: str, func_args: Iterator[set[str]]
    ) -> set[str]:
        # include both the function itself, and all arguments to the function as dependencies.
        # e.g. f(x, 1, y) should produce { 'f', 'x', 'y' }

        return set((func_name, *func_args))

    @v_args(inline=False)
    def list_of_expressions(self, tokens: Iterator[set[str]]) -> set[str]:
        return set(chain.from_iterable(tokens))


type DepsTransformer = TransformerRunner[[], set[str]]

dependencies_transformer_runner = TransformerRunner[[], set[str]](
    DependenciesTransformer
)

__all__ = ["dependencies_transformer_runner"]
