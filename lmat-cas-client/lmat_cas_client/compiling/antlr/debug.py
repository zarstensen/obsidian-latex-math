# pyright: reportIncompatibleMethodOverride = false, reportAssignmentType = false
from typing import override

import pydot
from antlr4 import (
    CommonTokenStream,
    FileStream,
    ParserRuleContext,
    ParseTreeVisitor,
)
from antlr4.tree.Tree import ErrorNodeImpl, TerminalNodeImpl, Tree
from ExprGrammar import ExprGrammar
from ExprLexer import ExprLexer

IN_FILE = "in.txt"
OUT_FILE = "out.dot"


class ParseTreeDotVisitor(ParseTreeVisitor):
    """
    Produce a pydot dot graph from the given parse tree,
    representing a visual graph of said parse tree.
    """

    def __init__(self) -> None:
        self.dot_graph: pydot.Dot = pydot.Dot(
            "Parse Tree",
            rankdir="TB",
            splines=True,
            nodesep=0.45,
            ranksep=0.7,
            pad=0.0,
            ordering="out",
        )
        self.__rule_subgraph = pydot.Subgraph()
        self.__term_subgraph = pydot.Subgraph()
        self.__err_subgraph = pydot.Subgraph()

        self.dot_graph.add_subgraph(self.__rule_subgraph)
        self.dot_graph.add_subgraph(self.__term_subgraph)
        self.dot_graph.add_subgraph(self.__err_subgraph)

        self.dot_graph.set_edge_defaults(
            arrowhead="none", headport="n", color="#808080", penwidth=1.75
        )

        style = {
            "shape": "box",
            "margin": "0,0.05",
            "height": 0,
            "width": 1.75,
            "style": "filled",
            "fillcolor": "#FFFFFF",
            "color": "#C0C0C0",
            "penwidth": 1.75,
        }

        term_style = {
            **style,
            "style": "filled,rounded",
            "fillcolor": "#A0AB88",
            "color": "#75775B",
            "fontcolor": "#FAFBF9",
        }

        err_style = {
            **term_style,
            "fillcolor": "#DD8F7D",
            "color": "#BC6A7A",
        }

        self.__rule_subgraph.set_node_defaults(**style)
        self.__term_subgraph.set_node_defaults(**term_style)
        self.__err_subgraph.set_node_defaults(**err_style)
        self.next_node_id: int = 0
        super().__init__()

    @override
    def visit(self, tree: Tree) -> pydot.Dot:
        super().visit(tree)
        return self.dot_graph

    @override
    def visitChildren(self, node: ParserRuleContext) -> str:
        results: list[str] = super().visitChildren(node)
        # sooo, add node for the rule? and connect to all stuff in results.
        n = str(self.next_node_id)
        self.next_node_id += 1

        rule_alias = type(node).__name__.removesuffix("Context")

        rule_name = ExprGrammar.ruleNames[node.getRuleIndex()]

        if rule_alias.lower() == rule_name.lower():
            label = f"{rule_name}"
        else:
            label = f'<{rule_alias} <font color="#808080"> ({rule_name}) </font>>'

        self.__rule_subgraph.add_node(pydot.Node(n, label=label))

        for ids in results:
            # TODO: add nodes for missing tokens
            self.dot_graph.add_edge(pydot.Edge(n, ids))

        return n

    @override
    def visitTerminal(self, node: TerminalNodeImpl) -> str:

        id = str(self.next_node_id)
        self.next_node_id += 1
        self.__term_subgraph.add_node(
            pydot.Node(
                id,
                label=f"{ExprGrammar.symbolicNames[node.getSymbol().type]}\n{node.getText()}",
                xlabel=f'<<font color="#004D62">* {node.getSymbol().tokenIndex}</font>>',
            )
        )
        return id

    @override
    def visitErrorNode(self, node: ErrorNodeImpl) -> str:
        id = str(self.next_node_id)
        self.next_node_id += 1

        label = "ERROR\n\\<missing\\>"

        symbol = node.getSymbol()

        if symbol and symbol.tokenIndex != -1:
            label = f"{ExprGrammar.symbolicNames[symbol.type]}\n\\<unexpected: {symbol.text}\\>"

        self.__err_subgraph.add_node(pydot.Node(id, label=label))
        return id

    @override
    def defaultResult(self) -> list[str]:
        return []

    @override
    def aggregateResult(self, aggregate: list[str], nextResult: str) -> list[str]:
        aggregate.append(nextResult)
        return aggregate


# if parser.getNumberOfSyntaxErrors() > 0:
#     print("syntax errors")

input_stream = FileStream(IN_FILE)
lexer = ExprLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = ExprGrammar(stream)
tree = parser.debug()
r = ParseTreeDotVisitor().visit(tree)

with open(OUT_FILE, "w") as f:
    _ = f.write(str(r))

print(f"======== AST ========\n{tree.res}")

