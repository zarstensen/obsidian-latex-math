# Generated from d:/DTU/School/.obsidian/plugins/obsidian-latex-math/lmat-cas-client/lmat_cas_client/compiling/antlr/grammar/ExprGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprGrammar import ExprGrammar
else:
    from ExprGrammar import ExprGrammar

import Ast


# This class defines a complete generic visitor for a parse tree produced by ExprGrammar.

class ExprGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprGrammar#debug.
    def visitDebug(self, ctx:ExprGrammar.DebugContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Command.
    def visitCommand(self, ctx:ExprGrammar.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#MultiplicativeOp.
    def visitMultiplicativeOp(self, ctx:ExprGrammar.MultiplicativeOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#UAdditiveOp.
    def visitUAdditiveOp(self, ctx:ExprGrammar.UAdditiveOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#AdditiveOp.
    def visitAdditiveOp(self, ctx:ExprGrammar.AdditiveOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Stub.
    def visitStub(self, ctx:ExprGrammar.StubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#ExponentialOp.
    def visitExponentialOp(self, ctx:ExprGrammar.ExponentialOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#Prefix.
    def visitPrefix(self, ctx:ExprGrammar.PrefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#atom.
    def visitAtom(self, ctx:ExprGrammar.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprGrammar#function.
    def visitFunction(self, ctx:ExprGrammar.FunctionContext):
        return self.visitChildren(ctx)



del ExprGrammar