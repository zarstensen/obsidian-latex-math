import os
import re as regex
from typing import Callable, Iterator

from lark import Lark, LarkError, Token, UnexpectedInput, UnexpectedToken
from lark.lark import PostLex
from lark.lexer import TerminalDef
from sympy import *

from .SympyParser import DefinitionStore, SympyParser
from .transformers.LatexTransformer import LatexTransformer


# Represents a scope to be handled by the ScopePostLexer.
# This class provides a series of terminals pairs which define the start and end of this scope.
#
# The replace_tokens dict is a dict between a terminal type, and either:
# - A string representing the new type of this token, the value is preserved.
# - A list of TerminalDef, which (going from left to right) replaces the given terminal type, if its pattern matches its value.
class LexerScope:
    def __init__(self,
                    scope_pairs: list[tuple[regex.Pattern, regex.Pattern|Callable[[regex.Match[str]], regex.Pattern]]] = [],
                    replace_tokens: dict[str, str|list[TerminalDef]] = {}
                ):
        self.scope_pairs = scope_pairs
        self.replace_tokens = replace_tokens

    def token_handler(self, token_stream: Iterator[Token], _scope_start_token: Token) -> Iterator[Token]:
        for t in token_stream:
            # try to replace the token
            if t.type in self.replace_tokens:
                if isinstance(self.replace_tokens[t.type], str):
                    yield Token(self.replace_tokens[t.type], t.value)
                    continue

                for replace_token in self.replace_tokens[t.type]:
                    if regex.fullmatch(replace_token.pattern.to_regexp(), t.value):
                        yield Token(replace_token.name, t.value)
                        break
                else:
                    # no tokens could replace it anyways, so just return the original one.
                    yield t
            else:
                yield t

class MultiArgScope(LexerScope):
    def __init__(self, arg_count: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.arg_count = arg_count

    def token_handler(self, token_stream: Iterator[Token], scope_start_token: Token) -> Iterator[Token]:
        for _ in range(1, self.arg_count):

            token = next(super().token_handler(token_stream, scope_start_token), None)

            if token is None:
                return

            yield token
            yield Token("_MULTIARG_DELIMITER", "")

        token = next(super().token_handler(token_stream, scope_start_token), None)

        if token is None:
            return

        yield token
        yield Token("_MULTIARG_EOS", "")

class MatrixScope(LexerScope):
    def token_handler(self, token_stream: Iterator[Token], scope_start_token: Token) -> Iterator[Token]:
        ignore_regex = r'(\\left\s*(\\)?.|\\right\s*(\\)?.|\s)'
        expected_end_token_type = scope_start_token.type.replace('BEGIN', 'END')
        expected_end_token_value = regex.sub(ignore_regex, '', scope_start_token.value).replace('\\begin', '\\end')
        for token in super().token_handler(token_stream, scope_start_token):
            yield token
            if token.type == expected_end_token_type and regex.sub(ignore_regex, '', token.value) == expected_end_token_value:
                yield Token('_MATRIX_ENV_END', '')

class PartialDiffScope(LexerScope):
    def token_handler(self, token_stream, _scope_start_token):

        for token in super().token_handler(token_stream, _scope_start_token):
            yield token
            if token.type == '_R_BRACE':
                break

        next_token = next(super().token_handler(token_stream, _scope_start_token), None)

        if next_token is None:
            return

        if next_token.type == '_L_BRACE':
            yield Token('_DERIV_ARG_SEPARATOR', next_token.value)
        else:
            yield next_token


# The ScopePostLexer aims to provide context to the lalr parser during tokenization.
# It does this by recognizing pairs of terminals, which define a scope.
# Inside this scope, terminals can be specified which should be replaced by other terminals,
# or optionally a custom token handler can be given, for more complex operations.
class ScopePostLexer(PostLex):

    # setup scopes using the terminals defined in the given parser.
    def initialize_scopes(self, parser: Lark):
        self.scopes = [
            # Scope for inner products,
            # is here so we dont go into the abs scope below.
            LexerScope(
                scope_pairs=[
                    ("_L_ANGLE", "_R_ANGLE")
                ],
                replace_tokens={
                    "_L_BAR": "_INNER_PRODUCT_SEPARATOR",
                    "_COMMA": "_INNER_PRODUCT_SEPARATOR"
                }
            ),
            # Scope for pairing up '|' characters for abs rules.
            LexerScope(
                scope_pairs=[
                    ("_L_BAR", "_R_BAR"),
                    ("_L_DOUBLE_BAR", "_R_DOUBLE_BAR")
                ],
                replace_tokens={
                    "_L_BAR": "_R_BAR",
                    "_L_DOUBLE_BAR": "_R_DOUBLE_BAR",
                }
            ),
            # Scope for latex commands which require multiple arguments,
            # that is \command{arg1}{arg2}...{argN}.
            MultiArgScope(
                arg_count=2,
                scope_pairs=[
                    ("_FUNC_FRAC", "_MULTIARG_EOS"),
                    ("_FUNC_BINOM", "_MULTIARG_EOS")
                ]
            ),
            # Scope for functions which require the _DIFFERENTIAL_SYMBOL be prioritized over symbols.
            PartialDiffScope(
                scope_pairs=[
                    ("_FUNC_DERIVATIVE", "_R_BRACE")
                ],
                replace_tokens={
                    "SINGLE_LETTER_SYMBOL": [ parser.get_terminal("_DIFFERENTIAL_SYMBOL") ],
                    "FORMATTED_SYMBOLS": [ parser.get_terminal("_DIFFERENTIAL_SYMBOL") ],
                }
            ),
            LexerScope(
                scope_pairs=[
                    ("_FUNC_INTEGRAL", "_DIFFERENTIAL_SYMBOL"),
                    ("_DERIV_ARG_SEPARATOR", "_R_BRACE")
                ],
                replace_tokens={
                    "SINGLE_LETTER_SYMBOL": [ parser.get_terminal("_DIFFERENTIAL_SYMBOL") ],
                    "FORMATTED_SYMBOLS": [ parser.get_terminal("_DIFFERENTIAL_SYMBOL") ],
                }
            ),
            MatrixScope(
                scope_pairs=[
                    ("CMD_BEGIN_MATRIX", "_MATRIX_ENV_END"),
                    ("CMD_BEGIN_ARRAY", "_MATRIX_ENV_END"),
                    ("CMD_BEGIN_VMATRIX", "_MATRIX_ENV_END")
                ],
                replace_tokens={
                    "_ALIGN": "_MATRIX_COL_DELIM",
                    "_LATEX_NEWLINE": "MATRIX_ROW_DELIM"
                }
            ),
            LexerScope(
                scope_pairs = [
                    ("_CMD_BEGIN_ALIGN", "_CMD_END_ALIGN"),
                    ("_CMD_BEGIN_CASES", "_CMD_END_CASES")
                ],
                replace_tokens={
                    "_LATEX_NEWLINE": "_EXPR_DELIM"
                }
            ),
            # General scope for L R token pairs.
            # This makes sure stuff like |(|x|)| does not get parsed as "|(|", "x" and "|)|" but instead as "|(|x|)|"
            LexerScope(
                scope_pairs=[("_?L_(.*)", lambda match : f"_?R_{match.groups()[0]}")]
            )
        ]

    def process(self, stream: Iterator[Token]) -> Iterator[Token]:
        yield from self._process_scope(stream, LexerScope(), None, None)

    def _process_scope(self, stream, scope: LexerScope, scope_begin_token: Token | None, scope_end_terminal: str | None):
        for token in scope.token_handler(stream, scope_begin_token):
            yield token

            # check if we are ourselves at an end terminal
            # if we are, go out of the scope.
            if scope_end_terminal is not None and regex.fullmatch(scope_end_terminal, token.type):
                break

            # check if the token starts a scope
            for new_scope in self.scopes:
                for scope_pair in new_scope.scope_pairs:
                    match = regex.fullmatch(scope_pair[0], token.type)
                    if match:
                        end_terminal = scope_pair[1] if isinstance(scope_pair[1], str) else scope_pair[1](match)
                        yield from self._process_scope(stream, new_scope, token, end_terminal)
                        break # do not consider other scopes
                # do not continue if the inner loop was broken out of.
                else:
                    continue
                break

class PrettyLarkError(LarkError):
    pass

## The LmatLatexParser is responsible for parsing a latex string in the context of an LmatEnvironment.
class LatexParser(SympyParser):

    def __init__(self, grammar_file: str = None):
        if grammar_file is None:
            grammar_file = os.path.join(
                os.path.dirname(__file__), "latex_math_grammar.lark"
            )

        post_lexer = ScopePostLexer()

        self.parser = Lark.open(
            grammar_file,
            rel_to=os.path.dirname(grammar_file),
            parser="lalr",
            start="latex_string",
            lexer="contextual",
            debug=False,
            cache=True,
            propagate_positions=True,
            maybe_placeholders=True,
            postlex=post_lexer
        )

        post_lexer.initialize_scopes(self.parser)

    # Parse the given latex expression into a sympy expression, substituting any information into the expression, present in the current environment.
    def parse(self, latex_str: str, definitions_store: DefinitionStore):
        transformer = LatexTransformer(definitions_store)

        try:
            parse_tree = self.parser.parse(latex_str)
        except UnexpectedInput as e:
            raise self._prettify_unexpected_input(e, latex_str) from e

        expr = transformer.transform(parse_tree)

        return expr

    _PARSE_ERR_PRETTY_STR_SPAN = 30
    # Maximum number of expected tokens to show to the user.
    # If the number of expected tokens is greater, do not show any.
    _PARSE_ERR_MAX_EXPECTED_TOKENS = 6

    # Produce a LarkError with a user readable error message which contains the following info:
    #   - A snippet of the problematic latex source, pinpointing exactly where the parse error occured.
    #   - A list of expected strings or user readable* tokens (optional)
    #
    # *user readable as in NOT _CMD_SOME_TOKEN_YADA_YADA
    #
    def _prettify_unexpected_input(self, lark_error: UnexpectedInput, latex_src: str) -> PrettyLarkError:

        # if lark did not figure out where the error occured,
        # we just assume it was at the end of the string.
        if lark_error.pos_in_stream is None:
            lark_error.pos_in_stream = len(latex_src) - 1

        pretty_err = f"{lark_error.get_context(latex_src, LatexParser._PARSE_ERR_PRETTY_STR_SPAN)}Expression is invalid from here."

        if isinstance(lark_error, UnexpectedToken) and len(lark_error.expected) <= LatexParser._PARSE_ERR_MAX_EXPECTED_TOKENS:
            pretty_terminals = self._prettify_terminals(lark_error.expected)
            pretty_err += f"\nExpected one of the following:\n{'\n'.join(pretty_terminals)}"

        return PrettyLarkError(pretty_err)

    # Returns a list of user readable (pretty) strings derived from the given list of terminals.
    # If the terminal pattern is simply a string equality check, this string is returned,
    # otherwise the the terminal name is prettified and returned instead.
    def _prettify_terminals(self, terminal_names: list[str]) -> list[str]:
        pretty_terminals = []

        for term_name in terminal_names:
            term = self.parser.get_terminal(term_name)
            term_pattern = term.pattern

            unescaped_value = regex.sub(r'\\(.)', r'\1', term_pattern.value)

            if regex.fullmatch(term_pattern.to_regexp(), unescaped_value):
                pretty_terminals.append(f"'{unescaped_value}'")
            else:
                pretty_terminals.append(term_name.replace('_', ' ').capitalize().strip())

        return pretty_terminals
