lexer grammar ExprLexer;

options {
    language = Python3;
}

@header {
from enum import Enum

class AddMode(Enum):
    DEFAULT = 0
    ENV = 1
    LIM = 2
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

def hasAddMode(self, mode: AddMode) -> AddMode:
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

fragment F_IGNORE:
    F_WS
    | F_SPACING
    | F_TEXT
    | '\\' ('limits' | 'nolimits')
    | '\\displaystyle'
    | '\\' ('left' | 'right');

IGNORE: F_IGNORE -> skip;

// === Hard Coded Operators (cannot be redefined because of special syntax requirements) ===

fragment CDOT: '\\cdot';

PLUS: '+';
MINUS: '-';
MULT: '*' | '\\ast' | CDOT;
DIV: '/' | '\\over';
POW: '^' -> pushMode(COMM_ARG);

TIMES: '\\times';
CROSS_PROD: '\\cross' 'product'? | '\\cp';
DOT_PROD: '\\dotproduct' | '\\vdot';

FRAC:
    ('\\' [dtcs]? 'frac' | '\\nicefrac') -> pushMode(COMM_ARG), pushMode(COMM_ARG);
BINOM:
    '\\' [dt]? 'binom' -> pushMode(COMM_ARG), pushMode(COMM_ARG);

SQRT: '\\sqrt' -> pushMode(COMM_ARG);

CONJUGATE: ('\\bar' | '\\overline') -> pushMode(COMM_ARG);

VEC_UNIT: ('\\vu' | '\\vectorunit') -> pushMode(COMM_ARG);

MOD: '\\' 'b'? 'mod';

// TODO: ...iiint support
INT: '\\int' 'op'?;
DIFFERENTIAL: '\\dd' | '\\differential';

PHYS_PARTIAL_DERIVATIVE: (
        '\\p' 'artial'? 'derivative'
        | '\\' 'p'? 'dv' '*'?
    ) -> pushMode(COMM_ARG);

LIMIT: '\\lim' {self.pushAddMode(AddMode.LIM)};
LIMIT_ARROW: {self.hasAddMode(AddMode.LIM)}? ('\\to' | '\\' 'long' 'rightarrow' '\\mapsto' | '\\xrightarrow' BRACE_TEXT) {self.remAddMode(AddMode.LIM)};

SUM: '\\sum';
PRODUCT: '\\prod';

// postfix operators

BANG: '!';
PERCENT: '\\%';
PERMILLE: '\\textperthousand';


// === Literals === TODO: primes? TODO: code action for remapping this to function
fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Z];

fragment F_SYMBOL: LETTER+ | SYMBOL_FORMAT;
// TODO: ONLY match this one IFFFFF  F_SYMBOL is *NOT* a function
fragment F_INDEXED_SYMBOL: F_SYMBOL F_WS? '_' F_WS? BRACE_TEXT;
SYMBOL: F_SYMBOL | F_INDEXED_SYMBOL;

fragment F_COMMAND: '\\' LETTER+;
COMMAND: F_COMMAND;

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
    '\\vec' | '\\va' '*'? | '\\vectorarrow'
    | '\\vb' '*'? | '\\vectorbold'
    | '\\hat'
    | '\\tilde';
   
   // TODO: predicate which is just a list of formatters
// // vec arr as in the arrow above a symbol fragment VEC_ARR_FORMAT: '\\vec' | '\\va' '*'? |
// '\\vectorarrow'; // vec bold as in non italic and bold, to indicate a vector fragment
// VEC_BOLD_FORMAT: '\\vectorbold' | '\\vb' '*'?; fragment HAT_FORMAT: '\\hat'?; fragment
// TILDE_FORMAT: '\\tilde'?;

// TODO: should plain brace text also just be here?
fragment SYMBOL_FORMAT: (MATH_FORMAT | CMD_FORMAT) (
        // atom cases
        F_WS DIGIT
        | F_WS LETTER
        | F_WS? F_COMMAND
        // brace surrounded argument case
        | F_WS? BRACE_TEXT
    );

COMMA: ',';
UNDERSCORE: '_';
EQUAL: '=';

// indexing?
// rethink a bit maybe, we have a more powerfull lexer + parser,
// should indexing work differently for symbols v.s. functions?
// how does one know if a definition is a function vs symbol
// so x_n() := x^2 then x_n is a function?, not really how you notate it usually
// i guess it would just be, IF SYMBOL_{SYMBOL,SYMBOL,SYMBOL} is possible,
// then treat it as a function? ONLY if one index symbol appears in definition body.
// could be something like that,
// sooooo... just need to somehow lex {...} and {SYMBOL,SYMBOL,SYMBOL} differently...
// that should be possible?

// === Delimiters === TODO: why the push and pop?, well because { } is special in latex
LBRACE: '{' { self.pushAddMode(AddMode.DEFAULT) } -> pushMode(DEFAULT_MODE);
RBRACE: '}' { self.popAddMode() } -> popMode;

LPAREN: '(';
RPAREN: ')';

LBRACE_LITERAL: '\\{';
RBRACE_LITERAL: '\\}';

LBRACKET: '\\[';
RBRACKET: '\\]';

LCEIL: '\\lceil';
RCEIL: '\\rceil';

LFLOOR: '\\lfloor';
RFLOOR: '\\rfloor';

LANGLE: '\\langle' | '<';
RANGLE: '\\rangle' | '>';

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

BEGIN_MATRIX: CMD_BEGIN '{' F_WS? MATRIX_ENV F_WS? '}' {self.pushAddMode(AddMode.ENV)};
END_MATRIX: CMD_END '{' F_WS? MATRIX_ENV F_WS? '}' {self.popAddMode()};

BEGIN_V_MATRIX: CMD_BEGIN '{' F_WS? V_MATRIX_ENV F_WS? '}' {self.pushAddMode(AddMode.ENV)};
END_V_MATRIX: CMD_END '{' F_WS? V_MATRIX_ENV F_WS? '}' {self.popAddMode()};

BEGIN_ARRAY: ('\\left' F_WS? ('('|'\\{'|'\\['|'\\lfloor'|'\\langle'|'<') )? F_WS? CMD_BEGIN '{' F_WS? ARRAY_ENV F_WS? '}' F_WS? ('{' ([clr|:]|F_WS)+ '}')? 
    {self.pushAddMode(AddMode.ENV)};
END_ARRAY: CMD_END '{' F_WS? ARRAY_ENV F_WS? '}' ( '\\right' (')'|'\\}'|'\\]'|'\\rfloor'|'\\rangle'|'>') ){self.popAddMode()};

BEGIN_ENV: CMD_BEGIN BRACE_TEXT {self.pushAddMode(AddMode.ENV)};
END_ENV: CMD_END BRACE_TEXT {self.popMode()};

ENV_EL_SEP: '&' { self.topAddMode() == AddMode.ENV }?;
ENV_ROW_SEP: '\\\\' { self.topAddMode() == AddMode.ENV }?;


mode COMM_ARG;

ARG_DIGIT: DIGIT -> type(NUMBER), popMode;
ARG_LETTER: LETTER -> type(SYMBOL), popMode;
ARG_COMM: F_COMMAND -> type(COMMAND), popMode;

ARG_LBRACE: '{' {self.pushAddMode(AddMode.DEFAULT)} -> type(LBRACE), mode(DEFAULT_MODE);

ARG_WS: F_WS -> skip;
