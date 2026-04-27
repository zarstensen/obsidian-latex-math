from typing import NamedTuple

class Symbol(NamedTuple):
    symbol: str

class Number(NamedTuple):
    number: str

class ExpOp(NamedTuple):
    base: "Expr"
    exponent: "Expr"

class UPostfixOp(NamedTuple):
    operand: "Expr"

class MultOp(NamedTuple):
    lhs: "Expr"
    rhs: "Expr"

class DivOp(NamedTuple):
    num: "Expr"
    denom: "Expr"

class AddOp(NamedTuple):
    lhs: "Expr"
    rhs: "Expr"

class SubOp(NamedTuple):
    lhs: "Expr"
    rhs: "Expr"
class UMinusOp(NamedTuple):
    operand: "Expr"

class AppliedHardFunc(NamedTuple):
    func: "HardFunc"

Expr = ExpOp | UPostfixOp | MultOp | DivOp | AddOp | SubOp | UMinusOp | Symbol | Number | AppliedHardFunc

class Binom(NamedTuple):
    n: Expr
    k: Expr

class Sqrt(NamedTuple):
    operand: Expr

class Conjugate(NamedTuple):
    operand: Expr

class UnitVec(NamedTuple):
    operand: Expr

HardFunc = Binom | Sqrt | Conjugate | UnitVec

e = SubOp(Number("123"), AppliedHardFunc(Sqrt(SubOp(Symbol("\\pi"), Number("3")))))

def ppAF(f: HardFunc):
    match f:
        case Sqrt(o):
            return f"\\sqrt{{{pp(o)}}}"

def pp(expr: Expr):
    match expr:
        case SubOp(lhs, rhs):
            return pp(lhs) + '-' + pp(rhs)
        case Number(n) | Symbol(n):
            return n
        case AppliedHardFunc(f):
            return ppAF(f)

print(pp(e))