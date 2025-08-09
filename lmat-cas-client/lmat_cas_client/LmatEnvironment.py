
from typing import Optional, Self

from pydantic import BaseModel, Field
from sympy import Symbol

from lmat_cas_client.compiling.Compiler import (
    latex_to_dependencies_compiler,
    latex_to_sympy_compiler_no_deps_assert,
)
from lmat_cas_client.compiling.Definitions import (
    AssumptionDefinition,
    SerializedDefinition,
    SerializedFunctionDefinition,
)
from lmat_cas_client.compiling.DefinitionStore import (
    DefinitionStore,
)


class FunctionDef(BaseModel):
    args: list[str]
    expr: str

## The LmatEnvironment type represents a dictionary
## parsed from a json encoded LmatEnvironment typescript class.
class LmatEnvironment(BaseModel):
    symbols: dict[str, list[str]] = Field(default_factory=dict)

    variables: dict[str, str] = Field(default_factory=dict)
    functions: dict[str, FunctionDef] = Field(default_factory=dict)

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

        for function_name, function_def in environment.functions.items():
            definitions[function_name] = SerializedFunctionDefinition(
                compiler = latex_to_sympy_compiler_no_deps_assert,
                dependencies_compiler = latex_to_dependencies_compiler,
                func_name = function_name,
                serialized_body = function_def.expr,
                variables = function_def.args
                )

        for variable_name, variable_def in environment.variables.items():
            definitions[variable_name] = SerializedDefinition(
                compiler = latex_to_sympy_compiler_no_deps_assert,
                dependencies_compiler = latex_to_dependencies_compiler,
                serialized_definition = variable_def
                )

        return DefinitionStore(definitions)
