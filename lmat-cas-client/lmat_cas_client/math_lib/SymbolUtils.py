from typing import Iterable

import regex
from sympy import (
    Complexes,
    FiniteSet,
    Integers,
    Interval,
    Rationals,
    Reals,
    Set,
    Symbol,
    oo,
    true,
)

__FORMATTED_SYMBOL_REGEX = r"(?:\\[^{]*{\s*)?(%s)(?:\s*})?(\s*_{.*})?"
__symbols_priority = [
    __FORMATTED_SYMBOL_REGEX % ("[xyz]",),
    __FORMATTED_SYMBOL_REGEX % ("[ut]",),
]


# Convert the given symbol into a sortable key, prioritizing first the _symbols_priority list,
# second lexicographical ordering of all matched regex group, and third lexicographical ordering of the original symbols string.
def symbols_var_order_key(symb: Symbol):
    priority = len(__symbols_priority)

    symbol_str = str(symb)
    compare_key = symbol_str

    for new_priority, priority_check in enumerate(reversed(__symbols_priority)):
        match = regex.match(priority_check, symbol_str)

        if match:
            priority = new_priority
            # only the regex groups are used for the compare key,
            # this allows us to ignore certain irrelevant aspects of the symbol str,
            # such as formatting.
            compare_key = "".join(filter(None, match.groups()))

    return (priority, compare_key, str(symb))


# Return the given list of symbols in order of most likely to least likely symbol to be treated as a variable instead of a constant.
# e.g. the symbols a, b, c, x, y, z have the following ordering: x, y, z, a, b, c
# because x, y and z are more often used as variables compared to a, b and c.
def symbols_variable_order(symbols: Iterable[Symbol]) -> list[Symbol]:
    return sorted(symbols, key=symbols_var_order_key)


def symbol_assumptions_set(symbol: Symbol) -> Set:
    """
    Map a symbol to a sympy Set, of which the symbol resides in.
    This Set is intended to be restrictive'ish, but still represent one of the
    main types of number sets.

    The set is picked based on the Symbol's assumptions.

    Args:
        symbol (Symbol)

    Returns:
        Set
    """
    res: Set = Complexes
    if symbol.is_real == true:
        res = res.intersect(Reals)
    if symbol.is_rational == true:
        res = res.intersect(Rationals)
    if symbol.is_positive == true:
        res = res.intersect(Interval(0, oo))
    if symbol.is_negative == true:
        res = res.intersect(Interval(-oo, 0))
    if symbol.is_nonzero == true:
        res = FiniteSet(0).complement(res)
    if symbol.is_integer == true:
        res = res.intersect(Integers)
    if symbol.is_imaginary == true:
        res = res.intersect(Reals.complement(Complexes))

    return res
