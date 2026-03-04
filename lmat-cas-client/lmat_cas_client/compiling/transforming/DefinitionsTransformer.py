from collections.abc import Iterable
from typing import ChainMap, Mapping, Optional, cast

from lark import Transformer, Tree, v_args
from sympy import Function, Symbol

from lmat_cas_client.compiling.definition.DefinitionStore import (
    AstDef,
    AstFunDef,
    DefinitionStore,
    EmptyDefinition,
    FunctionDefinition,
    SymbolDefinition,
    SympyDef,
    SympyUndefFunDef,
)
from lmat_cas_client.compiling.definition.DefinitionStoreResolver import AstTransformer
from lmat_cas_client.compiling.definition.EmptyResolver import EmptyResolver
from lmat_cas_client.compiling.transforming.cas_expr.UndefinedAtomsTransformer import (
    SymbolIr,
)
from lmat_cas_client.compiling.transforming.DependenciesTransformer import (
    DepsTransformer,
)
from lmat_cas_client.compiling.transforming.TransformerRunner import TransformerRunner


@v_args(inline=True)
class DefinitionsTransformer(Transformer):
    """
    Transform's an AST produced from cas_def.lark into a DefinitionStore.
    This transformer expects that AST's passed to expr_transformer,
    and put in definitions, is transformable without any further processing,
    by said expr_transformer.

    This can be done by removing namespaces from imported grammars,
    via the AstNamespaceRemover visitor.
    """

    def __init__(
        self,
        expr_transformer: AstTransformer,
        dependencies_transformer: DepsTransformer,
    ):
        self._expr_transformer = expr_transformer
        self._dependencies_transformer = dependencies_transformer
        pass

    def cas_expr_def(self, *stores: DefinitionStore) -> DefinitionStore:
        return dict(ChainMap(*reversed(stores)))

    def symbol_cas_expr_def(
        self, def_ast: Tree, value_ast: Optional[Tree] = None
    ) -> DefinitionStore:
        def_val: Symbol = (
            cast(SymbolIr, self._expr_transformer.transform(def_ast, EmptyResolver()))
            .as_symbol()
            .value
        )

        if value_ast is None:
            return {def_val.name: EmptyDefinition()}

        return {
            def_val.name: SymbolDefinition(
                AstDef(value_ast),
                deps=self._dependencies_transformer.transform(value_ast),  # type: ignore[arg-type]
            )
        }

    def assumption_def(self, *args: Tree | Mapping[str, bool]) -> DefinitionStore:
        symbs: Iterable[Tree] = cast(tuple[Tree], args[:-1])
        assum: Mapping[str, bool] = cast(Mapping[str, bool], args[-1])

        store: DefinitionStore = {}

        for symb in symbs:
            def_val: Symbol = (
                cast(
                    SymbolIr,
                    self._expr_transformer.transform(symb, EmptyResolver()),
                )
                .as_symbol()
                .value
            )

            store[def_val.name] = SymbolDefinition(
                SympyDef(Symbol(def_val.name, **assum))
            )

        return store

    def function_def(
        self, func_ast: Tree, params: tuple[str], body_ast: Optional[Tree] = None
    ) -> DefinitionStore:
        func: Symbol = (
            cast(SymbolIr, self._expr_transformer.transform(func_ast, EmptyResolver()))
            .as_symbol()
            .value
        )

        if body_ast is None:
            return {func.name: EmptyDefinition()}

        return {
            func.name: FunctionDefinition(
                AstFunDef(body_ast, Function(func.name)),
                params=params,
                deps=self._dependencies_transformer.transform(body_ast).difference(  # type: ignore[arg-type]
                    params
                ),
            )
        }

    def function_assumption_def(
        self, func_ast: Tree, params: tuple[str], assumptions: Mapping[str, bool]
    ) -> DefinitionStore:
        func: Symbol = (
            cast(SymbolIr, self._expr_transformer.transform(func_ast, EmptyResolver()))
            .as_symbol()
            .value
        )

        return {
            func.name: FunctionDefinition(
                SympyUndefFunDef(Function(func.name, **assumptions)), params=params
            )
        }

    def function_params(self, *params: Tree) -> tuple[str, ...]:
        return tuple(
            cast(SymbolIr, self._expr_transformer.transform(p, EmptyResolver()))
            .as_symbol()
            .value.name
            for p in params
        )

    # ==== assumption sets ====
    def SET_COMPLEX(self, _):
        return {"complex": True}

    def SET_REAL(self, _):
        return {"real": True}

    def SET_IMAGINARY(self, _):
        return {"imaginary": True}

    def SET_RATIONAL(self, _):
        return {"rational": True}

    def SET_INTEGER(self, _):
        return {"integer": True}

    def SET_NATURAL(self, _):
        return {"integer": True, "positive": True, "nonzero": True}

    def SET_EVEN(self, _):
        return {"even": True}

    def SET_ODD(self, _):
        return {"odd": True}

    def SET_PRIME(self, _):
        return {"prime": True}

    def ext_real_set(self, *_):
        return {"extended_real": True}

    def algebraic_set(self, *_):
        return {"algebraic": True}

    def positive_set(self, assum: Mapping[str, bool], *_):
        return {**assum, "positive": True}

    def nonnegative_set(self, assum: Mapping[str, bool], *_):
        return {**assum, "nonnegative": True}

    def negative_set(self, assum: Mapping[str, bool], *_):
        return {**assum, "negative": True}

    def nonpositive_set(self, assum: Mapping[str, bool], *_):
        return {**assum, "nonpositive": True}

    def natural0_set(self, assum: Mapping[str, bool], *_):
        return {**assum, "nonzero": False}


definitions_transformer_runner = TransformerRunner[
    [AstTransformer, DepsTransformer],
    DefinitionStore,
](DefinitionsTransformer)

__all__ = ["definitions_transformer_runner"]
