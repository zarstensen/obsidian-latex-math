from grammar.SystemOfExpr import SystemOfExpr
from grammar.SubstitutionCache import SubstitutionCache

from sympy.parsing.latex.lark.transformer import TransformToSymPyExpr
from sympy import *
from lark import Token


# The ObsimatLarkTransofmer class provides functions for transforming
# rules defined in obsimat_grammar.lark into sympy expressions.
class ObsimatLarkTransformer(TransformToSymPyExpr):

    SYMBOL_CREATION_METHODS = [
        'SYMBOL',
        'GREEK_SYMBOL_WITH_PRIMES',
        'LATIN_SYMBOL_WITH_LATIN_SUBSCRIPT',
        'GREEK_SYMBOL_WITH_LATIN_SUBSCRIPT',
        'LATIN_SYMBOL_WITH_GREEK_SUBSCRIPT',
        'GREEK_SYMBOL_WITH_GREEK_SUBSCRIPT',
        'multi_letter_symbol',
        'symbol_prime'
        ]

    # Constructs an ObsimatLarkTransformer.
    # environment: The environment to use for variable substitution.
    # symbol_getter: callback function for when the transformer needs to retreive the value of a variable, from its string name, during substitution.
    def __init__(self, substitution_cache: SubstitutionCache):
        super().__init__()
        self._substitution_cache = substitution_cache
        
        # wrap all symbol rules and terminal handlers in a method which attempts to 
        # substitute the symbol for a variable defined in the given environment.
        for symbol_method in self.SYMBOL_CREATION_METHODS:
            symbol_transform = getattr(self, symbol_method)
            setattr(self, symbol_method, lambda tokens, symbol_transform=symbol_transform: self._try_substitute(symbol_transform, tokens))
    
    # tries to substitute the symbol returned form the symbol_transform callable, with a variable defined in the environment.
    # if there is no such variable, the symbol is returned as is.
    def _try_substitute(self, symbol_transform, tokens):
        symbol = symbol_transform(tokens)
        
        substituted_value = self._substitution_cache.get_substitution(str(symbol))
        
        if substituted_value is not None:
            return substituted_value
        else:
            return symbol

    def matrix_norm(self, tokens):
        with evaluate(True):
            return tokens[1].doit().norm()

    def matrix_inner_product(self, tokens):
        with evaluate(True):
            return tokens[1].doit().dot(tokens[3].doit(), hermitian=True, conjugate_convention="right")

    def quick_derivative(self, tokens):
        if len(tokens[0].free_symbols) == 0:
            return S(0)
        else:
            return diff(tokens[0], list(tokens[0].free_symbols)[0], len(tokens[1]))

    def math_constant(self, tokens):
        match str(tokens[0]):
            case "\\pi":
                return S.Pi
            case "\\tau":
                return 2 * S.Pi
            case "e":
                return S.Exp1
            case "i":
                return I
            case _:
                raise ValueError("Unknown mathematical constant")

    def system_of_expressions(self, tokens):
        return SystemOfExpr(list(filter(lambda t: not isinstance(t, Token), tokens)))

    class system_of_expressions_expr:
        @staticmethod
        def visit_wrapper(f, data, children, meta):
            # location adata is needed for system_of_expressions handler.
            return (children[0], meta)

    def align_rel(self, tokens):
        # just ignore the alignment characters
        return next(filter(lambda t: t.type != "MATRIX_COL_DELIM", tokens))

    def partial_relation(self, tokens):
        relation_token = None
        expression = None
        is_left = None
        if isinstance(tokens[0], Token):
            relation_token = tokens[0]
            expression = tokens[1]
            is_left = False
        else:
            relation_token = tokens[1]
            expression = tokens[0]
            is_left = True

        relation_type = ObsimatLarkTransformer._relation_token_to_type(relation_token)
        # these invalid relations just get a dummy variable to the side they miss a variable.
        if is_left == True:
            return relation_type(expression, Dummy())
        elif is_left == False:
            return relation_type(Dummy(), expression)

        raise ValueError("Invalid relation")

    class chained_relation:
        @staticmethod
        def visit_wrapper(f, data, children, meta):
            relation_type = ObsimatLarkTransformer._relation_token_to_type(children[1])

            # see a chained relation as a system of equations.
            # TODO: maybe check if left hand side is SystemOfExpr, and create a new SystemOfExpr containing the right hand side if so.
            return SystemOfExpr(
                [
                    (children[0], meta),
                    (relation_type(children[0].rhs, children[2]), meta),
                ]
            )

    @staticmethod
    def _relation_token_to_type(token):
        match token.type:
            case "EQUAL":
                return Eq
            case "NOT_EQUAL":
                return Ne
            case "LT":
                return Lt
            case "LTE":
                return Le
            case "GT":
                return Gt
            case "GTE":
                return Ge
            case _:
                raise ValueError("Invalid relation token")
