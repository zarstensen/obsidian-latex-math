from __future__ import annotations

from abc import ABC
from enum import Enum
from typing import Callable, Union

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

# ======== misc ========

@frozen
class Placeholder(AstNode):
    pass

@frozen
class AmbigApplyFunc(AstNode):
    apply_func_candidate: ApplyFunc
    # additional exp_op which also needs to be resolved
    # e.g. for f(x)^2 it should be seen as the following
    # i guess this is true for any postfix operator actually...
    # f *is* function:
    # (f(x))^2
    # f *is not* function:
    # f * x^2
    # what about... a \div f(x)
    # in one case it would be
    # (a / f) * x
    # whilst in the other it would be
    # a / (f(x))
    # aaaaaaaaaaaaaaaaaaaaaaa
    postfix_op: Callable[[ParserRuleContext, AExpr], PostfixOp] | None
    prefix_op: Callable[[ParserRuleContext, AExpr], AExpr] | None

Ir = Placeholder | AmbigApplyFunc


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
class ABinOp(AstNode, ABC):
    lhs: AExpr
    rhs: AExpr

@frozen
class AUnaryOp(AstNode, ABC):
    operand: AExpr

@frozen
class Symbol(AstNode):
    name: str

@frozen
class Number(AstNode):
    number: str

@frozen
class ApplyFunc(AUnaryOp):
    args: tuple[AExpr, ...]


@frozen
class ExpOp(AstNode):
    base: AExpr
    exponent: AExpr

SubscriptSlot = Union["AExpr", tuple[Union["AExpr", None], Union["AExpr", None]]] | None

@frozen
class SubscriptForm:
    """
    Represents the form of the subscript of some symbol.
    Specifically, this stores the brackets at the start / end of the subscript as well as the delimiters used in the subscript.
    """
    brackets: tuple[str | None, str | None]
    slot_seps: tuple[str, ...]

@frozen
class Subscript(AstNode):
    slots: tuple[SubscriptSlot, ...]
    form: SubscriptForm

@frozen
class SubscriptOp(AstNode):
    val: AExpr
    sub: Subscript


@frozen
class MultOp(ABinOp):
    pass


@frozen
class XProdOp(ABinOp):
    pass


@frozen
class ModOp(ABinOp):
    pass


@frozen
class DivOp(AstNode):
    num: AExpr
    denom: AExpr


@frozen
class AddOp(ABinOp):
    pass


@frozen
class SubOp(ABinOp):
    pass


@frozen
class UMinusOp(AUnaryOp):
    pass


@frozen
class UPlusOp(AUnaryOp):
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
class Factorial(AUnaryOp):
    pass


@frozen
class Percent(AUnaryOp):
    pass


@frozen
class Permille(AUnaryOp):
    pass

PostfixOp = ExpOp | SubscriptOp | Factorial | Percent | Permille


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
class Parens(AUnaryOp):
    pass

@frozen
class Abs(AUnaryOp):
    pass


@frozen
class Norm(AUnaryOp):
    pass


@frozen
class Floor(AUnaryOp):
    pass


@frozen
class Ceil(AUnaryOp):
    pass


@frozen
class DotProd(ABinOp):
    pass


@frozen
class Root(AstNode):
    op: AExpr
    index: AExpr | None


@frozen
class Conjugate(AUnaryOp):
    pass


@frozen
class UnitVec(AUnaryOp):
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
    | Parens
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
    | Ir
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
