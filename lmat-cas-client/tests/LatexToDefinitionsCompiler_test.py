from lmat_cas_client.compiling.Compiler import (
    LatexToDefinitionCompiler,
)
from lmat_cas_client.compiling.definition.DefinitionStore import (
    Definition,
)
from lmat_cas_client.compiling.transforming.cas_expr.CasExprTransformer import (
    cas_expr_transformer_runner,
)
from lmat_cas_client.compiling.transforming.DependenciesTransformer import (
    dependencies_transformer_runner,
)


class TestLatexToDefinitionCompiler:
    compiler = LatexToDefinitionCompiler(
        cas_expr_transformer_runner, dependencies_transformer_runner
    )

    def test_comments(self):
        result = self.compiler.compile(
            r"""
            a := \lim_{x \to 5} \frac{1}{x}
            """,
        )

        assert isinstance(result, Definition)
