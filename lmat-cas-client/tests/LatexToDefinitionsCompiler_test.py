# mypy: disable-error-code="union-attr"
from lmat_cas_client.compiling.Compiler import (
    LatexToDefStoreCompiler,
    LatexToLogicDefStoreCompiler,
)
from lmat_cas_client.compiling.definition.DefinitionStore import (
    FunctionDefinition,
    SymbolDefinition,
)
from lmat_cas_client.compiling.definition.EmptyResolver import EmptyResolver
from lmat_cas_client.compiling.transforming.cas_expr.CasExprTransformer import (
    cas_expr_transformer_runner,
)
from sympy import Function, Symbol, sympify


class TestLatexToDefinitionCompiler:
    compiler = LatexToDefStoreCompiler()
    logic_compiler = LatexToLogicDefStoreCompiler()

    def test_symbol_defs(self):
        result = self.compiler.compile(
            r"""
            a := b + c
            """,
        )

        assert len(result) == 1
        assert isinstance(result["a"], SymbolDefinition)
        assert cas_expr_transformer_runner.transform(
            result["a"].value.ast, EmptyResolver()
        ).get_expr(-1) == sympify("b + c")

    def test_assumption_defs(self):
        from sympy import Symbol

        # Complex
        result = self.compiler.compile(r"x \in \mathbb{C}")
        assert len(result) == 1
        assert isinstance(result["x"], SymbolDefinition)
        assert result["x"].value.expr == Symbol("x", complex=True)

        # Algebraic Number
        result = self.compiler.compile(r"x \in \overline{\mathbb{Q}}")
        assert len(result) == 1
        assert isinstance(result["x"], SymbolDefinition)
        assert result["x"].value.expr == Symbol("x", algebraic=True)

        # Extended real
        result = self.compiler.compile(r"x \in \overline{\mathbb{R}}")
        assert len(result) == 1
        assert isinstance(result["x"], SymbolDefinition)
        assert result["x"].value.expr == Symbol("x", extended_real=True)

        # Real
        result = self.compiler.compile(r"x \in \mathbb{R}")
        assert len(result) == 1
        assert isinstance(result["x"], SymbolDefinition)
        assert result["x"].value.expr == Symbol("x", real=True)

        # Imaginary
        result = self.compiler.compile(r"x \in \mathbb{I}")
        assert len(result) == 1
        assert isinstance(result["x"], SymbolDefinition)
        assert result["x"].value.expr == Symbol("x", imaginary=True)

        # Rational
        result = self.compiler.compile(r"x \in \mathbb{Q}")
        assert len(result) == 1
        assert isinstance(result["x"], SymbolDefinition)
        assert result["x"].value.expr == Symbol("x", rational=True)
        # Integer
        result = self.compiler.compile(r"x \in \mathbb{Z}")
        assert len(result) == 1
        assert isinstance(result["x"], SymbolDefinition)
        assert result["x"].value.expr == Symbol("x", integer=True)

        # Even
        result = self.compiler.compile(r"x \in \mathbb{E}")
        assert len(result) == 1
        assert isinstance(result["x"], SymbolDefinition)
        assert result["x"].value.expr == Symbol("x", even=True)

        # Odd
        result = self.compiler.compile(r"x \in \mathbb{O}")
        assert len(result) == 1
        assert isinstance(result["x"], SymbolDefinition)
        assert result["x"].value.expr == Symbol("x", odd=True)

        # Prime
        result = self.compiler.compile(r"x \in \mathbb{P}")
        assert len(result) == 1
        assert isinstance(result["x"], SymbolDefinition)
        assert result["x"].value.expr == Symbol("x", prime=True)

        # Positive (two notations)
        result = self.compiler.compile(r"x \in \mathbb{R}_{+}")
        assert len(result) == 1
        assert isinstance(result["x"], SymbolDefinition)
        assert result["x"].value.expr == Symbol("x", positive=True)

        result = self.compiler.compile(r"x \in \mathbb{R}_{>0}")
        assert len(result) == 1
        assert isinstance(result["x"], SymbolDefinition)
        assert result["x"].value.expr == Symbol("x", positive=True)

        # Nonnegative
        result = self.compiler.compile(r"x \in \mathbb{R}_{\geq 0}")
        assert len(result) == 1
        assert isinstance(result["x"], SymbolDefinition)
        assert result["x"].value.expr == Symbol("x", nonnegative=True)

        # Negative (two notations)
        result = self.compiler.compile(r"x \in \mathbb{R}_{-}")
        assert len(result) == 1
        assert isinstance(result["x"], SymbolDefinition)
        assert result["x"].value.expr == Symbol("x", negative=True)

        result = self.compiler.compile(r"x \in \mathbb{R}_{<0}")
        assert len(result) == 1
        assert isinstance(result["x"], SymbolDefinition)
        assert result["x"].value.expr == Symbol("x", negative=True)

        # Nonpositive
        result = self.compiler.compile(r"x \in \mathbb{R}_{\leq 0}")
        assert len(result) == 1
        assert isinstance(result["x"], SymbolDefinition)
        assert result["x"].value.expr == Symbol("x", nonpositive=True)

    def test_multi_symb_assumption(self):
        result = self.compiler.compile(r"x, y, z \in \mathbb{P}")

        assert len(result) == 3
        assert result["x"].value.expr == Symbol("x", prime=True)
        assert result["y"].value.expr == Symbol("y", prime=True)
        assert result["z"].value.expr == Symbol("z", prime=True)

    def test_function_def(self):
        result = self.compiler.compile(r"f(x) := x^3")

        assert len(result) == 1
        assert isinstance(result["f"], FunctionDefinition)
        assert result["f"].params == ("x",)
        assert result["f"].value.unapplied == Function("f")

        result = self.compiler.compile(r"g (x, y, zet) := x + y + zet + c")

        assert len(result) == 1
        assert isinstance(result["g"], FunctionDefinition)
        assert result["g"].params == ("x", "y", "zet")
        assert result["g"].value.unapplied == Function("g")

    def test_function_assumption(self):
        result = self.compiler.compile(r"f (x) \mapsto \mathbbm{R}")

        assert len(result) == 1
        assert isinstance(result["f"], FunctionDefinition)
        assert result["f"].params == ("x",)
        assert result["f"].value.undef_fun == Function("f", real=True)

    def test_multiple_definitions(self):
        result = self.compiler.compile(
            r"x := 2 y \cdot 5 \quad z \in \mathbbm{R} \land z (x) := C"
        )

        assert len(result) == 2
        assert isinstance(result["x"], SymbolDefinition)
        assert isinstance(result["z"], FunctionDefinition)

    def test_logic_definitions(self):
        result = self.logic_compiler.compile(r"A := B \lor C \land D")

        assert len(result) == 1
        assert isinstance(result["A"], SymbolDefinition)
