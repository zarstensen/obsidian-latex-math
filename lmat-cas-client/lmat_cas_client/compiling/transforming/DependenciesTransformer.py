
from itertools import chain
from typing import Iterator

from lark import Discard, Token, v_args
from sympy import Expr, Function, Symbol
from sympy.physics.units import Quantity

from lmat_cas_client.compiling.DefinitionStore import DefinitionStore
from lmat_cas_client.compiling.transforming.TransformerCore import TransformerRunner
from lmat_cas_client.compiling.transforming.UndefinedAtomsTransformer import (
    UndefinedAtomsTransformer,
)


@v_args(inline=True)
class DependenciesTransformer(UndefinedAtomsTransformer):
    """
    Transforms an AST produced from latex_math_grammar.lark into a set of undefined symbol and function names.
    """

    def __init__(self):
        UndefinedAtomsTransformer.__init__(self, DefinitionStore())

    def latex_math_string(self, dependencies: list[Symbol|Function] = []) -> set[str]:
        return set(dependency.name for dependency in dependencies)

    def __default__(self, _data, children, _meta):

        symbols = [ ]

        for child in children:
            if child is None or isinstance(child, Token):
                continue
            elif isinstance(child, list) or isinstance(child, tuple):
                symbols.extend(child)
            else:
                symbols.append(child)

        if len(symbols) == 0:
            return Discard

        return symbols

    def unit(self, unit_symbol: Symbol) -> Quantity | Symbol:
        symbol_or_unit = super().unit(unit_symbol)

        if isinstance(symbol_or_unit, Quantity):
            return Discard

        return symbol_or_unit

    def undefined_function(self, func_name: Token, func_args: Iterator[Expr]) -> Function | Expr:
        # include both the function itself, and all arguments to the function as dependencies.
        # e.g. f(x, 1, y) should produce [ 'f', 'x', 'y' ]
        return [ Function(func_name.value[:-1]), *func_args ]

    @v_args(inline=False)
    def list_of_expressions(self, tokens: Iterator[Expr]) -> list[Expr]:
        return list(chain.from_iterable(tokens))

dependencies_transformer_runner = TransformerRunner[[], set[str]](DependenciesTransformer)

__all__ = [ "dependencies_transformer_runner" ]
