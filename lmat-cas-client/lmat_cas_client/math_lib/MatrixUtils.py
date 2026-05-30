from typing import cast

from sympy import *


# Check if the given sympy object can be treated as a matrix.
def is_matrix[T](obj: T) -> bool:
    return hasattr(obj, "is_Matrix") and obj.is_Matrix


# If the given object is not a matrix, try to construct a 0d (1 by 1) Matrix containing the given value.
# If it is already a matrix, returns the matrix without modifying it in any way.
def ensure_matrix(obj: Basic | MatrixBase) -> MatrixBase:
    if not is_matrix(obj):
        return Matrix([obj])
    return cast(MatrixBase, obj)


def ensure_scalar(obj: Basic) -> Expr:

    if is_matrix(obj):
        mat = cast(MatrixBase, cast(object, obj))
        if mat.shape == (1, 1):
            return ensure_scalar(cast(Basic, cast(object, mat[0])))
        else:
            assert False

    # TODO: maybe aasssert is instance here?
    return cast(Expr, obj)
