from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Optional

from attr import frozen
from lmat_cas_client.compiling.definition.DefinitionStore import (
    Definition,
    FunctionDefinition,
    SymbolDefinition,
)
from sympy import Basic


@frozen
class SymbolResToken:
    name: str


@frozen
class FunctionResToken:
    name: str


type ResolverToken = SymbolResToken | FunctionResToken


class DefinitionResolver(ABC):
    """
    The Resolver class provides an interface for resolving values from Definitions.
    To resolve a value, one must first recieve a ResolverToken from the get_resolver_token method.
    This returns a simple typed token which can be passed to relevant resolve_* methods.
    """

    @abstractmethod
    def get_resolver_token(self, def_id: str) -> Optional[ResolverToken]:
        """
        Get an appropiate ResolverToken for the definition type which def_id is defined to.


        Args:
            def_id (str): Key in a DefinitionStore.

        Returns:
            Optional[ResolverToken]: Appropiate ResolverToken, to be passed to any resolve_* methods
            null if def_id is not tied to a resolvable definition.
        """
        pass

    @abstractmethod
    def get_definition(self, def_id: str) -> Optional[Definition]:
        """
        Retrieve the definition object associated with the given definition
        id.
        This can be supplied to all methods which a ResolverToken can be passed to,
        do note that this means the resolver is then no longer aware of what id the Definition
        is tied to, so any optional caching will not occur.
        """
        pass

    @abstractmethod
    def resolve_value(self, target: SymbolResToken | SymbolDefinition) -> Basic:
        """
        Resolve the value of a symbol definition.
        """
        pass

    @abstractmethod
    def resolve_body(self, target: FunctionResToken | FunctionDefinition) -> Basic:
        """
        Resolve the body of a function definition.
        Parameters are simply seen as symbols when resolving the body value.
        """
        pass

    @abstractmethod
    def resolve_params(
        self, target: FunctionResToken | FunctionDefinition
    ) -> tuple[Basic]:
        """
        Resolve the parameters to a function definition.
        The parameters are returned as Sympy objects (most likely Symbol)
        """
        pass

    @abstractmethod
    def resolve_unapplied(self, target: FunctionResToken | FunctionDefinition) -> Basic:
        """
        Resolve the unapplied version of a function definition.
        i.e. the f in f(x) := ...
        """
        pass

    @abstractmethod
    def resolve_applied(
        self,
        target: FunctionResToken | FunctionDefinition,
        params: Iterable[Definition],
    ) -> Basic:
        """
        Resolve the applied value of a function definition.
        i.e. if f is f(x, y, z, ...) := ...
        then the result of evaluating f(1, 42, 11, ...) is what this returns
        """
        pass
