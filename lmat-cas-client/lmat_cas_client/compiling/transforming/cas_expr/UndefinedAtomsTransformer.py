from typing import Iterator

from lark import Token, Transformer, v_args
from lmat_cas_client.compiling.definition.DefinitionStore import (
    SymbolDefinition,
    SympyDef,
)
from lmat_cas_client.compiling.definition.Resolver import (
    DefinitionResolver,
    FunctionResToken,
    SymbolResToken,
)
from lmat_cas_client.math_lib.units import UnitUtils
from sympy import Expr, Function, Number, Symbol
from sympy.physics.units import Quantity


@v_args(inline=True)
class UndefinedAtomsTransformer(Transformer):
    """
    Handles transformation of rules relating to user defined (or undefined for that matter) symbols or functions.
    """

    def __init__(self, definition_resolver: DefinitionResolver):
        self.__definition_store = definition_resolver

    def combine_symbol(self, *symbols: Symbol) -> Symbol:
        return Symbol("".join(map(str, symbols)))

    def substitute_symbol(self, substitute_symbol: Symbol) -> Symbol | Expr:
        match self.__definition_store.get_resolver_token(substitute_symbol.name):
            case SymbolResToken() as token:
                return self.__definition_store.resolve_value(token)
            case FunctionResToken() as token:
                return self.__definition_store.resolve_unapplied(token)
            case _:
                return substitute_symbol

    def indexed_symbol(
        self, symbol: Symbol, index_contents: Symbol | Number | str, primes: str | None
    ) -> Symbol:
        primes = "" if primes is None else primes

        match index_contents:
            case Symbol():
                index_contents = index_contents.name
            case Number():
                index_contents = str(index_contents)

        if not index_contents.startswith("{") or not index_contents.endswith("}"):
            index_contents = f"{{{index_contents}}}"

        return Symbol(f"{symbol.name}_{index_contents}{primes}")

    def formatted_symbol(
        self, formatter: Token, symbol_contents: str, primes: str | None
    ) -> Symbol:
        formatter_text = str(formatter)
        primes = "" if primes is None else primes

        if not symbol_contents.startswith("{") and not symbol_contents.endswith("}"):
            symbol_contents = f"{{{str(symbol_contents)}}}"

        return Symbol(f"{formatter_text}{symbol_contents}{primes}")

    def unit(self, unit_symbol: Symbol) -> Quantity | Symbol:

        unit = UnitUtils.str_to_unit(unit_symbol.name)

        if unit is not None:
            return unit
        else:
            return self.substitute_symbol(unit_symbol)

    def undefined_function(
        self, func_head: Symbol, func_args: Iterator[Expr] = None
    ) -> Function | Expr:
        match self.__definition_store.get_resolver_token(func_head.name):
            case FunctionResToken() as token:
                return self.__definition_store.resolve_applied(
                    token, map(lambda a: SymbolDefinition(SympyDef(a)), func_args)
                )
            case _:
                return Function(func_head.name)(*func_args)
