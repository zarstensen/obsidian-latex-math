parser grammar Gram;
options {
	tokenVocab = Lex;
	language = Python3;
}

debug: expr EOF;

expr:
	LPAREN expr RPAREN
	| LBRACE expr RBRACE
	| expr POW expr
	| expr (MUL | DIV |) expr
	| expr (PLUS | MINUS) expr
	| function
	| COMM
	| NUMBER
	| WORD
	| DX
	;

function:
	FRAC (LBRACE expr RBRACE | atom) (LBRACE expr RBRACE | atom)
	| INT expr
	;


atom: NUMBER | WORD | COMM;