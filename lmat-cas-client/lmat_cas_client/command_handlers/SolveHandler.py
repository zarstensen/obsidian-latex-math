from typing import Any, Generator, Iterable, cast, override

from pydantic import BaseModel
from sympy import *
from sympy.core.relational import Relational
from sympy.solvers.solveset import NonlinearError

from lmat_cas_client.Client import HandlerError
from lmat_cas_client.compiling.Compiler import (
    lmat_env_to_definition_store,
)
from lmat_cas_client.LmatEnvironment import LmatEnvironment
from lmat_cas_client.LmatLatexPrinter import lmat_latex
from lmat_cas_client.math_lib.SymbolUtils import (
    symbol_assumptions_set,
    symbols_variable_order,
)
from lmat_cas_client.math_lib.units import UnitUtils

from .CommandHandler import *


def _split_matrix_eqs(equations: Iterable[Basic]) -> Generator[Basic, None, None]:
    """
    Split every matrix equation (matrix on lhs and rhs) into a series of equations,
    for each element in the matrices.

    Args:
        equations (list[Basic])

    Raises:
        HandlerError

    Yields:
        Basic: new equations generated from equations arg.
    """
    for eq in equations:
        match eq:
            case Relational():
                match cast(Any, eq.lhs), cast(Any, eq.rhs):
                    case MatrixBase() as lhs_mat, MatrixBase() as rhs_mat:
                        if lhs_mat.shape != rhs_mat.shape:
                            raise HandlerError(
                                f"Cannot solve equations with different matrix shapes!\nlhs was {lhs_mat.shape} rhs was {rhs_mat.shape}"
                            )

                        for row in range(lhs_mat.rows):
                            for col in range(rhs_mat.cols):
                                yield type(eq)(lhs_mat[row, col], rhs_mat[row, col])
                    case _:
                        yield eq
            case _:
                yield eq


class SolveMessage(BaseModel):
    expression: str
    symbols: list[str]
    environment: LmatEnvironment


class SolveResult(CommandResult):
    # The maximum number of finite solution to display it as a disjunction of solutions.
    # instead of the set itself.
    MAX_RELATIONAL_FINITE_SOLUTIONS = 5

    def __init__(self, solution: Any, symbols: list[Any]):
        super().__init__()
        self.solution = solution
        self.symbols = symbols

    @override
    def getResponsePayload(self) -> tuple[str, dict]:
        solutions_set = self.solution

        if len(self.symbols) == 1:
            symbols = self.symbols[0]
        else:
            symbols = tuple(self.symbols)

        if (
            isinstance(solutions_set, FiniteSet)
            and len(solutions_set) <= SolveResult.MAX_RELATIONAL_FINITE_SOLUTIONS
        ):
            rel_sol_set = solutions_set.as_relational(symbols)

            if rel_sol_set == false:
                rel_sol_set = EmptySet

            return CommandResult.result(dict(solution_set=lmat_latex(rel_sol_set)))
        else:
            return CommandResult.result(
                dict(
                    solution_set=f"{lmat_latex(symbols)} \\in {lmat_latex(solutions_set)}"
                )
            )


# tries to solve the given latex expression.
# if a symbol is not given, and the expression is multivariate, this mode sends a response with status multivariate_equation,
# along with a list of possible symbols to solve for in its symbols key.
# if successfull its sends a message with status solved, and the result in the result key.
class SolveHandler(CompilingCommandHandler):
    @override
    def handle(self, message: SolveMessage | MessageLike) -> SolveResult:
        message = SolveMessage.model_validate(message)

        definition_store = lmat_env_to_definition_store(
            message.environment, self._def_store_compiler
        )

        equations = list(
            _split_matrix_eqs(
                self._cas_expr_compiler.compile(
                    message.expression, definition_store
                ).get_all_expr()
            )
        )

        # get a list of free symbols, by combining all the equations individual free symbols.
        free_symbols = set(
            symbol for equation in equations for symbol in equation.free_symbols
        )

        if len(free_symbols) == 0:
            raise HandlerError("Cannot solve equation if no free symbols are present.")

        symbols: list[Symbol | None] = [None] * len(message.symbols)

        for free_symbol in free_symbols:
            if str(free_symbol) in message.symbols:
                symbol_index = message.symbols.index(str(free_symbol))
                symbols[symbol_index] = cast(Symbol, free_symbol)

        if None in symbols:
            raise HandlerError(f"No such symbols: {message.symbols}")

        match equations, symbols:
            case [eq], [Symbol() as symb]:
                solution_set = solveset(eq, symb, domain=symbol_assumptions_set(symb))
            case _:
                try:
                    solution_set = linsolve(equations, symbols)
                except NonlinearError:
                    solution_set = nonlinsolve(equations, symbols)

        unit_system = message.environment.unit_system

        # if there is a finite number of solutions, go through each solution, simplify it, and convert units in it.
        if isinstance(solution_set, FiniteSet):
            if unit_system is not None:
                solution_set = FiniteSet(
                    *(
                        UnitUtils.auto_convert(simplify(sol.doit()), unit_system)
                        for sol in solution_set.args
                    )
                )
            else:
                solution_set = FiniteSet(
                    *(
                        UnitUtils.auto_convert(simplify(sol.doit()))
                        for sol in solution_set.args
                    )
                )

        if solution_set == false:
            solution_set = EmptySet

        return SolveResult(solution_set, symbols)


class SolveInfoMessage(BaseModel):
    expression: str
    environment: LmatEnvironment


class SolveInfoResult(CommandResult):
    def __init__(self, symbols, equation_count: int):
        super().__init__()
        self.symbols = symbols
        self.equation_count = equation_count

    @override
    def getResponsePayload(self) -> tuple[str, dict]:
        return CommandResult.result(
            dict(
                required_symbols=self.equation_count,
                available_symbols=[
                    dict(sympy_symbol=str(s), latex_symbol=lmat_latex(s))
                    for s in self.symbols
                ],
            )
        )


# retreive equation info needed for configuring a solution through the solve command.
# returns number of required symbols, and a list of symbols to choose from.
class SolveInfoHandler(CompilingCommandHandler):
    @override
    def handle(self, message: SolveInfoMessage | MessageLike) -> SolveInfoResult:
        message = SolveInfoMessage.model_validate(message)
        definition_store = lmat_env_to_definition_store(
            message.environment, self._def_store_compiler
        )
        equations = list(
            _split_matrix_eqs(
                self._cas_expr_compiler.compile(
                    message.expression, definition_store
                ).get_all_expr()
            )
        )

        # time for a full symbols list, and a default symbols list maybe?
        # or it should be ordered such that the first n symbols are the default symbols.

        symbols = set(
            cast(Symbol, symbol)
            for equation in equations
            for symbol in equation.free_symbols
        )
        ordered_symbols = symbols_variable_order(symbols)

        return SolveInfoResult(symbols=ordered_symbols, equation_count=len(equations))
