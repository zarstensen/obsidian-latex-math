from enum import Enum
from typing import override

from pydantic import BaseModel
from sympy import *
from sympy.logic.boolalg import Boolean, as_Boolean, truth_table
from tabulate import tabulate

from lmat_cas_client.Client import HandlerError
from lmat_cas_client.compiling.Compiler import Compiler
from lmat_cas_client.compiling.DefinitionStore import DefinitionStore
from lmat_cas_client.compiling.transforming.PropositionsTransformer import (
    PropositionExpr,
)
from lmat_cas_client.LmatEnvironment import LmatEnvironment
from lmat_cas_client.LmatLatexPrinter import lmat_latex

from .CommandHandler import *


# Enum of all truth table formats this handler supports.
class TruthTableFormat(Enum):
    MARKDOWN = "md"
    LATEX_ARRAY = "latex-array"

class TruthTableMessage(BaseModel):
    expression: str
    environment: LmatEnvironment
    # requested table format
    truth_table_format: TruthTableFormat

# base class for all truth table results.
# each implementation is for a distinct TruthTableFormat
class TruthTableResult(CommandResult):
    def __init__(self, columns: tuple[Expr], serialized_proposition: str, truth_table: tuple[tuple[Boolean]]):
        super().__init__()
        self.columns = columns
        self.serialized_proposition = serialized_proposition
        self.truth_table = truth_table

# implementation for MARKDOWN
class TruthTableResultMarkdown(TruthTableResult):

    def getResponsePayload(self) -> dict:
        markdown_table_contents = []

        # create true false strings, last column are bold to make it visually distinguishable.
        for row in self.truth_table:
            markdown_table_contents.append([ "T" if elem else "F" for elem in row ])
            markdown_table_contents[-1][-1] = f"**{markdown_table_contents[-1][-1]}**"

        headers = [*map(lmat_latex, self.columns), self.serialized_proposition]
        headers = [ f"${header}$" for header in headers ]

        return CommandResult.result({
            'truth_table': tabulate(markdown_table_contents,
                                    headers=headers,
                                    tablefmt='pipe',
                                    colalign=('center' for _ in range(len(self.columns) + 1)))
        })

# implementation for LATEX_ARRAY
class TruthTableResultLatex(TruthTableResult):

    def getResponsePayload(self) -> dict:
        array_contents = []

        for row in self.truth_table:
            array_contents.append("&".join(map(lmat_latex, row)))

        array_contents = r'\\ \hline '.join(array_contents)

        array_options = fr"{{{':'.join(('c' for _ in self.columns))}|c}}"

        headers = fr"{'&'.join(map(lmat_latex, self.columns))} & {self.serialized_proposition}"

        return CommandResult.result({
            'truth_table': fr"\begin{{array}}{array_options}{headers}\\ \hline{array_contents}\end{{array}}"
        })

# TruthTableHandler attempts to generate a truth table from the given expression.
# Expects a PropositionExpr so will fail if it is not.
class TruthTableHandler(CommandHandler):

    def __init__(self, compiler: Compiler[[DefinitionStore], Expr]):
        super().__init__()
        self._compiler = compiler

    @override
    def handle(self, message: TruthTableMessage) -> TruthTableResult:
        message = TruthTableMessage.model_validate(message)

        definitions_store = LmatEnvironment.create_definition_store(message.environment)
        sympy_expr = self._compiler.compile(message.expression, definitions_store)

        if not isinstance(sympy_expr, PropositionExpr):
            raise HandlerError(f"Expression must be a proposition, was {type(sympy_expr)}")

        sympy_expr = sympify(sympy_expr)

        columns = sorted(sympy_expr.free_symbols, key=str)

        truth_table_data = []

        # Sympy by defaults starts with all False, but truth tables usually start with all True,
        # so the result is reversed here to achieve this.
        for row in reversed(tuple(truth_table(sympy_expr, columns))):
            truth_table_data.append([*map(as_Boolean, row[0]), row[1]])

        result_cls = None

        # Select result class dependant on requested table format
        match message.truth_table_format:
            case TruthTableFormat.MARKDOWN:
                result_cls = TruthTableResultMarkdown
            case TruthTableFormat.LATEX_ARRAY:
                result_cls = TruthTableResultLatex
            case _:
                raise HandlerError(f"Unknown table format: {message.truth_table_format}")

        return result_cls(columns, message.expression, truth_table_data)
