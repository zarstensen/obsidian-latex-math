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
	| DX;

function:
	FRAC (LBRACE expr RBRACE | atom) (LBRACE expr RBRACE | atom)
	| INT+ expr DX+
	| INT+ FRAC LBRACE DX+ RBRACE (LBRACE expr RBRACE | atom) DX+;

atom: NUMBER | WORD | COMM;