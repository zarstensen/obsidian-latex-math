import lmat_cas_client.math_lib.units.UnitDefinitions as units
from lmat_cas_client.command_handlers.ConvertUnitsHandler import *
from lmat_cas_client.command_handlers.EvalHandler import *
from lmat_cas_client.command_handlers.SolveHandler import *
from lmat_cas_client.compiling.Compiler import LatexToSympyCompiler
from lmat_cas_client.math_lib.units.UnitUtils import auto_convert
from sympy import *


## Tests the unit conversions.
class TestUnitConversion:
    compiler = LatexToSympyCompiler()

    def test_single_term_to_derived_unit(self):
        handler = EvalHandler(self.compiler)
        result = handler.handle({"expression": "{kg} * {m} / {s}^2", "environment": {}})

        assert result.sympy_expr == units.newton

    def test_single_term_to_base_units(self):
        handler = EvalHandler(self.compiler)
        result = handler.handle({"expression": "{J} / {m} * {s}^2", "environment": {}})

        assert result.sympy_expr == units.kilogram * units.meter

    def test_multiple_terms(self):
        handler = EvalHandler(self.compiler)
        result = handler.handle({
            "expression": "{J} / {m} * {s}^2 + {kg} * {m} / {s}^2",
            "environment": {},
        })

        assert result.sympy_expr == units.kilogram * units.meter + units.newton

    def test_explicit_conversion(self):
        handler = ConvertUnitsHandler(self.compiler)
        result = handler.handle({
            "expression": "7.2 * {km} / {h}",
            "target_units": ["m", "s"],
            "environment": {},
        })

        assert result.sympy_expr == 2.0 * units.meter / units.second

        result = handler.handle({
            "expression": "10 {gee}",
            "target_units": ["m", "s"],
            "environment": {},
        })
        assert (
            result.sympy_expr - 98.06650 * units.meter / (units.seconds**2)
            < 1e-15 * units.meter / units.seconds**2
        )

    def test_solve_conversion(self):
        handler = SolveHandler(self.compiler)
        result = handler.handle({
            "expression": "2 x = 50 {kg}",
            "environment": {},
            "symbols": ["x"],
        })

        assert result.solution == FiniteSet(25 * units.kilogram)

    def test_units_in_matrix(self):
        handler = EvalHandler(self.compiler)
        result = handler.handle({
            "expression": r"""
                {km}
                \begin{bmatrix}
                1 {km} \\
                2 {s}/{km} \\
                3 {N}
                \end{bmatrix}
            """,
            "environment": {},
        })

        assert result.sympy_expr == Matrix([
            units.kilometer**2,
            2 * units.second,
            3000 * units.joule,
        ])

    def test_units_not_in_system(self):
        not_a_unit = symbols("NotAUnit")

        handler = EvalHandler(self.compiler)
        result = handler.handle({"expression": "{NotAUnit}", "environment": {}})

        assert result.sympy_expr == not_a_unit

    def test_simplification(self):
        handler = EvalHandler(self.compiler)
        result = handler.handle({"expression": r"\sqrt{ {s}^2 }", "environment": {}})

        assert result.sympy_expr == units.second

    def test_brace_units(self):
        handler = EvalHandler(self.compiler)
        result = handler.handle({
            "expression": r"\frac{{kg}\,{m}^{2}}{{s}^2}",
            "environment": {},
        })
        assert result.sympy_expr == units.joule

    def test_physical_constants(self):
        handler = EvalHandler(self.compiler)
        result = handler.handle({
            "expression": r"5 {gee} \cdot (10 {minutes})^2",
            "environment": {},
        })
        assert result.sympy_expr == 17651970.0 * units.meters

        handler = EvalHandler(self.compiler)
        result = handler.handle({"expression": r"{R}", "environment": {}})
        assert simplify(
            result.sympy_expr
            - 8.31446
            * units.kg
            * units.m**2
            / (units.kelvin * units.mol * units.second**2)
        ) < 1e-4 * units.kg * units.m**2 / (units.kelvin * units.mol * units.second**2)

    def test_preprocessed_quantity_names(self):
        handler = EvalHandler(self.compiler)
        result = handler.handle({
            "expression": r"{e_0} \cdot \frac{{\mu_0}}{{avogadro_{constant}}} + {\ohm}",
            "environment": {},
        })
        assert simplify(result.sympy_expr) == auto_convert(
            units.e0 * units.u0 / units.avogadro_constant + units.ohm
        )

    def test_custom_quanteties(self):
        handler = EvalHandler(self.compiler)
        result = handler.handle({
            "expression": r"{m_p} \cdot 5.97863739847862 \cdot 10^{26}",
            "environment": {},
        })
        assert abs(simplify(result.sympy_expr) - 1 * units.kg) < 1e-13 * units.kg
