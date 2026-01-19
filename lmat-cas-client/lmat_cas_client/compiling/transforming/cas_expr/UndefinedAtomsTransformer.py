from ctypes import ArgumentError
from typing import Iterator

from attr import frozen
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
from sympy import Expr, Number, Symbol
from sympy.physics.units import Quantity


@frozen
class ImplicitMul:
    """
    This is needed for when a maybe_function_application rule does *not* apply the function,
    then the expression should be interpreted as an implicit multiplication between the
    function head and body.
    However, this needs to happen at a higher level scope, so we need this special class
    to represent this, and then only higher up in the implicit_multiplication handler,
    actually perform the implicit multiplication.

    An example of where this is problematic can be seen here:

    \sin f (x)

    *if* f is a function, then this should be interpreted as

    \sin(f(x))

    *if* f is NOT a function, then this should be interpreted as

    \sin(f) * x

    The parser currently parses this as the first case,
    but this transformer injects this class when f is not a function,
    so we can bubble up to the second case in the rule handlers.
    """

    lhs: Expr
    rhs: Expr


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

    def maybe_function_application(
        self, func_head: Symbol, func_args: Iterator[Expr] = None
    ) -> Expr | ImplicitMul:
        match self.__definition_store.get_resolver_token(func_head.name):
            case FunctionResToken() as token:
                return self.__definition_store.resolve_applied(
                    token, map(lambda a: SymbolDefinition(SympyDef(a)), func_args)
                )
            case _:
                # if it is not a defined function,
                # we must interpret it as an implicit multiplication between func_head and func_args,
                # IF func_args only contains 1 parameter, otherwise what the user has written, does not make sense,
                # you cannot have an implicit multiplication between a symbol, and a function argument list.
                if len(func_args) != 1:
                    raise ArgumentError(
                        f"Cannot multiply symbol {func_head} with argument list ({','.join(map(str, func_args))})!"
                        f"\nIf you want {func_head} to be an undefined function, place a function assumption somewhere above this function."
                        "\ne.g."
                        f"\n${func_head}(x, y, ...) \\mapsto \\mathbb{{C}}$"
                    )

                return ImplicitMul(self.substitute_symbol(func_head), func_args[0])
