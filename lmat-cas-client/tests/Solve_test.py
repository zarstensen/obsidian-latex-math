import sympy.physics.units as u
from lmat_cas_client.command_handlers.SolveHandler import *
from lmat_cas_client.compiling.Compiler import LatexToSympyCompiler
from sympy import *


class TestSolve:
    compiler = LatexToSympyCompiler()

    def test_solve_with_domain(self):
        x = symbols("x")

        handler = SolveHandler(self.compiler)
        result = handler.handle(
            {
                "expression": r"\sin(x) = 0",
                "environment": {"solve_domain": "Interval.Ropen(0, 2 * pi)"},
                "symbols": ["x"],
            }
        )

        assert result.symbols == [x]
        assert result.solution == FiniteSet(0, pi)

    def test_solve_soe(self):
        x, y, z = symbols("x y z")

        handler = SolveHandler(self.compiler)

        result = handler.handle(
            {
                "expression": r"""
            \begin{align}
            x + y + z & = 5 \\
            2x + 5z & = 10 \\
            2y + x & = 3 \\
            \end{align}
            """,
                "environment": {},
                "symbols": ["x", "y", "z"],
            }
        )

        assert result.solution == FiniteSet((15, -6, -4))
        assert result.symbols == [x, y, z]

        result = handler.handle(
            {
                "expression": r"""
            \begin{align}
            3 * x^2 & = 2 * y \\
            y &= \frac{3}{2} x \\
            \end{align}
            """,
                "environment": {},
                "symbols": ["x", "y"],
            }
        )

        assert result.solution == FiniteSet((0, 0), (1, Rational(3, 2)))
        assert result.symbols == [x, y]

    def test_solve_multivariate(self):
        x, y, z = symbols("x y z")

        handler = SolveHandler(self.compiler)

        result = handler.handle(
            {
                "expression": r"""
            \begin{cases}
            x + y = z \\
            x - y = -z \\
            \end{cases}
            """,
                "symbols": ["x", "y"],
                "environment": {},
            }
        )

        assert result.solution == FiniteSet((0, z))
        assert result.symbols == [x, y]

        result = handler.handle(
            {
                "expression": r"""
            \begin{cases}
            x + y = z \\
            x - y = -z \\
            \end{cases}
            """,
                "symbols": ["y", "z"],
                "environment": {},
            }
        )

        assert result.solution == EmptySet
        assert result.symbols == [y, z]

    def test_solve_simplify(self):
        handler = SolveHandler(self.compiler)

        result = handler.handle(
            {
                "expression": r"x^2 = 5 {kW} {h}",
                "environment": {},
                "symbols": ["x"],
            }
        )

        assert result.solution == FiniteSet(
            sqrt(5 * 3600000 * u.joule), -sqrt(5 * 3600000 * u.joule)
        )

    def test_solve_info(self):
        handler = SolveInfoHandler(self.compiler)

        x, a = symbols("x a")

        result = handler.handle({"expression": r"\csc(x) + a", "environment": {}})

        assert result.symbols == [x, a]
        assert result.equation_count == 1

        handler = SolveInfoHandler(self.compiler)

        x, t, u, a, b, c = symbols("x t u a b c")

        result = handler.handle(
            {
                "expression": r"""
            \begin{cases}
            \int_a^b x \dd x = 25 \\
            \frac{c}{u} = t \\
            \end{cases}
            """,
                "environment": {},
            }
        )

        assert result.symbols == [t, u, a, b, c]
        assert result.equation_count == 2
