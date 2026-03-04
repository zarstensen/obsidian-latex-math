from collections.abc import Iterable
from typing import override

from lmat_cas_client.compiling.definition.DefinitionStore import (
    FunctionDefinition,
    SymbolDefinition,
)
from lmat_cas_client.compiling.definition.Resolver import (
    Definition,
    DefinitionResolver,
    FunctionResToken,
    SymbolResToken,
)
from sympy import Basic


class EmptyResolver(DefinitionResolver):
    """
    The EmptyResolver implementation NEVER resolves *any* definition id to a value.
    """

    @override
    def get_resolver_token(self, _def_id: str):
        return None

    @override
    def get_definition(self, _def_id: str):
        return None

    @override
    def resolve_value(self, _target: SymbolResToken | SymbolDefinition) -> Basic:
        raise NotImplementedError()

    @override
    def resolve_body(self, _target: FunctionResToken | FunctionDefinition) -> Basic:
        raise NotImplementedError()

    @override
    def resolve_params(
        self, _target: FunctionResToken | FunctionDefinition
    ) -> tuple[Basic]:
        raise NotImplementedError()

    @override
    def resolve_unapplied(
        self, _target: FunctionResToken | FunctionDefinition
    ) -> Basic:
        raise NotImplementedError()

    @override
    def resolve_applied(
        self,
        _target: FunctionResToken | FunctionDefinition,
        _params: Iterable[Definition],
    ) -> Basic:
        raise NotImplementedError()
