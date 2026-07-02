from __future__ import annotations

from abc import abstractmethod
from collections import defaultdict
from typing import Callable, Iterator, MutableMapping, Protocol, Self

import sympy as sp
from attrs import frozen
from sortedcontainers import SortedList

from lmat_cas_client.compiling.antlr import Ast

type SpVal = sp.Basic | sp.MatrixBase


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

    def group_key(self) -> GroupKey:
        return (self.head_id, self.subscript_form, len(self.arg_params))

    def sort_key(self) -> SortKey:
        def bound_count(params: Params) -> int:
            return sum(1 for p in params if p is BoundParam)

        return (
            bound_count(self.index_params),
            bound_count(self.arg_params),
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


type Definition = tuple[Signature, Ast.AExpr]


# do a substitution on the entire AST?

class Scope:

    @staticmethod
    def _definition_key(definition: Definition):
        signature, _ = definition
        return signature.sort_key()

    def __init__(self: Self):
        self.signatures: MutableMapping[Signature.GroupKey, SortedList[Definition]] = (
            defaultdict(lambda: SortedList(key=Scope._definition_key))
        )

    def register(self: Self, definitions: tuple[Definition, ...]):
        for defi in definitions:
            self.register_single(defi)

    def register_single(self: Self, definition: Definition):
        signature, body = definition
        self.signatures[signature.group_key()].add((signature, body))

    def unregister(self: Self, definitions: tuple[Definition, ...]):
        for defi in definitions:
            self.unregister_single(defi)

    def unregister_single(self: Self, definition: Definition):
        signature, _ = definition
        if signature.group_key() not in self.signatures:
            return

        self.signatures[signature.group_key()].discard(definition)

        if len(self.signatures[signature.group_key()]) == 0:
            del self.signatures[signature.group_key()]

    # so just loop over this one until it matches one, and then that is it
    def _overrides(self, signature: Signature) -> Iterator[Definition]:
        return self.signatures.get(signature.group_key(), ())

    # what should this return even? a list of the new signatures + bodies, and the body itself maybe?
    # so this resolves the expression the signature is associated with + the definitions which should be present when evaluating it.
    def resolve(
        self, signature: Signature, lit_eq_checker: LiteralParam.EqChecker
    ) -> tuple[Ast.AExpr, tuple[Definition, ...]] | None:

        for sig, bod in self._overrides(signature):
            res = sig.overrideSigs(signature, lit_eq_checker)
            if res is not None:
                return (bod, res)
        return None
