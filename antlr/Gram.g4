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
	| FRAC (LBRACE expr RBRACE | atom) (
		LBRACE expr RBRACE
		| atom
	)
	| COMM
	| NUMBER
	| WORD;

atom: NUMBER | WORD | COMM;