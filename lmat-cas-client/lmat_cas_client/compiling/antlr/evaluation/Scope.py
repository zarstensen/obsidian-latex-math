from __future__ import annotations

from abc import abstractmethod
from collections import defaultdict
from typing import Callable, Iterable, MutableMapping, Protocol, Self, cast

from attrs import frozen
from sortedcontainers import SortedList

from lmat_cas_client.compiling.antlr import Ast


# literal param stores the literal value itself +
#
@frozen
class LiteralParam:
    type EqChecker = Callable[[LiteralParam, LiteralParam], bool]
    value: Ast.AExpr


type LiteralParams = tuple[LiteralParam, ...]


# bound param stores how it should be bounded, that makes sense
# not any reason to store anything else
@frozen
class BoundParam:
    signature: Signature


type Param = LiteralParam | BoundParam
type Params = tuple[Param, ...]

type HeadId = str


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self: Self, other: Self, /) -> bool: ...


@frozen
class Signature:
    type GroupKey = tuple[HeadId, Ast.SubscriptForm, int]
    type SortKey = tuple[int, int]

    head_id: HeadId
    subscript_form: Ast.SubscriptForm = Ast.SubscriptForm((None, None), ())
    index_params: Params = ()
    arg_params: Params = ()

    @staticmethod
    def from_a_expr(a_expr: Ast.AExpr) -> Signature | None:

        """
        Convert the given AExpr to an equivalent scope Signature, if it were to be a definition in a Scope.
        If this is not possible, return None.
        """
        head_id = None
        subscript_form = Ast.SubscriptForm((None, None), ())
        index_params: tuple[Ast.AExpr, ...] = ()
        arg_params: tuple[Ast.AExpr, ...] = ()

        match a_expr:
            # lone symbol: x
            case Ast.Symbol(_, symbol_name):
                head_id = symbol_name
                pass
            # subscritped symbol: x_i
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
        return (self.head_id, self.subscript_form, len(self.arg_params))

    def sort_key(self) -> SortKey:
        def litteral_count(params: Params) -> int:
            return sum(1 for p in params if p is LiteralParam)

        return (
            litteral_count(self.index_params),
            litteral_count(self.arg_params),
        )

    def overrideSigs(
        self, other: Self, literal_comparer: LiteralParam.EqChecker
    ) -> tuple[Definition, ...] | None:
        if (
            self.head_id != other.head_id
            or len(self.index_params) != len(other.index_params)
            or len(self.arg_params) != len(other.arg_params)
        ):
            return None

        things = []

        for param, other_param in (
            *zip(self.index_params, other.index_params),
            *zip(self.arg_params, other.arg_params),
        ):
            match (param, other_param):
                # TODO: some comments for this scenario explaining it.
                # what is this scenario
                # that is if we have f_{10} as the signature and f_{*bound*} as the thing it wants to match
                case (LiteralParam(), BoundParam()):
                    return None
                case (LiteralParam(), LiteralParam()):
                    if not literal_comparer(param, other_param):
                        return None
                case (BoundParam(sig), LiteralParam(literal)):
                    things.append((sig, literal))

        return tuple(things)

    def __attrs_post_init__(self):
        index_param_count = len(self.index_params)
        slot_seps_count = len(self.subscript_form.slot_seps)
        # TODO: better assert fail messages
        assert (
            index_param_count == 0
            and slot_seps_count == 0
            or index_param_count - 1 == slot_seps_count
        ), "Subscript form separators and index parameters did not match up!"

type OptDefinition = tuple[Signature, Ast.AExpr | None]
type Definition = tuple[Signature, Ast.AExpr]



# this stays the same right?
# its just the transformer which is new?
# this is also cleaner interms of separation and stuff i guess...
class Definitions:

    type Id = int
    type _DefEntry = tuple[Signature.SortKey, Id]

    def __init__(self: Self):
        self._next_id = 0
        self._definitions: MutableMapping[Definitions.Id, OptDefinition] = dict()

        self.signatures: MutableMapping[Signature.GroupKey, SortedList[Definitions._DefEntry]] = (
            defaultdict(lambda: SortedList())
        )

    def register(self: Self, definitions: tuple[OptDefinition, ...]) -> tuple[Id, ...]:
        ids = []

        for defi in definitions:
            ids.append(self.register_single(defi))

        return tuple(ids)

    def register_single(self: Self, definition: OptDefinition) -> Id:
        def_id = self._next_id
        self._next_id += 1

        return self.reregister_single(definition, def_id)


    # also adds a definition with the given ID if it does not exist, but overwrites if it does exist
    def reregister_single(self, definition: OptDefinition, definition_id: Id):
        if definition_id in self._definitions:
            self.unregister_single(definition_id)

        self._definitions[definition_id] = definition

        signature, _ = definition
        self.signatures[signature.group_key()].add((signature.sort_key(), definition_id))

        return definition_id

    def unregister(self: Self, definition_ids: tuple[Id, ...]):
        for def_id in definition_ids:
            self.unregister_single(def_id)

    def unregister_single(self: Self, definition_id: Id):
        if definition_id not in self._definitions:
            return

        signature, _ = self._definitions[definition_id]

        signature_group = self.signatures[signature.group_key()]

        signature_group.discard(next(filter(lambda de: de[1] == definition_id, signature_group)))

        del self._definitions[definition_id]

        if len(signature_group) == 0:
            del self.signatures[signature.group_key()]

    # so just loop over this one until it matches one, and then that is it
    def _overrides(self, signature: Signature) -> Iterable[Id]:
        return map(lambda de: de[1], reversed(self.signatures.get(signature.group_key(), ())))

    def get_definition(self, id: Id) -> Definition:
        opt_def = self.get_opt_definition(id)

        match opt_def:
            case _, None:
                raise KeyError("The given definition id points to a defintion with a None body")
            case sig, bod:
                return (sig, bod)

    def get_opt_definition(self, id: Id) -> OptDefinition:
        return self._definitions[id]

    def resolve(
        self, signature: Signature, lit_eq_checker: LiteralParam.EqChecker
    ) -> tuple[Id, tuple[Definition, ...]] | None:

        for def_id in self._overrides(signature):
            sig, bod = self.get_opt_definition(def_id)
            res = sig.overrideSigs(signature, lit_eq_checker)
            if res is not None:
                return (def_id, res) if bod is not None else None
        return None
