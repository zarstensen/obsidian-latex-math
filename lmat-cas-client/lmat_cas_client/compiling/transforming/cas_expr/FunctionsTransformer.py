from enum import Enum
from typing import Any, Iterator, Optional

import sympy
from lark import Token, Transformer, v_args
from lmat_cas_client.compiling.definition.Resolver import (
    DefinitionResolver,
    FunctionResToken,
)
from lmat_cas_client.compiling.transforming.cas_expr.UndefinedAtomsTransformer import (
    ImplicitMul,
)
from lmat_cas_client.math_lib import Functions, MatrixUtils
from lmat_cas_client.math_lib.SymbolUtils import symbols_variable_order
from sympy import *
from sympy.core.function import UndefinedFunction
from sympy.tensor.array import derive_by_array


class ImplicitMulStrategy(Enum):
    """
    What strategy to use when an ImplicitMul class is recieved.
    """

    LHS = 0
    """
    Indicates the current rule handler should perform work
    on the left hand side (lhs) of the implicit multiplication,
    e.g. sin should use this, as the sin in \sin f(x) should be applied to
    f and not (x)
    """
    RHS = 1
    """
    Like LHS, but indicate that the right hand side shoul be used
    instead (rhs). e.g. f(x)! should use this, as ! should be applied
    to (x) and not f.
    """
    MULT = 2
    """
    Indicate that the current rule handler should apply the implicit multiplication,
    and then work with the result.
    """


def implicit_mul_strategy(strategy: ImplicitMulStrategy):
    """
    Use this decorator for any rule handlers which may receive ImplicitMul structs.
    Depending on the chosen strategy, the relevant parts of ImplicitMul is automatically
    passed to the rule handler, and an appropiate ImplicitMul object is constructed and
    returned from the rule handlers result.
    Note that at most 1 arg can be an ImplicitMul if the LHS or RHS strategy is picked.
    """

    def _decorator(handler):
        def _wrapped(*args: Any):
            new_args = []
            had_failed_apply = False

            # search for an ImplicitMul in args, if found
            # substitute in lhs, rhs or implicit mul of both, depending on
            # chosen strategy.
            for arg in args:
                match arg:
                    case ImplicitMul(lhs, rhs):
                        assert (
                            not had_failed_apply or strategy == ImplicitMulStrategy.MULT
                        )
                        match strategy:
                            case ImplicitMulStrategy.LHS:
                                new_args.append(lhs)
                            case ImplicitMulStrategy.RHS:
                                new_args.append(rhs)
                            case ImplicitMulStrategy.MULT:
                                new_args.append(lhs * rhs)
                        had_failed_apply = True
                    case arg:
                        new_args.append(arg)

            # return result wrapped in an ImplicitMul for further bubbling up.
            if had_failed_apply and strategy != ImplicitMulStrategy.MULT:
                match strategy:
                    case ImplicitMulStrategy.LHS:
                        return ImplicitMul(handler(*new_args), rhs)
                    case ImplicitMulStrategy.RHS:
                        return ImplicitMul(lhs, handler(*new_args))
            else:
                # except if we aplied the ImplicitMul
                return handler(*new_args)

        return _wrapped

    return _decorator


@v_args(inline=True)
class BuiltInFunctionsTransformer(Transformer):
    """
    The FucntionsTransformer holds the implementation of various mathematical function rules,
    defined in the latex math grammar.
    """

    def __init__(self, definition_resolver: DefinitionResolver):
        self.__definition_resolver = definition_resolver

    @implicit_mul_strategy(ImplicitMulStrategy.LHS)
    def trig_function(
        self, func_token: Token, exponent: Expr | None, arg: Expr
    ) -> Expr:
        func_type = func_token.type.replace("FUNC_", "").lower()

        is_inverse = False

        if exponent == -1:
            exponent = 1
            is_inverse = not is_inverse

        if is_inverse:
            if func_type.startswith("a"):
                func_type = func_type[1:]
            else:
                func_type = "a" + func_type

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

    @implicit_mul_strategy(ImplicitMulStrategy.LHS)
    def log_implicit_base(
        self, func_token: Token, exponent: Expr | None, arg: Expr
    ) -> Expr:
        log_type = func_token.type
        base = 10 if log_type == "FUNC_LG" else None

        if base is not None:
            log_val = log(arg, base)
        else:
            log_val = log(arg)

        return self._try_raise_exponent(log_val, exponent)

    @implicit_mul_strategy(ImplicitMulStrategy.LHS)
    def log_explicit_base(
        self, _func_token: Token, base: Expr, exponent: Expr | None, arg: Expr
    ) -> Expr:
        return self._try_raise_exponent(log(arg, base), exponent)

    @implicit_mul_strategy(ImplicitMulStrategy.LHS)
    def log_explicit_base_exponent_first(
        self, func_token: Token, exponent: Expr | None, base: Expr, arg: Expr
    ) -> Expr:
        return self.log_explicit_base(func_token, base, exponent, arg)

    @implicit_mul_strategy(ImplicitMulStrategy.LHS)
    def exponential(self, exponent: Expr | None, arg: Expr) -> Expr:
        return self._try_raise_exponent(exp(arg), exponent)

    @implicit_mul_strategy(ImplicitMulStrategy.RHS)
    def factorial(self, arg: Expr) -> Expr:
        return factorial(arg)

    @implicit_mul_strategy(ImplicitMulStrategy.RHS)
    def percent(self, arg: Expr) -> Expr:
        return Mul(arg, 100**-1)

    @implicit_mul_strategy(ImplicitMulStrategy.RHS)
    def permille(self, arg: Expr) -> Expr:
        return Mul(arg, 1000**-1)

    def upper_gamma(self, s: Expr, x: Expr = 0) -> Expr:
        return uppergamma(s, x)

    def lower_gamma(self, s: Expr, x: Expr) -> Expr:
        return lowergamma(s, x)

    @implicit_mul_strategy(ImplicitMulStrategy.LHS)
    def limit(
        self, symbol: Expr, approach_value: Expr, direction: str | None, arg: Expr
    ) -> Expr:
        # default direction of limits is both positive and negative.
        direction = "+-" if direction is None else direction
        return limit(arg, symbol, approach_value, direction)

    @implicit_mul_strategy(ImplicitMulStrategy.LHS)
    def real_part(self, exponent: Expr | None, val: Expr) -> Expr:
        return self._try_raise_exponent(re(val), exponent)

    @implicit_mul_strategy(ImplicitMulStrategy.LHS)
    def imaginary_part(self, exponent: Expr | None, val: Expr) -> Expr:
        return self._try_raise_exponent(im(val), exponent)

    @implicit_mul_strategy(ImplicitMulStrategy.LHS)
    def argument(self, exponent: Expr | None, val: Expr) -> Expr:
        return self._try_raise_exponent(arg(val), exponent)

    @implicit_mul_strategy(ImplicitMulStrategy.LHS)
    def sign(self, exponent: Expr | None, val: Expr) -> Expr:
        return self._try_raise_exponent(sign(val), exponent)

    def limit_direction(self, direction_token: Token) -> str:
        return direction_token.value

    @implicit_mul_strategy(ImplicitMulStrategy.MULT)
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

    def derivative_symbols_first(
        self, power: Optional[Expr], symbols: Iterator[tuple[Symbol, int]], expr: Expr
    ):
        exponent_sum = sum(s[1] for s in symbols)

        if power is not None and power != exponent_sum:
            raise ValueError(
                f"Power mismatch in derivative, expected sum of exponents to be {power}, but was {exponent_sum}"
            )

        return diff(expr, *symbols)

    def derivative_func_first(
        self, power: Optional[Expr], expr: Expr, symbols: Iterator[tuple[Expr, Expr]]
    ):
        return self.derivative_symbols_first(power, symbols, expr)

    def derivative_phys_symbols_first(
        self, power: Optional[Expr], symbol: Expr, expr: Expr
    ):
        return self.derivative_symbols_first(
            power, [(symbol, power if power is not None else 1)], expr
        )

    def derivative_phys_func_first(
        self, power: Optional[Expr], expr: Expr, symbol: Expr
    ):
        return self.derivative_symbols_first(
            power, [(symbol, power if power is not None else 1)], expr
        )

    @implicit_mul_strategy(ImplicitMulStrategy.RHS)
    def derivative_prime(self, expr: Expr, primes: Token):
        body, variables = self._expr_as_function(expr, range(0, 2))

        if len(variables) == 0:
            return S.Zero
        else:
            return diff(body, variables[0], primes.value.count("'"), evaluate=False)

    def integral_no_bounds(self, expr: Expr | None, symbol: Expr):
        expr = 1 if expr is None else expr
        return integrate(expr, symbol)

    def integral_lower_bound_first(
        self, lower_bound: Expr, upper_bound: Expr, expr: Expr | None, symbol: Expr
    ):
        expr = 1 if expr is None else expr
        return integrate(expr, (symbol, lower_bound, upper_bound))

    def integral_upper_bound_first(
        self, upper_bound: Expr, lower_bound: Expr, expr: Expr | None, symbol: Expr
    ):
        return self.integral_lower_bound_first(lower_bound, upper_bound, expr, symbol)

    # Series Specific Implementations

    def sum_start_iter_first(
        self,
        iter_symbol: Expr,
        _: Token,
        start_iter: Expr,
        end_iter: Expr,
        expression: Expr,
    ) -> Expr:
        return Sum(expression, (iter_symbol, start_iter, end_iter))

    def sum_end_iter_first(
        self,
        end_iter: Expr,
        iter_symbol: Expr,
        separator: Token,
        start_iter: Expr,
        expression: Expr,
    ) -> Expr:
        return self.sum_start_iter_first(
            iter_symbol, separator, start_iter, end_iter, expression
        )

    def product_start_iter_first(
        self,
        iter_symbol: Expr,
        _: Token,
        start_iter: Expr,
        end_iter: Expr,
        expression: Expr,
    ) -> Expr:
        return Product(expression, (iter_symbol, start_iter, end_iter))

    def product_end_iter_first(
        self,
        end_iter: Expr,
        iter_symbol: Expr,
        separator: Token,
        start_iter: Expr,
        expression: Expr,
    ) -> Expr:
        return self.product_start_iter_first(
            iter_symbol, separator, start_iter, end_iter, expression
        )

    # Matrix Specific Implementations

    def norm(self, arg: Expr) -> Expr:
        return MatrixUtils.ensure_matrix(arg).norm()

    def inner_product(self, lhs: Expr, rhs: Expr) -> Expr:
        return MatrixUtils.ensure_matrix(lhs).dot(
            MatrixUtils.ensure_matrix(rhs), conjugate_convention="right"
        )

    @implicit_mul_strategy(ImplicitMulStrategy.LHS)
    def determinant(self, exponent: Expr | None, mat: Expr) -> Expr:
        return self._try_raise_exponent(MatrixUtils.ensure_matrix(mat).det(), exponent)

    @implicit_mul_strategy(ImplicitMulStrategy.LHS)
    def trace(self, exponent: Expr | None, mat: Expr) -> Expr:
        return self._try_raise_exponent(
            MatrixUtils.ensure_matrix(mat).trace(), exponent
        )

    @implicit_mul_strategy(ImplicitMulStrategy.LHS)
    def adjugate(self, exponent: Expr | None, mat: Expr) -> Expr:
        return self._try_raise_exponent(
            MatrixUtils.ensure_matrix(mat).adjugate(), exponent
        )

    @implicit_mul_strategy(ImplicitMulStrategy.LHS)
    def rref(self, exponent: Expr | None, mat: Expr) -> Expr:
        return self._try_raise_exponent(
            MatrixUtils.ensure_matrix(mat).rref()[0], exponent
        )

    @implicit_mul_strategy(ImplicitMulStrategy.LHS)
    def unitvec(self, exponent: Expr | None, vector: Expr) -> Expr:
        return self._try_raise_exponent(
            MatrixUtils.ensure_matrix(vector).normalized(), exponent
        )

    @implicit_mul_strategy(ImplicitMulStrategy.RHS)
    def exp_transpose(self, mat: Expr, exponent: Token) -> Expr:
        exponents_str = exponent.value
        exponents_str = (
            exponents_str
            .replace("{", "")
            .replace("}", "")
            .replace("\\ast", "H")
            .replace("*", "H")
            .replace("\\prime", "T")
            .replace("'", "T")
            .replace(" ", "")
        )

        for e in exponents_str:
            if e == "T":
                mat = mat.transpose()
            elif e == "H":
                mat = mat.adjoint()
            else:
                raise RuntimeError(f"Unexpected exponent: {e}")

        return mat

    # Linear Alg Specific Implementations

    @implicit_mul_strategy(ImplicitMulStrategy.LHS)
    def gradient(self, exponent: Expr | None, expr: Expr) -> Expr:
        body, variables = self._expr_as_function(expr)
        return self._try_raise_exponent(
            Matrix(derive_by_array(body, variables)), exponent
        )

    @implicit_mul_strategy(ImplicitMulStrategy.LHS)
    def hessian(self, exponent: Expr | None, expr: Expr) -> Expr:
        body, variables = self._expr_as_function(expr)
        return self._try_raise_exponent(hessian(body, variables), exponent)

    @implicit_mul_strategy(ImplicitMulStrategy.LHS)
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

    @implicit_mul_strategy(ImplicitMulStrategy.LHS)
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
                    f"All arguments must be scalars.\nArgument [{i}] was [{type(arg)}]"
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

    @implicit_mul_strategy(ImplicitMulStrategy.MULT)
    def modulo(self, a: Expr, b: Expr) -> Expr:
        return Mod(a, b)

    # Helper Methods

    # tries to raise arg to the given exponent, except if it is None,
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
    def _expr_as_function(
        self, expr: Expr, target_variables: int | Range | None = None
    ) -> tuple[Expr, tuple[Symbol]]:
        params = None
        body = None

        if isinstance(expr, UndefinedFunction):
            match self.__definition_resolver.get_resolver_token(expr.name):
                case FunctionResToken() as token:
                    body = self.__definition_resolver.resolve_body(token)
                    params = self.__definition_resolver.resolve_params(token)

        if params is None or body is None:
            params = symbols_variable_order(expr.free_symbols)
            body = expr

            match target_variables:
                case Range() as target_variable_range:
                    params = params[: max(target_variable_range)]
                case int() as target_variable_count:
                    params = params[:target_variable_count]

        # verify result
        match target_variables:
            case int() as target_variable_count:
                if len(params) != target_variables:
                    raise RuntimeError(
                        f"Expected {target_variable_count} variables, but only found {len(params)} ({', '.join(map(str, params))})"
                    )
            case Range() as target_variable_range:
                if len(params) not in target_variable_range:
                    raise RuntimeError(
                        f"Expected {min(target_variable_range)} - {max(target_variable_range)} variables, but only found {len(params)} ({', '.join(map(str, params))})"
                    )

        # return result
        return body, params
