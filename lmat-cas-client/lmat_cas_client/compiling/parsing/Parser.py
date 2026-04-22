from typing import Callable, Iterable, Optional, cast

import regex
from lark import (
    Lark,
    LarkError,
    ParseTree,
    Token,
    Tree,
    UnexpectedInput,
    UnexpectedToken,
)


class PrettyParserError(LarkError):
    pass


class Parser:
    """
    Wrapper class for a Lark parser instance.
    provides a parse method which rethrows any UnexpectedInput exception, produced by the Lark parser,
    as an PrettyParserError with a more user friendly exception message.
    Additionally, this also adds a pre processor which perform broad transformations on the input before it is parsed by lark.
    """

    def __init__(
        self,
        lark_parser: Lark,
        *,
        pre_processor: Optional[Callable[[str], str]] = None,
        post_processor: Optional[Callable[[str, Tree], Tree]] = None,
    ):

        self._pre_processor = pre_processor or (lambda s: s)
        self._post_processor = post_processor or (lambda _ps, t: t)
        self._lark_parser = lark_parser

    @property
    def parser(self) -> Lark:
        return self._lark_parser

    def parse(self, text: str, *args, **kwargs) -> ParseTree:
        """
        parse the given piece of text with the lark parser instance.

        Args:
            text (str)

        Raises:
            PrettyParserError: prettified UnexpectedInput exception.

        Returns:
            ParseTree: result of the latex parser parse method.
        """

        pre_processed_text = self._pre_processor(text)

        try:
            ast_result = self._lark_parser.parse(pre_processed_text, *args, **kwargs)
        except UnexpectedInput as e:
            raise self._prettify_unexpected_input(e, pre_processed_text) from e

        return self._post_processor(pre_processed_text, ast_result)

    _PARSE_ERR_PRETTY_STR_SPAN = 30
    # Maximum number of expected tokens to show to the user.
    # If the number of expected tokens is greater, do not show any.
    _PARSE_ERR_MAX_EXPECTED_TOKENS = 6

    def _prettify_unexpected_input(
        self, lark_error: UnexpectedInput, parse_text: str
    ) -> PrettyParserError:
        """
        Produce a LarkError with a user readable error message which contains the following info:
        - A snippet of the problematic latex source, pinpointing exactly where the parse error occured.
        - A list of expected strings or user readable* tokens (optional)

        *user readable as in NOT _CMD_SOME_TOKEN_YADA_YADA

        Args:
            lark_error (UnexpectedInput): exception to prettify
            parse_text (str): the string passed to the parse method, which caused lark_error.

        Returns:
            PrettyParserError
        """

        # if lark did not figure out where the error occured,
        # we just assume it was at the end of the string.
        if lark_error.pos_in_stream is None:
            lark_error.pos_in_stream = cast(None, len(parse_text) - 1)

        pretty_err = f"\n{lark_error.get_context(parse_text, Parser._PARSE_ERR_PRETTY_STR_SPAN)}Expression is invalid from here."

        if (
            isinstance(lark_error, UnexpectedToken)
            and len(lark_error.expected) <= Parser._PARSE_ERR_MAX_EXPECTED_TOKENS
        ):
            pretty_terminals = self._prettify_terminals(lark_error.expected)
            pretty_err += (
                f"\nExpected one of the following:\n{'\n'.join(pretty_terminals)}"
            )
        error = PrettyParserError(pretty_err)

        pretty_terminals = []

        for t in lark_error.state.value_stack:
            match t:
                case Token():
                    pretty_terminals.append(repr(t))
                case Tree():
                    pretty_terminals.append(t.pretty())

        error.add_note(
            f"\nParser Input:\n\n{parse_text}\n\nPrevious Terminals:\n{'\n'.join(pretty_terminals)}"
        )
        return error

    def _prettify_terminals(self, terminal_names: Iterable[str]) -> list[str]:
        """
        Returns a list of user readable (pretty) strings derived from the given list of terminals.
        If the terminal pattern is simply a string equality check, this string is returned,
        otherwise the the terminal name is prettified and returned instead.

        Args:
            terminal_names (list[str])

        Returns:
            list[str]: list of prettified terminal names, order corresponds to the original order in terminal_names
        """
        pretty_terminals = []

        for term_name in terminal_names:
            try:
                term = self.parser.get_terminal(term_name)
                term_pattern = term.pattern

                unescaped_value = regex.sub(r"\\(.)", r"\1", term_pattern.value)

                if regex.fullmatch(term_pattern.to_regexp(), unescaped_value):
                    pretty_terminals.append(f"'{unescaped_value}'")
                    continue
            except KeyError:
                # this happens if the terminal is a %declare terminal
                continue

            pretty_terminals.append(term_name.replace("_", " ").capitalize().strip())

        return pretty_terminals


lark_parser_defaults = {
    "parser": "lalr",
    "lexer": "contextual",
    "debug": False,
    "cache": True,
    "propagate_positions": True,
    "maybe_placeholders": True,
    "regex": True,
}

__all__ = ["lark_parser_defaults"]
