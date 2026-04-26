parser grammar ExprGrammar;
options {
	tokenVocab = ExprLexer;
	language = Python3;
}

@header {
import Ast
}

debug: omgomgomg = expr EOF;

// TODO: should probably begin implementing the visitor / transformer now that way tests can be set
// up and stuff like that, and also seems to not really have any reamining glaring problems which
// have not been covered.
expr
	returns[res: Expr]:
	<assoc = right> expr POW (atom | LBRACE expr RBRACE)	# ExponentialOp
	| expr (BANG | PERCENT | PERMILLE)						# Prefix
	| COMMAND LPAREN expr RPAREN							# Command
	| COMMAND LBRACE expr RBRACE							# Command
	| COMMAND expr											# Command
	| expr (MULT | DIV) expr								# MultiplicativeOp
	| lhs = expr (PLUS | MINUS) rhs = expr					# AdditiveOp
	| (PLUS | MINUS) expr									# UAdditiveOp
	| expr expr												# MultiplicativeOp
	| LPAREN expr RPAREN									# Stub
	| function												# Stub
	| atom {$res = $atom.res }								# Stub;

atom
	returns[res: Ast.Atom]:
	SYMBOL {$res = Ast.Symbol($SYMBOL.text)}
	| COMMAND {$res = Ast.Symbol($COMMAND.text)}
	| NUMBER {$res = Ast.Number($NUMBER.text)};

function: FUNCTION LPAREN (expr (COMMA expr)*)? RPAREN;