
from typing import Optional, Self

from pydantic import BaseModel, Field
from sympy import Symbol
from sympy.core.function import AppliedUndef

from lmat_cas_client.compiling.Compiler import LatexToSympyCompiler
from lmat_cas_client.compiling.Definitions import (
    AssumptionDefinition,
    AstDefinition,
    AstFunctionDefinition,
)
from lmat_cas_client.compiling.DefinitionStore import (
    DefinitionStore,
)
from lmat_cas_client.compiling.parsing.LatexParser import latex_parser
from lmat_cas_client.compiling.transforming.DependenciesTransformer import (
    dependencies_transformer_runner,
)
from lmat_cas_client.compiling.transforming.SympyTransformer import (
    sympy_transformer_runner,
)


class EnvDefinition(BaseModel):
    name_expr: str
    value_expr: str

## The LmatEnvironment type represents a dictionary
## parsed from a json encoded LmatEnvironment typescript class.
class LmatEnvironment(BaseModel):
    symbols: dict[str, list[str]] = Field(default_factory=dict)

    definitions: list[EnvDefinition] = Field(default_factory=list)

    unit_system: Optional[str] = None

    domain: Optional[str] = None

    # Create a definition store populated with definitions based on the environments symbols, variables and functions fields.
    @staticmethod
    def create_definition_store(environment: Self) -> DefinitionStore:
        environment = LmatEnvironment.model_validate(environment)

        definitions = { }

        for symbol_name, assumption_expr in environment.symbols.items():
            definitions[symbol_name] = AssumptionDefinition(Symbol(
                symbol_name,
                **{ assumption: True for assumption in assumption_expr }
                ))

        latex_to_sympy_compiler = LatexToSympyCompiler()

        for definition in environment.definitions:

            definition_id = latex_to_sympy_compiler.compile(definition.name_expr, DefinitionStore())

            match definition_id:
                case Symbol() as def_symbol:
                    definitions[def_symbol.name] = AstDefinition(
                        expr_transformer = sympy_transformer_runner,
                        dependencies_transformer = dependencies_transformer_runner,
                        ast_definition = latex_parser.parse(definition.value_expr)
                    )
                case AppliedUndef() as def_function:
                    definitions[def_function.name] = AstFunctionDefinition(
                        expr_transformer = sympy_transformer_runner,
                        dependencies_transformer = dependencies_transformer_runner,
                        func_name = def_function.name,
                        ast_body = latex_parser.parse(definition.value_expr),
                        variables = [ arg.name for arg in def_function.args ]
                    )
                case _:
                    pass

        return DefinitionStore(definitions)
