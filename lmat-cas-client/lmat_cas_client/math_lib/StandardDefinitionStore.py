import sympy

from lmat_cas_client.compiling.definition.DefinitionStore import (
    DefinitionStore,
    SymbolDefinition,
    SympyDef,
)

"""
StandardDefinitionStore provides a DefinitionStore populated with various common mathematical constants and (soon) functions.
"""
StandardDefinitionStore: DefinitionStore = {
    # Math Constants
    r"e": SymbolDefinition(SympyDef(sympy.E)),
    r"\pi": SymbolDefinition(SympyDef(sympy.pi)),
    r"i": SymbolDefinition(SympyDef(sympy.I)),
}
