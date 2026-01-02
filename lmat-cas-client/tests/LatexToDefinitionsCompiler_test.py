from lmat_cas_client.compiling.definitions.DefinitionStore import Definition, DefinitionStore
from lmat_cas_client.compiling.Compiler import (
    LatexToCasExprCompiler,
    LatexToDefinitionCompiler,
)
from lmat_cas_client.compiling.transforming.DependenciesTransformer import (
    dependencies_transformer_runner,
)
from lmat_cas_client.compiling.transforming.cas_expr.CasExprTransformer import (
    cas_expr_transformer_runner,
)


class TestLatexToDefinitionCompiler:
    compiler = LatexToDefinitionCompiler()

    def test_comments(self):
        result = self.compiler.compile(
            r"""
            a := \lim_{x \to 5} \frac{1}{x}
            """,
        )

        assert isinstance(result, Definition)
