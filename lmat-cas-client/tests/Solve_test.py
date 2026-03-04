import pytest
import sympy.physics.units as u
from lmat_cas_client.command_handlers.SolveHandler import *
from lmat_cas_client.compiling.Compiler import (
    LatexToCasExprCompiler,
    LatexToDefStoreCompiler,
)
from sympy import *


class TestSolve:
    cas_expr_compiler = LatexToCasExprCompiler()
    def_store_compiler = LatexToDefStoreCompiler()

    @pytest.mark.parametrize(
        "expr,solve_symbs,defs,exp_symbs,exp_sol",
        [
            (
                "x^2-100 = 0",
                ["x"],
                [r"x \in R_{+}"],
                [Symbol("x", real=True, positive=True)],
                FiniteSet(10),
            ),
            (
                r"(x - \pi)(x - 10)(x + \frac{1}{3}) = 0",
                ["x"],
                [r"x \in Q_{+}"],
                [Symbol("x", rational=True, positive=True)],
                FiniteSet(10),
            ),
            (
                r"x^3 + 3x^2 - i x^2 - 3i x = 0",
                ["x"],
                [r"x \in I"],
                [Symbol("x", imaginary=True)],
                FiniteSet(I),
            ),
        ],
    )
    def test_solve_with_assumptions(
        self,
        expr: str,
        solve_symbs: list[str],
        defs: list[str],
        exp_symbs: list[Symbol],
        exp_sol: Set,
    ):
        handler = SolveHandler(self.cas_expr_compiler, self.def_store_compiler)
        result = handler.handle({
            "expression": expr,
            "environment": {"definitionsv2": defs},
            "symbols": solve_symbs,
        })

        assert result.symbols == exp_symbs
        assert result.solution == exp_sol

    def test_solve_soe(self):
        x, y, z = symbols("x y z")

        handler = SolveHandler(self.cas_expr_compiler, self.def_store_compiler)

        result = handler.handle({
            "expression": r"""
            \begin{align}
            x + y + z & = 5 \\
            2x + 5z & = 10 \\
            2y + x & = 3 \\
            \end{align}
            """,
            "environment": {},
            "symbols": ["x", "y", "z"],
        })

        assert result.solution == FiniteSet((15, -6, -4))
        assert result.symbols == [x, y, z]

        result = handler.handle({
            "expression": r"""
            \begin{align}
            3 * x^2 & = 2 * y \\
            y &= \frac{3}{2} x \\
            \end{align}
            """,
            "environment": {},
            "symbols": ["x", "y"],
        })

        assert result.solution == FiniteSet((0, 0), (1, Rational(3, 2)))
        assert result.symbols == [x, y]

        result = handler.handle({
            "expression": r"""
                \begin{bmatrix}
                3 & 2 & -1 \\
                2 & -2 & 4 \\
                2 & -1 & 2
                \end{bmatrix}
                \begin{bmatrix}
                x \\
                y \\
                z
                \end{bmatrix}
                =
                \begin{bmatrix}
                1 \\
                -2 \\
                0
                \end{bmatrix}

                """,
            "environment": {},
            "symbols": ["x", "y", "z"],
        })

        assert result.solution == FiniteSet((1, -2, -2))
        assert result.symbols == [x, y, z]

    def test_solve_multivariate(self):
        x, y, z = symbols("x y z")

        handler = SolveHandler(self.cas_expr_compiler, self.def_store_compiler)

        result = handler.handle({
            "expression": r"""
            \begin{cases}
            x + y = z \\
            x - y = -z \\
            \end{cases}
            """,
            "symbols": ["x", "y"],
            "environment": {},
        })

        assert result.solution == FiniteSet((0, z))
        assert result.symbols == [x, y]

        result = handler.handle({
            "expression": r"""
            \begin{cases}
            x + y = z \\
            x - y = -z \\
            \end{cases}
            """,
            "symbols": ["y", "z"],
            "environment": {},
        })

        assert result.solution == EmptySet
        assert result.symbols == [y, z]

    def test_solve_simplify(self):
        handler = SolveHandler(self.cas_expr_compiler, self.def_store_compiler)

        result = handler.handle({
            "expression": r"x^2 = 5 {kW} {h}",
            "environment": {},
            "symbols": ["x"],
        })

        assert result.solution == FiniteSet(
            sqrt(5 * 3600000 * u.joule), -sqrt(5 * 3600000 * u.joule)
        )

    def test_solve_info(self):
        handler = SolveInfoHandler(self.cas_expr_compiler, self.def_store_compiler)

        x, a = symbols("x a")

        result = handler.handle({"expression": r"\csc(x) + a", "environment": {}})

        assert result.symbols == [x, a]
        assert result.equation_count == 1

        handler = SolveInfoHandler(self.cas_expr_compiler, self.def_store_compiler)

        x, t, u, a, b, c = symbols("x t u a b c")

        result = handler.handle({
            "expression": r"""
            \begin{cases}
            \int_a^b x \dd x = 25 \\
            \frac{c}{u} = t \\
            \end{cases}
            """,
            "environment": {},
        })

        assert result.symbols == [t, u, a, b, c]
        assert result.equation_count == 2
