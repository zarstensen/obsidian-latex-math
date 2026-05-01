from abc import ABC
from dataclasses import dataclass, field
from enum import Enum


from antlr4 import ParserRuleContext


@dataclass(frozen=True)
class AstNode(ABC):
    ctx: ParserRuleContext = field(repr=False)


@dataclass(frozen=True)
class Symbol(AstNode):
    symbol: str


@dataclass(frozen=True)
class Number(AstNode):
    number: str


@dataclass(frozen=True)
class ExpOp(AstNode):
    base: "Expr"
    exponent: "Expr"


@dataclass(frozen=True)
class MultOp(AstNode):
    lhs: "Expr"
    rhs: "Expr"


@dataclass(frozen=True)
class DivOp(AstNode):
    num: "Expr"
    denom: "Expr"


@dataclass(frozen=True)
class AddOp(AstNode):
    lhs: "Expr"
    rhs: "Expr"


@dataclass(frozen=True)
class SubOp(AstNode):
    lhs: "Expr"
    rhs: "Expr"


@dataclass(frozen=True)
class UMinusOp(AstNode):
    op: "Expr"


@dataclass(frozen=True)
class UPlusOp(AstNode):
    op: "Expr"


@dataclass(frozen=True)
class AppliedBuiltinFunc(AstNode):
    func: "BuiltinFunc"


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
    | AppliedBuiltinFunc
)


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
class Sqrt(AstNode):
    op: Expr


@dataclass(frozen=True)
class Conjugate(AstNode):
    op: Expr


@dataclass(frozen=True)
class UnitVec(AstNode):
    op: Expr


BuiltinFunc = Factorial | Percent | Permille | Binom | Sqrt | Conjugate | UnitVec | Limit

