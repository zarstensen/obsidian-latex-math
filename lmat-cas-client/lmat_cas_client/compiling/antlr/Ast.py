from __future__ import annotations

from abc import ABC
from enum import Enum
from typing import Union

from antlr4 import ParserRuleContext
from attrs import evolve, field, frozen


class CombOpId(Enum):
    Permutations = "P"
    Combinations = "C"


def combOpFromId(ctx: ParserRuleContext, n: AExpr, kr: AExpr, op: CombOpId):
    match op:
        case CombOpId.Permutations:
            return Permutations(ctx, n, kr)
        case CombOpId.Combinations:
            return Binom(ctx, n, kr)

@frozen
class AstNode(ABC):
    ctx: ParserRuleContext = field(repr=False)

    def mut_ctx[T: AstNode](self: T, ctx: ParserRuleContext) -> T:
        return evolve(self, ctx=ctx)

# ======== relational ========

@frozen
class RelOp(AstNode, ABC):
    lhs: AExpr
    rhs: AExpr | Rel

@frozen
class Eq(RelOp):
    pass

@frozen
class Neq(RelOp):
    pass

@frozen
class Lt(RelOp):
    pass

@frozen
class Lte(RelOp):
    pass

@frozen
class Gt(RelOp):
    pass

@frozen
class Gte(RelOp):
    pass

Rel = Eq | Neq | Lt | Lte | Gt | Gte

# ======== arithmetic expression ========

@frozen
class BinOp(AstNode, ABC):
    lhs: AExpr
    rhs: AExpr


@frozen
class UnaryOp(AstNode, ABC):
    arg: AExpr

@frozen
class Symbol(AstNode):
    name: str


@frozen
class Number(AstNode):
    number: str


@frozen
class Function(AstNode):
    name: str


@frozen
class ApplyFunc(AstNode):
    func: Function
    args: tuple[AExpr, ...]


@frozen
class ExpOp(AstNode):
    base: AExpr
    exponent: AExpr

SubscriptSlot = Union["AExpr", tuple[Union["AExpr", None], Union["AExpr", None]]] | None

@frozen
class Subscript(AstNode):
    slots: tuple[SubscriptSlot, ...]
    separators: tuple[str, ...]
    delimiters: tuple[str | None, str | None]

@frozen
class SubscriptOp(AstNode):
    val: AExpr
    sub: Subscript


@frozen
class MultOp(BinOp):
    pass


@frozen
class XProdOp(BinOp):
    pass


@frozen
class ModOp(BinOp):
    pass


@frozen
class DivOp(AstNode):
    num: AExpr
    denom: AExpr


@frozen
class AddOp(BinOp):
    pass


@frozen
class SubOp(BinOp):
    pass


@frozen
class UMinusOp(UnaryOp):
    pass


@frozen
class UPlusOp(UnaryOp):
    pass


@frozen
class Sum(AstNode):
    expr: AExpr
    var: AExpr
    range: tuple[AExpr, AExpr]


@frozen
class Product(AstNode):
    expr: AExpr
    var: AExpr
    range: tuple[AExpr, AExpr]


@frozen
class Integral(AstNode):
    integrand: AExpr
    diff: AExpr
    bounds: tuple[AExpr, AExpr] | None


@frozen
class Differential(AstNode):
    differentiand: AExpr
    differentials: list[tuple[AExpr, AExpr | None]]


class LimitDir(Enum):
    POSITIVE = "+"
    NEGATIVE = "-"
    BOTH = "+-"


@frozen
class Limit(AstNode):
    expr: AExpr
    var: AExpr
    poa: AExpr
    dir: LimitDir


@frozen
class EvalAt(AstNode):
    expr: AExpr
    subs_start: tuple[tuple[AExpr, AExpr], ...]
    subs_end: tuple[tuple[AExpr, AExpr], ...] | None


@frozen
class Factorial(UnaryOp):
    pass


@frozen
class Percent(UnaryOp):
    pass


@frozen
class Permille(UnaryOp):
    pass


@frozen
class Binom(AstNode):
    n: AExpr
    k: AExpr


@frozen
class Permutations(AstNode):
    n: AExpr
    r: AExpr


@frozen
class Derangements(AstNode):
    n: AExpr


@frozen
class Abs(UnaryOp):
    pass


@frozen
class Norm(UnaryOp):
    pass


@frozen
class Floor(UnaryOp):
    pass


@frozen
class Ceil(UnaryOp):
    pass


@frozen
class DotProd(BinOp):
    pass


@frozen
class Root(AstNode):
    op: AExpr
    index: AExpr | None


@frozen
class Conjugate(UnaryOp):
    pass


@frozen
class UnitVec(UnaryOp):
    pass


@frozen
class Matrix(AstNode):
    elements: list[list[AExpr]]
    beg_cmd: str
    end_cmd: str


@frozen
class DetMatrix(AstNode):
    elements: list[list[AExpr]]


AExpr = (
    Symbol
    | Number
    | Function
    | ApplyFunc
    | ExpOp
    | SubscriptOp
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

@frozen
class AExprEntry(AstNode):
    a_expr: AExpr

@frozen
class RelEntry(AstNode):
    rel: Rel

SystemEntry = AExprEntry | RelEntry

@frozen
class SystemEnv(AstNode):
    elems: list[SystemEntry]

@frozen
class AndChain(AstNode):
    elems: list[SystemEntry]

System = SystemEnv | AndChain

AlgStmt = System | AExpr | Rel
