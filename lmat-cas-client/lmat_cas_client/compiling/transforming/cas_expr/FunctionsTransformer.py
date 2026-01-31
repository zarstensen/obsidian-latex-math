from collections.abc import Iterable
from typing import Any, Iterator, Optional, cast

import sympy
from lark import Token, Transformer, v_args
from lmat_cas_client.compiling.definition.Resolver import (
    DefinitionResolver,
    FunctionResToken,
)
from lmat_cas_client.compiling.transforming.cas_expr.UndefinedAtomsTransformer import (
    BodyStrat,
    LhsStrat,
    RhsStrat,
    SymbolStrat,
)
from lmat_cas_client.compiling.transforming.Ir import ir_strat
from lmat_cas_client.math_lib import Functions, MatrixUtils
from lmat_cas_client.math_lib.SymbolUtils import symbols_variable_order
from sympy import *
from sympy.core.function import UndefinedFunction
from sympy.tensor.array import derive_by_array


def _try_raise_exponent(arg: Expr, exponent: Expr | int | None):
    if exponent is not None and exponent != 1:
        return pow(arg, exponent)
    else:
        return arg


def func_exp(*, exp_pos: int = 1):
    """
    decorator for all rule handlers which handle a function,
    which supports applying an exponentiation, by raising the function head to some power,
    i.e. f^y(x)
    """

    def _decorator(handler):
        def _wrapped(*args: Any, **kwargs: Any):
            assert len(args) > exp_pos
            no_exp_args = list(args)
            exponent = no_exp_args.pop(exp_pos)

            return _try_raise_exponent(handler(*no_exp_args, **kwargs), exponent)

        return _wrapped

    return _decorator


@v_args(inline=True)
class BuiltInFunctionsTransformer(Transformer):
    """
    The FucntionsTransformer holds the implementation of various mathematical function rules,
    defined in the latex math grammar.
    """

    def __init__(self, definition_resolver: DefinitionResolver):
        self.__resolver = definition_resolver

    @ir_strat(arg=LhsStrat)
    def trig_function(
        self, func_token: Token, exponent: Expr | int | None, arg: Expr
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

        return _try_raise_exponent(trig_func(arg), exponent)

    @ir_strat()
    def frac(self, numerator: Expr, denominator: Expr) -> Expr:
        return numerator * denominator**-1

    @ir_strat()
    def binom(self, n: Expr, k: Expr) -> Expr:
        return binomial(n, k)

    @ir_strat()
    def sqrt(self, degree: Expr | None, arg: Expr) -> Expr:
        if degree is None:
            return sqrt(arg)
        else:
            return root(arg, degree)

    @ir_strat()
    def conjugate(self, arg: Expr) -> Expr:
        return conjugate(arg)

    @func_exp(exp_pos=2)
    @ir_strat(arg=LhsStrat)
    def log_implicit_base(self, func_token: Token, arg: Expr) -> Expr:
        log_type = func_token.type
        base = 10 if log_type == "FUNC_LG" else None

        if base is not None:
            log_val = log(arg, base)
        else:
            log_val = log(arg)

        return log_val

    @func_exp(exp_pos=3)
    @ir_strat(arg=LhsStrat)
    def log_explicit_base(self, _func_token: Token, base: Expr, arg: Expr) -> Expr:
        return log(arg, base)

    @ir_strat(arg=LhsStrat)
    def log_explicit_base_exponent_first(
        self, func_token: Token, exponent, base: Expr, arg: Expr
    ) -> Expr:
        return self.log_explicit_base(func_token, base, exponent, arg)

    @func_exp()
    @ir_strat(arg=LhsStrat)
    def exponential(self, arg: Expr) -> Expr:
        return exp(arg)

    @ir_strat(arg=RhsStrat)
    def factorial(self, arg: Expr) -> Expr:
        return factorial(arg)

    @ir_strat(arg=RhsStrat)
    def percent(self, arg: Expr) -> Expr:
        return Mul(arg, 100**-1)

    @ir_strat(arg=RhsStrat)
    def permille(self, arg: Expr) -> Expr:
        return Mul(arg, 1000**-1)

    @ir_strat()
    def upper_gamma(self, s: Expr, x: Expr | int = 0) -> Expr:
        return uppergamma(s, x)

    @ir_strat()
    def lower_gamma(self, s: Expr, x: Expr) -> Expr:
        return lowergamma(s, x)

    @ir_strat(arg=LhsStrat)
    def limit(
        self, symbol: Expr, approach_value: Expr, direction: str | None, arg: Expr
    ) -> Expr:
        # default direction of limits is both positive and negative.
        direction = "+-" if direction is None else direction
        return limit(arg, symbol, approach_value, direction)

    @func_exp()
    @ir_strat(val=LhsStrat)
    def real_part(self, val: Expr) -> Expr:
        return re(val)

    @func_exp()
    @ir_strat(val=LhsStrat)
    def imaginary_part(self, val: Expr) -> Expr:
        return im(val)

    @func_exp()
    @ir_strat(val=LhsStrat)
    def argument(self, val: Expr) -> Expr:
        return arg(val)

    @func_exp()
    @ir_strat(val=LhsStrat)
    def sign(self, val: Expr) -> Expr:
        return sign(val)

    @ir_strat()
    def limit_direction(self, direction_token: Token) -> str:
        return direction_token.value

    @ir_strat()
    def abs(self, arg: Expr) -> Expr:
        # if arg is a matrix, this notation actually means taking its determinant.
        if MatrixUtils.is_matrix(arg):
            return cast(MatrixBase, arg).det()

        return Abs(arg)

    @ir_strat()
    def floor(self, arg: Expr):
        return floor(arg)

    @ir_strat()
    def ceil(self, arg: Expr):
        return ceiling(arg)

    @ir_strat()
    def max(self, args: Iterator[Expr]):
        return Max(*args)

    @ir_strat()
    def min(self, args: Iterator[Expr]):
        return Min(*args)

    @ir_strat(symbol=SymbolStrat)
    def diff_symbol_exponent(self, symbol: Symbol, exponent: Expr | None):
        return (symbol, 1 if exponent is None else exponent)

    @ir_strat()
    def diff_symbol_arg_list(self, *arg_list: tuple[Expr, Expr]):
        return [*arg_list]

    @ir_strat(expr=BodyStrat)
    def derivative_symbols_first(
        self, power: Optional[Expr], symbols: Iterable[tuple[Symbol, int]], expr: Expr
    ):
        exponent_sum = sum(s[1] for s in symbols)

        if power is not None and power != exponent_sum:
            raise ValueError(
                f"Power mismatch in derivative, expected sum of exponents to be {power}, but was {exponent_sum}"
            )

        return diff(expr, *symbols)

    @ir_strat(expr=BodyStrat)
    def derivative_func_first(
        self, power: Optional[Expr], expr: Expr, symbols: Iterable[tuple[Symbol, int]]
    ):
        return self.derivative_symbols_first(power, symbols, expr)

    @ir_strat(expr=BodyStrat, symbol=SymbolStrat)
    def derivative_phys_symbols_first(
        self, power: Optional[Expr], symbol: Symbol, expr: Expr
    ):
        return self.derivative_symbols_first(
            power, [(symbol, int(power) if power is not None else 1)], expr
        )

    @ir_strat(expr=BodyStrat, symbol=SymbolStrat)
    def derivative_phys_func_first(
        self, power: Optional[Expr], expr: Expr, symbol: Symbol
    ):
        return self.derivative_symbols_first(
            power, [(symbol, int(power) if power is not None else 1)], expr
        )

    @ir_strat(expr=(RhsStrat, BodyStrat))
    def derivative_prime(self, expr: Expr, primes: Token):
        body, variables = self._expr_as_function(expr, range(0, 2))

        if len(variables) == 0:
            return S.Zero
        else:
            return diff(body, variables[0], primes.value.count("'"), evaluate=False)

    @ir_strat()
    def integral_no_bounds(self, expr: Expr | int | None, symbol: Expr):
        expr = 1 if expr is None else expr
        return integrate(expr, symbol)

    @ir_strat()
    def integral_lower_bound_first(
        self,
        lower_bound: Expr,
        upper_bound: Expr,
        expr: Expr | int | None,
        symbol: Expr,
    ):
        expr = 1 if expr is None else expr
        return integrate(expr, (symbol, lower_bound, upper_bound))

    @ir_strat()
    def integral_upper_bound_first(
        self, upper_bound: Expr, lower_bound: Expr, expr: Expr | None, symbol: Expr
    ):
        return self.integral_lower_bound_first(lower_bound, upper_bound, expr, symbol)

    # Series Specific Implementations

    @ir_strat()
    def sum_start_iter_first(
        self,
        iter_symbol: Expr,
        _: Token,
        start_iter: Expr,
        end_iter: Expr,
        expression: Expr,
    ) -> Expr:
        return Sum(expression, (iter_symbol, start_iter, end_iter))

    @ir_strat()
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

    @ir_strat()
    def product_start_iter_first(
        self,
        iter_symbol: Expr,
        _: Token,
        start_iter: Expr,
        end_iter: Expr,
        expression: Expr,
    ) -> Expr:
        return Product(expression, (iter_symbol, start_iter, end_iter))

    @ir_strat()
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

    @ir_strat()
    def norm(self, arg: Expr) -> Expr:
        return MatrixUtils.ensure_matrix(arg).norm()

    @ir_strat()
    def inner_product(self, lhs: Expr, rhs: Expr) -> Expr:
        return MatrixUtils.ensure_matrix(lhs).dot(
            MatrixUtils.ensure_matrix(rhs), conjugate_convention="right"
        )

    @func_exp()
    @ir_strat(mat=LhsStrat)
    def determinant(self, mat: Expr) -> Expr:
        return MatrixUtils.ensure_matrix(mat).det()

    @func_exp()
    @ir_strat(mat=LhsStrat)
    def trace(self, mat: Expr) -> Expr:
        return MatrixUtils.ensure_matrix(mat).trace()

    @func_exp()
    @ir_strat(mat=LhsStrat)
    def adjugate(self, mat: Expr) -> Expr:
        return MatrixUtils.ensure_matrix(mat).adjugate()

    @func_exp()
    @ir_strat(mat=LhsStrat)
    def rref(self, mat: Expr) -> Expr:
        return MatrixUtils.ensure_matrix(mat).rref()[0]

    @func_exp()
    @ir_strat(vector=LhsStrat)
    def unitvec(self, vector: Expr) -> Expr:
        return MatrixUtils.ensure_matrix(vector).normalized()

    @ir_strat(mat=RhsStrat)
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

    @func_exp()
    @ir_strat(expr=LhsStrat)
    def gradient(self, expr: Expr, eval_point: None | list[Expr]) -> MatrixBase:
        body, variables = self._expr_as_function(
            expr, len(eval_point) if eval_point is not None else None
        )
        res = Matrix(derive_by_array(body, variables))

        if eval_point:
            return res.subs({v: p for v, p in zip(variables, eval_point)})
        else:
            return res

    @func_exp()
    @ir_strat(expr=LhsStrat)
    def hessian(self, expr: Expr, eval_point: None | list[Expr]) -> Expr:
        body, variables = self._expr_as_function(
            expr, len(eval_point) if eval_point is not None else None
        )
        res = hessian(body, variables)

        if eval_point:
            return res.subs({v: p for v, p in zip(variables, eval_point)})
        else:
            return res

    @func_exp()
    @ir_strat(expr=LhsStrat)
    def jacobian(self, expr: Expr, eval_point: None | list[Expr]) -> Expr:
        body, variables = self._expr_as_function(
            expr, len(eval_point) if eval_point is not None else None
        )
        matrix = MatrixUtils.ensure_matrix(body)

        if not matrix.rows == 1 and not matrix.cols == 1:
            raise ShapeError("Jacobian expects a single row or column vector")

        # sympy has a built in jacobian, but it does not have an evaluate option,
        # so we just do it manually here.

        gradients = []

        for item in matrix:  # type: ignore[attr-defined]
            gradients.append(Matrix([derive_by_array(item, variables)]))

        jacobian = Matrix.vstack(*gradients)

        if eval_point:
            return jacobian.subs({v: p for v, p in zip(variables, eval_point)})
        else:
            return jacobian

    @ir_strat(expr=LhsStrat)
    def taylor(
        self,
        degree: Expr,
        expr: Expr,
        exp_point: Expr | int | None,
        args: Optional[list[Expr]],
    ):
        degree = simplify(degree)

        expr, variables = self._expr_as_function(
            expr, len(args) if args is not None else None
        )

        # make sure expansion point is a tuple
        exp_point = 0 if exp_point is None else simplify(sympify(exp_point))

        if not MatrixUtils.is_matrix(exp_point):
            exp_point_elems = (exp_point,) * len(variables)
        else:
            exp_point_elems = tuple(exp_point)  # type: ignore[arg-type]

        # Make sure all arguments are scalars, or the first argument is a vector
        if args is not None:
            args = list(map(simplify, args))

            if len(args) == 1 and MatrixUtils.is_matrix(args[0]):
                args_mat: MatrixBase = cast(MatrixBase, args[0])

                if args_mat.shape[0] != 1 and args_mat.shape[1] != 1:
                    raise RuntimeError(
                        "Variables matrix must be a n-dimensional vector.\n"
                        f"Was a {args_mat.shape} matrix."
                    )

                args = list(map(simplify, args_mat))  # type: ignore[call-overload]

            for i, arg in enumerate(args):
                if MatrixUtils.is_matrix(arg):
                    raise RuntimeError(
                        f"All arguments must be scalars.\nArgument [{i}] was [{type(arg)}]"
                    )

        return Functions.taylor(
            expr,
            degree,
            variables,
            tuple(args or variables),
            cast(tuple[Expr], exp_point_elems),
        )

    # Combinatorial Functions

    @ir_strat()
    def permutations(self, n: Expr, k: Expr):
        return Functions.permutations(n, k)

    @ir_strat()
    def combinations(self, n: Expr, k: Expr):
        return binomial(n, k)

    @ir_strat()
    def derangements(self, n: Expr):
        return Functions.derangements(n)

    # Divisibility Functions

    @ir_strat()
    def gcd(self, a: Expr, b: Expr) -> Expr:
        return gcd(a, b)

    @ir_strat()
    def lcm(self, a: Expr, b: Expr) -> Expr:
        return lcm(a, b)

    @ir_strat()
    def modulo(self, a: Expr, b: Expr) -> Expr:
        return Mod(a, b)

    # Indexing

    @ir_strat()
    def index_range(self, begin: Optional[Expr], end: Optional[Expr]):
        return slice(begin, end)

    @ir_strat()
    def index_all(self, _token: Optional[Token] = None):
        return slice(None)

    @ir_strat()
    def index_singular(self, index: Expr):
        return index

    @ir_strat()
    def indicies_2d(
        self,
        row_index: Optional[Expr | slice] = None,
        col_index: Optional[Expr | slice] = None,
    ):
        return row_index if row_index is not None else slice(None), (
            col_index if col_index is not None else slice(None)
        )

    @ir_strat()
    def indicies_1d(self, index: Expr | slice):
        return index

    @ir_strat()
    def complement_indexing(
        self,
        index_target: MatrixBase,
        indicies: tuple[Expr | slice, Expr | slice] | Expr | slice,
    ):
        """
        like standard_indexing, but instead of keeping
        elements in the passed RangeIndex objects,
        this rule removes them, and returns the resulting matrix.
        """
        if not MatrixUtils.is_matrix(index_target):
            index_target = Matrix(index_target)

        match indicies:
            case [row_index, col_index]:
                if not isinstance(row_index, slice):
                    row_index = slice(row_index, row_index + 1)

                if not isinstance(col_index, slice):
                    col_index = slice(col_index, col_index + 1)

                if row_index != slice(None):
                    for _ in range(
                        (row_index.stop or index_target.shape[0])
                        - (row_index.start or 0)
                    ):
                        index_target.row_del(row_index.start or 0)

                if col_index != slice(None):
                    for _ in range(
                        (col_index.stop or index_target.shape[1])
                        - (col_index.start or 0)
                    ):
                        index_target.col_del(col_index.start or 0)

                return index_target
            case index:
                assert not isinstance(index, tuple)
                if not isinstance(index, slice):
                    index = slice(index, index + 1)

                return Matrix([
                    *index_target[: index.start or 0],  # type: ignore[misc]
                    *index_target[
                        index.stop or len(index_target) :  # type: ignore[misc]
                    ],
                ])

    @ir_strat()
    def standard_indexing(
        self,
        index_target: MatrixBase,
        indicies: tuple[Expr | slice, Expr | slice] | Expr | slice,
    ):
        """
        Indexes a matrix target using the passed indicies objects.

        if a pair of indicies is passed,
        it is indexed as a 2d matrix.

        if only 1 index is passed, the target is flattened and indexed as such.
        """

        if not MatrixUtils.is_matrix(index_target):
            index_target = Matrix(index_target)

        match indicies:
            case [row_index, col_index]:
                return index_target[
                    row_index,  # type: ignore[misc]
                    col_index,  # type: ignore[misc]
                ]

            case index:
                return index_target[index]  # type: ignore[misc]

    # Helper Methods

    # from the given expression, return a function body expression, and a tuple of variables the function body expects.
    # the target_variables parameter can be set to hint the function how many variables should be expected from the expression.
    #
    # If the expression has an entry in the definition store, its function definition body and variables is used.
    # Otherwise the expression itself is used as the body, and the variables are extracted from its free symbols.
    def _expr_as_function(
        self, expr: Expr, target_variables: int | range | None = None
    ) -> tuple[Expr, tuple[Symbol, ...]]:
        params = None
        body = None

        if isinstance(expr, UndefinedFunction):
            match self.__resolver.get_resolver_token(expr.name):
                case FunctionResToken() as token:
                    body = self.__resolver.resolve_body(token)
                    params = self.__resolver.resolve_params(token)

        if params is None or body is None:
            params = symbols_variable_order(cast(set[Symbol], expr.free_symbols))
            body = expr

            match target_variables:
                case Range() as target_variable_range:
                    params = params[: max(target_variable_range)]
                case int() as target_variable_count:
                    params = params[:target_variable_count]

        # verify result
        match target_variables:
            case int() as target_variable_count:
                if len(params) != target_variable_count:
                    raise RuntimeError(
                        f"Expected {target_variable_count} variables, but only found {len(params)} ({', '.join(map(str, params))})"
                    )
            case Range() as target_variable_range:
                if len(params) not in target_variable_range:
                    raise RuntimeError(
                        f"Expected {min(target_variable_range)} - {max(target_variable_range)} variables, but only found {len(params)} ({', '.join(map(str, params))})"
                    )

        # return result
        return body, tuple(params)
