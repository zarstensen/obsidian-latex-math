from collections import ChainMap
from collections.abc import Iterable
from typing import Any, MutableMapping, Optional, cast, override

from lmat_cas_client.compiling.transforming.cas_expr.CasExprTransformer import CasExpr
from lmat_cas_client.compiling.transforming.TransformerRunner import TransformerRunner
from sympy import Basic, Expr, Symbol

from .DefinitionStore import (
    AstDef,
    AstFunDef,
    Definition,
    DefinitionStore,
    EmptyDefinition,
    FunctionDefinition,
    SymbolDefinition,
    SympyDef,
    SympyFunDef,
    SympyUndefFunDef,
)
from .Resolver import (
    DefinitionResolver,
    FunctionResToken,
    ResolverToken,
    SymbolResToken,
)

type AstTransformer = TransformerRunner[[DefinitionResolver], CasExpr]


class DefinitionStoreResolver(DefinitionResolver):
    """
    DefinitionStoreResolver resolves Definition's from some global DefinitionStore,
    from which Definition dependencies are pulled from.
    Resolved definitions are also cached, in the case they are not simple get operations.
    """

    def __init__(
        self,
        global_store: DefinitionStore,
        transformer: AstTransformer,
        args_store: Optional[DefinitionStore] = None,
        cache: Optional[MutableMapping[Any, Basic]] = None,
    ):
        super().__init__()

        self._global_store = global_store
        self._args_store = args_store or {}
        # Split args store and global store up here
        # as we do not want to propegate argument definitions to nested function calls.
        self._combined_store = ChainMap(self._args_store, self._global_store)
        self._transformer = transformer
        self._cache = cache or {}

    @override
    def get_resolver_token(self, def_id: str) -> Optional[ResolverToken]:

        if def_id not in self._combined_store:
            return None

        # split SymbolDefinition and FunctionDefinition into 2 distinct ResolverToken's
        match self.get_definition(def_id):
            case SymbolDefinition():
                return SymbolResToken(def_id)
            case FunctionDefinition():
                return FunctionResToken(def_id)
            case EmptyDefinition():
                return None
            case _:
                assert False

    @override
    def get_definition(self, def_id: str):
        if def_id not in self._combined_store:
            return None

        return self._combined_store[def_id]

    @override
    def resolve_value(self, target: SymbolResToken | SymbolDefinition):
        # verify token is correct
        cache_key = None
        match target:
            case SymbolResToken(def_id):
                # check cache
                cache_key = def_id

                if self._is_cached(cache_key, id=def_id):
                    return self._cache[cache_key]

                symbol_definition: SymbolDefinition = cast(
                    SymbolDefinition, self._combined_store[def_id]
                )
            case SymbolDefinition() as symbol_definition:
                pass
            case _:
                assert False, "Token is not of the correct type"

        # resolve value

        match symbol_definition.value:
            case SympyDef(expr):
                return expr
            case AstDef(tree):
                cas_expr = self._transformer.transform(tree, self._override_args({}))
                return self._cached(cas_expr.get_expr(-1), key=cache_key, id=def_id)
            case _:
                assert False, "Failed to resolve value"

    @override
    def resolve_body(self, target: FunctionResToken | FunctionDefinition):
        cache_key = None
        match target:
            case FunctionResToken(def_id):
                cache_key = def_id

                if self._is_cached(cache_key, id=def_id):
                    return self._cache[cache_key]

                function_definition: FunctionDefinition = cast(
                    FunctionDefinition, self._combined_store[def_id]
                )
            case FunctionDefinition() as function_definition:
                pass
            case _:
                assert False, "Token is not of the correct type"

        match function_definition.value:
            case AstFunDef(body_ast, _):
                cas_expr = self._transformer.transform(
                    body_ast, self._override_args({})
                )
                return self._cached(cas_expr.get_expr(-1), key=cache_key, id=def_id)
            case SympyFunDef(body):
                return body
            case SympyUndefFunDef(fun):
                # Undefined function's body is exactly the same as its applied value,
                # except its arguments are just its parameters.
                return fun(*self.resolve_params(target))
            case _:
                assert False, "Failed to resolve body"

    @override
    def resolve_params(self, target: FunctionResToken | FunctionDefinition):
        match target:
            case FunctionResToken(def_id):
                function_definition: FunctionDefinition = cast(
                    FunctionDefinition, self._combined_store[def_id]
                )
            case FunctionDefinition() as function_definition:
                pass
            case _:
                assert False, "Token is not of the correct type"

        return tuple(map(lambda s: Symbol(s), function_definition.params))

    @override
    def resolve_unapplied(self, target: FunctionResToken | FunctionDefinition):
        match target:
            case FunctionResToken(def_id):
                # resolve_unapplied is uncached for now.
                # not realy a reason to cache currently.

                function_definition: FunctionDefinition = cast(
                    FunctionDefinition, self._combined_store[def_id]
                )
            case FunctionDefinition() as function_definition:
                pass
            case _:
                assert False, "Token is not of the correct type"

        match function_definition.value:
            case AstFunDef(_, unapplied):
                return unapplied
            # TODO: what should SympyFunDef be here?
            case SympyUndefFunDef(fun):
                return fun
            case _:
                assert False, "Failed to resolve body"

    @override
    def resolve_applied(
        self,
        target: FunctionResToken | FunctionDefinition,
        arguments: Iterable[Definition],
    ):
        arguments = tuple(arguments)
        cache_key = None

        match target:
            case FunctionResToken(def_id):
                cache_key = (def_id, arguments)

                if self._is_cached(cache_key, id=def_id):
                    return self._cache[cache_key]

                function_definition: FunctionDefinition = cast(
                    FunctionDefinition, self._combined_store[def_id]
                )
            case FunctionDefinition() as function_definition:
                pass
            case _:
                assert False, "Token is not of the correct type"

        if len(function_definition.params) != len(arguments):
            raise ValueError(
                f"Received too {'many' if len(function_definition.params) < len(arguments) else 'few'} arguments!\nExpected {len(function_definition.params)} for parameters {function_definition.params}, got {len(arguments)} arguments"
            )

        arg_resolver = self._override_args({
            p: a for p, a in zip(function_definition.params, arguments)
        })
        match function_definition.value:
            case AstFunDef(body_ast, _):
                cas_expr = self._transformer.transform(body_ast, arg_resolver)
                return self._cached(cas_expr.get_expr(-1), key=cache_key, id=def_id)
            case SympyFunDef(body):
                # subs the resolved parameters into the body Expr.
                params = self.resolve_params(target)

                subs_dict: dict[Basic | complex, Expr] = dict()

                for param in params:
                    param_token = arg_resolver.get_resolver_token(param.name)
                    match param_token:
                        case SymbolResToken():
                            subs_dict[param] = arg_resolver.resolve_value(param_token)
                        case FunctionResToken():
                            subs_dict[param] = arg_resolver.resolve_unapplied(
                                param_token
                            )

                return body.subs(subs_dict)
            case SympyUndefFunDef(fun):
                # Create new resolver with arguments set to definition, then ask for the value

                args = []

                for param_name in function_definition.params:
                    param_token = arg_resolver.get_resolver_token(param_name)
                    match param_token:
                        case SymbolResToken():
                            args.append(arg_resolver.resolve_value(param_token))
                        case FunctionResToken():
                            args.append(arg_resolver.resolve_unapplied(param_token))

                return fun(*args)
            case _:
                assert False, "Failed to resolve body"

    def _cached(self, value: Basic, *, key: Any, id: str) -> Basic:
        """
        Try to cache the given value at the given key,
        and return the cached value

        Args:
            value (Basic): Value to cache
            key (Any): Key to cache the value under
            id (str): definition id the parent resolve call is tied to,
            this is relevant for when to *not* cache the value.
        """
        try:
            if id not in self._args_store and key is not None:
                self._cache[key] = value
        except TypeError:
            pass  # if key is unhashable, simply dont cache.
        return value

    def _is_cached(self, key: Any, *, id: str) -> bool:
        try:
            return id not in self._args_store and key in self._cache
        except TypeError:
            return False

    def _override_args(self, new_args: DefinitionStore) -> "DefinitionStoreResolver":
        """
        Return a clone of the current instance with a new args_store.
        """
        return DefinitionStoreResolver(
            self._global_store, self._transformer, new_args, self._cache
        )
