import inspect
from abc import ABC, abstractmethod
from enum import Enum, auto
from inspect import BoundArguments, Parameter, Signature
from typing import (
    Any,
    Callable,
    Iterable,
    Mapping,
    Optional,
    override,
)

from attr import frozen
from sympy import Expr


@frozen
class IrResolveStrategy:
    """
    Provide a strategy for resolving a value, typically from an Ir object captured in the callables environment
    + optionally a function to wrap the result of a rule into some other object, most likely another IrStrategies object.
    """

    resolve: Callable[[], Any]
    post_resolve: Optional[Callable[[Any], Any]] = None


class ResolveStrategyKind(Enum):
    """
    Base enum for all enum's representing some sort of strategy for resolving a value from an Ir object.
    """

    pass


class ImplicitStrat(ResolveStrategyKind):
    """
    Series of ResolveStrategyKind's which are always guaranteed to be present in an IrStrategies object.
    """

    DEFAULT = auto()
    """
    Default strategy, as specified when constructing the IrStrategies object.
    """
    BUBBLE_UP = auto()
    """
    Do not attempt to resolve any values, instead simply resolve the IrStrategies object itself
    """


type IrStrategyMap = Mapping[ResolveStrategyKind, IrResolveStrategy]


class IrStrategies:
    """
    Holds a series of IrResolveStrategy objects, each tied to a corresponding ResolveStrategyKind enum.

    """

    def __init__(self, strategies: IrStrategyMap, default_strat: ResolveStrategyKind):
        self._strategies: dict[ResolveStrategyKind, IrResolveStrategy] = dict(
            strategies
        ) | {
            ImplicitStrat.DEFAULT: strategies[default_strat],
            ImplicitStrat.BUBBLE_UP: IrResolveStrategy(lambda: self),
        }

        # sanity check that all ImplicitStrat's are always provided.
        for implicit_strat in ImplicitStrat:
            assert (
                implicit_strat in self._strategies
            ), f"ImplicitStrat {implicit_strat} missing from strategies: {self._strategies}"

    def __getitem__(self, strat_kind: ResolveStrategyKind) -> IrResolveStrategy:
        """
        Retrieve the IrResolveStrategy tied to the given ResolveStrategyKind.
        """
        return self._strategies[strat_kind]

    def __contains__(self, strat_kind: ResolveStrategyKind) -> bool:
        """
        Check if the given strat_kind is associated to an IrResolveStrategy.
        """
        return strat_kind in self._strategies

    def get_prioritized(self, ordered_strats: Iterable[ResolveStrategyKind]):
        """
        return the IrResolveStrategy of the first strat enum in ordered_strat,
        which is present in the current IrStrategies object.

        Pass an ImplicitStrat to guarantee a successfull call.
        """
        for strat in ordered_strats:
            if strat not in self:
                continue

            return self[strat]

        raise ValueError(
            "No such strategies were found! make sure to pass an ImplicitStrat to guarantee this exception is not thrown."
        )


class Ir(ABC):
    """
    Represent some data as an intermediate representation during an AST transform.
    Each Ir representation must provide a series of strategies for resolving a concrete value.

    This allows transformer rule's to provide essentially lazy evaluated multi return types.

    This is usefull for when a grammar rule may be interpreted differently, depending on the context it is in.

    f.ex:

    ...
    """

    @abstractmethod
    def strategies(self) -> IrStrategies:
        pass


# need a decorator, which takes positional arguments (by name?) an applies some strategy / multiple strategies prioritized in some order, maybe a default strategy,
# and also aplies the post_handler to the result of the strategy
# default resolve strat has to be implicit, then we now we can handle all IrStrategies.
def ir_strat(
    default_resolve_strat: ImplicitStrat = ImplicitStrat.DEFAULT,
    **resolve_strats: ResolveStrategyKind | Iterable[ResolveStrategyKind],
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
    resolve_strats_norm: dict[str, Iterable[ResolveStrategyKind]] = {
        p: [s] if isinstance(s, ResolveStrategyKind) else s
        for p, s in resolve_strats.items()
    }

    # attempt to resolve a value from the given argument, and a series of strategies to use.
    # this also returns the optional post resolver of the used IrResolverStrategy, as the second return value.
    # if arg_val is not IrStrategies, it just returns the original argument, and None
    def _try_resolve_ir_arg(arg_val: Any, strategies: Iterable[ResolveStrategyKind]):
        match arg_val:
            case IrStrategies():
                strat = arg_val.get_prioritized((*strategies, default_resolve_strat))
                return strat.resolve(), strat.post_resolve
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


# TODO: this should maybe be moved to where the other mul is
class MultStrat(ResolveStrategyKind):
    LHS = auto()
    RHS = auto()
    MULT = auto()


@frozen
class MultIr(Ir):
    lhs: Expr
    rhs: Expr

    @override
    def strategies(self) -> IrStrategies:
        return IrStrategies(
            {
                MultStrat.LHS: IrResolveStrategy(
                    lambda: self.lhs, lambda r: MultIr(r, self.rhs).strategies()
                ),
                MultStrat.RHS: IrResolveStrategy(
                    lambda: self.rhs,
                    lambda r: MultIr(self.lhs, r).strategies(),
                ),
                MultStrat.MULT: IrResolveStrategy(
                    lambda: self.lhs * self.rhs
                ),  # this should maybe be value?
            },
            MultStrat.MULT,
        )


# TODO: SYMBOL is probably going to be moved out of this one, as it
# is also needed for the diff stuff
class IndexStrat(ResolveStrategyKind):
    INDEX_VALUE = auto()
    SYMBOL = auto()


@frozen
class IndexIr(Ir):
    # TODO: implement this one
    pass

    @override
    def strategies(self):
        return IrStrategies(
            {
                IndexStrat.SYMBOL: IrResolveStrategy(lambda: None),
                IndexStrat.SYMBOL: IrResolveStrategy(lambda: None),
            },
            IndexStrat.INDEX_VALUE,
        )
