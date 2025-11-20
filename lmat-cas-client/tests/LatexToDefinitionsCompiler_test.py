from lmat_cas_client.compiling.Compiler import LatexToDefinitionCompiler


class TestLatexToSympyCompiler:
    compiler = LatexToDefinitionCompiler()

    def test_comments(self):
        result = self.compiler.compile(
            r"""
            a := \lim_{x \to 5} \frac{1}{x}
            """
        )

        print(result)
