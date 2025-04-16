from sympy_client.grammar.ObsimatLatexParser import ObsimatLatexParser
from sympy_client.modes.EvalMode import eval_handler
from sympy_client.modes.EvalfMode import evalf_handler
from sympy_client.modes.FactorMode import factor_handler
from sympy_client.modes.ExpandMode import expand_handler
from sympy_client.modes.ApartMode import apart_handler
from tests.MockResponse import MockResponse
import asyncio

from sympy import *


## Tests the evaluate mode.
class TestEvaluate:
    parser = ObsimatLatexParser()
    
    def test_simple_evaluate(self):
        response = MockResponse()
        asyncio.run(eval_handler({"expression": "1+1", "environment": {}}, response, self.parser))
        assert response.hasResult()
        
        result = response.getResult()
            
        with evaluate(False):
            assert result['result'] == 2
            
    def test_escaped_spaces(self):
        response = MockResponse()
        asyncio.run(eval_handler({"expression": r"1\ + \ 1", "environment": {}}, response, self.parser))
        assert response.hasResult()
        
        result = response.getResult()
            
        with evaluate(False):
            assert result['result'] == 2
        
        
    def test_matrix_single_line(self):
        response = MockResponse()
        asyncio.run(eval_handler({"expression": r"2 \cdot \begin{bmatrix} 1 \\ 1 \end{bmatrix}", "environment": {}}, response, self.parser))
        assert response.hasResult()
        
        result = response.getResult()

        assert result['result'].rhs == 2 * Matrix([[1], [1]])
        
                
    def test_matrix_multi_line(self):
        response = MockResponse()
        asyncio.run(eval_handler({"expression": r"""
        2
        \cdot 
        \begin{bmatrix} 
        1 \\ 1
        \end{bmatrix}
        """, "environment": {}}, response, self.parser))
        
        assert response.hasResult()
        
        result = response.getResult()

        assert result['result'].rhs == 2 * Matrix([[1], [1]])
        
    def test_matrix_normal(self):
        response = MockResponse()
        asyncio.run(eval_handler({"expression": r"""
        \Vert
        \begin{bmatrix}
        20 \\
        30 \\
        40 \\
        50
        \end{bmatrix}
        \Vert
        """, "environment": {}}, response, self.parser))
        
        assert response.hasResult()
        
        result = response.getResult()

        assert result['result'] == sqrt(20**2 + 30**2 + 40**2 + 50**2)
        
    def test_matrix_inner_prodcut(self):
        response = MockResponse()
        asyncio.run(eval_handler({"expression": r"""
        \langle 
        \begin{bmatrix}
        1 \\
        2
        \end{bmatrix}
        |
        \begin{bmatrix}
        2 \\
        4
        \end{bmatrix}
        \rangle
        """, "environment": {}}, response, self.parser))
        
        assert response.hasResult()
        
        result = response.getResult()

        assert result['result'] == 1 * 2 + 2 * 4
        
        
    def test_relational_evaluation(self):
        a, b = symbols("a b")
        
        response = MockResponse()
        asyncio.run(eval_handler({"expression": r"""
        5 + 5 + 5 + 5 = 10 + 10
        """, "environment": {}}, response, self.parser))
        
        assert response.hasResult()
        
        result = response.getResult()

        assert result['result'] == 20
        
        response.reset()
        asyncio.run(eval_handler({"expression": r"""
        a = b = (a - b)^2
        """, "environment": {}}, response, self.parser))
        
        assert response.hasResult()
        
        result = response.getResult()

        assert result['result'] == (a - b)**2
        
        response.reset()
        asyncio.run(eval_handler({"expression": r"""
        1 = 2 = 1
        """, "environment": {}}, response, self.parser))
        
        assert response.hasResult()
        
        result = response.getResult()

        assert result['result'] == 1
        
        response.reset()
        asyncio.run(eval_handler({"expression": r"""
            \begin{cases}
            2 + 2 + 2 + 2 &= 4 + 2 + 2 \\
                          &= 4 + 4
            \end{cases}
            """, "environment": {}}, response, self.parser))
        
        assert response.hasResult()
        
        result = response.getResult()
        
        assert result['result'] == 8
        assert result['metadata']['start_line'] == 4
        assert result['metadata']['end_line'] == 4
        
        response.reset()

        asyncio.run(eval_handler({"expression": r"""
            1 = 2 = 3 = 4 = 5 = 6 = 7 = 8
            """, "environment": {}}, response, self.parser))

        assert response.hasResult()
        
        result = response.getResult()
        assert result['result'] == 8
        
    
    def test_variable_substitution(self):
        
        response = MockResponse()
        
        asyncio.run(eval_handler({
            "expression": r"a + b",
            "environment": {
                "variables": {
                    "a": "2",
                    "b": "3"
                    }
                }
            },
            response,
            self.parser
        ))
        
        assert response.hasResult()
        assert response.getResult()['result'] == 5
        
        asyncio.run(eval_handler({
            "expression": r"\alpha",
            "environment": {
                "variables": {
                    "\\alpha": "2"
                    }
                }
            },
            response,
            self.parser
        ))
        
        assert response.hasResult()
        assert response.getResult()['result'] == 2
        
        
        response.reset()
        asyncio.run(eval_handler({
            "expression": r"A^T B",
            "environment": {
                "variables": {
                    "A": r"""
                    \begin{bmatrix}
                    1 \\ 2
                    \end{bmatrix}
                    """,
                    "B": r"""
                    \begin{bmatrix}
                    3 \\ 4
                    \end{bmatrix}
                    """
                    }
                }
            },
            response,
            self.parser
        ))
        
        assert response.hasResult()
        assert response.getResult()['result'].rhs == Matrix([11])
        
        response.reset()
        asyncio.run(eval_handler({
            "expression": r"\sin{abc}",
            "environment": {
                "variables": {
                    "abc": "1"
                    }
                }
            },
            response,
            self.parser
        ))
        
        assert response.hasResult()
        assert response.getResult()['result'] == sin(1)
        
                
        response.reset()
        asyncio.run(eval_handler({
            "expression": r"\sqrt{ val_{sub} + val_2^val_{three}}",
            "environment": {
                "variables": {
                    "val_{sub}": "7",
                    "val_2": "3",
                    "val_{three}": "2"
                    }
                }
            },
            response,
            self.parser
        ))
        
        assert response.hasResult()
        assert response.getResult()['result'] == 4
        
        
    def test_gradient(self):
        x, y = symbols("x y")
        response = MockResponse()
        
        asyncio.run(eval_handler({
            "expression": r"\nabla (x^2 y + y^2 x)",
            "environment": { }
            },
            response,
            self.parser
        ))
        
        assert response.hasResult()
        assert response.getResult()['result'].rhs == Matrix([[y * (2 * x + y), x * (2 * y + x)]])
    
    def test_evalf(self):
        response = MockResponse()
        asyncio.run(evalf_handler({"expression": "5/2", "environment": {}}, response, self.parser))
        assert response.hasResult()
        
        result = response.getResult()
            
        assert result['result'].rhs == 2.5
    
    
    def test_expand(self):
        a, b = symbols("a b")
        response = MockResponse()
        asyncio.run(expand_handler({"expression": "(a + b)^2", "environment": {}}, response, self.parser))
        assert response.hasResult()
        
        result = response.getResult()['result'].rhs
        assert result == a**2 + 2 * a * b + b**2
    
    
    def test_factor(self):
        x = symbols("x")
        response = MockResponse()
        asyncio.run(factor_handler({"expression": "x^3 - 10x^2 + 3x + 54", "environment": {}}, response, self.parser))
        assert response.hasResult()
        
        result = response.getResult()['result'].rhs
        assert result == (x - 9) * (x - 3) * (x + 2)

    
    
    def test_apart(self):
        x = symbols("x")
        response = MockResponse()
        asyncio.run(apart_handler({"expression": "\\frac{8x + 7}{x^2 + x - 2}", "environment": {}}, response, self.parser))
        assert response.hasResult()
        
        result = response.getResult()['result'].rhs
        assert result == 3 / (x + 2) + 5 / (x - 1)

    def test_quick_derivative(self):
        x = symbols("x")
        response = MockResponse()
        asyncio.run(expand_handler({"expression": "(x^5 + 3x^4 + 2x + 5)'''", "environment": {}}, response, self.parser))
        assert response.hasResult()
        
        result = response.getResult()['result'].rhs
        
        assert result == 60 * x**2 + 72 * x
    
    def test_function(self):
        
        # standard function
        response = MockResponse()
        asyncio.run(expand_handler({"expression": "f(25, -2)", "environment": { "functions": { "f": { "args": ["x", "y"], "expr": "2x + y^2" } } }}, response, self.parser))
        assert response.hasResult()
        
        result = response.getResult()['result']
        
        assert result == 54
        
        # function with arg name defined as variables
        response.reset()
        asyncio.run(expand_handler({"expression": "f(y)", "environment": { "functions": { "f": { "args": ["x"], "expr": "2x" } }, "variables": { "x": "-1", "y": "99" } }}, response, self.parser))
        assert response.hasResult()
        
        result = response.getResult()['result']
        
        assert result == 198
        
        
        # function with matrices as input.
        
        response.reset()
        asyncio.run(expand_handler({"expression": r"f(\begin{bmatrix} 5 & 10 \end{bmatrix})", "environment": { "functions": { "f": { "args": ["x"], "expr": "x x^T" } }, "variables": { "x": "-1", "y": "99" } }}, response, self.parser))
        assert response.hasResult()
        
        result = response.getResult()['result'].rhs
        
        assert result == Matrix([125])
    
    # TODO: add hessian test, jacobi tests and so on...