
import regex
from lark import Lark, LarkError, UnexpectedInput, UnexpectedToken


class PrettyParserError(LarkError):
    pass

class PrettyParser:
    def __init__(self, lark_parser: Lark):
        self._lark_parser = lark_parser

    @property
    def parser(self) -> Lark:
        return self._lark_parser

    def parse(self, text: str, *args, **kwargs):
        try:
            return self._lark_parser.parse(text, *args, **kwargs)
        except UnexpectedInput as e:
            raise self._prettify_unexpected_input(e, text) from e

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
    def _prettify_unexpected_input(self, lark_error: UnexpectedInput, latex_src: str) -> PrettyParserError:

        # if lark did not figure out where the error occured,
        # we just assume it was at the end of the string.
        if lark_error.pos_in_stream is None:
            lark_error.pos_in_stream = len(latex_src) - 1

        pretty_err = f"{lark_error.get_context(latex_src, PrettyParser._PARSE_ERR_PRETTY_STR_SPAN)}Expression is invalid from here."

        if isinstance(lark_error, UnexpectedToken) and len(lark_error.expected) <= PrettyParser._PARSE_ERR_MAX_EXPECTED_TOKENS:
            pretty_terminals = self._prettify_terminals(lark_error.expected)
            pretty_err += f"\nExpected one of the following:\n{'\n'.join(pretty_terminals)}"

        return PrettyParserError(pretty_err)

    # Returns a list of user readable (pretty) strings derived from the given list of terminals.
    # If the terminal pattern is simply a string equality check, this string is returned,
    # otherwise the the terminal name is prettified and returned instead.
    def _prettify_terminals(self, terminal_names: list[str]) -> list[str]:
        pretty_terminals = []

        for term_name in terminal_names:
            try:
                term = self.parser.get_terminal(term_name)
                term_pattern = term.pattern

                unescaped_value = regex.sub(r'\\(.)', r'\1', term_pattern.value)

                if regex.fullmatch(term_pattern.to_regexp(), unescaped_value):
                    pretty_terminals.append(f"'{unescaped_value}'")
                    continue
            except KeyError:
                # this happens if the terminal is a %declare terminal
                continue

            pretty_terminals.append(term_name.replace('_', ' ').capitalize().strip())

        return pretty_terminals
