import inspect
from abc import ABC
from inspect import BoundArguments, Parameter, Signature
from typing import (
    Any,
    Callable,
    ClassVar,
    Iterable,
    Optional,
    Protocol,
    cast,
    runtime_checkable,
)

from attrs import frozen


@frozen
class Resolved[T]:
    """
    Represents a value resolved from an Ir object,
    using a ResolveStrategy.
    """

    value: T
    """
    Resolved value
    """
    post_resolve: Optional[Callable[[Any], Any]] = None
    """
    Optional post resolve handler, which
    should be called when done working with the resolved value.
    """


@runtime_checkable
class ResolveStrategy(Protocol):
    """
    Base class for all Ir resolving strategies.
    An Ir object implements many of these strategies
    """

    _resolve_method: ClassVar[str]


class ImplicitResolveStrat(ResolveStrategy):
    """
    Base class for all ResolveStrategy classes,
    which are guaranteed to be implemented by all Ir objects.
    """

    pass


class SupportsDefault(ImplicitResolveStrat):
    """
    Resolve value from Ir using some default ResolveStrategy,
    specified by supplying a type to the _default_strat static field.
    """

    _resolve_method: ClassVar[str] = "as_default"
    _default_strat: ClassVar[type[ResolveStrategy]]

    def as_default(self) -> Resolved[Any]:
        return getattr(self, self._default_strat._resolve_method)()


class SupportsBubbleUp(ImplicitResolveStrat):
    """
    Resolving a value using this strat simply returns the original Ir.
    """

    _resolve_method: ClassVar[str] = "as_bubble_up"

    def as_bubble_up(self) -> Resolved["Ir"]:
        return Resolved(cast("Ir", self))


class Ir(ABC, SupportsDefault, SupportsBubbleUp):
    """
    Base class for an Intermediate representation inside a Lark AST.
    Each implementing class specifies how a concrete value can be resolved,
    by implementing various ResolveStrategy classes.
    """

    def resolve(
        self, strategies: Iterable[type[ResolveStrategy]]
    ) -> Optional[Resolved[Any]]:
        """
        Attempt to resolve a value from the given list of strategies.
        uses the first strategy which the current Ir implements.
        """
        for capability in strategies:
            if isinstance(self, capability):
                return getattr(self, capability._resolve_method)()

        return None


def ir_strat(
    default_resolve_strat: type[ImplicitResolveStrat] = SupportsDefault,
    **resolve_strats: type[ResolveStrategy] | Iterable[type[ResolveStrategy]],
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
    resolve_strats_norm: dict[str, Iterable[type[ResolveStrategy]]] = {
        p: [s] if isinstance(s, type) else s for p, s in resolve_strats.items()
    }

    # attempt to resolve a value from the given argument, and a series of strategies to use.
    # this also returns the optional post resolver of the used IrResolverStrategy, as the second return value.
    # if arg_val is not IrStrategies, it just returns the original argument, and None
    def _try_resolve_ir_arg(arg_val: Any, strategies: Iterable[type[ResolveStrategy]]):
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
