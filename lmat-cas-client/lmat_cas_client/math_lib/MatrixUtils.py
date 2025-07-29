from sympy import *


# Check if the given sympy object can be treated as a matrix.
def is_matrix(obj: Basic) -> bool:
    return hasattr(obj, "is_Matrix") and obj.is_Matrix

# If the given object is not a matrix, try to construct a 0d (1 by 1) Matrix containing the given value.
# If it is already a matrix, returns the matrix without modifying it in any way.
def ensure_matrix(obj: Basic) -> MatrixBase:
    if not is_matrix(obj):
        return Matrix([obj])
    return obj
