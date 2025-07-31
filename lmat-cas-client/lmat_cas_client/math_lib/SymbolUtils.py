from typing import Iterable

import regex
from sympy import Symbol

__FORMATTED_SYMBOL_REGEX = r"(?:\\[^{]*{\s*)?(%s)(?:\s*})?(\s*_{.*})?"
__symbols_priority = [
            __FORMATTED_SYMBOL_REGEX % ("[xyz]",),
            __FORMATTED_SYMBOL_REGEX % ("[ut]",)
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
