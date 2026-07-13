from __future__ import annotations

from enum import Enum

from attrs import frozen

from lmat_cas_client.compiling.antlr.ast import AlgStmtAst
from lmat_cas_client.compiling.antlr.ast.AstNode import AstNode


@frozen
class Definition(AstNode):
    head: AlgStmtAst.Symbol
    subscript: AlgStmtAst.Subscript | None
    func_args: tuple[AlgStmtAst.AExpr] | None
    body: AlgStmtAst.AExpr | None


@frozen
class Assumption(AstNode):
    head: AlgStmtAst.Symbol
    subscript: AlgStmtAst.Subscript | None
    func_args: tuple[AlgStmtAst.AExpr] | None
    set: Set | None

BindingStmt = Definition | Assumption
BindingStmts = tuple[BindingStmt, ...]

class SetBound(Enum):
    POSITIVE = 0
    NONNEGATIVE = 1
    NEGATIVE = 2
    NONPOSITIVE = 3
    NONZERO = 4
    NONE = 5


class SetType(Enum):
    COMPLEX = 0
    REAL = 1
    IMAGINARY = 2
    RATIONAL = 3
    INTEGER = 4
    NATURAL = 5
    EVEN = 6
    ODD = 7
    PRIME = 8
    EXT_REAL = 9
    ALGEBRAIC = 10


@frozen
class Set(AstNode):
    set_type: SetType
    set_bound: SetBound

