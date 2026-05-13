lexer grammar ExprLexer;

options {
    language = Python3;
}

@header {
from enum import Enum

class AddMode(Enum):
    DEFAULT = 0
    OPT_ARG = 1
    ENV = 2
    MATRIX = 3
    LIM = 4
}

@members {

add_mode_stack = [ AddMode.DEFAULT ]

def pushAddMode(self, mode: AddMode):
    self.add_mode_stack.append(mode)

def popAddMode(self) -> AddMode:
    return self.add_mode_stack.pop()

def remAddMode(self, mode: AddMode):
    self.add_mode_stack.reverse()
    self.add_mode_stack.remove(mode)
    self.add_mode_stack.reverse()

def topAddMode(self) -> AddMode:
    return self.add_mode_stack[-1]

def hasAddMode(self, mode: AddMode) -> bool:
    return mode in self.add_mode_stack
}

tokens {
    FUNCTION,
    CMD_FUNCTION
}

// === Skip and Ignore tokens ===

fragment F_WS: [\p{White_Space}];

fragment F_SPACING:
    '\\' (
        | '!'
        | ','
        | ':'
        | ';'
        | '*' // NOTE: what are these?
        | '-' //
        | '.' //
        | '/' //
        | '(' //
        | '=' //
    )
    | '\\' 'neg'? (
        'thinspace'
        | 'thinspace'
        | 'medspace'
        | 'thickspace'
    )
    | '\\v' ('rule' | 'center' | 'box' | 'skip' | 'space')
    | '\\hfill'
    | '~';

fragment BRACE_TEXT: '{' ( '\\' [{}] | .)*? '}';
fragment F_TEXT: '\\text' 'tt'? F_WS? BRACE_TEXT;
fragment COMMENT: '%' .*? '\n';

fragment F_IGNORE:
    F_WS
    | F_SPACING
    | F_TEXT
    | COMMENT
    | '\\' ('limits' | 'nolimits')
    | '\\displaystyle'
    | '\\' ('left' | 'right');

IGNORE: F_IGNORE -> skip;

// === Hard Coded Operators (cannot be redefined because of special syntax requirements) ===

fragment CDOT: '\\cdot';

fragment F_MULT: '*' | '\\ast' | CDOT;

// arithmetic operators
PLUS: '+';
MINUS: '-';
MULT: F_MULT;
DIV: '/' | '\\over';
POW: '^' -> pushMode(COMM_ARG);

// relational operators
EQ: '=';
NEQ: '\\ne' 'q'?;
LT: '<';
LTE: '<=' | '\\leq' 'slant'? | '\\le';
GT: '>';
GTE: '>=' | '\\geq' 'slant'? | '\\ge';

TIMES: '\\times';
CROSS_PROD: '\\cross' 'product'? | '\\cp';
DOT_PROD: '\\dotproduct' | '\\vdot';

FRAC:
    ('\\' [dtcs]? 'frac' | '\\nicefrac') -> pushMode(COMM_ARG), pushMode(COMM_ARG);
BINOM:
    '\\' [dt]? 'binom' -> pushMode(COMM_ARG), pushMode(COMM_ARG);

// all of these should somehow also be part of COMM_ARG.......... :(
SQRT: '\\sqrt' -> pushMode(COMM_ARG);

CONJUGATE: ('\\bar' | '\\overline') -> pushMode(COMM_ARG);

VEC_UNIT: ('\\vu' | '\\vectorunit') -> pushMode(COMM_ARG);

MOD: '\\' 'b'? 'mod';

// TODO: ...iiint support
INT: '\\int' 'op'?;
DIFFERENTIAL: '\\dd' | '\\differential';

PHYS_DERIVATIVE: (
        '\\derivative' '*'?
        | '\\dv' '*'?
    ) -> pushMode(COMM_ARG);

PHYS_PARTIAL_DERIVATIVE: (
        '\\p' 'artial'? 'derivative' '*'?
        | '\\pdv' '*'?
    ) -> pushMode(COMM_ARG);

LIMIT: '\\lim' {self.pushAddMode(AddMode.LIM)};
LIMIT_ARROW:
    {self.hasAddMode(AddMode.LIM)}? (
        '\\to'
        | '\\' 'long' 'rightarrow' '\\mapsto'
        | '\\xrightarrow' BRACE_TEXT
    ) {self.remAddMode(AddMode.LIM)};

SUM: '\\sum';
PRODUCT: '\\prod';

// postfix operators

BANG: '!';
PERCENT: '\\%';
PERMILLE: '\\textperthousand';


COMMA: ',';
// not exactly COMM_ARG, something different
UNDERSCORE: '_' -> pushMode(COMM_ARG);

SEMICOLON: ';';
STAR: '\\star';
DOTS: '\\dots' [cbmio] | '\\' [lc]? 'dots' | ('\\cdot'|'.') ('\\cdot'|'.') ('\\cdot'|'.')?;

// indexing? rethink a bit maybe, we have a more powerfull lexer + parser, should indexing work
// differently for symbols v.s. functions? how does one know if a definition is a function vs symbol
// so x_n() := x^2 then x_n is a function?, not really how you notate it usually i guess it would
// just be, IF ID_{ID,ID,ID} is possible, then treat it as a function? ONLY if one
// index symbol appears in definition body. could be something like that, sooooo... just need to
// somehow lex {...} and {ID,ID,ID} differently... that should be possible?

// === Delimiters === TODO: why the push and pop?, well because { } is special in latex
LBRACE:
    '{' {self.pushAddMode(AddMode.DEFAULT) } -> pushMode(DEFAULT_MODE);
RBRACE: '}' {self.popAddMode() } -> popMode;

LPAREN: '(' | '\\lparen';
RPAREN: ')' | '\\rparen';

LBRACE_LITERAL: '\\{';
RBRACE_LITERAL: '\\}';

LBRACKET: '[';
RBRACKET: ']' {
if self.topAddMode() == AddMode.OPT_ARG:
    self.popAddMode()
    self.popMode()
};

LBRACK_CMD: '\\lbrack';
RBRACK_CMD: '\\rbrack';

LCEIL: '\\lceil';
RCEIL: '\\rceil';

LFLOOR: '\\lfloor';
RFLOOR: '\\rfloor';

LANGLE: '\\langle';
RANGLE: '\\rangle';

BAR: '|' | '\\mid';
DOUBLE_BAR: '||' | '\\mid' F_WS? '\\mid' | '\\' [lr] 'Vert';

// === Command Math Functions === as in defined by a latex command, not just written plainly.
// alternative: one can pass arguments to these without surrounding them with parenthesees. how do
// you do the dynamic amount of arguments then?

fragment F_OPERATOR: '\\operatorname' | '\\mathrm';

// === Matrix Time !!! ===

fragment CMD_BEGIN: '\\begin';
fragment CMD_END: '\\end';

fragment ARRAY_ENV: 'array';
fragment MATRIX_ENV: [bp]? 'small'? 'matrix';
fragment V_MATRIX_ENV: 'v' 'small'? 'matrix';

BEGIN_MATRIX:
    CMD_BEGIN '{' F_WS? MATRIX_ENV F_WS? '}' {self.pushAddMode(AddMode.MATRIX)};
END_MATRIX:
    CMD_END '{' F_WS? MATRIX_ENV F_WS? '}' {self.popAddMode()};

BEGIN_V_MATRIX:
    CMD_BEGIN '{' F_WS? V_MATRIX_ENV F_WS? '}' {self.pushAddMode(AddMode.MATRIX)};
END_V_MATRIX:
    CMD_END '{' F_WS? V_MATRIX_ENV F_WS? '}' {self.popAddMode()};

BEGIN_ARRAY: (
        '\\left' F_WS? (
            '('
			| '\\lparen'
            | '\\{'
            | '['
            | '\\lbrack'
            | '\\lfloor'
            | '\\langle'
            | '<'
        )
    )? F_WS? CMD_BEGIN F_WS? '{' F_WS? ARRAY_ENV F_WS? '}' F_WS? (
        '{' ([clr|:] | F_WS)+ '}'
    )? {self.pushAddMode(AddMode.MATRIX)};
END_ARRAY:
    CMD_END F_WS? '{' F_WS? ARRAY_ENV F_WS? '}' F_WS? (
        '\\right' F_WS? (
            ')'
			| '\\rparen'
            | '\\}'
            | ']'
            | '\\rbrack'
            | '\\rfloor'
            | '\\rangle'
            | '>'
        )
    ) {self.popAddMode()};

BEGIN_ENV: CMD_BEGIN BRACE_TEXT {self.pushAddMode(AddMode.ENV)};
END_ENV: CMD_END BRACE_TEXT {self.popAddMode()};

ENV_EL_SEP: '&' { self.topAddMode() == AddMode.MATRIX }?;
ENV_ROW_SEP: '\\\\' { self.topAddMode() in (AddMode.MATRIX, AddMode.ENV) }?;
ENV_SEP_SKIP: ('&' | '\\\\') -> skip;

// === Literals === TODO: primes? TODO: code action for remapping this to function

NUMBER: DIGIT+ | DIGIT* '.' DIGIT+;

BIN_NUMBER:
    '0' ('b' | '\\mathrm{b}') [01]+
    | '\\mathrm{0b' [01]+ '}';

OCT_NUMBER:
    '0' ('o' | '\\mathrm{o}') [0-7]+
    | '\\mathrm{0o' [0-7]+ '}';

HEX_NUMBER:
    '0' ([xX] | '\\mathrm{' [xX] '}') [0-7]+
    | '\\mathrm{0' [xX] [0-7]+ '}';

fragment MATH_FORMAT: '\\math' LETTER+;
fragment CMD_FORMAT:
    '\\vec'
    | '\\va' '*'?
    | '\\vectorarrow'
    | '\\vb' '*'?
    | '\\vectorbold'
    | '\\hat'
    | '\\tilde';

// TODO: predicate which is just a list of formatters // vec arr as in the arrow above a symbol
// fragment VEC_ARR_FORMAT: '\\vec' | '\\va' '*'? | '\\vectorarrow'; // vec bold as in non italic
// and bold, to indicate a vector fragment VEC_BOLD_FORMAT: '\\vectorbold' | '\\vb' '*'?; fragment
// HAT_FORMAT: '\\hat'?; fragment TILDE_FORMAT: '\\tilde'?;

// TODO: should plain brace text also just be here?
fragment ID_FORMAT: (MATH_FORMAT | CMD_FORMAT) (
        // atom cases
        F_WS DIGIT
        | F_WS LETTER
        | F_WS? F_COMMAND
        // brace surrounded argument case
        | F_WS? BRACE_TEXT
    );

fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Z];

fragment F_ID: LETTER+ | ID_FORMAT;

DELTA: '\\Delta';

// TODO: ONLY match this one IFFFFF  F_ID is *NOT* a function
// ooooo thats a good point....
// fragment F_INDEXED_ID: F_ID {True}? F_WS? '_' F_WS? BRACE_TEXT;
ID: F_ID | ID_FORMAT;

fragment F_COMMAND: '\\' LETTER+;
COMMAND: F_COMMAND;

mode COMM_ARG;

ARG_DIGIT: DIGIT -> type(NUMBER), popMode;
ARG_ID: (LETTER | ID_FORMAT) -> type(ID), popMode;
ARG_COMM: F_COMMAND
{
start = self._tokenStartCharIndex
self._input.seek(start)
self.popMode()
self.skip()
};

// special case needed for limits, where it is valid syntax to have + or - in the superscript.
// should not really create problems elsewhere, but if it does, this can always be in a second mode specifically
// for lexing after a POW terminal.
ARG_PLUS: '+' -> type(PLUS), popMode;
ARG_MINUS: '-' -> type(MINUS), popMode;

ARG_LBRACE:
    '{' {self.pushAddMode(AddMode.DEFAULT)} -> type(LBRACE), mode(DEFAULT_MODE);

ARG_LBRACKET:
    '[' {self.pushAddMode(AddMode.OPT_ARG)} -> type(LBRACKET), pushMode(DEFAULT_MODE);

ARG_WS: F_WS -> skip;
