from typing import ChainMap, Optional, Self

from pydantic import BaseModel, Field
from sympy import Function, Symbol
from sympy.core.function import AppliedUndef

from lmat_cas_client.compiling.Compiler import LatexToCasExprCompiler
from lmat_cas_client.compiling.definition.DefinitionStore import (
    AstDef,
    AstFunDef,
    DefinitionStore,
    EmptyDefinition,
    FunctionDefinition,
    SymbolDefinition,
    SympyDef,
)
from lmat_cas_client.compiling.parsing.CasExprParser import cas_expr_parser
from lmat_cas_client.compiling.transforming.DependenciesTransformer import (
    dependencies_transformer_runner,
)
from lmat_cas_client.math_lib.StandardDefinitionStore import StandardDefinitionStore


class EnvDefinition(BaseModel):
    name_expr: str
    value_expr: str


## The LmatEnvironment type represents a dictionary
## parsed from a json encoded LmatEnvironment typescript class.
class LmatEnvironment(BaseModel):
    symbols: dict[str, list[str]] = Field(default_factory=dict)

    definitions: list[EnvDefinition] = Field(default_factory=list)

    unit_system: Optional[str] = None

    solve_domain: Optional[str] = None

    # Create a definition store populated with definitions based on the environments symbols, variables and functions fields.
    @staticmethod
    def create_definition_store(environment: Self) -> DefinitionStore:
        environment = LmatEnvironment.model_validate(environment)

        definition_store: DefinitionStore = {}

        for symbol_name, assumption_expr in environment.symbols.items():
            definition_store[symbol_name] = SymbolDefinition(
                SympyDef(
                    Symbol(
                        symbol_name,
                        **{assumption: True for assumption in assumption_expr},
                    )
                )
            )

        latex_to_sympy_compiler = LatexToCasExprCompiler()

        for definition in environment.definitions:
            definition_id = latex_to_sympy_compiler.compile(definition.name_expr, {})
            # its not going to be like this for long anyways, so no point in making it pretty.

            definition_id = definition_id.get_expr(-1)

            match definition_id:
                case Symbol() as def_symbol:
                    if definition.value_expr == "":
                        definition_store[def_symbol.name] = EmptyDefinition()
                    else:
                        ast = cas_expr_parser.parse(definition.value_expr)
                        definition_store[def_symbol.name] = SymbolDefinition(
                            AstDef(ast),
                            deps=dependencies_transformer_runner.transform(ast),
                        )
                case AppliedUndef() as def_function:
                    if definition.value_expr == "":
                        definition_store[def_function.name] = EmptyDefinition()
                    else:
                        ast = cas_expr_parser.parse(definition.value_expr)
                        definition_store[def_function.name] = FunctionDefinition(
                            AstFunDef(ast, Function(def_function.name)),
                            deps=dependencies_transformer_runner.transform(
                                ast
                            ),  # TODO remove params from this set.
                            params=[arg.name for arg in def_function.args],
                        )
                case _:
                    pass

        def_store = ChainMap(definition_store, StandardDefinitionStore)

        return def_store
