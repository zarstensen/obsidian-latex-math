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
from sympy import Expr, Function, Symbol
from sympy.physics.units import Quantity


@v_args(inline=True)
class UndefinedAtomsTransformer(Transformer):
    """
    Handles transformation of rules relating to user defined (or undefined for that matter) symbols or functions.
    """

    def __init__(self, definition_resolver: DefinitionResolver):
        self.__definition_store = definition_resolver

    def combine_symbol(self, *symbol_strings: str) -> str:
        return "".join(map(str, symbol_strings))

    def substitute_symbol(self, symbol_name: str) -> Symbol | Expr:
        match self.__definition_store.get_resolver_token(str(symbol_name)):
            case SymbolResToken() as token:
                return self.__definition_store.resolve_value(token)
            case FunctionResToken() as token:
                return self.__definition_store.resolve_unapplied(token)
            case _:
                return Symbol(symbol_name)

    def indexed_symbol(
        self, symbol: Expr, index: Expr | str, primes: str | None
    ) -> str:
        primes = "" if primes is None else primes
        indexed_text = str(index)

        if not indexed_text.startswith("{") or not indexed_text.endswith("}"):
            indexed_text = f"{{{indexed_text}}}"

        return f"{symbol}_{indexed_text}{primes}"

    def formatted_symbol(
        self, formatter: Token, text: str | list[str], primes: str | None
    ) -> str:
        formatter_text = str(formatter)
        primes = "" if primes is None else primes

        if not text.startswith("{") and not text.endswith("}"):
            text = f"{{{str(text)}}}"

        return f"{formatter_text}{text}{primes}"

    def unit(self, unit_symbol: str) -> Quantity | Symbol:

        unit = UnitUtils.str_to_unit(unit_symbol)

        if unit is not None:
            return unit
        else:
            return self.substitute_symbol(unit_symbol)

    def undefined_function(
        self, func_name: str, func_args: Iterator[Expr] = None
    ) -> Function | Expr:
        match self.__definition_store.get_resolver_token(func_name):
            case FunctionResToken() as token:
                return self.__definition_store.resolve_applied(
                    token, map(lambda a: SymbolDefinition(SympyDef(a)), func_args)
                )
            case _:
                return Function(func_name)(*func_args)
