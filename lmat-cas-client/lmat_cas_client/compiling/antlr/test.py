from token import NUMBER
from typing import override

from antlr4 import TerminalNode, Token
from antlr4.tree.Tree import TerminalNodeImpl
from ExprGrammar import ExprGrammar
from .ExprGrammarVisitor import ExprGrammarVisitor


class EGV(ExprGrammarVisitor):
    @override
    def visitAdditiveOp(self, ctx: ExprGrammar.AdditiveOpContext):
        return super().visitAdditiveOp(ctx)

    @override
    def visitAtom(self, ctx: ExprGrammar.AtomContext):
        match list(ctx.getChildren()):
            case [TerminalNodeImpl() as term]:
                pass
            case _:
                assert False

        match term.getSymbol().type:
            case ExprGrammar.NUMBER:
                pass
            case ExprGrammar.SYMBOL:
                pass
            case ExprGrammar.COMMAND:
                pass

        return super().visitAtom(ctx)
