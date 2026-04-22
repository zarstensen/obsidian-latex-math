# Generated from d:/DTU/School/.obsidian/plugins/obsidian-latex-math/lmat-cas-client/lmat_cas_client/compiling/antlr/ExprGrammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprGrammar import ExprGrammar
else:
    from ExprGrammar import ExprGrammar

# This class defines a complete generic visitor for a parse tree produced by ExprGrammar.

class ExprGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprGrammar#debug.
    def visitDebug(self, ctx:ExprGrammar.DebugContext):
        return self.visitChildren(ctx)



del ExprGrammar