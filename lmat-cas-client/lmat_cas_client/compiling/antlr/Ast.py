from __future__ import annotations

from abc import ABC
from dataclasses import dataclass, field, replace
from enum import Enum

from antlr4 import ParserRuleContext


class CombOpId(Enum):
    Permutations = 'P'
    Combinations = 'C'

def combOpFromId(ctx: ParserRuleContext, n: AExpr, kr: AExpr, op: CombOpId):
    match op:
        case CombOpId.Permutations:
            return Permutations(ctx, n, kr)
        case CombOpId.Combinations:
            return Binom(ctx, n, kr)

class Index:
    pass

@dataclass(frozen=True)
class AstNode(ABC):
    ctx: ParserRuleContext = field(repr=False)

    def mut_ctx[T: AstNode](self: T, ctx: ParserRuleContext) -> T:
        return replace(self, ctx=ctx)

# ======== a_expr =========

AExpr = int

@dataclass(frozen=True)
class BinOp(AstNode, ABC):
    lhs: AExpr
    rhs: AExpr

@dataclass(frozen=True)
class UnaryOp(AstNode, ABC):
    arg: AExpr


@dataclass(frozen=True)
class Symbol(AstNode):
    symbol: str

@dataclass(frozen=True)
class Number(AstNode):
    number: str

@dataclass(frozen=True)
class ExpOp(AstNode):
    base: AExpr
    exponent: AExpr


@dataclass(frozen=True)
class IndexOp(AstNode):
    IndexEntry = AExpr | tuple[AExpr | None, AExpr | None] | None

    val: AExpr
    index: tuple[IndexEntry, ...]

@dataclass(frozen=True)
class MultOp(BinOp):
    pass

@dataclass(frozen=True)
class ModOp(BinOp):
    pass

@dataclass(frozen=True)
class DivOp(AstNode):
    num: AExpr
    denom: AExpr

@dataclass(frozen=True)
class AddOp(BinOp):
    pass

@dataclass(frozen=True)
class SubOp(AstNode):
    pass

@dataclass(frozen=True)
class UMinusOp(UnaryOp):
    pass

@dataclass(frozen=True)
class UPlusOp(UnaryOp):
    pass

@dataclass(frozen=True)
class Sum(AstNode):
    expr: AExpr
    var: AExpr
    range: tuple[AExpr, AExpr]

@dataclass(frozen=True)
class Product(AstNode):
    expr: AExpr
    var: AExpr
    range: tuple[AExpr, AExpr]

@dataclass(frozen=True)
class Integral(AstNode):
    integrand: AExpr
    diff: AExpr
    bounds: tuple[AExpr, AExpr] | None


@dataclass(frozen=True)
class Differential(AstNode):
    differentiand: AExpr
    differentials: list[tuple[AExpr, AExpr | None]]


class LimitDir(Enum):
    POSITIVE = 1
    NEGATIVE = 2
    BOTH = 3

@dataclass(frozen=True)
class Limit:
    expr: AExpr
    var: AExpr
    poa: AExpr
    dir: LimitDir


@dataclass(frozen=True)
class Factorial(UnaryOp):
    pass

@dataclass(frozen=True)
class Percent(UnaryOp):
    pass

@dataclass(frozen=True)
class Permille(UnaryOp):
    pass


@dataclass(frozen=True)
class Binom(AstNode):
    n: AExpr
    k: AExpr

@dataclass(frozen=True)
class Permutations(AstNode):
    n: AExpr
    r: AExpr

@dataclass(frozen=True)
class Derangements(AstNode):
    n: AExpr

@dataclass(frozen=True)
class Root(AstNode):
    op: AExpr
    index: AExpr | None


@dataclass(frozen=True)
class Conjugate(UnaryOp):
    pass


@dataclass(frozen=True)
class UnitVec(UnaryOp):
    pass

@dataclass(frozen=True)
class Matrix(AstNode):
    elements: list[list[AExpr]]
    beg_cmd: str
    end_cmd: str
