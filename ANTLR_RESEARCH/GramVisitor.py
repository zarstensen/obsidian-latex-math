# Generated from d:/DTU/School/.obsidian/plugins/obsidian-latex-math/ANTLR_RESEARCH/Gram.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Gram import Gram
else:
    from Gram import Gram

# This class defines a complete generic visitor for a parse tree produced by Gram.

class GramVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Gram#debug.
    def visitDebug(self, ctx:Gram.DebugContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gram#expr.
    def visitExpr(self, ctx:Gram.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gram#function.
    def visitFunction(self, ctx:Gram.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gram#atom.
    def visitAtom(self, ctx:Gram.AtomContext):
        return self.visitChildren(ctx)



del Gram