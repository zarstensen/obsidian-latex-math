from abc import abstractmethod
from ctypes import ArgumentError
from typing import List, cast, final, override

from attr import frozen
from lark import Token, Transformer, Tree, Visitor, v_args
from lmat_cas_client.compiling.definition.DefinitionStore import (
    SymbolDefinition,
    SympyDef,
)
from lmat_cas_client.compiling.definition.Resolver import (
    DefinitionResolver,
    FunctionResToken,
    SymbolResToken,
)
from lmat_cas_client.compiling.transforming.Ir import (
    Capability,
    Ir,
    MultIr,
    Resolved,
    SupportsBubbleUp,
    ir_strat,
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


class SymbolStrat(Capability):
    _resolve_method = "as_symbol"

    @abstractmethod
    def as_symbol(self) -> Resolved[Symbol]:
        pass


class SubstituteStrat(Capability):
    _resolve_method = "as_substituted"

    @abstractmethod
    def as_substituted(self) -> Resolved[Expr]:
        pass


@final
@frozen
class SymbolIr(Ir, SymbolStrat, SubstituteStrat):
    symbol: Symbol
    resolver: DefinitionResolver

    _default_strat = SubstituteStrat

    @override
    def as_symbol(self) -> Resolved[Symbol]:
        return Resolved(self.symbol)

    @override
    def as_substituted(self) -> Resolved[Expr]:
        match self.resolver.get_resolver_token(self.symbol.name):
            case SymbolResToken() as token:
                return Resolved(cast(Expr, self.resolver.resolve_value(token)))
            case FunctionResToken() as token:
                return Resolved(cast(Expr, self.resolver.resolve_unapplied(token)))
            case _:
                return cast(Resolved[Expr], self.as_symbol())


@v_args(inline=True)
class UndefinedAtomsTransformer(Transformer):
    """
    Handles transformation of rules relating to user defined (or undefined for that matter) symbols or functions.
    """

    def __init__(self, definition_resolver: DefinitionResolver):
        self.__resolver = definition_resolver

    def combine_symbol(self, *symbols: Symbol) -> SymbolIr:
        symbol = Symbol("".join(map(str, symbols)))

        return SymbolIr(symbol, self.__resolver)

    @ir_strat(symbol=SymbolStrat, index_contents=SymbolStrat)
    def indexed_symbol(
        self, symbol: Symbol, index_contents: Symbol | Number | str, primes: str | None
    ) -> SymbolIr:
        primes = "" if primes is None else primes

        match index_contents:
            case Symbol():
                index_contents = index_contents.name
            case Number():
                index_contents = str(index_contents)

        if not index_contents.startswith("{") or not index_contents.endswith("}"):
            index_contents = f"{{{index_contents}}}"

        return self.combine_symbol(Symbol(f"{symbol.name}{primes}_{index_contents}"))

    def formatted_symbol(
        self, formatter: Token, symbol_contents: str, primes: str | None
    ) -> SymbolIr:
        formatter_text = str(formatter)

        if not symbol_contents.startswith("{") and not symbol_contents.endswith("}"):
            symbol_contents = f"{{{str(symbol_contents)}}}"

        return self.combine_symbol(
            Symbol(f"{formatter_text}{symbol_contents}{primes or ''}")
        )

    @ir_strat(unit_symbol_ir=SupportsBubbleUp)
    def unit(self, unit_symbol_ir: Ir) -> Quantity | Symbol | Expr:

        assert isinstance(unit_symbol_ir, SymbolStrat)
        unit_symbol: Symbol = unit_symbol_ir.as_symbol().value

        unit = UnitUtils.str_to_unit(unit_symbol.name)

        if unit is not None:
            return unit
        else:
            return cast(Expr, unit_symbol_ir.as_default().value)

    @ir_strat(func_head=SymbolStrat)
    def maybe_function_application(
        self, func_head: Symbol, func_args: List[Expr]
    ) -> Expr | MultIr:
        match self.__resolver.get_resolver_token(func_head.name):
            case FunctionResToken() as token:
                return cast(
                    Expr,
                    self.__resolver.resolve_applied(
                        token, map(lambda a: SymbolDefinition(SympyDef(a)), func_args)
                    ),
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

                return MultIr(
                    SymbolIr(func_head, self.__resolver).as_substituted().value,
                    func_args[0],
                )


class IndexInjector(Visitor):
    INDEX_RULES = []

    def __init__(self, src_text):
        self._src_text = src_text

    @override
    def __default__(self, node: Tree):
        if node.data not in self.INDEX_RULES:
            return node

        match node.children:
            case [_, index_node, *_] if isinstance(index_node, Tree):
                index_meta = index_node.meta
            case _:
                assert False, "rule is not a valid index rule"

        node.children.insert(
            0, self._src_text[index_meta.start_pos : index_meta.end_pos]
        )
        return node
