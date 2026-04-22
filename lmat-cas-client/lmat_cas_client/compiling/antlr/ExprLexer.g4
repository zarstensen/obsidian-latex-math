lexer grammar ExprLexer;

options {
	language = Python3;
}

@members {
dx_counter = 0
}

tokens {
	FUNCTION
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

fragment F_TEXT: '\\text' 'tt'? F_WS? '{' ( '\\' [{}] | .)*? '}';

fragment F_IGNORE:
	F_WS
	| F_SPACING
	| F_TEXT
	| '\\' ('limits' | 'nolimits')
	| '\\displaystyle'
	| '\\' ('left' | 'right');

IGNORE: F_IGNORE -> skip;

// === Basic Operators ===

fragment CDOT: '\\cdot';

PLUS: '+';
MINUS: '-';
MULT: '*' | '\\ast' | CDOT;
DIV: '/' | '\\over';

TIMES: '\\times';
CROSS_PROD: '\\cross' 'product'? | '\\cp';
DOT_PROD: '\\dotproduct' | '\\vdot';

FRAC:
	'\\' [dtcs]? 'frac' -> pushMode(COMM_ARG), pushMode(COMM_ARG)
	| '\\nicefrac' -> pushMode(COMM_ARG), pushMode(COMM_ARG);
BINOM:
	'\\' [dt]? 'binom' -> pushMode(COMM_ARG), pushMode(COMM_ARG);

FUNC_SQRT: '\\sqrt' -> pushMode(COMM_ARG);

CONJUGATE:
	'\\bar' -> pushMode(COMM_ARG)
	| '\\overline' -> pushMode(COMM_ARG);

MOD: '\\' 'b'? 'mod';

// === Literals === TODO: primes? TODO: code action for remapping this to function
SYMBOL: [a-zA-Z]+;

COMMAND: '\\' [a-zA-Z]+;

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

// === Delimiters ===
fragment F_LBRACE: '{';
// TODO: why the push and pop?, well because { } is special in latex
LBRACE: F_LBRACE -> pushMode(DEFAULT_MODE);
RBRACE: '}' -> popMode;

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

// all of these could just be defined in theory? square root is special, though so not this one
// FUNC_EXP: '\\expr'; FUNC_LOG: '\\log'; FUNC_LN: '\\ln'; FUNC_MIN: '\\min'; FUNC_MAX: '\\max';
// FUNC_RE: '\\Re' | '\\real'; FUNC_IM: '\\Im' | '\\imaginary'; FUNC_ARG: '\\arg'; FUNC_SIGN:
// F_OPERATOR F_WS? '{' F_WS? 'sgn' F_WS? '}';

// TODO: next up int and dx stuff!!!
FRAC:
	'frac' -> pushMode(COMM_ARG), pushMode(COMM_ARG); // twice?
INT: 'int' { self.dx_counter += 1 }; // increment DX counter
// check if we *can* lex a DX, and then decrement the DX counter
DX: { self.dx_counter > 0 }? 'd' LETTER+ { self.dx_counter -= 1 };

fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Z];

NUMBER: DIGIT+;
WORD: LETTER+;
COMM: '\\' [a-zA-Z]+;
WS: F_WS -> skip;

mode COMM_ARG;

ARG_DIGIT: DIGIT -> type(NUMBER), popMode;
ARG_LETTER: LETTER -> type(WORD), popMode;
ARG_LBRACE: F_LBRACE -> type(LBRACE), mode(DEFAULT_MODE);
ARG_COMM: '\\' [a-zA-Z]+ -> type(COMM), popMode;
ARG_WS: F_WS -> skip;