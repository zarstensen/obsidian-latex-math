from __future__ import annotations

from collections import defaultdict
from typing import Callable, Iterable, MutableMapping, Self, cast

from attrs import frozen
from sortedcontainers import SortedList

from lmat_cas_client.compiling.antlr import Ast


@frozen
class LiteralParam:
    """
    Represents a parameter in a definition which must always obtain a specific literal value.
    """

    type EqChecker = Callable[[LiteralParam, LiteralParam], bool]
    """
    :class:`LiteralParam` s store ASTs but their equality should not be based on the ASTs themselves,
    as this also checks if the structure, not only the value represented by the ASTs are equal.

    Instead, one has to supply a custom function which checks whether the ASTs stored by the
    :class:`LiteralParam` s store the same *value*, regardless of the structure of the individual ASTs themselves.
    """

    literal: Ast.AExpr

type LiteralParams = tuple[LiteralParam, ...]


@frozen
class BoundParam:
    """
    Represents a parameter in a definition, which can be bounded to an arbitrary argument.
    """

    signature: Signature
    """
    The :class:`Signature` which the bound value should use to register itself in a :class:`Definitions` object.
    """


type Param = LiteralParam | BoundParam
type Params = tuple[Param, ...]

type HeadId = str
"""
Type alias for the "head" of a :class:`Signature`.
This refers to the primary symbol of the :class:`Signature`, appearing before any potential subscript or function arguments.
e.g. ``"x"`` is the head id for ``x_{i}`` and ``"f"`` is the head id for ``f(x)``
"""

@frozen
class Signature:
    """
    Represents a "key" in a :class:`Definitions` object which maps the signature of a symbol to a concrete defined value.
    """

    type GroupKey = tuple[HeadId, Ast.SubscriptForm, int]
    """
    If 2 signatures have the same :class:`GroupKey` they act as overrides for the same symbol.
    If they do not have the same :class:`GroupKey`, they are not signatures for the same symbol.

    e.g. ``x_{1,2}`` and ``x_{y,z}`` have the same group key
    (same :data:`HeadId`, same :class:`~Ast.SubscriptForm`, and same no. func args)
    and in this case ``x_{1,2}`` would act as an override to ``x_{y,z}``
    (assuming ``y`` and ``z`` are :class:`BoundParam` s).

    where ``f(1)`` and ``f(x, y)`` do not have the same group key (different no. func args),
    so any function call of the form ``f(..., ...)`` will never look for a value tied to the ``f(1)`` signature.
    """

    type OverridePriorityKey = tuple[int, int]
    """
    The :class:`OverridePriorityKey` describes the priority of a specific :class:`Signature` over other
    signatures with the same :class:`GroupKey`.
    If 2 signatures have the same :class:`GroupKey` and are both valid candidates for some symbol
    or function application, the one with the largest :class:`OverridePriorityKey` should be picked.
    """

    head_id: HeadId
    subscript_form: Ast.SubscriptForm = Ast.SubscriptForm()
    index_params: Params = ()
    arg_params: Params = ()

    @staticmethod
    def from_a_expr(a_expr: Ast.AExpr) -> Signature | None:
        """
        Tries to convert the given :class:`~Ast.AExpr` into a :class:`Signature`.
        This is only possible if the expression is a symbol (optionally with a subscript) or a function application.

        Returns:
            :class:`Signature` object with :attr:`head_id` and :attr:`subscript_form` derived from the
            ``a_expr``. :attr:`index_params` and :attr:`arg_params` are populated with
            :class:`LiteralParam` s.
            If a :class:`Signature` object cannot be constructed from the expression, ``None`` is returned.
        """
        head_id = None
        subscript_form = Ast.SubscriptForm()
        index_params: tuple[Ast.AExpr, ...] = ()
        arg_params: tuple[Ast.AExpr, ...] = ()

        match a_expr:
            # lone symbol: x
            case Ast.Symbol(_, symbol_name):
                head_id = symbol_name
                pass
            # subscripted symbol: x_i
            case Ast.SubscriptOp(_, Ast.Symbol(_, symbol_name), subscript) if all(
                isinstance(slot, Ast.AExpr) for slot in subscript.slots
            ):
                head_id = symbol_name
                subscript_form = subscript.form
                index_params = cast(tuple[Ast.AExpr, ...], subscript.slots)
            # function call: f(x)
            case Ast.ApplyFunc(_, Ast.Symbol(_, symbol_name), args):
                head_id = symbol_name
                arg_params = args
            # function call with subscripted symbol: f_i(x)
            case Ast.ApplyFunc(
                _, Ast.SubscriptOp(_, Ast.Symbol(_, symbol_name), subscript), args
            ) if all(isinstance(slot, Ast.AExpr) for slot in subscript.slots):
                head_id = symbol_name
                subscript_form = subscript.form
                index_params = cast(tuple[Ast.AExpr, ...], subscript.slots)
                arg_params = args
            case _:
                return None

        return Signature(
            head_id,
            subscript_form,
            tuple(LiteralParam(e) for e in index_params),
            tuple(LiteralParam(e) for e in arg_params),
        )

    def group_key(self) -> GroupKey:
        """
        Construct a :class:`GroupKey` for the current :class:`Signature`.
        """
        return (self.head_id, self.subscript_form, len(self.arg_params))

    def override_priority_key(self) -> OverridePriorityKey:
        """
        Construct an :class:`OverridePriorityKey` for the current :class:`Signature`.
        """

        def litteral_count(params: Params) -> int:
            return sum(1 for p in params if p is LiteralParam)

        return (
            litteral_count(self.index_params),
            litteral_count(self.arg_params),
        )

    def try_bind(
        self, target: Signature, literal_comparer: LiteralParam.EqChecker
    ) -> tuple[Binding, ...] | None:
        """
        Try to bind the :class:`LiteralParam` s of some target :class:`Signature` to the
        current signature's :class:`BoundParam` s.
        This fails if the :class:`GroupKey` s are not the same *or* a :class:`LiteralParam` in the
        current signature is not equal to a :class:`LiteralParam` in the target signature.
        This also fails if the current :class:`Signature` has a :class:`LiteralParam` where the
        target :class:`Signature` has a :class:`BoundParam`.

        Args:
            literal_comparer: Callable used to determine if 2 :class:`LiteralParam` s should be
                considered equal.

        Returns:
            Tuple of :class:`Definition` s representing the bindings needed to bind the target
            :class:`Signature` to the current :class:`Signature`.
            If target could not be bound to the current :class:`Signature`, ``None`` is returned.
        """

        # signatures can only be bound to other signatures with the *same* GroupKey.
        if self.group_key() != target.group_key():
            return None

        bindings = []

        for param, target_param in (
            *zip(self.index_params, target.index_params),
            *zip(self.arg_params, target.arg_params),
        ):
            match (param, target_param):
                case (BoundParam(sig), LiteralParam(literal)):
                    # produce a binding here to the literal parameter.
                    bindings.append((sig, literal))
                case (LiteralParam(), LiteralParam()):
                    # 2 literal parameters must always be equal, before try_bind can succeed.
                    # otherwise one would be able to bind e.g. x_{1,2} to x_{2,z} which would not make sense.
                    if not literal_comparer(param, target_param):
                        return None
                case (LiteralParam(), BoundParam()):
                    # if we ever encounter this param combo, it means the current signature is more strict
                    # for this parameter, than the target.
                    # this should fail the bind, otherwise binding e.g. x_{y,z} to x_{1,2} would be valid.
                    return None

        return tuple(bindings)

    def bind(self, target: Signature, literal_comparer: LiteralParam.EqChecker) -> tuple[Binding, ...]:
        bindings = self.try_bind(target, literal_comparer)

        if bindings is None:
            raise ValueError("Target signature could not be bound to self.")

        return bindings

    def __attrs_post_init__(self):
        index_param_count = len(self.index_params)
        slot_seps_count = len(self.subscript_form.slot_seps)
        assert (
            index_param_count == 0
            and slot_seps_count == 0
            or index_param_count - 1 == slot_seps_count
        ), (
            f"Subscript form separators ({slot_seps_count}) and index parameters ({index_param_count})"
            f" did not match up!"
        )


type OptBinding = tuple[Signature, Ast.AExpr | None]

type Binding = tuple[Signature, Ast.AExpr]


class Scope:
    """
    The Scope object manages a set of bindings from Signatures to Ast.AExpr objects.
    Each binding has an ID associated with it, which can be used to unregister, or reregister (no change in override priority)
    the binding.
    """

    type BindingId = int
    type _DefEntry = tuple[Signature.OverridePriorityKey, Scope.BindingId]

    def __init__(self: Self):
        self._next_id = 0

        self._bindings: MutableMapping[Scope.BindingId, OptBinding] = dict()

        self._signature_priority_list: MutableMapping[
            Signature.GroupKey, SortedList[Scope._DefEntry]
        ] = defaultdict(lambda: SortedList())

    def register(self: Self, definitions: tuple[OptBinding, ...]) -> tuple[BindingId, ...]:
        ids = []

        for defi in definitions:
            ids.append(self.register_single(defi))

        return tuple(ids)

    def register_single(self: Self, binding: OptBinding) -> BindingId:
        """
        Register the given binding in the scope.
        Returns:
            BindingId to be used for reregistering or unregistering the binding.
        """
        def_id = self._next_id
        self._next_id += 1

        return self.reregister_single(binding, def_id)

    def reregister_single(self, binding: OptBinding, binding_id: BindingId):
        """
        Registers the given binding with the given binding_id.
        If a binding already exists with this id, it is replaced with the new binding.
        """
        if binding_id in self._bindings:
            self.unregister_single(binding_id)

        self._bindings[binding_id] = binding

        signature, _ = binding
        self._signature_priority_list[signature.group_key()].add(
            (signature.override_priority_key(), binding_id)
        )

    def unregister(self: Self, definition_ids: tuple[BindingId, ...]):
        for def_id in definition_ids:
            self.unregister_single(def_id)

    def unregister_single(self: Self, binding_id: BindingId):
        """
        Removes the binding associated with the given id from the scope.
        """

        if binding_id not in self._bindings:
            return

        signature, _ = self._bindings[binding_id]

        signature_group = self._signature_priority_list[signature.group_key()]

        signature_group.discard(
            next(filter(lambda de: de[1] == binding_id, signature_group))
        )

        del self._bindings[binding_id]

        if len(signature_group) == 0:
            del self._signature_priority_list[signature.group_key()]


    def get_binding(self, id: BindingId) -> Binding:
        """
        Retrieve the binding associated with the given id.
        The result is guaranteed to not bind to None.

        Raises:
            KeyError: No binding has the given id *or* the binding binds to None.
        """
        opt_def = self.get_opt_binding(id)

        match opt_def:
            case _, None:
                raise KeyError(
                    "The given definition id points to a defintion with a None body"
                )
            case sig, bod:
                return (sig, bod)

    def get_opt_binding(self, id: BindingId) -> OptBinding:
        """
        Retrieve the binding associated with the given id.
        """
        return self._bindings[id]

    def resolve(
        self, signature: Signature, lit_eq_checker: LiteralParam.EqChecker
    ) -> BindingId | None:
        """
        Resolves the highest prioritised binding, which the given signature can bind itself to.
        Priority is determined first by the bindings OverridePriorityKey and secondly by registration order
        (later registration are prioritized higher).

        Returns:
            The BindingId of the resolved binding if present *unless* it binds to None, then None is returned instead.
        """
        for binding_id in self._get_binding_candidates(signature):
            sig, bod = self.get_opt_binding(binding_id)
            res = sig.try_bind(signature, lit_eq_checker)
            if res is not None:
                return binding_id if bod is not None else None

        return None

    def _get_binding_candidates(self, signature: Signature) -> Iterable[BindingId]:
        """
        helper method for indexing into the _signature_priority_list map.
        signatures are stored in *reversed* priority order, due to how SortedList handles order of equal values.
        This function ensures the list is returned in the correct order.
        """
        return map(
            lambda de: de[1], reversed(self._signature_priority_list.get(signature.group_key(), ()))
        )
