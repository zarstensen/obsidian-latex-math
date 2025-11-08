import sympy

from lmat_cas_client.compiling.Definitions import SympyDefinition
from lmat_cas_client.compiling.DefinitionStore import DefinitionStore

### StandardDefinitionStore provides a DefinitionStore populated with various common mathematical constants and (soon) functions.
StandardDefinitionStore = DefinitionStore({
    # Math Constants
    r"e": SympyDefinition(sympy.E),
    r"\pi": SympyDefinition(sympy.pi),
    r"i": SympyDefinition(sympy.I),
})
