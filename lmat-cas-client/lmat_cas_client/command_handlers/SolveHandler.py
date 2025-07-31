from typing import Any, TypedDict, override

from sympy import *
from sympy.solvers.solveset import NonlinearError

from lmat_cas_client.Client import HandlerError
from lmat_cas_client.grammar.LmatEnvDefStore import LmatEnvDefStore
from lmat_cas_client.grammar.SympyParser import SympyParser
from lmat_cas_client.grammar.SystemOfExpr import SystemOfExpr
from lmat_cas_client.LmatEnvironment import LmatEnvironment
from lmat_cas_client.LmatLatexPrinter import lmat_latex
from lmat_cas_client.math_lib import UnitsUtils
from lmat_cas_client.math_lib.SymbolUtils import symbols_variable_order

from .CommandHandler import *


class SolveMessage(TypedDict):
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
    def getResponsePayload(self) -> dict:
        solutions_set = self.solution

        if len(self.symbols) == 1:
            symbols = self.symbols[0]
        else:
            symbols = tuple(self.symbols)

        if isinstance(solutions_set, FiniteSet) and len(solutions_set) <= SolveResult.MAX_RELATIONAL_FINITE_SOLUTIONS:
            return CommandResult.result(dict(solution_set=lmat_latex(solutions_set.as_relational(symbols))))
        else:
            return CommandResult.result(dict(
                solution_set=f"{lmat_latex(symbols)} \\in {lmat_latex(solutions_set)}"
            ))

# tries to solve the given latex expression.
# if a symbol is not given, and the expression is multivariate, this mode sends a response with status multivariate_equation,
# along with a list of possible symbols to solve for in its symbols key.
# if successfull its sends a message with status solved, and the result in the result key.
class SolveHandler(CommandHandler):

    def __init__(self, parser: SympyParser):
        super().__init__()
        self._parser = parser

    @override
    def handle(self, message: SolveMessage) -> SolveResult:
        equations = self._parser.parse(message['expression'],
                                         LmatEnvDefStore(self._parser, message['environment'])
                                         )

        # position information is not needed here,
        # so extract the equations into a tuple, which sympy can work with.
        if isinstance(equations, SystemOfExpr):
            equations = equations.get_all_expr()
        else:
            equations = (equations,)

        # get a list of free symbols, by combining all the equations individual free symbols.
        free_symbols = set(symbol for equation in equations for symbol in equation.free_symbols)

        if len(free_symbols) == 0:
            raise HandlerError("Cannot solve equation if no free symbols are present.")

        domain = S.Complexes

        if 'domain' in message['environment'] and message['environment']['domain'].strip() != "":
            domain = sympify(message['environment']['domain'])

        symbols = [ None ] * len(message['symbols'])

        if len(message['symbols']) != len(equations):
            raise HandlerError("Incorrect number of symbols provided.")

        for free_symbol in free_symbols:
            if str(free_symbol) in message['symbols']:
                symbol_index = message['symbols'].index(str(free_symbol))
                symbols[symbol_index] = free_symbol

        if None in symbols:
            raise HandlerError(f"No such symbols: {message['symbols']}")

        if len(equations) == 1 and len(symbols) == 1: # these two should always have equal lenth.
            solution_set = solveset(equations[0], symbols[0], domain=domain)
        else:
            try:
                solution_set = linsolve(equations, symbols)
            except NonlinearError:
                solution_set = nonlinsolve(equations, symbols)

        unit_system = message['environment'].get('unit_system', None)

        # if there is a finite number of solutions, go through each solution, simplify it, and convert units in it.
        if isinstance(solution_set, FiniteSet):
            if unit_system is not None:
                solution_set = FiniteSet(*(
                    UnitsUtils.auto_convert(simplify(sol.doit()), unit_system)
                    for sol in solution_set.args)
                    )
            else:
                solution_set = FiniteSet(*(
                    UnitsUtils.auto_convert(simplify(sol.doit()))
                    for sol in solution_set.args)
                    )

        return SolveResult(solution_set, symbols)

class SolveInfoMessage(TypedDict):
    expression: str
    environment: LmatEnvironment

class SolveInfoResult(CommandResult):

    def __init__(self, symbols, equation_count: int):
        super().__init__()
        self.symbols = symbols
        self.equation_count = equation_count

    @override
    def getResponsePayload(self) -> dict:

        return CommandResult.result(dict(
            required_symbols = self.equation_count,
            available_symbols = [ dict(sympy_symbol=str(s), latex_symbol=lmat_latex(s)) for s in self.symbols ]
        ))

# retreive equation info needed for configuring a solution through the solve command.
# returns number of required symbols, and a list of symbols to choose from.
class SolveInfoHandler(CommandHandler):
    def __init__(self, parser: SympyParser):
            super().__init__()
            self._parser = parser

    @override
    def handle(self, message: SolveInfoMessage) -> SolveInfoResult:
        equations = self._parser.parse(
                                    message['expression'],
                                    LmatEnvDefStore(self._parser, message['environment'])
                                )

        # ok this is the number of expressions
        if isinstance(equations, SystemOfExpr):
            equations = equations.get_all_expr()
        else:
            equations = (equations,)

        # time for a full symbols list, and a default symbols list maybe?
        # or it should be ordered such that the first n symbols are the default symbols.

        symbols = set(symbol for equation in equations for symbol in equation.free_symbols)
        ordered_symbols = symbols_variable_order(symbols)

        return SolveInfoResult(symbols=ordered_symbols, equation_count=len(equations))
