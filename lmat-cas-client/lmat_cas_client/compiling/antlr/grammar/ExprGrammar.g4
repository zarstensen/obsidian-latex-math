parser grammar ExprGrammar;
options {
	tokenVocab = ExprLexer;
	language = Python3;
}

debug: .*? EOF;
