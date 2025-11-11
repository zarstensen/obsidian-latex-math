from typing import Annotated

import sympy.physics.units as u
from sympy.physics.units.definitions.unit_definitions import *
from sympy.physics.units.quantities import PhysicalConstant
from sympy.physics.units.systems import SI

"""
UnitDefinitions re-exports all sympy defined constants and units, as well as some additional custom constants.
"""

# special constants not present in sympy

proton_mass: Annotated[
    PhysicalConstant,
    "Mass of a proton particle (https://physics.nist.gov/cgi-bin/cuu/Value?mp)",
] = PhysicalConstant("proton_mass", abbrev="m_p")

SI.set_quantity_dimension(proton_mass, u.mass)
SI.set_quantity_scale_factor(
    proton_mass,
    1.672_621_925_95 * 10 ** (-27) * u.kg,
)

neutron_mass: Annotated[
    PhysicalConstant,
    "Mass of a neutron particle (https://physics.nist.gov/cgi-bin/cuu/Value?mn)",
] = PhysicalConstant("neutron_mass", abbrev="m_n")

SI.set_quantity_dimension(neutron_mass, u.mass)
SI.set_quantity_scale_factor(
    neutron_mass,
    1.674_927_500_56 * 10 ** (-27) * u.kg,
)

electron_mass: Annotated[
    PhysicalConstant,
    "Mass of an electron particle (https://physics.nist.gov/cgi-bin/cuu/Value?me)",
] = PhysicalConstant("electron_mass", abbrev="m_e")

SI.set_quantity_dimension(electron_mass, u.mass)
SI.set_quantity_scale_factor(
    electron_mass,
    9.109_383_7139 * 10 ** (-31) * u.kg,
)
