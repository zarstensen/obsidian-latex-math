lexer grammar DefExprLexer;

options {
    language = Python3;
}

import AlgExprLexer;

DEF_SPACE: '\\' 'q'? 'quad' | '\\enspace';

DEF_OP: ':=';

// use this when declaring assumptions on a variable
VAR_ASSUME_OP: '\\in';

// use this when declaring assumptions on a function.
FUN_ASSUME_OP: '\\' 'long'? 'mapsto';

SET_FORMATTER: '\\' (
	| 'pmb'
	| 'boldsymbol'
	| 'mathbf'
	| 'mathbb'
	| 'mathbbm'
	| 'mathcal'
	| 'mathsrc'
);

SET_MINUS: 
	'\\' ( 'setminus' | 'backslash' )
	| '-'
	;

CMD_SET: '\\set';

