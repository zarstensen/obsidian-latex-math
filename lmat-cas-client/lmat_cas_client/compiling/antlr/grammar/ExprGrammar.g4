parser grammar ExprGrammar;
options {
	tokenVocab = ExprLexer;
	language = Python3;
}

@header {
import Ast
}

debug: expr EOF;

// TODO: should probably begin implementing the visitor / transformer now that way tests can be set
// up and stuff like that, and also seems to not really have any reamining glaring problems which
// have not been covered.
// The only final thing i can think of is presedence of \sum and \prod, but that should not be an issue either really
expr
	returns[res: Expr]:
	<assoc = right> expr POW (atom | LBRACE expr RBRACE)	# ExponentialOp
	| expr (BANG | PERCENT | PERMILLE)						# Prefix
	| FUNCTION LPAREN (expr (COMMA expr)*)? RPAREN							# Command
	| FUNCTION LBRACE expr RBRACE							# Command // Only allow these alternatives if function
	| FUNCTION expr											# Command // was from a command? this *could* be stored in the AST
	| expr (MULT | DIV) expr								# MultiplicativeOp
	| lhs = expr (PLUS | MINUS) rhs = expr					# AdditiveOp
	| (PLUS | MINUS) expr									# UAdditiveOp
	| expr expr												# MultiplicativeOp // dissallow if both expr are NUMBER
	| (SUM | PRODUCT | LIMIT) LPAREN expr RPAREN #Series
	| (SUM | PRODUCT | LIMIT) expr #Series
	| INT expr DIFFERENTIAL # int
	| LPAREN expr RPAREN									# Stub
	| atom {$res = $atom.res }								# Stub;

atom
	returns[res: Ast.Atom]:
	SYMBOL {$res = Ast.Symbol($SYMBOL.text)}
	| COMMAND {$res = Ast.Symbol($COMMAND.text)}
	| NUMBER {$res = Ast.Number($NUMBER.text)};

hard_func returns[res: Ast.HardFunc]:
	FRAC (num=atom | LBRACE num=expr RBRACE) (denom=atom | LBRACE denom=expr RBRACE)
	| BINOM (atom | LBRACE expr RBRACE) (atom | LBRACE expr RBRACE)
	| SQRT (atom | LBRACE expr RBRACE)
	| CONJUGATE (atom | LBRACE expr RBRACE)
	| VEC_UNIT (atom | LBRACE expr RBRACE);
