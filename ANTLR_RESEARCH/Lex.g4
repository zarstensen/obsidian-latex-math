lexer grammar Lex;

options {
	language = Python3;
}

@members {
dx_counter = 0
}

LPAREN: '(';
RPAREN: ')';
fragment F_LBRACE: '{';
LBRACE: F_LBRACE -> pushMode(DEFAULT_MODE);
RBRACE: '}' -> popMode;
POW: '^';
MUL: '*';
DIV: '/';
PLUS: '+';
MINUS: '-';
// TODO: next up int and dx stuff!!!
FRAC:
	'frac' -> pushMode(COMM_ARG), pushMode(COMM_ARG); // twice?
INT: 'int' { self.dx_counter += 1 }; // increment DX counter
// check if we *can* lex a DX, and then decrement the DX counter
DX: { self.dx_counter > 0 }? 'd' LETTER+ { self.dx_counter -= 1 };

fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Z];
fragment F_WS: [ \t\n];

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