from abc import abstractmethod
from ctypes import ArgumentError
from typing import ClassVar, List, cast, final, override

from attr import frozen
from lark import Token, Transformer, v_args
from lmat_cas_client.compiling.definition.DefinitionStore import (
    Definition,
    FunctionDefinition,
    SymbolDefinition,
    SympyDef,
    SympyFunDef,
)
from lmat_cas_client.compiling.definition.Resolver import (
    DefinitionResolver,
    FunctionResToken,
    SymbolResToken,
)
from lmat_cas_client.compiling.transforming.Ir import (
    Ir,
    Resolved,
    ResolveStrategy,
    SupportsBubbleUp,
    ir_strat,
)
from lmat_cas_client.math_lib.units import UnitUtils
from sympy import Basic, Expr, Number, Symbol
from sympy.physics.units import Quantity


class SymbolStrat(ResolveStrategy):
    """
    Ir object can be resolved as a sympy Symbol.
    """

    _resolve_method = "as_symbol"

    @abstractmethod
    def as_symbol(self) -> Resolved[Symbol]:
        pass


class SubstituteStrat(ResolveStrategy):
    """
    Ir object can have a defined value,
    which it can be substituted with.j
    """

    _resolve_method = "as_substituted"

    @abstractmethod
    def as_substituted(self) -> Resolved[Expr]:
        pass


@final
@frozen
class SymbolIr(Ir, SymbolStrat, SubstituteStrat):
    """
    Intermediate representation of a symbol in the AST.

    Args:
        SymbolStrat: resolves the original Symbol object.
        SubstituteStrat (_type_): resolves the symbol's defined value from a DefinitionResolver.
        if not present, returns the original Symbol object.
    """

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


class AppliedStrat(ResolveStrategy):
    """
    Ir object has an applied value, which this resolves.
    """

    _resolve_method = "as_applied"

    @abstractmethod
    def as_applied(self) -> Resolved[Basic]:
        pass


class BodyStrat(ResolveStrategy):
    """
    Ir object has a function body, which this resolves
    """

    _resolve_method = "as_body"

    @abstractmethod
    def as_body(self) -> Resolved[Basic]:
        pass


@final
@frozen
class FuncIr(Ir, AppliedStrat, BodyStrat):
    """
    Ir of a function application.
    Stores the arguments passed to the function,
    as well as the function definition itself.

    Args:
        AppliedStrat: Resolve the function value when applied with the given arguments.
        BodyStrat: Resolve the body of the function.
    """

    args: tuple[Definition, ...]
    func_target: FunctionResToken | FunctionDefinition
    resolver: DefinitionResolver

    _default_strat = AppliedStrat

    @override
    def as_applied(self) -> Resolved[Basic]:
        return Resolved(self.resolver.resolve_applied(self.func_target, self.args))

    @override
    def as_body(self) -> Resolved[Basic]:

        match self.func_target:
            case FunctionResToken(id):
                definition = cast(FunctionDefinition, self.resolver.get_definition(id))
            case FunctionDefinition() as definition:
                pass
            case _:
                assert False

        return Resolved(
            self.resolver.resolve_body(self.func_target),
            post_resolve=lambda r: FuncIr(
                self.args,
                FunctionDefinition(
                    SympyFunDef(r),
                    definition.params,
                    deps=definition.deps,  # type: ignore[arg-type]
                ),
                self.resolver,
            ),
        )


class LhsStrat(ResolveStrategy):
    """
    Ir object has a left hand expression, which this resolves to.
    """

    _resolve_method: ClassVar[str] = "as_lhs"  # noqa: F821

    @abstractmethod
    def as_lhs(self) -> Resolved[Expr]:
        pass


class RhsStrat(ResolveStrategy):
    """
    Ir object has a right hand expression, which this resolves to.
    """

    _resolve_method: ClassVar[str] = "as_rhs"

    @abstractmethod
    def as_rhs(self) -> Resolved[Expr]:
        pass


class MultStrat(ResolveStrategy):
    """
    Ir object can be resolved to all of it's factors
    multiplied together
    """

    _resolve_method: ClassVar[str] = "as_mult"

    @abstractmethod
    def as_mult(self) -> Resolved[Expr]:
        pass


@frozen
class MultIr(Ir, LhsStrat, RhsStrat, MultStrat):
    r"""
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

    _default_strat = MultStrat

    @override
    def as_lhs(self):
        return Resolved(self.lhs, lambda r: MultIr(r, self.rhs))

    @override
    def as_rhs(self):
        return Resolved(self.rhs, lambda r: MultIr(self.lhs, r))

    @override
    def as_mult(self):
        return Resolved(self.lhs * self.rhs)


@v_args(inline=True)
class UndefinedAtomsTransformer(Transformer):
    """
    Handles transformation of rules relating to user defined (or undefined for that matter) symbols or functions.
    """

    def __init__(self, definition_resolver: DefinitionResolver):
        self.__resolver = definition_resolver

    def combine_symbol(self, *symbols: Symbol) -> SymbolIr:
        return SymbolIr(Symbol("".join(map(str, symbols))), self.__resolver)

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
    ) -> FuncIr | MultIr:
        match self.__resolver.get_resolver_token(func_head.name):
            case FunctionResToken() as token:
                # if it is a defined function,
                # we need to wrap it in an intermediate reprensentation object,
                # in the case this is the child of a partial derivative (or similar) rule,
                # which needs to *first* differentiate the body and *then* apply the arguments to the
                # new body.
                return FuncIr(
                    tuple(map(lambda a: SymbolDefinition(SympyDef(a)), func_args)),
                    token,
                    self.__resolver,
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
