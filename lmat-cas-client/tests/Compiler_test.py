# mypy: disable-error-code="attr-defined"
from typing import Any

import pytest
from lmat_cas_client.compiling.Compiler import (
    LatexToCasExprCompiler,
    LatexToDefStoreCompiler,
    LatexToLogicCasExprCompiler,
    LatexToLogicDefStoreCompiler,
    lmat_env_to_definition_store,
)
from lmat_cas_client.compiling.definition.DefinitionStore import CyclicDependencyError
from lmat_cas_client.compiling.parsing import PrettyParserError
from lmat_cas_client.compiling.transforming.cas_expr.CasExprTransformer import CasExpr
from lmat_cas_client.compiling.transforming.LatexMatrix import LatexMatrix
from lmat_cas_client.LmatEnvironment import LmatEnvironment
from sympy import *
from sympy import Expr
from sympy.logic.boolalg import *


class TestLatexToCasExprCompiler:
    expr_compiler = LatexToCasExprCompiler()
    store_compiler = LatexToDefStoreCompiler()

    def _parse_expr(
        self, expr, environment: LmatEnvironment | Any = LmatEnvironment()
    ) -> CasExpr:
        environment = LmatEnvironment.model_validate(environment)
        return self.expr_compiler.compile(
            expr, lmat_env_to_definition_store(environment, self.store_compiler)
        )

    def _parse_single_expr(
        self, expr, environment: LmatEnvironment | Any = LmatEnvironment()
    ) -> Basic:
        return self._parse_expr(expr, environment).get_expr(-1)

    def test_comments(self):
        result = self._parse_single_expr(
            r"""
1 + 1 % test comment %%% comment
\cdot 50 \% % some more comments
% this is an empty line
\\\\\\\\\\\\\\%
- 100 \ \%
            """
        )

        assert result == 0.5

    def test_basic(self):
        a, b, c = symbols("a b c")
        # result = self.parser.doparse(r'-a i + b \pi + e + \frac{{a}}{b} + {a}^{b} \cdot f(a 25^2 symbol^{yaysymbol}) - \frac{50 - 70}5^{-99} - \frac{{km}}{{h}} \over \sin x + \sqrt[5]{x}')
        result = self._parse_single_expr(r"-a i \cdot (5 + 7)^c + b")
        assert result == -a * I * (5 + 7) ** c + b

    def test_non_base_10_numbers(self):
        result = self._parse_single_expr(r"0b1001 - \mathrm{0b0001} + 0\mathrm{b}1000")
        assert result == 16

        result = self._parse_single_expr(r"\frac{\mathrm{0XFF}}{0xf} + 0123")
        assert result == 140

    def test_trig_funcs(self):
        x, y, abc = symbols("x y abc")
        assert self._parse_single_expr(r"\sin x") == sin(x)
        assert self._parse_single_expr(r"\sin^y x") == sin(x) ** y
        assert simplify(
            self._parse_single_expr(r"\frac{\sin(abc)}{\cos {abc}}")
        ) == tan(abc)
        assert self._parse_single_expr(r"\arctan{abc}") == atan(abc)
        assert self._parse_single_expr(r"\mathrm{arcosh} y") == acosh(y)
        assert self._parse_single_expr(r"\operatorname{arcosh} y") == acosh(y)
        assert self._parse_single_expr(r"\sech y") == sech(y)
        assert self._parse_single_expr(r"\mathrm{arsech} y") == asech(y)
        assert self._parse_single_expr(r"\csch y") == csch(y)
        assert self._parse_single_expr(r"\mathrm{arcsch} y") == acsch(y)
        assert self._parse_single_expr(r"\coth y") == coth(y)
        assert self._parse_single_expr(r"\mathrm{arcoth} y") == acoth(y)

    def test_relations(self):
        x, y, z = symbols("x y z")
        assert tuple(self._parse_expr(r"x=y").get_all_expr()) == (Eq(x, y),)

        result = self._parse_expr(r"x = y < z")
        assert tuple(result.get_all_expr()) == (Eq(x, y), Lt(y, z))

    def test_matrix(self):
        assert self._parse_single_expr(
            r"\begin{bmatrix} 1 \\ 2 \end{bmatrix}"
        ) == Matrix([
            [1],
            [2],
        ])
        assert self._parse_single_expr(
            r"\begin{bmatrix} 1 & 2 \end{bmatrix}"
        ) == Matrix([[1, 2]])
        assert self._parse_single_expr(
            r"\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}"
        ) == Matrix([[1, 2], [3, 4]])
        assert self._parse_single_expr(
            r"\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}"
        ) == Matrix([[1, 2], [3, 4], [5, 6]])

    def test_mathematical_constants(self):
        assert self._parse_single_expr(r"\pi") == S.Pi
        assert self._parse_single_expr(r"e") == S.Exp1
        assert self._parse_single_expr(r"i") == I

    def test_ambigous_function_expressions(self):
        a, b, c = symbols("a b c")

        assert (
            self._parse_single_expr(r"(\sin(a) - b)^2 + c + (\sin(b) - a)")
            == (sin(a) - b) ** 2 + c + sin(b) - a
        )
        assert self._parse_single_expr(r"\sin(a) - b") == sin(a) - b
        assert self._parse_single_expr(r"\sin(5) - 75") == sin(5) - 75
        assert self._parse_single_expr(r"\sin(a - b)") == sin(a - b)
        assert self._parse_single_expr(r"\sin(a - b) - c") == sin(a - b) - c
        assert self._parse_single_expr(r"\sin a \cdot b - c") == sin(a) * b - c
        assert self._parse_single_expr(r"\sin{a \cdot b} - c") == sin(a * b) - c

    def test_implicit_multiplication(self):
        a, b, c = symbols("a b c")

        assert self._parse_single_expr(r"2 a") == 2 * a
        assert self._parse_single_expr(r"a b") == a * b
        assert self._parse_single_expr(r"a b c") == a * b * c
        assert self._parse_single_expr(r"a b \cdot c") == a * b * c
        assert self._parse_single_expr(r"a \cdot b c") == a * b * c

        # indexed_symbols
        x1, x2 = symbols("x_{1} x_{2}")

        assert self._parse_single_expr(r"x_1 x_{2}") == x1 * x2

        # functions
        assert self._parse_single_expr(r"b \sin(a)") == sin(a) * b
        assert self._parse_single_expr(r"\sin(a) b") == sin(a) * b

        # fractions
        assert self._parse_single_expr(r"\frac{a}{b} c") == a / b * c
        assert self._parse_single_expr(r"c \frac{a}{b}") == a / b * c

        # matricies
        assert self._parse_single_expr(
            r"""
            \begin{bmatrix}
            10 \\
            20
            \end{bmatrix}
            \begin{bmatrix}
            30 &
            40
            \end{bmatrix}
            """
        ) == Matrix([[10], [20]]) * Matrix([[30, 40]])

        assert self._parse_single_expr(
            r"""
            a
            \begin{bmatrix}
            30 &
            40
            \end{bmatrix}
            """
        ) == a * Matrix([[30, 40]])

        assert self._parse_single_expr(
            r"""
            \begin{bmatrix}
            30 &
            40
            \end{bmatrix}
            a
            """
        ) == a * Matrix([[30, 40]])

        # powers
        assert self._parse_single_expr(r"b a^2") == a**2 * b
        assert self._parse_single_expr(r"a^2 b") == a**2 * b

        # scripts
        x1 = symbols("x_{1}")
        assert self._parse_single_expr(r"b x_1") == x1 * b
        assert self._parse_single_expr(r"x_1 b") == x1 * b

        f, x = symbols("f x")

        assert self._parse_single_expr("f (x)") == f * x
        assert self._parse_single_expr("f(x)") == f * x
        assert self._parse_single_expr(
            r"f\left(x\right)", {"definitionsv2": [r"f(x) \mapsto C"]}
        ) == Function("f", complex=True)(x)
        assert self._parse_single_expr(r"f   \left(x\right)") == f * x

    def test_partial_relations(self):
        x, y = symbols("x y")

        assert self._parse_single_expr(r"= 25").rhs == 25
        assert self._parse_single_expr(r"x = ").lhs == x
        assert self._parse_single_expr(r"x =& ").lhs == x
        assert self._parse_single_expr(r"&=& 25").rhs == 25
        # check if normal relations have not broken
        assert self._parse_single_expr(r"x & = & y") == Eq(x, y)

    def test_multi_expressions(self):
        x, y, z = symbols("x y z")

        result = self._parse_expr(
            r"""
            \begin{align}
            x & = 2y 5z \\
            y & = x^2 \\
            z & = x + 2\frac{y}{x} \\
            \end{align}
            """
        )

        assert isinstance(result, CasExpr)
        assert len(result) == 3

        assert result.get_expr(0) == Eq(x, 2 * y * 5 * z)
        assert result.get_location(0).line == 3
        assert result.get_location(0).end_line == 3

        assert result.get_expr(1) == Eq(y, x**2)
        assert result.get_location(1).line == 4
        assert result.get_location(1).end_line == 4

        assert result.get_expr(2) == Eq(z, x + 2 * y / x)
        assert result.get_location(2).line == 5
        assert result.get_location(2).end_line is None

        result = self._parse_expr(
            r"""
            \begin{cases}
            x
            \end{cases}
            """
        )

        assert isinstance(result, CasExpr)
        assert len(result) == 1

        assert result.get_expr(0) == x
        assert result.get_location(0).line == 3

        result = self._parse_expr(
            r"""
            \begin{cases}
            x & = 2y
            \end{cases}
            """
        )

        assert isinstance(result, CasExpr)
        assert len(result) == 1

        assert result.get_expr(0) == Eq(x, 2 * y)
        assert result.get_location(0).line == 3

    def test_matrix_operations(self):
        result = self._parse_single_expr(
            r"A A^\ast",
            {
                "definitionsv2": [
                    r"""
                    A := \begin{bmatrix}
                         1 & 2 \\
                         i & 2 i
                         \end{bmatrix}
                    """
                ]
            },
        )

        assert result.doit() == Matrix([[5, -5 * I], [5 * I, 5]])

    def test_symbols(self):
        s_a = Symbol("variable")
        s_b = Symbol("v")
        s_c = Symbol("a_{1}")
        s_d = Symbol(r"\mathrm{X}")
        s_e = Symbol(r"\pmb{M}_{some label i;j}")
        s_f = Symbol(r"\alpha_{very_{indexed_{variable}}}")

        result = self._parse_single_expr(
            r"variable + v \cdot a_1 + \sqrt{\pmb{M}_{some label i;j}^{\alpha_{very_{indexed_{variable}}}}} + \mathrm{X}^{-1}"
        )

        assert result == s_a + s_b * s_c + sqrt(s_e**s_f) + s_d**-1

    def test_delta_symbols(self):
        delta_v = Symbol(r"\Delta{v}")
        delta_f = Function(r"\Delta{f}", real=True)
        x = Symbol("x")

        result = self._parse_single_expr(
            r"\Delta   f(x) + \Delta v + \Delta       v",
            {"definitionsv2": ["\Delta  f(x) \mapsto R"]},
        )

        assert result == delta_f(x) + 2 * delta_v

    def test_definitions(self):
        result = self._parse_single_expr(r"x", {"definitionsv2": [r"x \in \mathbb{R}"]})
        assert result == symbols("x", real=True)

        x = symbols("x", real=True)
        y = symbols("y", positive=True)
        result = self._parse_single_expr(
            r"a + b",
            {
                "definitionsv2": [
                    r"x \in \mathbbm{R}",
                    r"y \in \mathscr{R}_{+}",
                    r"a := x + y \quad b := y",
                ],
            },
        )

        assert result == x + y + y

        a, b, x, y = symbols("a b x y")

        result = self._parse_single_expr(
            "a + b + x + y",
            {
                "definitionsv2": [
                    r"x := y^2 - z",
                    r"y := 50",
                    r"z := 2 y",
                    r"A := B",
                    r"B := A + z",
                ]
            },
        )

        assert result == a + b + 50**2 - 2 * 50 + 50

        with pytest.raises(CyclicDependencyError):
            result = self._parse_single_expr(
                "A + B + x + y",
                {
                    "definitionsv2": [
                        r"x := y^2 - z",
                        r"y := 50",
                        r"z := 2 y",
                        r"A := B",
                        r"B := A + z",
                    ]
                },
            )

        with pytest.raises(CyclicDependencyError):
            result = self._parse_single_expr(
                "f(1, x)",
                {"definitionsv2": [r"x := y \quad y := x \land f (x, y) := x y"]},
            )

        result = self._parse_single_expr(
            "f(1, 2)",
            {"definitionsv2": [r"x := y \quad y := x \land f (x, y) := x y"]},
        )

        with pytest.raises(CyclicDependencyError):
            result = self._parse_single_expr(
                "f(10)",
                {"definitionsv2": [r"f (x) := g(x)", r"g (x) := f(x)"]},
            )

    def test_brace_units(self):
        import sympy.physics.units as u

        x, a, b = symbols("x a b")

        assert self._parse_single_expr(r"x {atm}") == x * u.atm

        assert (
            self._parse_single_expr(r"{a + b}^2 + {s}^2") == u.second**2 + (a + b) ** 2
        )

        result = self._parse_single_expr(r"{km} + \sin{x} + \frac{a}{{J}} + b")
        assert result == u.km + sin(x) + a / u.joule + b

    @pytest.mark.parametrize(
        "latex,environment,expected_expr",
        [
            # Standard expressions with parentheses notation
            (
                r"\mathbf{H}(x^2 + y^2)",
                {},
                Matrix([[2, 0], [0, 2]]),
            ),
            (
                r"\mathbf{H}(y x^5 + \sin(y))",
                {},
                Matrix([
                    [20 * Symbol("x") ** 3 * Symbol("y"), 5 * Symbol("x") ** 4],
                    [5 * Symbol("x") ** 4, -sin(Symbol("y"))],
                ]),
            ),
            # Indexed notation
            (
                r"\mathbf{H}_{x^2 + y^2}",
                {},
                Matrix([[2, 0], [0, 2]]),
            ),
            # With evaluation point - parentheses notation
            (
                r"\mathbf{H}(x^2 + y^2)(1, 2)",
                {},
                Matrix([[2, 0], [0, 2]]),
            ),
            # With evaluation point - indexed notation
            (
                r"\mathbf{H}_{x^2 + y^2}(0, 0)",
                {},
                Matrix([[2, 0], [0, 2]]),
            ),
            # With function definition - parentheses notation
            (
                r"\mathbf{H}(f)",
                {"definitionsv2": [r"f(x, y, z) := \log(x) + e^y"]},
                Matrix([
                    [-1 / Symbol("x") ** 2, 0, 0],
                    [0, exp(Symbol("y")), 0],
                    [0, 0, 0],
                ]),
            ),
            # With function definition - indexed notation
            (
                r"\mathbf{H}_{f}",
                {"definitionsv2": [r"f(x, y) := x^3 y + y^2"]},
                Matrix([
                    [6 * Symbol("x") * Symbol("y"), 3 * Symbol("x") ** 2],
                    [3 * Symbol("x") ** 2, 2],
                ]),
            ),
            # With function definition and evaluation point
            (
                r"\mathbf{H}(f)(1, 1)",
                {"definitionsv2": [r"f(x, y) := x^3 y + y^2"]},
                Matrix([[6, 3], [3, 2]]),
            ),
        ],
    )
    def test_hessian(self, latex: str, environment: dict, expected_expr: Expr):
        result = self._parse_single_expr(latex, environment)
        assert simplify(result.doit()) == simplify(expected_expr)

    @pytest.mark.parametrize(
        "latex,environment,expected_expr",
        [
            # Standard expressions with parentheses notation
            (
                r"\mathbf{J}(\begin{bmatrix} x + y \\ x \\ y\end{bmatrix})",
                {},
                Matrix([[1, 1], [1, 0], [0, 1]]),
            ),
            (
                r"\mathbf{J}(\begin{bmatrix} x^2 \\ y \\ x * y \end{bmatrix})",
                {},
                Matrix([[2 * Symbol("x"), 0], [0, 1], [Symbol("y"), Symbol("x")]]),
            ),
            # Indexed notation
            (
                r"\mathbf{J}_{\begin{bmatrix} x^2 \\ y^2 \end{bmatrix}}",
                {},
                Matrix([[2 * Symbol("x"), 0], [0, 2 * Symbol("y")]]),
            ),
            # Row vector
            (
                r"\mathbf{J}(\begin{bmatrix} x^2 & y^2 \end{bmatrix})",
                {},
                Matrix([[2 * Symbol("x"), 0], [0, 2 * Symbol("y")]]),
            ),
            # With evaluation point - parentheses notation
            (
                r"\mathbf{J}(\begin{bmatrix} x^2 \\ y \end{bmatrix})(2, 3)",
                {},
                Matrix([[4, 0], [0, 1]]),
            ),
            # With evaluation point - indexed notation
            (
                r"\mathbf{J}_{\begin{bmatrix} x + y \\ x - y \end{bmatrix}}(1, 1)",
                {},
                Matrix([[1, 1], [1, -1]]),
            ),
            # With function definition - parentheses notation
            (
                r"\mathbf{J}(f)",
                {
                    "definitionsv2": [
                        r"f(x, y, z) := \begin{bmatrix}\log(x)\\ \sin(y) \\ \cos(x) * \sin(y) \end{bmatrix}"
                    ]
                },
                Matrix([
                    [1 / Symbol("x"), 0, 0],
                    [0, cos(Symbol("y")), 0],
                    [
                        -sin(Symbol("x")) * sin(Symbol("y")),
                        cos(Symbol("x")) * cos(Symbol("y")),
                        0,
                    ],
                ]),
            ),
            # With function definition - indexed notation
            (
                r"\mathbf{J}_{f}",
                {
                    "definitionsv2": [
                        r"f(x, y) := \begin{bmatrix} x^2 y \\ x + y \end{bmatrix}"
                    ]
                },
                Matrix([[2 * Symbol("x") * Symbol("y"), Symbol("x") ** 2], [1, 1]]),
            ),
            # With function definition and evaluation point
            (
                r"\mathbf{J}(f)(1, 2)",
                {
                    "definitionsv2": [
                        r"f(x, y) := \begin{bmatrix} x y^2 \\ x^2 + y \end{bmatrix}"
                    ]
                },
                Matrix([[4, 4], [2, 1]]),
            ),
        ],
    )
    def test_jacobian(self, latex: str, environment: dict, expected_expr: Expr):
        result = self._parse_single_expr(latex, environment)
        assert simplify(result.doit()) == simplify(expected_expr)

    @pytest.mark.parametrize(
        "latex,environment,expected_expr",
        [
            # Standard expressions with parentheses notation
            (
                r"\nabla(x^2 + y^2)",
                {},
                Matrix([2 * Symbol("x"), 2 * Symbol("y")]),
            ),
            (
                r"\nabla(x^3 y + y^2)",
                {},
                Matrix([
                    3 * Symbol("x") ** 2 * Symbol("y"),
                    Symbol("x") ** 3 + 2 * Symbol("y"),
                ]),
            ),
            (
                r"\grad(x^2 + y^2 + z^2)",
                {},
                Matrix([2 * Symbol("x"), 2 * Symbol("y"), 2 * Symbol("z")]),
            ),
            # Indexed notation
            (
                r"\nabla_{x^2 + y^2}",
                {},
                Matrix([2 * Symbol("x"), 2 * Symbol("y")]),
            ),
            # With evaluation point - parentheses notation
            (
                r"\nabla(x^2 + y^2)(1, 2)",
                {},
                Matrix([2, 4]),
            ),
            # With evaluation point - indexed notation
            (
                r"\nabla_{x^2 + y^2}(2, 3)",
                {},
                Matrix([4, 6]),
            ),
            # With function definition - parentheses notation
            (
                r"\nabla(f)",
                {"definitionsv2": [r"f(x, y) := x^3 + y^2 + \sin(x)"]},
                Matrix([3 * Symbol("x") ** 2 + cos(Symbol("x")), 2 * Symbol("y")]),
            ),
            # With function definition - indexed notation
            (
                r"\nabla_{f}",
                {"definitionsv2": [r"f(x, y) := \log(x) + e^y"]},
                Matrix([1 / Symbol("x"), exp(Symbol("y"))]),
            ),
            # With function definition and evaluation point
            (
                r"\nabla(f)(1, 0)",
                {"definitionsv2": [r"f(x, y) := x^2 y + y^3"]},
                Matrix([0, 1]),
            ),
            # Three-variable function
            (
                r"\grad(f)",
                {"definitionsv2": [r"f(x, y, z) := x^2 + y^2 + z^2"]},
                Matrix([2 * Symbol("x"), 2 * Symbol("y"), 2 * Symbol("z")]),
            ),
            # Complex expression
            (
                r"\nabla(x y z)",
                {},
                Matrix([
                    Symbol("y") * Symbol("z"),
                    Symbol("x") * Symbol("z"),
                    Symbol("x") * Symbol("y"),
                ]),
            ),
        ],
    )
    def test_gradient(self, latex: str, environment: dict, expected_expr: Expr):
        result = self._parse_single_expr(latex, environment)
        assert simplify(result.doit()) == simplify(expected_expr)

    def test_rref(self):
        result = self._parse_single_expr(
            r"\mathrm{rref}(\begin{bmatrix} 20 & 50 \\ 10 & 25\end{bmatrix})"
        )

        assert result == Matrix([[1, Rational(5, 2)], [0, 0]])

    def test_percent_permille(self):
        result = self._parse_single_expr(r"25\% - 5\textperthousand")

        assert abs(result - (0.25 - 0.005)) <= 1e-14  # type: ignore[operator]

    def test_regression_101(self):
        x, y = symbols("x y")

        result = self._parse_single_expr(r"\sin x^2")

        assert result == sin(x**2)

        result = self._parse_single_expr(r"\sin(x)^2")

        assert result == sin(x) ** 2

        result = self._parse_single_expr(r"\log_{10} x^2")
        assert result == log(x**2, 10)

        result = self._parse_single_expr(r"\cos |x|")
        assert result == cos(abs(x))

        result = self._parse_single_expr(r"\sin x \mod y")
        assert result == Mod(sin(x), y)

        result = self._parse_single_expr(r"\log(x)!")
        assert result == factorial(log(x))

        result = self._parse_single_expr(r"\log x!!!")
        assert result == log(factorial(factorial(factorial(x))))

    def test_matrix_bracket_persistance(self):
        result = self._parse_single_expr(
            r"\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}"
        )

        assert isinstance(result, LatexMatrix)
        assert result.env_begin == r"\begin{pmatrix}"
        assert result.env_end == r"\end{pmatrix}"

        result = self._parse_single_expr(
            r"\left\{ \begin{array}{r | c : l} x & y^2 \\ z_3 & \mathrm{uv} \end{array} \right]"
        )

        assert isinstance(result, LatexMatrix)
        assert result.env_begin == r"\left\{ \begin{array}{r | c : l}"
        assert result.env_end == r"\end{array} \right]"

    def test_exception_types(self):
        # unexpected EOF
        with pytest.raises(PrettyParserError):
            self._parse_single_expr(r"\frac{25}{")

        # unexpected token
        with pytest.raises(PrettyParserError):
            self._parse_single_expr(r"\sum_{n}^{5} n")

    def test_text(self):
        result = self._parse_single_expr(r"a + \text{some text} b")

        a, b = symbols("a b")
        assert result == a + b

        result = self._parse_single_expr(
            r"""
            \begin{bmatrix}
            1 & 2 \text{123} \\
            3 & 4
            \end{bmatrix}
            """
        )
        assert result == Matrix([[1, 2], [3, 4]])

        result = self._parse_single_expr(
            r"""
            \sum_{n = 0 \text{some \textbf{nested \textit{text}}} and some not nested \text{text}}^1 n
            """
        )

        n = symbols("n")
        assert result == Sum(n, (n, 0, 1))

    def test_regression_150(self):
        assert self._parse_single_expr(r"a C") == sympify("a * C")
        assert self._parse_single_expr(r"a P") == sympify("a * P")

    def test_series_input_presedence(self):
        j = Symbol("j")
        assert self._parse_single_expr(r"\sum_{j = 0}^\infty (\frac{1}{2})^j") == Sum(
            Rational(1, 2) ** j, (j, 0, oo)
        )
        assert self._parse_single_expr(r"\sum_{j = 0}^\infty (\frac{1}{j})^j") == Sum(
            (1 / j) ** j, (j, 0, oo)
        )
        assert (
            self._parse_single_expr(r"\prod_{j = 0}^\infty 3 \cdot j^3 - j")
            == Product(3 * j**3, (j, 0, oo)) - j
        )

        assert (
            self._parse_single_expr(r"\prod_{j = 0}^\infty (j) j^j")
            == Product(j, (j, 0, oo)) * j**j
        )
        assert (
            self._parse_single_expr(r"\sum_{j = 0}^\infty {3 j} j ^2")
            == Sum(3 * j, (j, 0, oo)) * j**2
        )

    derivative_test_cases = [
        (r"\dv{x} x", Derivative(Symbol("x"), Symbol("x"))),
        (r"\dv[5]{x^7}{x}", Derivative(Symbol("x") ** 7, (Symbol("x"), 5))),
        (r"\dv[5]{x} x^7", Derivative(Symbol("x") ** 7, (Symbol("x"), 5))),
        (
            r"\dv*[3]{x} x^7 + y",
            Derivative(Symbol("x") ** 7, (Symbol("x"), 3)) + Symbol("y"),
        ),
        (
            r"\dv*[3]{x} {x^7 + y}",
            Derivative(Symbol("x") ** 7 + Symbol("y"), (Symbol("x"), 3)),
        ),
        (
            r"\dv[3]{x^5 + y} {x}",
            Derivative(Symbol("x") ** 5 + Symbol("y"), (Symbol("x"), 3)),
        ),
        (
            r"\dv[2]{x^7}{x} y",
            Derivative(Symbol("x") ** 7, (Symbol("x"), 2)) * Symbol("y"),
        ),
    ]

    partial_derivative_test_cases = list(
        map(
            lambda item: (item[0].replace(r"\dv", r"\pdv"), item[1]),
            derivative_test_cases,
        )
    )

    def _assert_compiles_to(self, latex: str, expected_expr: Expr) -> None:
        assert simplify(self._parse_single_expr(latex).doit()) == simplify(
            expected_expr
        )

    @pytest.mark.parametrize(
        "latex,expected_expr",
        derivative_test_cases + partial_derivative_test_cases,
    )
    def test_physics_derivative(self, latex, expected_expr):
        self._assert_compiles_to(latex, expected_expr)

    @pytest.mark.parametrize(
        "latex,expected_expr",
        [
            (r"\varepsilon", Symbol(r"\varepsilon")),
            (r"\va*repsilon", Symbol(r"\va*{r}") * Symbol("epsilon")),
        ],
    )
    def test_regression_192(self, latex, expected_expr):
        self._assert_compiles_to(latex, expected_expr)

    @pytest.mark.parametrize(
        "latex,expected_expr",
        [
            (r"\sin f(x)", sympify("sin(f) * x")),
            (r"\log g(y + z)", sympify("log(g) * (y + z)")),
            (r"\log_5 g(y + z)", sympify("log(g, 5) * (y + z)")),
            (r"\exp h(x^2)", sympify("exp(h) * x^2")),
            (
                r"f(6)! - gee(3)\% + h(1)\textperthousand",
                sympify("720 * f - 0.03 * gee + 0.001 * h"),
            ),
            (
                r"\lim_{x \to 5} f(x)",
                Limit(Symbol("f"), Symbol("x"), 5) * Symbol("x"),
            ),
            (
                r"\Re f(x) + \Im f(x) + \arg f(x) + \operatorname{sgn} f(x)",
                (
                    re(Symbol("f"))
                    + im(Symbol("f"))
                    + arg(Symbol("f"))
                    + sign(Symbol("f"))
                )
                * Symbol("x"),
            ),
            (r"f(x^2)'", sympify("f * 2 * x")),
            (r"\sum_{x=0}^5 f(x)", sympify("f * 15")),
            (r"f(\begin{matrix} 1 & 0 \end{matrix})^T", Symbol("f") * Matrix([1, 0])),
            #
            (r"f(g(h(j(x))))", sympify("f * g * h * j * x")),
            (
                r"\Re g(\sin f(x)^2)!",
                re(Symbol("g")) * factorial(sin(Symbol("f")) * Symbol("x") ** 2),
            ),
        ],
    )
    def test_maybe_applied_implicit_multiplication(
        self, latex: str, expected_expr: Expr
    ):
        self._assert_compiles_to(latex, expected_expr)

    @pytest.mark.parametrize(
        "latex,expected_expr",
        [
            (
                r"a \mod b \mod c \bmod d \bmod f",
                Mod(
                    Mod(Mod(Mod(Symbol("a"), Symbol("b")), Symbol("c")), Symbol("d")),
                    Symbol("f"),
                ),
            )
        ],
    )
    def test_mod_chaining(self, latex: str, expected_expr: Expr):
        self._assert_compiles_to(latex, expected_expr)

    @pytest.mark.parametrize(
        "latex_str,lmat_env,expected_expr",
        [
            (r"a_{b}'", {}, Symbol("a'_{b}")),
            (r"a_{b}", {}, Symbol("a_{b}")),
            (
                r"\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}_{[0]}",
                {},
                1,
            ),
            (r"\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}_{[1,1]}", {}, 4),
            (
                r"\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}_{[,1]}",
                {},
                Matrix([2, 4]),
            ),
            (
                r"\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9\end{bmatrix}_{[..1,1..]}",
                {},
                Matrix([[2, 3]]),
            ),
            (
                r"\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}_{(0;)}",
                {},
                Matrix([[3, 4]]),
            ),
            (r"\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}_{(1;1)}", {}, Matrix([1])),
            (
                r"\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}_{(;1)}",
                {},
                Matrix([1, 3]),
            ),
            (
                r"\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9\end{bmatrix}_{(1..;1)}",
                {},
                Matrix([[1, 3]]),
            ),
            (
                r"\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9\end{bmatrix}_{[1,\ast]}",
                {},
                Matrix([[4, 5, 6]]),
            ),
            (
                r"""\sum_{x=0}^4 \sum_{y=0}^4\begin{bmatrix}
  6  & 7  & 8  & 9  & 10 \\
  12 & 14 & 16 & 18 & 20 \\
  18 & 21 & 24 & 27 & 30 \\
  24 & 28 & 32 & 36 & 40 \\
  30 & 35 & 40 & 45 & 50
\end{bmatrix}_{[y, x]}""",
                {},
                600,
            ),
            (
                r"xf_{[0]}",
                {
                    "definitionsv2": [
                        r"xf := \begin{bmatrix} 2474 & 2574 & 2830 & 3219 & 3429 & 3448 & 3677 & 3872 & 4001 & 4116 \end{bmatrix}"
                    ]
                },
                2474,
            ),
            (
                r"\frac{1}{10} \sum_{j=0}^9 xf_{[j]}",
                {
                    "definitionsv2": [
                        r"xf := \begin{bmatrix} 2474 & 2574 & 2830 & 3219 & 3429 & 3448 & 3677 & 3872 & 4001 & 4116 \end{bmatrix}"
                    ]
                },
                3364,
            ),
        ],
    )
    def test_indexing(
        self, latex_str: str, lmat_env: LmatEnvironment, expected_expr: Expr
    ):
        assert simplify(
            self._parse_single_expr(latex_str, lmat_env)
        ).doit() == simplify(expected_expr)


class TestLatexToLogicCompiler:
    compiler = LatexToLogicCasExprCompiler()
    store_compiler = LatexToLogicDefStoreCompiler()

    def _parse_expr(
        self, expr, environment: LmatEnvironment | Any = LmatEnvironment()
    ) -> CasExpr:
        environment = LmatEnvironment.model_validate(environment)
        return self.compiler.compile(
            expr,
            lmat_env_to_definition_store(environment, self.store_compiler),
        )

    def _parse_single_expr(
        self, expr, environment: LmatEnvironment | Any = LmatEnvironment()
    ) -> Basic:
        return self._parse_expr(expr, environment).get_expr(-1)

    def test_propositions_presedence(self):
        a, b, c, d, e, f, g, h, i = symbols("A B C D E F G H I")

        # test presedence
        result = self._parse_single_expr(
            r"\neg A \odot B \oplus C \bar \vee D \wedge E \overline \wedge F \vee G \implies H \iff I"
        )
        assert simplify(result) == simplify(
            Equivalent(
                Implies(Or(Nand(And(Nor(Xor(Xnor(Not(a), b), c), d), e), f), g), h), i
            )
        )

        result = self._parse_single_expr(
            r"A \iff B \Longleftrightarrow C \longleftrightarrow D \leftrightharpoons E \rightleftharpoons F "
        )
        assert simplify(result) == simplify(Equivalent(a, b, c, d, e, f))

        result = self._parse_single_expr(
            r"A \implies B \to C \Longrightarrow D \longrightarrow E \nRightarrow F \rightarrow G"
        )
        assert simplify(result) == simplify(
            Not(((((a >> b) >> c) >> d) >> e) >> f) >> g
        )

        result = self._parse_single_expr(
            r"A \Longleftarrow B \longleftarrow C \Leftarrow D \leftarrow E"
        )
        assert simplify(result) == simplify((((a << b) << c) << d) << e)

        result = self._parse_single_expr(r"A \vee B")
        assert simplify(result) == simplify(Or(a, b))

        result = self._parse_single_expr(r"A \bar \wedge B \overline \wedge C")
        assert simplify(result) == simplify(Nand(a, b, c))

        result = self._parse_single_expr(r"A \wedge B")
        assert simplify(result) == simplify(And(a, b))

        result = self._parse_single_expr(r"A \bar \vee B \overline \vee C")
        assert simplify(result) == simplify(Nor(a, b, c))

        result = self._parse_single_expr(r"A \oplus B")
        assert simplify(result) == simplify(Xor(a, b))

        result = self._parse_single_expr(r"A \odot B")
        assert simplify(result) == simplify(Xnor(a, b))

        result = self._parse_single_expr(r"\neg A")
        assert simplify(result) == simplify(Not(a))

        result = self._parse_single_expr(r"\mathrm{T} \implies \mathrm{F}")
        assert simplify(result) == simplify(S.true >> S.false)

        result = self._parse_single_expr(r"(A \iff B) \wedge (C \iff D)")
        assert simplify(result) == simplify(And(Equivalent(a, b), Equivalent(c, d)))

        # TODO: this is no longer the respondibility of this part.

    # def test_symbolic_iff(self):
    #     result = self._parse_single_expr(
    #         r"\sqrt{\fracc3} \iff \frac{\sqrt{3}}{3} \sqrt{c}"
    #     )
    #     assert sympify(result)

    #     result = self._parse_single_expr(r"3 \iff 5")
    #     assert not sympify(result)

    #     a = Symbol("A")
    #     result = self._parse_single_expr(r"(c^2 \iff c) \vee A")
    #     assert simplify(result.expr) == a

    def test_proposition_variables(self):
        result = self._parse_single_expr(
            r"P \implies Q",
            {
                "definitionsv2": [
                    r"P := A \land B",
                    r"Q := B \vee A",
                ],
                # "definitions": [
                #     EnvDefinition(name_expr="P", value_expr=r"A \wedge B"),
                #     EnvDefinition(name_expr="Q", value_expr=r"B \vee A"),
                # ],
            },
        )

        a, b = symbols("A B")

        assert simplify(result) == simplify(Implies(And(a, b), Or(b, a)))
