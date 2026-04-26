from dataclasses import dataclass


@dataclass
class Expr:
    pass


@dataclass
class Atom(Expr):
    pass


@dataclass
class Symbol(Atom):
    symbol: str


@dataclass
class Number(Atom):
    symbol: str
