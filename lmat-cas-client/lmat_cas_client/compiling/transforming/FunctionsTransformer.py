from typing import Iterator

import sympy
from lark import Token, v_args
from sympy import *
from sympy.core.function import UndefinedFunction
from sympy.tensor.array import derive_by_array

from lmat_cas_client.compiling.Definitions import SympyDefinition
from lmat_cas_client.compiling.DefinitionStore import (
    DefinitionStore,
    FunctionDefinition,
)
from lmat_cas_client.compiling.transforming.DefinitionsTransformer import (
    DefinitionsTransformer,
)
from lmat_cas_client.math_lib import Functions, MatrixUtils
from lmat_cas_client.math_lib.SymbolUtils import symbols_variable_order


# The FucntionsTransformer holds the implementation of various mathematical function rules,
# defined in the latex math grammar.
@v_args(inline=True)
class BuiltInFunctionsTransformer(DefinitionsTransformer):

    def __init__(self, definitions_store: DefinitionStore):
        self.__definition_store = definitions_store

    def trig_function(self, func_token: Token, exponent: Expr | None, arg: Expr) -> Expr:
        func_type = func_token.type.replace('FUNC_', '').lower()

        is_inverse = False

        if exponent == -1:
            exponent = 1
            is_inverse = not is_inverse

        if is_inverse:
            if func_type.startswith('a'):
                func_type = func_type[1:]
            else:
                func_type = 'a' + func_type

        # find func name in sympy module, the tokens are named after their sympy equivalents.
        trig_func = getattr(sympy, func_type)

        return self._try_raise_exponent(trig_func(arg), exponent)

    def frac(self, numerator: Expr, denominator: Expr) -> Expr:
        return numerator * denominator**-1

    def binom(self, n: Expr, k: Expr) -> Expr:
        return binomial(n, k)

    def sqrt(self, degree: Expr | None, arg: Expr) -> Expr:
        if degree is None:
            return sqrt(arg)
        else:
            return root(arg, degree)

    def conjugate(self, arg: Expr) -> Expr:
        return conjugate(arg)

    def log_implicit_base(self, func_token: Token, exponent: Expr | None, arg: Expr) -> Expr:
        log_type = func_token.type
        base = 10 if log_type == 'FUNC_LG' else None

        if base is not None:
            log_val = log(arg, base)
        else:
            log_val = log(arg)

        return self._try_raise_exponent(log_val, exponent)

    def log_explicit_base(self, _func_token: Token, base: Expr, exponent: Expr | None, arg: Expr) -> Expr:
        return self._try_raise_exponent(log(arg, base), exponent)

    def log_explicit_base_exponent_first(self, func_token: Token, exponent: Expr | None, base: Expr, arg: Expr) -> Expr:
        return self.log_explicit_base(func_token, base, exponent, arg)

    def exponential(self, exponent: Expr | None, arg: Expr) -> Expr:
        return self._try_raise_exponent(exp(arg), exponent)

    def factorial(self, arg: Expr) -> Expr:
        return factorial(arg)

    def percent(self, arg: Expr) -> Expr:
        return Mul(arg, 100 ** -1)

    def permille(self, arg: Expr) -> Expr:
        return Mul(arg, 1000 ** -1)

    def upper_gamma(self, s: Expr, x: Expr = 0) -> Expr:
        return uppergamma(s, x)

    def lower_gamma(self, s: Expr, x: Expr) -> Expr:
        return lowergamma(s, x)

    def limit(self, symbol: Expr, approach_value: Expr, direction: str | None, arg: Expr) -> Expr:
        # default direction of limits is both positive and negative.
        direction = '+-' if direction is None else direction
        return limit(arg, symbol, approach_value, direction)

    def real_part(self, exponent: Expr | None, val: Expr) -> Expr:
        return self._try_raise_exponent(re(val), exponent)

    def imaginary_part(self, exponent: Expr | None, val: Expr) -> Expr:
        return self._try_raise_exponent(im(val), exponent)

    def argument(self, exponent: Expr | None, val: Expr) -> Expr:
        return self._try_raise_exponent(arg(val), exponent)

    def sign(self, exponent: Expr | None, val: Expr) -> Expr:
        return self._try_raise_exponent(sign(val), exponent)

    def limit_direction(self, direction_token: Token) -> str:
        return direction_token.value

    def abs(self, arg: Expr) -> Expr:
        # if arg is a matrix, this notation actually means taking its determinant.
        if MatrixUtils.is_matrix(arg):
            return arg.det()

        return Abs(arg)

    def floor(self, arg: Expr):
        return floor(arg)

    def ceil(self, arg: Expr):
        return ceiling(arg)

    def max(self, args: Iterator[Expr]):
        return Max(*args)

    def min(self, args: Iterator[Expr]):
        return Min(*args)

    def diff_symbol_exponent(self, symbol, exponent: Expr | None):
        return (symbol, 1 if exponent is None else exponent)

    def diff_symbol_arg_list(self, *arg_list: tuple[Expr, Expr]):
        return [*arg_list]

    def derivative_symbols_first(self, symbols: Iterator[tuple[Expr, Expr]], expr: Expr):
        return diff(expr, *symbols)

    def derivative_func_first(self, expr: Expr, symbols: Iterator[tuple[Expr, Expr]]):
        return self.derivative_symbols_first(symbols, expr)

    def derivative_prime(self, expr: Expr, primes: Token):

        body, variables = self._expr_as_function(expr, range(0, 2))

        if len(variables) == 0:
            return S.Zero
        else:
            return diff(body, variables[0], primes.value.count("'"), evaluate=False)

    def integral_no_bounds(self, expr: Expr | None, symbol: Expr):
        expr = 1 if expr is None else expr
        return integrate(expr, symbol)

    def integral_lower_bound_first(self, lower_bound: Expr, upper_bound: Expr, expr: Expr | None, symbol: Expr):
        expr = 1 if expr is None else expr
        return integrate(expr, (symbol, lower_bound, upper_bound))

    def integral_upper_bound_first(self, upper_bound: Expr, lower_bound: Expr, expr: Expr | None, symbol: Expr):
        return self.integral_lower_bound_first(lower_bound, upper_bound, expr, symbol)

    # Series Specific Implementations

    def sum_start_iter_first(self, iter_symbol: Expr, _: Token, start_iter: Expr, end_iter: Expr, expression: Expr) -> Expr:
        return Sum(expression, (iter_symbol, start_iter, end_iter))

    def sum_end_iter_first(self, end_iter: Expr, iter_symbol: Expr, separator: Token, start_iter: Expr, expression: Expr) -> Expr:
        return self.sum_start_iter_first(iter_symbol, separator, start_iter, end_iter, expression)

    def product_start_iter_first(self, iter_symbol: Expr, _: Token, start_iter: Expr, end_iter: Expr, expression: Expr) -> Expr:
        return Product(expression, (iter_symbol, start_iter, end_iter))

    def product_end_iter_first(self, end_iter: Expr, iter_symbol: Expr, separator: Token, start_iter: Expr, expression: Expr) -> Expr:
        return self.product_start_iter_first(iter_symbol, separator, start_iter, end_iter, expression)


    # Matrix Specific Implementations

    def norm(self, arg: Expr) -> Expr:
        return MatrixUtils.ensure_matrix(arg).norm()

    def inner_product(self, lhs: Expr, rhs: Expr) -> Expr:
        return MatrixUtils.ensure_matrix(lhs).dot(MatrixUtils.ensure_matrix(rhs), conjugate_convention='right')

    def determinant(self, exponent: Expr | None, mat: Expr) -> Expr:
        return self._try_raise_exponent(MatrixUtils.ensure_matrix(mat).det(), exponent)

    def trace(self, exponent: Expr | None, mat: Expr) -> Expr:
        return self._try_raise_exponent(MatrixUtils.ensure_matrix(mat).trace(), exponent)

    def adjugate(self, exponent: Expr | None, mat: Expr) -> Expr:
        return self._try_raise_exponent(MatrixUtils.ensure_matrix(mat).adjugate(), exponent)

    def rref(self, exponent: Expr | None, mat: Expr) -> Expr:
        return self._try_raise_exponent(MatrixUtils.ensure_matrix(mat).rref()[0], exponent)

    def exp_transpose(self, mat: Expr, exponent: Token) -> Expr:
        exponents_str = exponent.value
        exponents_str = exponents_str.replace('{', '').replace('}', '').replace('\\ast', 'H').replace('*', 'H').replace('\\prime', 'T').replace("'", 'T').replace(' ', '')

        for e in exponents_str:
            if e == 'T':
                mat = mat.transpose()
            elif e == 'H':
                mat = mat.adjoint()
            else:
                raise RuntimeError(f"Unexpected exponent: {e}")

        return mat

    # Linear Alg Specific Implementations

    def gradient(self, exponent: Expr | None, expr: Expr) -> Expr:
        body, variables = self._expr_as_function(expr)
        return self._try_raise_exponent(Matrix(derive_by_array(body, variables)), exponent)

    def hessian(self, exponent: Expr | None, expr: Expr) -> Expr:
        body, variables = self._expr_as_function(expr)
        return self._try_raise_exponent(hessian(body, variables), exponent)

    def jacobian(self, exponent: Expr | None, expr: Expr) -> Expr:
        body, variables = self._expr_as_function(expr)
        matrix = MatrixUtils.ensure_matrix(body)

        if not matrix.rows == 1 and not matrix.cols == 1:
            raise ShapeError("Jacobian expects a single row or column vector")

        # sympy has a built in jacobian, but it does not have an evaluate option,
        # so we just do it manually here.

        gradients = []

        for item in matrix:
            gradients.append(Matrix([derive_by_array(item, variables)]))

        return self._try_raise_exponent(Matrix.vstack(*gradients), exponent)

    def taylor(self, degree: Expr, expr: Expr, exp_point: Expr | None, *args: Expr):
        degree = simplify(degree)

        # make sure expansion point is a tuple
        exp_point = 0 if exp_point is None else simplify(exp_point)

        if not MatrixUtils.is_matrix(exp_point):
            exp_point = (exp_point,) * len(args)
        else:
            exp_point = tuple(exp_point)

        # Make sure all arguments are scalars, or the first argument is a vector
        args = tuple(map(simplify, args))

        if len(args) == 1 and MatrixUtils.is_matrix(args[0]):
            args_mat: MatrixBase = args[0]

            if args_mat.shape[0] != 1 and args_mat.shape[1] != 1:
                raise RuntimeError(
                    "Variables matrix must be a n-dimensional vector.\n"
                    f"Was a {args_mat.shape} matrix."
                )

            args = tuple(map(simplify, args_mat))

        for i, arg in enumerate(args):
            if MatrixUtils.is_matrix(arg):
                raise RuntimeError(
                    "All arguments must be scalars.\n"
                    f"Argument [{i}] was [{type(arg)}]"
                    )

        expr, variables = self._expr_as_function(expr, len(args))

        return Functions.taylor(expr, degree, variables, args, exp_point)

    # Combinatorial Functions

    def permutations(self, n: Expr, k: Expr):
        return Functions.permutations(n, k)

    def combinations(self, n: Expr, k: Expr):
        return binomial(n, k)

    def derangements(self, n: Expr):
        return Functions.derangements(n)

    # Divisibility Functions

    def gcd(self, a: Expr, b: Expr) -> Expr:
        return gcd(a, b)


    def lcm(self, a: Expr, b: Expr) -> Expr:
        return lcm(a, b)

    def modulo(self, a: Expr, b: Expr) -> Expr:
        return Mod(a, b)

    # Helper Methods

    # tries to raise arg to the given exponent, exept if it is None,
    # or doing so results in no change to the resulting expression.
    def _try_raise_exponent(self, arg: Expr, exponent: Expr | None) -> Expr:
        if exponent is not None and exponent != 1:
            return pow(arg, exponent)
        else:
            return arg

    # from the given expression, return a function body expression, and a tuple of variables the function body expects.
    # the target_variables parameter can be set to hint the function how many variables should be expected from the expression.
    #
    # If the expression has an entry in the definition store, its function definition body and variables is used.
    # Otherwise the expression itself is used as the body, and the variables are extracted from its free symbols.
    def _expr_as_function(self, expr: Expr, target_variables: int | Range | None = None) -> tuple[Expr, tuple[Symbol]]:

        variables = None
        body = None

        if isinstance(expr, UndefinedFunction):
            func_def: FunctionDefinition = self.__definition_store.get_definition(expr.name)

            if isinstance(func_def, FunctionDefinition):
                variables = [
                                self.__definition_store.get_definition(
                                        var_name,
                                        default=SympyDefinition(Symbol(var_name))
                                    ).defined_value(self.__definition_store)
                                for var_name in func_def.variables
                            ]

                body = func_def.applied_value(self.__definition_store)

        if variables is None or body is None:
            variables = symbols_variable_order(expr.free_symbols)
            body = expr

            match target_variables:
                case Range() as target_variable_range:
                    variables = variables[:max(target_variable_range)]
                case int() as target_variable_count:
                    variables = variables[:target_variable_count]

        # verify result
        match target_variables:
            case int() as target_variable_count:
                if len(variables) != target_variables:
                    raise RuntimeError(f"Expected {target_variable_count} variables, but only found {len(variables)} ({", ".join(map(str, variables))})")
            case Range() as target_variable_range:
                if len(variables) not in target_variable_range:
                    raise RuntimeError(f"Expected {min(target_variable_range)} - {max(target_variable_range)} variables, but only found {len(variables)} ({", ".join(map(str, variables))})")


        # return result
        return body, variables
