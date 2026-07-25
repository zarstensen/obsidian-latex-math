lexer grammar DefStmtLexer;

options {
    language = Python3;
	superClass = LexerBase;
}

import AlgStmtLexer;

// TODO: this should go out of set mode
fragment F_DEF_SEP: '\\' 'q'? 'quad' | '\\enspace';

DEF_SEP: F_DEF_SEP;

DEF_OP: ':=';

// use this when declaring assumptions on a variable
VAR_ASSUME_OP: '\\in' -> pushMode(SET);

// use this when declaring assumptions on a function.
FUN_ASSUME_OP: '\\' 'long'? 'mapsto' -> pushMode(SET);

mode SET;

SET_COMPLEX: 'C';
SET_REAL: 'R';
SET_IMAGINARY: 'I';
SET_RATIONAL: 'Q';
SET_INTEGER: 'Z';
SET_NATURAL: 'N';
SET_EVEN: 'E';
SET_ODD: 'O';
SET_PRIME: 'P';

SET_FORMATTER: '\\' (
	| 'pmb'
	| 'boldsymbol'
	| 'mathbf'
	| 'mathbb'
	| 'mathbbm'
	| 'mathcal'
	| 'mathsrc'
);

SET_LBRACE: F_LBRACE;
SET_RBRACE: F_RBRACE;

SET_ZERO: '0';
SET_UNDERSCORE: '_';

SET_MINUS: 
	'\\' ( 'setminus' | 'backslash' )
	;

SET_SUB: '-';
SET_ADD: '+';

SET_LT: F_LT;
SET_LTE: F_LTE;
SET_GT: F_GT;
SET_GTE: F_GTE;

SET_OVERLINE: '\\' ('bar' | 'overline'); 

SET_CMD: '\\set';

SET_DEF_SEP: F_DEF_SEP -> popMode;
