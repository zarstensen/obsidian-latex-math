from collections.abc import Iterable
from typing import override

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
    def get_resolver_token(self, _name: str):
        return None

    @override
    def resolve_value(self, _token: SymbolResToken) -> Basic:
        raise NotImplementedError()

    @override
    def resolve_body(self, _token: FunctionResToken) -> Basic:
        raise NotImplementedError()

    @override
    def resolve_params(self, _token: FunctionResToken) -> tuple[Basic]:
        raise NotImplementedError()

    @override
    def resolve_unapplied(self, _token: FunctionResToken) -> Basic:
        raise NotImplementedError()

    @override
    def resolve_applied(
        self, _token: FunctionResToken, _params: Iterable[Definition]
    ) -> Basic:
        raise NotImplementedError()
