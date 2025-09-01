from lark import Token, Transformer, v_args
from sympy import *
from sympy.logic.boolalg import *

from lmat_cas_client.math_lib import Functions

from .SystemOfExpr import SystemOfExpr


class PropositionExpr:
    """
    return type for the PropositionsTransformer.
    Simply wraps a propositional expression,
    is primarily used to detect if an expression came from PropositionsTransformer.
    """
    def __init__(self, expr):
        self.expr = expr

    def _sympy_(self):
        return self.expr

@v_args(inline=True)
class PropositionsTransformer(Transformer):
    """
    The FucntionsTransformer holds the implementation of various mathematical function rules,
    defined in the latex math grammar.
    """

    def CMD_TAUTOLOGY(self, _) -> Expr:
        return S.true

    def CMD_CONTRADICTION(self, _) -> Expr:
        return S.false

    @v_args(meta=True, inline=True)
    def proposition_chain(self, meta, *props: Expr) -> SystemOfExpr | PropositionExpr:
        if len(props) > 1:
            return SystemOfExpr([(PropositionExpr(prop), meta) for prop in props])
        else:
            s = PropositionExpr(props[0])
            sympify(s)
            return PropositionExpr(props[0])

    def prop_iff(self, *args: tuple[Expr]) -> Expr:
        return Functions.SymbolicIff(*args)

    def prop_negated_iff(self, *args: tuple[Expr]) -> Expr:
        return Not(Functions.SymbolicIff(*args))

    def prop_implies(self, *args: tuple[Expr|Token]) -> Expr:

        args = list(reversed(args))

        while len(args) > 1:
            left = args.pop()
            op_token = args.pop()
            right = args.pop()

            match op_token.type:
                case "_PROP_OP_LR_IMPLICATION":
                    implication = Implies(left, right, evaluate=False)
                case "_PROP_OP_NEG_LR_IMPLICATION":
                    implication = Not(Implies(left, right, evaluate=False), evaluate=False)
                case "_PROP_OP_RL_IMPLICATION":
                    implication = Implies(right, left, evaluate=False)
                case "_PROP_OP_NEG_RL_IMPLICATION":
                    implication = Not(Implies(right, left, evaluate=False), evaluate=False)
                case _:
                    raise ValueError(f"Unexpected token: {repr(op_token)}")

            args.append(implication)

        return args[0]

    def prop_or(self, *args: tuple[Expr]) -> Expr:
        return Or(*args, evaluate=False)

    def prop_nand(self, *args: tuple[Expr]) -> Expr:
        return Nand(*args, evaluate=False)

    def prop_and(self, *args: tuple[Expr]) -> Expr:
        return And(*args, evaluate=False)

    def prop_nor(self, *args: tuple[Expr]) -> Expr:
        return Nor(*args, evaluate=False)

    def prop_xor(self, *args: tuple[Expr]) -> Expr:
        return Xor(*args, evaluate=False)

    def prop_xnor(self, *args: tuple[Expr]) -> Expr:
        return Xnor(*args, evaluate=False)

    def prop_not(self, arg: Expr) -> Expr:
        return Not(arg, evaluate=False)
