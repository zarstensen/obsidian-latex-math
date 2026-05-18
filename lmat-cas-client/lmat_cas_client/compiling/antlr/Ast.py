from __future__ import annotations

from abc import ABC
from dataclasses import dataclass, field, replace
from enum import Enum
from typing import Union

from antlr4 import ParserRuleContext


class CombOpId(Enum):
    Permutations = "P"
    Combinations = "C"


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

# ======== relational ========

@dataclass(frozen=True)
class RelOp(AstNode, ABC):
    lhs: AExpr
    rhs: AExpr | Rel

@dataclass(frozen=True)
class Eq(RelOp):
	pass

@dataclass(frozen=True)
class Neq(RelOp):
	pass

@dataclass(frozen=True)
class Lt(RelOp):
	pass

@dataclass(frozen=True)
class Lte(RelOp):
	pass

@dataclass(frozen=True)
class Gt(RelOp):
	pass

@dataclass(frozen=True)
class Gte(RelOp):
	pass

Rel = Eq | Neq | Lt | Lte | Gt | Gte

# ======== arithmetic expression ========

@dataclass(frozen=True)
class BinOp(AstNode, ABC):
    lhs: AExpr
    rhs: AExpr


@dataclass(frozen=True)
class UnaryOp(AstNode, ABC):
    arg: AExpr

@dataclass(frozen=True)
class Symbol(AstNode):
    name: str


@dataclass(frozen=True)
class Number(AstNode):
    number: str


@dataclass(frozen=True)
class Function(AstNode):
    name: str


@dataclass(frozen=True)
class ApplyFunc(AstNode):
    func: Function
    args: tuple[AExpr, ...]


@dataclass(frozen=True)
class ExpOp(AstNode):
    base: AExpr
    exponent: AExpr

IndexEntry = Union["AExpr", tuple[Union["AExpr", None], Union["AExpr", None]]] | None

@dataclass(frozen=True)
class IndexOp(AstNode):
    val: AExpr
    index: tuple[IndexEntry, ...]


@dataclass(frozen=True)
class MultOp(BinOp):
    pass


@dataclass(frozen=True)
class XProdOp(BinOp):
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
class SubOp(BinOp):
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
    POSITIVE = "+"
    NEGATIVE = "-"
    BOTH = "+-"


@dataclass(frozen=True)
class Limit(AstNode):
    expr: AExpr
    var: AExpr
    poa: AExpr
    dir: LimitDir


@dataclass(frozen=True)
class EvalAt(AstNode):
    expr: AExpr
    subs_start: tuple[tuple[AExpr, AExpr], ...]
    subs_end: tuple[tuple[AExpr, AExpr], ...] | None


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
class Abs(UnaryOp):
    pass


@dataclass(frozen=True)
class Norm(UnaryOp):
    pass


@dataclass(frozen=True)
class Floor(UnaryOp):
    pass


@dataclass(frozen=True)
class Ceil(UnaryOp):
    pass


@dataclass(frozen=True)
class DotProd(BinOp):
    pass


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


@dataclass(frozen=True)
class DetMatrix(AstNode):
    elements: list[list[AExpr]]


AExpr = (
    Symbol
    | Number
    | Function
    | ApplyFunc
    | ExpOp
    | IndexOp
    | MultOp
    | XProdOp
    | ModOp
    | DivOp
    | AddOp
    | SubOp
    | UMinusOp
    | UPlusOp
    | Sum
    | Product
    | Integral
    | Differential
    | Limit
    | EvalAt
    | Factorial
    | Percent
    | Permille
    | Binom
    | Permutations
    | Derangements
    | Abs
    | Norm
    | Floor
    | Ceil
    | DotProd
    | Root
    | Conjugate
    | UnitVec
    | Matrix
    | DetMatrix
)

# ======== System ========

@dataclass(frozen = True)
class AExprEntry(AstNode):
	a_expr: AExpr

@dataclass(frozen = True)
class RelEntry(AstNode):
	a_expr: Rel

SystemEntry = AExprEntry | RelEntry

@dataclass(frozen=True)
class SystemEnv(AstNode):
	elems: list[SystemEntry]

@dataclass(frozen=True)
class AndChain(AstNode):
	elems: list[SystemEntry]

System = SystemEnv | AndChain
