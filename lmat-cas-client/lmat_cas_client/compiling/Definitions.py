
from typing import Iterable, override

from sympy import Expr, Function, Symbol
from sympy.core.function import AppliedUndef

from lmat_cas_client.compiling.CompilerCore import Compiler

from .DefinitionStore import (
    Definition,
    DefinitionStore,
    FunctionDefinition,
)


# SympyDefinition simply holds a sympy expression as its defined value.
class SympyDefinition(Definition):
    def __init__(self, sympy_expr):
        self._sympy_expr = sympy_expr

    @override
    def defined_value(self, _definition_store: DefinitionStore):
        # TODO: Currently does not use a definition store for anything as it is never needed,
        # but should probably be added in the future
        return self._sympy_expr

    @override
    def dependencies(self) -> set[str]:
        # return all free symbol names and applied undefined function names as dependencies.
        return set(
                map(
                    lambda d: d.name,
                    self._sympy_expr.free_symbols | self._sympy_expr.atoms(AppliedUndef)
                    )
                )

# Specialized SympyDefinition for sympy Symbols.
class AssumptionDefinition(SympyDefinition):
    def __init__(self, symbol_assumption: Symbol):
        super().__init__(symbol_assumption)

    @override
    def dependencies(self) -> set[str]:
        # assumptions have no dependencies, butSympyDefinition would return the symbol itself as such,
        # so we need to explicitly return an empty set here.
        return set()

# Definition holding a serialized form of data, which needs a Compiler for retreiving their defined value.
class SerializedDefinition(Definition):
    # compiler: compiler to use for compiling the defined value
    # dependencies_compiler: compiler to use for compiling a set of definitions from the serialized data
    def __init__(self, compiler: Compiler[Expr, [DefinitionStore]], dependencies_compiler: Compiler[set[str], []], serialized_definition: str):
        self._serialized_definition = serialized_definition
        self._compiler = compiler
        self._dependencies_compiler = dependencies_compiler

    @override
    def defined_value(self, definition_store: DefinitionStore):
        return self._compiler.compile(self._serialized_definition, definition_store)

    @override
    def dependencies(self) -> set[str]:
        return self._dependencies_compiler.compile(self._serialized_definition)

# Like SerializedDefinition, but with FunctionDefinition as a base
class SerializedFunctionDefinition(FunctionDefinition):
    def __init__(self, compiler: Compiler[Expr, [DefinitionStore]], dependencies_compiler: Compiler[set[str], []], func_name, serialized_body, variables: Iterable[str]):
        super().__init__(variables)
        self._func_name = func_name
        self._serialized_body = serialized_body
        self._compiler = compiler
        self._dependencies_compiler = dependencies_compiler

    @override
    def defined_value(self, _definition_store: DefinitionStore) -> Function:
        return Function(self._func_name)

    @override
    def applied_value(self, definition_store: DefinitionStore, args: Iterable[Definition] | None = None) -> Expr:
        if args is None:
            args = tuple()
        else:
            args = tuple(args)

            if len(args) != len(self.variables):
                raise ValueError(f"Incorrect number of function args provided.\nExpected {len(self.variables)} ({', '.join(self.variables)}) got {len(self.args)}")

        args_definitions = { }

        for variable_name, argument_definition in zip(self.variables, args):
            args_definitions[variable_name] = argument_definition

        return self._compiler.compile(self._serialized_body, definition_store.override(args_definitions))

    @override
    def dependencies(self) -> set[str]:
        return self._dependencies_compiler.compile(self._serialized_body).difference(self._variables)
