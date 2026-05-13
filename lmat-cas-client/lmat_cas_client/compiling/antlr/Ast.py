from __future__ import annotations

from abc import ABC
from dataclasses import dataclass, field, replace
from enum import Enum

from antlr4 import ParserRuleContext


class CombOpId(Enum):
	Permutations = 'P'
	Combinations = 'C'

def combOpFromId(ctx: ParserRuleContext, n: Expr, kr: Expr, op: CombOpId):
	match op:
		case CombOpId.Permutations:
			return Permutations(ctx, n, kr)
		case CombOpId.Combinations:
			return Binom(ctx, n, kr)


@dataclass(frozen=True)
class AstNode(ABC):
    ctx: ParserRuleContext = field(repr=False)

    def mut_ctx[T: AstNode](self: T, ctx: ParserRuleContext) -> T:
        return replace(self, ctx=ctx)


@dataclass(frozen=True)
class Symbol(AstNode):
    symbol: str

@dataclass(frozen=True)
class SubscriptSymbol(AstNode):
	symbol: Symbol
	subscript: list[Expr]

@dataclass(frozen=True)
class Number(AstNode):
    number: str


@dataclass(frozen=True)
class Matrix(AstNode):
    elements: list[list[Expr]]
    beg_cmd: str
    end_cmd: str


@dataclass(frozen=True)
class ExpOp(AstNode):
    base: Expr
    exponent: Expr


@dataclass(frozen=True)
class MultOp(AstNode):
    lhs: Expr
    rhs: Expr


@dataclass(frozen=True)
class ModOp(AstNode):
    lhs: Expr
    rhs: Expr

@dataclass(frozen=True)
class DivOp(AstNode):
    num: Expr
    denom: Expr


@dataclass(frozen=True)
class AddOp(AstNode):
    lhs: Expr
    rhs: Expr


@dataclass(frozen=True)
class SubOp(AstNode):
    lhs: Expr
    rhs: Expr


@dataclass(frozen=True)
class UMinusOp(AstNode):
    op: Expr


@dataclass(frozen=True)
class UPlusOp(AstNode):
    op: Expr

@dataclass(frozen=True)
class Sum(AstNode):
	expr: Expr
	var: Expr
	range: tuple[Expr, Expr]

@dataclass(frozen=True)
class Product(AstNode):
	expr: Expr
	var: Expr
	range: tuple[Expr, Expr]

@dataclass(frozen=True)
class AppliedBuiltinFunc(AstNode):
    func: BuiltinFunc


Expr = (
    ExpOp
    | MultOp
    | DivOp
    | AddOp
    | SubOp
    | UMinusOp
    | UPlusOp
    | Symbol
    | Number
    | Matrix
    | AppliedBuiltinFunc
)


@dataclass(frozen=True)
class Integral(AstNode):
    integrand: Expr
    diff: Expr
    bounds: tuple[Expr, Expr] | None


@dataclass(frozen=True)
class Differential(AstNode):
	differentiand: Expr
	differentials: list[tuple[Expr, Expr | None]]

class LimitDir(Enum):
    POSITIVE = 1
    NEGATIVE = 2
    BOTH = 3


@dataclass(frozen=True)
class Limit:
    expr: Expr
    var: Expr
    poa: Expr
    dir: LimitDir


@dataclass(frozen=True)
class Factorial(AstNode):
    op: Expr


@dataclass(frozen=True)
class Percent(AstNode):
    op: Expr


@dataclass(frozen=True)
class Permille(AstNode):
    op: Expr


@dataclass(frozen=True)
class Binom(AstNode):
    n: Expr
    k: Expr

@dataclass(frozen=True)
class Permutations(AstNode):
	n: Expr
	r: Expr

@dataclass(frozen=True)
class Derangements(AstNode):
	n: Expr

@dataclass(frozen=True)
class Root(AstNode):
    op: Expr
    index: Expr | None


@dataclass(frozen=True)
class Conjugate(AstNode):
    op: Expr


@dataclass(frozen=True)
class UnitVec(AstNode):
    op: Expr


BuiltinFunc = Factorial | Percent | Permille | Binom | Root | Conjugate | UnitVec
