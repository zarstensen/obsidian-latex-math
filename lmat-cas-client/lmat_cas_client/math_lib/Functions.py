# This file contains all sorts of additional math related functions not implemented by sympy.

from itertools import combinations

from sympy import *
from sympy.core.numbers import int_valued
from sympy.logic.boolalg import as_Boolean


def permutations(n: Expr, k: Expr):
    return Mul(factorial(n), factorial((n - k)) ** S.NegativeOne)


def derangements(n: Expr):
    return (factorial(n) - lowergamma(n + 1, -1)) / E


def taylor(
    expression: Expr,
    degree: Expr,
    variables: list[Symbol],
    arguments: list[Expr],
    expansion_point: tuple[Expr],
):
    if len(variables) != len(arguments):
        raise RuntimeError(
            "Variables dimension and arguments dimension must be equal.\n"
            f"Variables dimension: {len(variables)}\n"
            f"Arguments dimension: {len(arguments)}"
        )

    dimension = len(variables)  # or len(arguments)

    # degree must be a positive natural number.
    degree = simplify(degree)

    if not int_valued(degree) or degree < 0:
        raise RuntimeError(
            "Degree of taylor series must be a natural number.\n" f"Was [{degree}]"
        )

    if len(expansion_point) != dimension:
        raise RuntimeError(
            "Taylor series variable dimension and expansion point dimension must be equal.\n"
            f"Variable dimension: {dimension}\n"
            f"Expansion point dimension: {len(expansion_point)}"
        )

    # Now the taylor polynomial can be computed.
    # See here for reference: https://en.wikipedia.org/wiki/Taylor_series#Taylor_series_in_several_variables

    # start out with building a list of directional derivatives from expr,
    # The final 2D jagged array contains all possible permutations of directional derivatives up to an order of the taylor polynomial degree
    # idx 0 represents derivative order, and idx 1 represents a specific unique derivative of that order.
    # So the length of the n'th row in taylor_pol_terms would be dimension^n

    taylor_pol_terms: list[list[Expr]] = [[expression]]

    for _ in range(degree):
        taylor_pol_terms.append([])

        for prev_derivative in taylor_pol_terms[-2]:
            for arg in variables:
                new_derivative = prev_derivative.diff(arg)
                taylor_pol_terms[-1].append(new_derivative)

    # The expansion point is now substituted into all directional derivates.

    exp_point_subs = dict()

    for variable, exp_scalar in zip(variables, expansion_point):
        exp_point_subs[variable] = exp_scalar

    for diff in taylor_pol_terms:
        for i, d in enumerate(diff):
            diff[i] = d.subs(exp_point_subs)

    # The (x - x_d)^n terms are now multiplied onto the derivatives.
    for i in range(0, degree):
        for j in range(i, degree):
            for k, arg in enumerate(variables):
                step = dimension**j
                for n in range(step):
                    taylor_pol_terms[j + 1][k * step + n] *= arg - exp_point_subs[arg]

    # construct taylor polynomial by scaling each sum row by 1/n! and adding them together.
    taylor_polynomial = taylor_pol_terms[0][0]

    for d in range(degree):
        taylor_polynomial += Rational(1, factorial(d + 1)) * sum(
            taylor_pol_terms[d + 1]
        )

    # finally substitute the args into the computed taylor polynomial
    args_subs = dict()

    for variable, arg in zip(variables, arguments):
        args_subs[variable] = arg

    return taylor_polynomial.subs(args_subs)


# SymbolicIff is an "extension" (functionality wise, not class wise) of the Equivalent (iff) function.
# It does the exact thing that Equivalent does, but if one of the args are not a boolean, it instead checks
# if all args equal each other.
# This does mean that this is technically not an Iff, as SymbolicIff evaluates to a True or False value if one of the args is not boolean,
# where it might make more sense to evaluate to a symbolic result.
# An example is SymbolicIff(2 * a, 2), here it will return False, because 2 * a != 2, for some values of a, but it is technically true for a = 1.
# Therefore this is more akin to a universal quantification combined with an iff in the symbolic case.
class SymbolicIff(Function):

    @classmethod
    def eval(cls, *args: Expr) -> Expr:
        try:
            args_bool = (as_Boolean(arg) for arg in args)
            return Equivalent(*args_bool)
        except TypeError:
            simplified_args = [simplify(arg) for arg in args]
            return all(a.equals(b) for a, b in combinations(simplified_args, 2))
