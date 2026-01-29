import inspect
from abc import ABC, abstractmethod
from inspect import BoundArguments, Parameter, Signature
from typing import (
    Any,
    Callable,
    ClassVar,
    Iterable,
    Optional,
    Protocol,
    Self,
    override,
    runtime_checkable,
)

from attr import frozen
from sympy import Expr


@frozen
class Resolved[T]:
    value: T
    post_resolve: Optional[Callable[[Any], Any]] = None


@runtime_checkable
class Capability(Protocol):
    _resolve_method: ClassVar[str]


class ImplicitCapability(Capability):
    pass


class SupportsDefault(ImplicitCapability):
    _resolve_method: ClassVar[str] = "as_default"
    _default_strat: ClassVar[type[Capability]]

    def as_default(self) -> Resolved[Any]:
        return getattr(self, self._default_strat._resolve_method)()


class SupportsBubbleUp(ImplicitCapability):
    _resolve_method: ClassVar[str] = "as_bubble_up"

    def as_bubble_up(self) -> Resolved[Self]:
        return Resolved(self)


class Ir(ABC, SupportsDefault, SupportsBubbleUp):
    def resolve(
        self, capabilities: Iterable[type[Capability]]
    ) -> Optional[Resolved[Any]]:
        for capability in capabilities:
            if isinstance(self, capability):
                return getattr(self, capability._resolve_method)()

        return None


# need a decorator, which takes positional arguments (by name?) an applies some strategy / multiple strategies prioritized in some order, maybe a default strategy,
# and also aplies the post_handler to the result of the strategy
# default resolve strat has to be implicit, then we now we can handle all IrStrategies.
def ir_strat(
    default_resolve_strat: type[ImplicitCapability] = SupportsDefault,
    **resolve_strats: type[Capability] | Iterable[type[Capability]],
):
    """
    Decorator for handling automatic resolution of IrStrategies objects passed to decorated function.

    If an IrStrategies is passed, then this decorator first looks for a valid strategy present in resolve_strats,
    under the parameter name the IrStrategies was passed to, and otherwise uses the default_resolve_strat to resolve a value
    from the IrStrategies object.
    Said resolved value is then passed as the actual argument to the decorated function.

    :param default_resolve_strat: Default ResolveStrategyKind to use for arguments not explicitly passed.
    Must be an ImplicitStrat, so a value is guaranteed to be resolved.
    :type default_resolve_strat: ImplicitStrat
    :param resolve_strats: Parameters in the decorated function (keys) and a (optionally list of) ResolveStrategyKind to use
    on the arguments to said parameters, before the decorated function is called.
    :type resolve_strats: ResolveStrategyKind | Iterable[ResolveStrategyKind]
    """

    # make sure all elements are iterables,
    # this makes some logic later down the line easier to handle.
    resolve_strats_norm: dict[str, Iterable[type[Capability]]] = {
        p: [s] if isinstance(s, type) else s for p, s in resolve_strats.items()
    }

    # attempt to resolve a value from the given argument, and a series of strategies to use.
    # this also returns the optional post resolver of the used IrResolverStrategy, as the second return value.
    # if arg_val is not IrStrategies, it just returns the original argument, and None
    def _try_resolve_ir_arg(arg_val: Any, strategies: Iterable[type[Capability]]):
        match arg_val:
            case Ir():
                strat = arg_val.resolve((*strategies, default_resolve_strat))
                assert strat is not None
                return strat.value, strat.post_resolve
            case _:
                return arg_val, None

    # apply resolution strategies to all args in the passed bound_args object.
    # andlers *args and **kwargs, as if each entry in the tuple / dict is a unique argument.
    def _apply_ir_strategies_to_args(
        bound_args: BoundArguments, func_signature: Signature
    ):
        post_resolvers = []

        for param_name, arg_val in bound_args.arguments.items():
            param = func_signature.parameters[param_name]

            # check if we should treat this argument differently.
            match param.kind:
                case Parameter.VAR_KEYWORD:
                    for key, value in arg_val.items():
                        resolved_val, post_resolver = _try_resolve_ir_arg(
                            value,
                            resolve_strats_norm.get(param_name) or [],
                        )

                        # modify arguments in place
                        bound_args.arguments[param_name][key] = resolved_val

                        if post_resolver is not None:
                            post_resolvers.append(post_resolver)

                case Parameter.VAR_POSITIONAL:
                    # we have to build a whole new list here,
                    # as the tuple the varargs are stored in is immutable
                    new_vargs = []
                    for value in arg_val:
                        resolved_val, post_resolver = _try_resolve_ir_arg(
                            value,
                            resolve_strats_norm.get(param_name) or [],
                        )

                        new_vargs.append(resolved_val)

                        if post_resolver is not None:
                            post_resolvers.append(post_resolver)

                    bound_args.arguments[param_name] = tuple(new_vargs)

                case _:
                    resolved_val, post_resolver = _try_resolve_ir_arg(
                        arg_val,
                        resolve_strats_norm.get(param_name) or [],
                    )

                    bound_args.arguments[param_name] = resolved_val

                    if post_resolver is not None:
                        post_resolvers.append(post_resolver)

        return post_resolvers

    def _decorator(func):
        func_signature = inspect.signature(func)

        def _wrapper(*args, **kwargs):
            bound_args = func_signature.bind(*args, **kwargs)
            bound_args.apply_defaults()

            post_resolvers = _apply_ir_strategies_to_args(bound_args, func_signature)

            result = func(*bound_args.args, **bound_args.kwargs)

            for post_resolve in post_resolvers:
                result = post_resolve(result)

            return result

        return _wrapper

    return _decorator


# IMPLS move down
class SupportsLhs(Capability):
    _resolve_method: ClassVar[str] = "as_lhs"

    @abstractmethod
    def as_lhs(self) -> Resolved[Expr]:
        pass


class SupportsRhs(Capability):
    _resolve_method: ClassVar[str] = "as_rhs"

    @abstractmethod
    def as_rhs(self) -> Resolved[Expr]:
        pass


class SupportsMult(Capability):
    _resolve_method: ClassVar[str] = "as_mult"

    @abstractmethod
    def as_mult(self) -> Resolved[Expr]:
        pass


@frozen
class MultIr(Ir, SupportsLhs, SupportsRhs, SupportsMult):
    lhs: Expr
    rhs: Expr

    _default_strat = SupportsMult

    @override
    def as_lhs(self):
        return Resolved(self.lhs, lambda r: MultIr(r, self.rhs))

    @override
    def as_rhs(self):
        return Resolved(self.rhs, lambda r: MultIr(self.lhs, r))

    @override
    def as_mult(self):
        return Resolved(self.lhs * self.rhs)


# TODO: this should maybe be moved to where the other mul is
# class MultStrat(ResolveStrategyKind):
#     LHS = auto()
#     RHS = auto()
#     MULT = auto()


# @frozen
# class MultIr(Ir):
#     lhs: Expr
#     rhs: Expr

#     @override
#     def strategies(self) -> IrStrategies:
#         return IrStrategies(
#             {
#                 MultStrat.LHS: IrResolveStrategy(
#                     lambda: self.lhs, lambda r: MultIr(r, self.rhs).strategies()
#                 ),
#                 MultStrat.RHS: IrResolveStrategy(
#                     lambda: self.rhs,
#                     lambda r: MultIr(self.lhs, r).strategies(),
#                 ),
#                 MultStrat.MULT: IrResolveStrategy(
#                     lambda: self.lhs * self.rhs
#                 ),  # this should maybe be value?
#             },
#             MultStrat.MULT,
#         )


# # TODO: SYMBOL is probably going to be moved out of this one, as it
# # is also needed for the diff stuff
# class IndexStrat(ResolveStrategyKind):
#     INDEX_VALUE = auto()
#     SYMBOL = auto()


# @frozen
# class IndexIr(Ir):
#     # TODO: implement this one
#     pass

#     @override
#     def strategies(self):
#         return IrStrategies(
#             {
#                 IndexStrat.SYMBOL: IrResolveStrategy(lambda: None),
#                 IndexStrat.SYMBOL: IrResolveStrategy(lambda: None),
#             },
#             IndexStrat.INDEX_VALUE,
#         )


# class SymbolStrat(ResolveStrategyKind):
#     SUBSTITUTE = auto()
#     SYMBOL = auto()


# @frozen
# class SymbolIr(Ir):
#     resolver: DefinitionResolver
#     symbol: Symbol

#     @override
#     def strategies(self):
#         def substitute():
#             match self.resolver.get_resolver_token(self.symbol.name):
#                 case SymbolResToken() as token:
#                     return cast(Expr, self.resolver.resolve_value(token))
#                 case FunctionResToken() as token:
#                     return cast(Expr, self.resolver.resolve_unapplied(token))
#                 case _:
#                     return self.symbol

#         return IrStrategies(
#             {
#                 SymbolStrat.SUBSTITUTE: IrResolveStrategy(substitute),
#                 SymbolStrat.SYMBOL: IrResolveStrategy(lambda: self.symbol),
#             },
#             SymbolStrat.SUBSTITUTE,
#         )
