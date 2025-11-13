import sys
from copy import copy

import sympy.physics.units as u
from sympy import Add, Expr, MatrixBase, Rel
from sympy.physics.units.quantities import PhysicalConstant, Quantity
from sympy.physics.units.systems import SI
from sympy.physics.units.unitsystem import UnitSystem

from . import UnitDefinitions

# Maps an alias to its corresponding Quantity object.
UNIT_ALIAS_MAP = {}

__defined_units_quantities = {
    unit_name: getattr(UnitDefinitions, unit_name)
    for unit_name in dir(UnitDefinitions)
    if isinstance(getattr(UnitDefinitions, unit_name), Quantity)
}


# preprocess unit / constant str, such that they make more sense when written in latex.
def __preprocess_quantity_str(alias: str) -> str:
    # remove underscores, as this looks wierd in latex, remove braces, as indexed units and constants are otherwise never matched,
    # due to the way the parser handles indexed symbols.
    return alias.replace("_", "").replace("{", "").replace("}", "")


def __add_unit_aliases(str_units: list[tuple[str, Quantity]]):
    for alias, unit in str_units:
        alias = __preprocess_quantity_str(alias)
        if alias not in UNIT_ALIAS_MAP:
            UNIT_ALIAS_MAP[alias] = unit


# add SI units
__add_unit_aliases(((str(unit), unit) for unit in SI._units))
__add_unit_aliases(((str(unit.abbrev), unit) for unit in SI._units))

# add units specified in the defined_units module
__add_unit_aliases(
    (
        (key, unit)
        for key, unit in __defined_units_quantities.items()
        if not isinstance(unit, PhysicalConstant)
    )
)

__add_unit_aliases(
    (
        (str(unit.abbrev), unit)
        for unit in __defined_units_quantities.values()
        if not isinstance(unit, PhysicalConstant)
    )
)

__add_unit_aliases(
    (
        (key, unit)
        for key, unit in __defined_units_quantities.items()
        if isinstance(unit, PhysicalConstant)
    )
)

__add_unit_aliases(
    (
        (str(unit.abbrev), unit)
        for unit in __defined_units_quantities.values()
        if isinstance(unit, PhysicalConstant)
    )
)

# add LaTeX Math specific unit aliases.
__add_unit_aliases([
    ("min", u.minute),
    ("sec", u.second),
    ("epsilon_0", u.vacuum_permittivity),
    ("\\epsilon_0", u.vacuum_permittivity),
    ("e_0", u.vacuum_permittivity),
    ("mu_0", u.vacuum_permeability),
    ("\\mu_0", u.vacuum_permeability),
    ("N_A", u.avogadro_constant),
    ("N_0", u.avogadro_number),
    ("\\omega_P", u.planck_angular_frequency),
    ("\\ohm_P", u.planck_angular_frequency),
    ("\\omega", u.ohms),
    ("\\ohm", u.ohms),
])


def auto_convert(sympy_expr: Expr, unit_system: UnitSystem = SI) -> Expr:
    """
    attempt to automatically convert the units in the given sympy expression.
    this convertion method prioritizes as few units as possible raised to the lowest power possible (or lowest root possible).

    Returns:
        Expr: input expression, with its units converted.
    """

    if isinstance(sympy_expr, MatrixBase):
        new_matrix_contents = []

        for value in sympy_expr:
            new_matrix_contents.append(auto_convert(value, unit_system))

        return type(sympy_expr)(*sympy_expr.shape, new_matrix_contents)
    # relationals and non sympy objects should not be auto converted
    elif isinstance(sympy_expr, Rel) or not isinstance(sympy_expr, Expr):
        return sympy_expr

    if not isinstance(sympy_expr, Add):
        sympy_expr = [sympy_expr]
    else:
        sympy_expr = list(sympy_expr.args)

    converted_expressions = []

    for expr in sympy_expr:
        curr_complexity = get_unit_complexity(expr)

        # unit complexity cannot be determined for expression for some reason.
        if curr_complexity is None:
            converted_expressions.append(expr)
            continue

        # Conver to using all base units of system.
        for units in [unit_system._base_units, *unit_system.get_units_non_prefixed()]:
            converted_expr = u.convert_to(expr, units)
            converted_expr_complexity = get_unit_complexity(converted_expr)

            if converted_expr_complexity < curr_complexity:
                curr_complexity = converted_expr_complexity
                expr = converted_expr

        converted_expressions.append(expr)

    return Add(*converted_expressions)


# find sympy unit which has the given str representation.
def str_to_unit(unit_str: str) -> Quantity | None:
    unit_str = __preprocess_quantity_str(unit_str)

    # attempt to replace the symbol with a corresponding unit.
    if unit_str not in UNIT_ALIAS_MAP:
        return None
    else:
        unit = copy(UNIT_ALIAS_MAP[unit_str])
        unit._latex_repr = unit_str
        return unit


#
#
def get_unit_complexity(expression: Expr) -> int:
    """
    get the 'complexity' of a unit.
    complexity is defined as the sum of all units raised power absolute value (or 1/power if 0 < power < 1).


    Returns:
        int: "complexity" of input unit.
    """
    if not hasattr(expression, "as_powers_dict"):
        return None

    complexity = 0

    for val, pow in expression.as_powers_dict().items():
        # PhysicalConstants should always be auto converted from,
        # so if the input contains one the maximum possible complexity is returned.
        if isinstance(val, PhysicalConstant):
            return sys.maxsize

        if isinstance(val, Quantity):
            if 0 < abs(pow) < 1:
                pow = 1 / pow

            complexity += abs(pow)

    return complexity
