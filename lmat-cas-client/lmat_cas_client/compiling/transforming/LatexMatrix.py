from typing import override

from sympy import ImmutableDenseMatrix, MatrixBase, MutableDenseMatrix
from sympy.core.sympify import converter


class LatexMatrix(MatrixBase):
    """
    The LatexMatrix class stores additional info about the eventual latex representation of a sympy matrix.
    """

    env_begin: str | None = None
    env_end: str | None = None


class MutableLatexMatrix(LatexMatrix, MutableDenseMatrix):  # type: ignore[override,misc]
    def __new__(
        cls, *args, env_begin: str | None = None, env_end: str | None = None, **kwargs
    ):
        # only the class type is propagated during matrix computations,
        # so a custom class is created for each new instance, which stores the latex strings.
        lmat_cls = type(
            f"MutableLatexMatrix {env_begin} {env_end}",
            (cls,),
            {"env_begin": env_begin, "env_end": env_end, "__new__": super().__new__},
        )

        return lmat_cls(*args, **kwargs)

    @override
    def as_immutable(self):
        return ImmutableLatexMatrix(
            self, env_begin=self.env_begin, env_end=self.env_end
        )


class ImmutableLatexMatrix(LatexMatrix, ImmutableDenseMatrix):  # type: ignore[override,misc]
    def __new__(
        cls, *args, env_begin: str | None = None, env_end: str | None = None, **kwargs
    ):
        lmat_cls = type(
            f"ImmutableLatexMatrix {env_begin} {env_end}",
            (cls,),
            {"env_begin": env_begin, "env_end": env_end, "__new__": super().__new__},
        )

        return lmat_cls(*args, **kwargs)


converter[ImmutableLatexMatrix] = lambda x: type(x)(x)
