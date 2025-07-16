from typing import Iterator

import regex
import sympy
from lark import Token, Transformer, v_args
from sympy import *
from sympy.core.numbers import int_valued
from sympy.tensor.array import derive_by_array

from sympy_client.grammar.SympyParser import DefinitionStore


# The FucntionsTransformer holds the implementation of various mathematical function rules,
# defined in the latex math grammar.
@v_args(inline=True)
class FunctionsTransformer(Transformer):

    def __init__(self, definitions_store: DefinitionStore):
        self.__definitions_store = definitions_store

        self._symbols_priority = [
            FunctionsTransformer.__FORMATTED_SYMBOL_REGEX % ("[xyz]",),
            FunctionsTransformer.__FORMATTED_SYMBOL_REGEX % ("[ut]",)
        ]



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
        if self._is_matrix(arg):
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
        return self._ensure_matrix(arg).norm()

    def inner_product(self, lhs: Expr, rhs: Expr) -> Expr:
        return self._ensure_matrix(lhs).dot(self._ensure_matrix(rhs), conjugate_convention='right')

    def determinant(self, exponent: Expr | None, mat: Expr) -> Expr:
        return self._try_raise_exponent(self._ensure_matrix(mat).det(), exponent)

    def trace(self, exponent: Expr | None, mat: Expr) -> Expr:
        return self._try_raise_exponent(self._ensure_matrix(mat).trace(), exponent)

    def adjugate(self, exponent: Expr | None, mat: Expr) -> Expr:
        return self._try_raise_exponent(self._ensure_matrix(mat).adjugate(), exponent)

    def rref(self, exponent: Expr | None, mat: Expr) -> Expr:
        return self._try_raise_exponent(self._ensure_matrix(mat).rref()[0], exponent)

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
        matrix = self._ensure_matrix(body)

        if not matrix.rows == 1 and not matrix.cols == 1:
            raise ShapeError("Jacobian expects a single row or column vector")

        # sympy has a built in jacobian, but it does not have an evaluate option,
        # so we just do it manually here.

        gradients = []

        for item in matrix:
            gradients.append(Matrix([derive_by_array(item, variables)]))

        return self._try_raise_exponent(Matrix.vstack(*gradients), exponent)

    def taylor(self, degree: Expr, expr: Expr, exp_point: Expr | None, *args: Expr):
        # degree must be a positive natural number.
        degree = simplify(degree)

        if not int_valued(degree) or degree < 0:
            raise RuntimeError(
                "Degree of taylor series must be a natural number.\n"
                f"Was [{degree}]"
                )

        # make sure expansion point is a vector of length len(args)
        exp_point = 0 if exp_point is None else simplify(exp_point)

        if not self._is_matrix(exp_point):
            exp_point = (exp_point,) * len(args)
        elif exp_point.shape[0] != 1 and exp_point.shape[1] != 1:
            raise RuntimeError(
                "Expansion point must be a n-dimentional vector.\n"
                f"Was a {exp_point.shape} matrix."
                )
        else:
            exp_point = tuple(exp_point)

        # Make sure all arguments are scalars, or the first argument is a vector
        args = tuple(map(simplify, args))

        if len(args) == 1 and self._is_matrix(args[0]):
            args_mat: MatrixBase = args[0]

            if args_mat.shape[0] != 1 and args_mat.shape[1] != 1:
                raise RuntimeError(
                    "Variables matrix must be a n-dimensional vector.\n"
                    f"Was a {args_mat.shape} matrix."
                )

            args = tuple(map(simplify, args_mat))

        for arg in args:
            if self._is_matrix(arg):
                raise RuntimeError(
                    "All arguments must be scalars.\n"
                    f"Argument [{i}] was [{type(arg)}]"
                    )

        # Make sure dimensions are consistent
        if len(exp_point) != len(args):
            raise RuntimeError(
                "Expansion point and variable count must be equal.\n"
                f"Expansion point dimension: {len(exp_point)}\n"
                f"Variable count: {len(args)}"
                )

        # Now the taylor polynomial is actually computed.
        # See here for reference: https://en.wikipedia.org/wiki/Taylor_series#Taylor_series_in_several_variables
        expr, variables = self._expr_as_function(expr, len(args))

        exp_point_subs = dict()

        for variable, exp_scalar in zip(variables, exp_point):
            exp_point_subs[variable] = exp_scalar

        # start out with building a list of directional derivatives from expr,
        # idx 0 represents derivative order, and idx 1 represents a specific unique derivative of that order.

        taylor_pol_terms: list[list[Expr]] = [ [ expr ] ]

        for _ in range(degree):
            taylor_pol_terms.append([])

            for prev_derivative in taylor_pol_terms[-2]:
                for arg in variables:
                    new_derivative = prev_derivative.diff(arg)
                    taylor_pol_terms[-1].append(new_derivative)

        # now substitute the expansion point into all derivates.
        for diff in taylor_pol_terms:
            for i, d in enumerate(diff):
                diff[i] = d.subs(exp_point_subs)


        # multiply the (x - x_d)^n terms onto the derivatives.
        for i in range(0, degree):
            for j in range(i, degree):
                for k, arg in enumerate(variables):
                    step = len(variables) ** j
                    for l in range(step):
                        taylor_pol_terms[j + 1][k * step + l] *= (arg - exp_point_subs[arg])

        # construct taylor polynomial by scaling each sum row by 1/n! and adding them together.
        taylor_polynomial = taylor_pol_terms[0][0]

        for d in range(degree):
            taylor_polynomial += Rational(1, factorial(d + 1)) * sum(taylor_pol_terms[d + 1])

        # finally substitute the args into the computed taylor polynomial
        args_subs = dict()

        for variable, arg in zip(variables, args):
            args_subs[variable] = arg

        return taylor_polynomial.subs(args_subs)

    # Combinatorial Functions

    def permutations(self, n: Expr, k: Expr):
        return Mul(factorial(n), factorial((n - k)) ** S.NegativeOne)

    def combinations(self, n: Expr, k: Expr):
        return binomial(n, k)

    def derangements(self, n: Expr):
        return (factorial(n) - lowergamma(n + 1, -1)) / E

    # Divisibility Functions

    def gcd(self, a: Expr, b: Expr) -> Expr:
        return gcd(a, b)


    def lcm(self, a: Expr, b: Expr) -> Expr:
        return lcm(a, b)

    def modulo(self, a: Expr, b: Expr) -> Expr:
        return Mod(a, b)

    # Helper Methods

    @v_args(inline=False)
    def list_of_expressions(self, tokens: Iterator[Expr]) -> list[Expr]:
        return list(filter(lambda x: not isinstance(x, Token) or x.type != 'COMMA', tokens))

    # tries to raise arg to the given exponent, exept if it is None,
    # or doing so results in no change to the resulting expression.
    def _try_raise_exponent(self, arg: Expr, exponent: Expr | None) -> Expr:
        if exponent is not None and exponent != 1:
            return pow(arg, exponent)
        else:
            return arg

    def _is_matrix(self, obj: Basic) -> bool:
        return hasattr(obj, "is_Matrix") and obj.is_Matrix

    # If the given object is not a matrix, try to construct a 0d Matrix containing the given value.
    # If it is already a matrix, returns the matrix without modifying it in any way.
    def _ensure_matrix(self, obj: Basic) -> MatrixBase:
        if not self._is_matrix(obj):
            return Matrix([obj])
        return obj

    # Convert the given symbol into a sortable key, prioritizing first the _symbols_priority list, and second Lexicographical ordering.
    def _symbols_key(self, symb: Symbol):
        priority = len(self._symbols_priority)

        symbol_str = str(symb)
        compare_key = symbol_str

        for new_priority, priority_check in enumerate(reversed(self._symbols_priority)):
            match = regex.match(priority_check, symbol_str)

            if match:
                priority = new_priority
                # only the regex groups are used for the compare key,
                # this allwos us to ignore certain irrelevant aspects of the symbol str,
                # such as formatting.
                compare_key = "".join(filter(None, match.groups()))

        return (priority, compare_key)

    # from the given expression, return a function body expression, and a tuple of variables the function body expects.
    # the target_variables parameter can be set to hint the function how many variables should be expected from the expression.
    #
    # If the expression has an entry in the definition store, its function definition body and variables is used.
    # Otherwise the expression itself is used as the body, and the variables are extracted from its free symbols.
    def _expr_as_function(self, expr: Expr, target_variables: int | Range | None = None) -> tuple[Expr, tuple[Symbol]]:

        variables = list(sorted(expr.free_symbols, key=self._symbols_key))

        match target_variables:
            case Range() as target_variable_range:
                variables = variables[:max(target_variable_range)]
            case int() as target_variable_count:
                variables = variables[:target_variable_count]

        body = expr

        if isinstance(expr, Symbol):
            func_def = self.__definitions_store.get_function_definition(
                self.__definitions_store.deserialize_function(
                    str(expr)
                    )
                )

            if func_def is not None:
                variables = func_def.args
                body = func_def.get_body()

        match target_variables:
            case int() as target_variable_count:
                if len(variables) != target_variables:
                    raise RuntimeError(f"Expected {target_variable_count} variables, but only found {len(variables)} ({", ".join(map(str, variables))})")
            case Range() as target_variable_range:
                if len(variables) not in target_variable_range:
                    raise RuntimeError(f"Expected {min(target_variable_range)} - {max(target_variable_range)} variables, but only found {len(variables)} ({", ".join(map(str, variables))})")


        return body, variables

    __FORMATTED_SYMBOL_REGEX = r"(?:\\[^{]*{\s*)?(%s)(?:\s*})?(\s*_{.*})?"
