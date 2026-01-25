from ctypes import ArgumentError
from typing import List, Optional, cast, override

from attr import frozen
from lark import Discard, Token, Transformer, Tree, Visitor, v_args
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
from sympy import N, Expr, MatrixBase, Number, Symbol
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


@frozen
class RangeIndex:
    beg: Optional[Expr]
    end: Optional[Expr]


class SingularIndex(RangeIndex):
    def __init__(self, index: Expr):
        super().__init__(beg=index, end=index + 1)


ALL_INDEX = RangeIndex(beg=None, end=None)


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
                return cast(Expr, self.__definition_store.resolve_value(token))
            case FunctionResToken() as token:
                return cast(Expr, self.__definition_store.resolve_unapplied(token))
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

    def unit(self, unit_symbol: Symbol) -> Quantity | Symbol | Expr:

        unit = UnitUtils.str_to_unit(unit_symbol.name)

        if unit is not None:
            return unit
        else:
            return self.substitute_symbol(unit_symbol)

    def maybe_function_application(
        self, func_head: Symbol, func_args: List[Expr]
    ) -> Expr | ImplicitMul:
        match self.__definition_store.get_resolver_token(func_head.name):
            case FunctionResToken() as token:
                return cast(
                    Expr,
                    self.__definition_store.resolve_applied(
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

                return ImplicitMul(self.substitute_symbol(func_head), func_args[0])

    def index_range(self, begin: Optional[Expr], end: Optional[Expr]):
        return RangeIndex(begin, end)

    def index_all(self):
        return ALL_INDEX

    def index_singular(self, index: Expr):
        return SingularIndex(index)

    def indicies_2d(
        self,
        row_index: Optional[RangeIndex] = None,
        col_index: Optional[RangeIndex] = None,
    ):
        return row_index or ALL_INDEX, col_index or ALL_INDEX

    @staticmethod
    def _index_symbol_prime(handler):
        def _wrapper(
            self: "UndefinedAtomsTransformer",
            index_str: str,
            index_target: Expr,
            *args,
        ):
            match index_target, args:
                case Symbol() as symbol, [*new_args, Token() | None as primes] if (
                    primes is None or primes.type == "PRIMES"
                ):
                    return handler(
                        self,
                        index_str,
                        self.substitute_symbol(
                            Symbol(
                                f"{symbol.name}{primes.value if primes is not None else ''}"
                            )
                        ),
                        *new_args,
                    )
                case _:
                    return handler(self, index_str, index_target, *args)

        return _wrapper

    @staticmethod
    def _index_fallback(handler):
        def _wrapper(
            self: "UndefinedAtomsTransformer", index_str: str, index_target: Expr, *args
        ):
            if hasattr(index_target, "__getitem__"):
                return handler(self, index_target, *args)
            elif isinstance(index_target, Symbol):
                return self.substitute_symbol(
                    Symbol(f"{index_target.name}_{{{index_str.strip()}}}")
                )
            else:
                assert False, "AAAAAAAA"

        return _wrapper

    @_index_symbol_prime
    @_index_fallback
    def complement_2d_indexing(
        self, index_target: MatrixBase, indicies: tuple[RangeIndex, RangeIndex]
    ):
        row, col = indicies

        if row != ALL_INDEX:
            for _ in range((row.end or index_target.shape[0]) - (row.beg or 0)):
                index_target.row_del(row.beg or 0)

        if col != ALL_INDEX:
            for _ in range((col.end or index_target.shape[1]) - (col.beg or 0)):
                index_target.col_del(col.beg or 0)

        return index_target

    @_index_symbol_prime
    @_index_fallback
    def standard_2d_indexing(
        self, index_target: MatrixBase, indicies: tuple[RangeIndex, RangeIndex]
    ):

        row, col = indicies

        index_value: MatrixBase = index_target[
            row.beg : row.end,  # type: ignore[misc]
            col.beg : col.end,  # type: ignore[misc]
        ]

        if isinstance(row, SingularIndex) and isinstance(col, SingularIndex):
            return index_value[0]

        return index_value

    @_index_symbol_prime
    @_index_fallback
    def standard_1d_indexing(
        self, index_target: MatrixBase, index: Optional[RangeIndex | int | Symbol]
    ):
        match index:
            case None:
                index = ALL_INDEX
            case RangeIndex():
                pass
            case _:
                index = SingularIndex(cast(Expr, index))

        index_value: MatrixBase = index_target[index.beg : index.end, :]  # type: ignore[misc]

        if isinstance(index, SingularIndex) and index_target.shape[1] == 1:
            return index_value[0]

        return index_value


class IndexInjector(Visitor):
    INDEX_RULES = [
        "standard_2d_indexing",
        "standard_1d_indexing",
        "complement_2d_indexing",
    ]

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
