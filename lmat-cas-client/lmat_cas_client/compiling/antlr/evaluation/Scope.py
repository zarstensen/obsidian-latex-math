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

type Definition = tuple[Signature, Ast.AExpr]


# this stays the same right?
# its just the transformer which is new?
# this is also cleaner interms of separation and stuff i guess...
class Scopes:

    @staticmethod
    def _definition_key(definition: Definition):
        signature, _ = definition
        return signature.sort_key()

    def __init__(self: Self):
        self.signatures: MutableMapping[Signature.GroupKey, SortedList[Definition]] = (
            defaultdict(lambda: SortedList(key=Scopes._definition_key))
        )

    # TODO: there are some ways of going about undefining variables:
    # a) remove all definitions from the scope (this could also be a function?)
    # b) have an explicit value, which indicates variable is undefined
    # c) have an explicit function, which marks the variable as being undefined
	# d) have a stack of scopes which can be pushed and popped, then somehow one can also mutate a scope already in the stack.
	#    finding a definition is then a matter of searching through the scopes individually?
	#    Its a bit wierd because a scope in this context is not intuitive? so resolving a definition happens in a new scope, as well as sum, limits, products, integrals and differentials maybe?
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

    def unregister_signature(self: Self, signature: Signature, lit_eq_checker: LiteralParam.EqChecker) -> tuple[Definition, ...]:
        unregistered_defs: list[Definition] = []

        resolved = self.resolve(signature, lit_eq_checker)

        while resolved is not None:

            resolved_sig, resolved_body, _ = resolved

            self.unregister_single((resolved_sig, resolved_body))
            unregistered_defs.append((resolved_sig, resolved_body))

            resolved = self.resolve(signature, lit_eq_checker)

        return tuple(reversed(unregistered_defs))


    # so just loop over this one until it matches one, and then that is it
    def _overrides(self, signature: Signature) -> Iterable[Definition]:
        return reversed(self.signatures.get(signature.group_key(), ()))

    # what should this return even? a list of the new signatures + bodies, and the body itself maybe?
    # so this resolves the expression the signature is associated with + the definitions which should be present when evaluating it.
    def resolve(
        self, signature: Signature, lit_eq_checker: LiteralParam.EqChecker
    ) -> tuple[Signature,Ast.AExpr, tuple[Definition, ...]] | None:

        for sig, bod in self._overrides(signature):
            res = sig.overrideSigs(signature, lit_eq_checker)
            if res is not None:
                # body is None => this should explicitly *not* be defined
                return (sig, bod, res) if bod is not None else None 
        return None

class Scopes:
	def __init__(self):
		self.scopes = []
	
	def push_scope(self, scope: Scopes):
		self.scopes.append(scope)
	
	def remove_scope(self, scope: Scopes):
		self.scopes.remove(scope)
	
	def resolve(self, signature: Signature, lit_eq_checker: LiteralParam.EqChecker) -> tuple[Signature, Ast.AExpr, tuple[Definition, ...], Scopes] | None:
		for scope in reversed(self.scopes):

			res = scope.resolve(signature, lit_eq_checker)

			if res is not None:
				sig, bod, defs = res
				return sig, bod, defs, scope

		return None
