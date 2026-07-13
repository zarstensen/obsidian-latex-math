from abc import ABC
from typing import Callable, cast

import attrs
from antlr4 import ParserRuleContext
from attrs import evolve, field, frozen


@frozen
class AstNode(ABC):
    ctx: ParserRuleContext = field(repr=False, eq=False)

    def mut_ctx[T: AstNode](self: T, ctx: ParserRuleContext) -> T:
        return evolve(self, ctx=ctx)

LocRange = tuple[int, int]

def ctx_to_loc(ctx: ParserRuleContext) -> LocRange:
    """
    Extract location information from a ParserRuleContext object into a LocRange.
    """
    start_token = ctx.start
    end_token = ctx.stop

    assert start_token is not None and end_token is not None

    return (start_token.start, end_token.stop)


def visit_children[TNode: AstNode, TChild: AstNode](
    node: TNode,
    visitor: Callable[[TChild], TChild],
    exclude_children: set[attrs.Attribute] | None = None,
):
    """
    Call visitor on all fields of node which extend AstNode.
    This also includes all AstNode's in arbitrarily nested tuples and lists.

    the visitor returns a new child node which the previous child is replaced with.
    returns a new version of node, which contains the newly replaced children.

    visitor is not invoked for fields present in exclude_children.
    """

    def _visit_nested(
        val: object,
        visitor: Callable[[TChild], TChild],
    ) -> object:
        match val:
            case AstNode() as child:
                child = visit_children(child, visitor)
                return visitor(cast(TChild, child))
            case (list() | tuple()) as children:
                return type(children)(
                    _visit_nested(child, visitor) for child in children
                )
            case _:
                return val

    exclude_children = exclude_children or set()

    node_fields: tuple[attrs.Attribute[TNode]] = attrs.fields(type(node))

    new_children: dict[str, object] = {}

    for field in node_fields:
        field_val = getattr(node, field.name)

        if field in exclude_children:
            continue

        new_val = _visit_nested(field_val, visitor)
        if new_val is not field_val:
            new_children[field.name] = new_val

    return attrs.evolve(node, **new_children)
