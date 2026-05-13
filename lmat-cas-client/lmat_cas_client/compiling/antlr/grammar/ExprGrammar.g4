parser grammar ExprGrammar;
options {
	tokenVocab = ExprLexer;
	language = Python3;
}

@header {
import lmat_cas_client.compiling.antlr.Ast as Ast
from typing import cast
}

@members {
func_set: set[str] = set()
}

//TODO:
// - [x] matrices / environments - [x] derivatives (physics + frac) - [x] integrals - [x] optional
// latex arg (\\sqrt[...]{}) - [ ] abs + norm + maybe other things i have missed? - [x]
// combinatorics special notation {_n C ^k} - [x] differential grammar, this maybe depends on
// optional latex arg?
// - [x] how to handle args to derivatives VERY IMPORTANT!!!!!!
//   SOLUTION: has to be done during evaluation, so the derivatives first go through all their function children and differentiate, and *then* apply their arguments during evaluation,
//   so nothing parser specific, should be fine
// - [ ] inner product, floor, ceil, norm
// - [x] modulo
// - [ ] matrix indexing
// - [ ] determinant matrix
// - [x] degangements special syntax {! ...}
// - [x] Delta?
// - [ ] cross product
// - [ ] organize

debug
	returns[res = cast(Ast.Expr, None)]: (expr_system {$res = $expr_system.res} | a_expr {$res = $a_expr.res}) EOF ;

relation: a_expr rel_op relation
	| a_expr;

// TODO: should probably begin implementing the visitor / transformer now that way tests can be set
// up and stuff like that, and also seems to not really have any reamining glaring problems which
// have not been covered.
a_expr
	returns[res = cast(Ast.Expr, None)]
	locals[node_t: type]:
	base = a_expr POW exp = pow_arg UNDERSCORE index = index_arg
		{$res=Ast.ExpOp($ctx, $base.res, $exp.res)}                                                                                                              # IndexPow
	| <assoc = right> base = a_expr POW exp = pow_arg
		{$res=Ast.ExpOp($ctx, $base.res, $exp.res)}                                                                                                              # Pow
	| a_expr UNDERSCORE index = index_arg # Index

	// \int \frac{\dd ...} {...} case
	| INT int_bounds FRAC LBRACE DIFFERENTIAL diff=a_expr RBRACE recip_integrand=latex_cmd_arg
		{$res = Ast.Integral($ctx, Ast.DivOp($recip_integrand.ctx, Ast.Number($recip_integrand.ctx, "1"), $recip_integrand.res), $diff.res, $int_bounds.bounds)} # Int
	// \int ... \dd ... case
	| INT int_bounds integrand=a_expr DIFFERENTIAL diff=a_expr
		{$res = Ast.Integral($ctx, $integrand.res, $diff.res, $int_bounds.bounds)}                                                                               # Int

	| op = a_expr (
		BANG {$node_t = Ast.Factorial}
		| PERCENT {$node_t = Ast.Percent}
		| PERMILLE {$node_t = Ast.Permille}
	) {$res = $node_t($ctx, $op.res)}                                                                                                                            # Prefix

	// \dv{...}{...} cases
	| PHYS_PARTIAL_DERIVATIVE (LBRACKET a_expr RBRACKET)? latex_cmd_arg LBRACE diff_l=a_expr RBRACE LBRACE diff_r=a_expr RBRACE
		{$res = Ast.Differential($ctx, $latex_cmd_arg.res, [($diff_l.res, None), ($diff_r.res, None)])}                                                          # Deriv
	| (PHYS_DERIVATIVE | PHYS_PARTIAL_DERIVATIVE) (LBRACKET degree=a_expr RBRACKET)? latex_cmd_arg LBRACE a_expr RBRACE
		{$res = Ast.Differential($ctx, $latex_cmd_arg.res, [($a_expr.res, $degree.res)])}                                                                        # Deriv
	| (PHYS_DERIVATIVE | PHYS_PARTIAL_DERIVATIVE) (LBRACKET degree=a_expr RBRACKET)? latex_cmd_arg diffand_last=a_expr
		{$res = Ast.Differential($ctx, $a_expr.res, [($latex_cmd_arg.res, $degree.res)])}                                                                        # Deriv
	// \frac{\dd ...}{\dd .. \dd ..} cases
	| FRAC LBRACE DIFFERENTIAL (LBRACKET degree=a_expr RBRACKET)? a_expr RBRACE LBRACE diff_vars RBRACE    
		{$res = Ast.Differential($ctx, $a_expr.res, $diff_vars.res)}                                                                                             # Deriv
	| FRAC LBRACE DIFFERENTIAL (LBRACKET degree=a_expr RBRACKET)? RBRACE LBRACE diff_vars RBRACE a_expr    
		{$res = Ast.Differential($ctx, $a_expr.res, $diff_vars.res)}                                                                                             # Deriv

	| FUNCTION LPAREN (a_expr (COMMA a_expr)*)? RPAREN                                                                                                           # Function
	| FUNCTION LBRACE a_expr RBRACE                                                                                                                              # Function // Only allow these alternatives if function
	| FUNCTION a_expr                                                                                                                                            # Function // was from a command? this *could* be stored in the AST

	| LIMIT UNDERSCORE LBRACE lim_var=symbol LIMIT_ARROW lim_poa=a_expr limit_dir RBRACE a_expr
		{$res = Ast.Limit($a_expr.res, $lim_var.res, $lim_poa.res, $limit_dir.res)}                                                                              # Limit

	| lhs = a_expr (
		MULT {$node_t = Ast.MultOp}
		| DIV {$node_t = Ast.DivOp}
		| MOD {$node_t = Ast.ModOp}
	) rhs = a_expr {$res = $node_t($ctx, $lhs.res, $rhs.res)}                                                                                                    # MultiplicativeOp
	// dissallow if rhs is number (maybe should be toh number?) or if the following token is a PLUS / MINUS (i.e. a -b does should never be seen as a * (-b)).
	|  lhs = a_expr {((self._input.LA(-1), self._input.LA(1)) != (self.NUMBER, self.NUMBER) and self._input.LA(1) not in (self.PLUS, self.MINUS))}? rhs = a_expr 
		{$res = Ast.MultOp($ctx, $lhs.res, $rhs.res)}                                                                                                            # MultiplicativeOp

	| (SUM {$node_t = Ast.Sum} | PRODUCT {$node_t = Ast.Product}) series_range_args LPAREN a_expr RPAREN
		{$res = $node_t($ctx, $a_expr.res, $series_range_args.symb, ($series_range_args.start, $series_range_args.end))}                                         # Series
	| (SUM {$node_t = Ast.Sum} | PRODUCT {$node_t = Ast.Product}) series_range_args a_expr
		{$res = $node_t($ctx, $a_expr.res, $series_range_args.symb, ($series_range_args.start, $series_range_args.end))}                                         # Series

	| lhs = a_expr (
		PLUS {$node_t = Ast.AddOp}
		| MINUS {$node_t = Ast.SubOp}
	) rhs = a_expr {$res = $node_t($ctx, $lhs.res, $rhs.res)}                                                                                                    # AdditiveOp
	| (
		PLUS {$node_t = Ast.UPlusOp}
		| MINUS {$node_t = Ast.UMinusOp}
	) a_expr {$res = $node_t($ctx, $a_expr.res)}                                                                                                                 # UAdditiveOp

	| combinatorial {$res = $combinatorial.res}                                                                                                                  # Comb
	| delim_expr {$res = $delim_expr.res}                                                                                                                        # DelimitedExpr
	| builtin_func {$res = $builtin_func.res}                                                                                                                    # Stub
	| matrix {$res = $matrix.res }                                                                                                                               # Stub
	| symbol {$res = $symbol.res}                                                                                                                                # Stub
	| NUMBER {$res = Ast.Number($ctx, $NUMBER.text) }                                                                                                            # Stub;


rel_op: EQ | NEQ | LT | LTE | GT | GTE;

// matches an atom value, provided the preceeding token,
// pushed the COMM_ARG lexer mode.
// an atom is either a singular letter, or a singular digit.
atom
	returns[res: Ast.Expr]:
	// TODO: if symbol is in func_set, return function instead.
	primary_symbol {$res = $primary_symbol.res}
	| NUMBER {$res = Ast.Number($ctx, $NUMBER.text)};

// \cmd [[..]]
//      ^ matches the arguments to a latex command
//
// can either be an atom (singular digit, letter or command, this is handled by the lexer), or a brace surrounded expression.
latex_cmd_arg
	returns[res: Ast.Expr]:
	atom {$res = $atom.res }
	| LBRACE a_expr RBRACE {$res = $a_expr.res};

// .. ^ [[..]]
//      ^ matches the rhs argument to a exponential operation
pow_arg
	returns[res: Ast.Expr]:
	atom {$res = $atom.res }
	| builtin_func {$res = $builtin_func.res}
	| LBRACE a_expr RBRACE {$res = $a_expr.res};

// \int [[_a^b]] .. \dd ..
//      ^ int_bounds matches the bounds of a bounded integral
int_bounds returns[bounds: tuple[Ast.Expr, Ast.Expr] | None]: 
	POW upper=latex_cmd_arg UNDERSCORE lower=latex_cmd_arg {$bounds = ($lower.res, $upper.res)}
	| UNDERSCORE lower=latex_cmd_arg POW upper=latex_cmd_arg {$bounds = ($lower.res, $upper.res)}
	| {$bounds = None};
	
diff_var locals[deg: Ast.Expr | None = None]:
	DIFFERENTIAL a_expr POW latex_cmd_arg {$diff_vars::res.append(($a_expr.res, $latex_cmd_arg.res))}
	| DIFFERENTIAL a_expr {$diff_vars::res.append(($a_expr.res, None))};

// \frac{\dd ..}{[[\dd .. ^ ..]]...}
//               ^ matches all the differential variables + optionally their degree in a
//                 partial derivative.
diff_vars returns[res: list[tuple[Ast.Expr, Ast.Expr | None]] = []]: diff_var+;

// \lim_{ .. \to .. [[^(+|-)]] }
//                  ^ limit_dir matches the direction for which the limit should be considered
limit_dir returns[res: Ast.LimitDir]:
	{$res = Ast.LimitDir.BOTH}
	| POW LBRACE (PLUS | MINUS) RBRACE {$res = Ast.LimitDir.BOTH}
	| POW PLUS {$res = Ast.LimitDir.POSITIVE}
	| POW MINUS {$res = Ast.LimitDir.NEGATIVE};

// \sum [[_{..=..}^..]] ..
//      ^ matches the range arguments to a series
//        including the inverted alternative, where the superscript is first.
series_range_args
	returns[symb: Ast.Ast.Expr, start: Ast.Expr, end: Ast.Expr]:
	UNDERSCORE LBRACE var=a_expr EQ s=a_expr RBRACE POW e=pow_arg {
$symb = $var.res
$start = $s.res
$end = $e.res
}
	| POW e=pow_arg UNDERSCORE LBRACE var=a_expr EQ s=a_expr RBRACE {
$symb = $var.res
$start = $s.res
$end = $e.res
};


// matches a symbol from a lone ID or COMMAND token
primary_symbol returns[res: Ast.Expr]:
	ID {$res = Ast.Symbol($ctx, $ID.text)}
	| COMMAND {$res = Ast.Symbol($ctx, $COMMAND.text)};

// matches a symbol prefixed with a \Delta symbol.
// e.g. \Delta x
delta_symbol returns[res: Ast.Expr]:
	DELTA primary_symbol {$res = Ast.Symbol($ctx, f"{$DELTA.text} {$primary_symbol.res.symbol}")};

symbol returns[res: Ast.Expr]:
	primary_symbol {$res = $primary_symbol.res}
	| delta_symbol {$res = $delta_symbol.res};

// matches operators which are notated via. surrounding an expression with delimiters.
// e.g. (..), |..|
delim_expr returns[res: Ast.Expr]:
	LPAREN a_expr RPAREN {$res = $a_expr.res.mut_ctx($ctx)}
	| BAR a_expr BAR //{$res = Ast.Abs($ctx, $a_expr.res)}
	| LFLOOR a_expr RFLOOR //{$res = Ast.Floor($ctx, $a_expr.res)}
	| LCEIL a_expr RCEIL //{$res = Ast.Ceil($ctx, $a_expr.res)}
	| LANGLE a_expr (BAR|COMMA) a_expr RANGLE;

combinatorial returns[res: Ast.Expr]: 
	LBRACE (UNDERSCORE|POW) n=a_expr op=ID {($op.text in Ast.CombOpId)}? POW k=a_expr RBRACE
	{$res = Ast.combOpFromId($ctx, $n.res, $k.res, Ast.CombOpId($op.text))}
	| LBRACE ID {$ID.text == 'D'}? POW n=a_expr RBRACE // TODO this should not be here maybe?
	{$res = Ast.Derangements($ctx, $n.res)}
	| LBRACE BANG n=a_expr RBRACE {$res = Ast.Derangements($ctx, $n.res)};



// TODO: what should the last rule be called? which matches a index value, i.e. not a range or a catch all, just a concrete index
singular_index: a_expr;
range_index: from=a_expr? (COLON|DOTS) to=a_expr?;
all_index: MULT | STAR;

index_entry: singular_index | range_index | all_index | ;

index_arg:
	LBRACE (LBRACKET|LPAREN)? index_entry ((COMMA | SEMICOLON) index_entry)+ (LBRACKET|LPAREN)? RBRACE
	| atom
	| builtin_func;

// these are exclusively built in math functions accessed via. latex commands,
// as in \sqrt .., but not .. ! as this is *not* a command.
builtin_func
	returns[res: Ast.BuiltinFunc]:
	FRAC num = latex_cmd_arg den = latex_cmd_arg {$res = Ast.DivOp($ctx, $num.res, $den.res)}
	| BINOM n = latex_cmd_arg k = latex_cmd_arg {$res = Ast.Binom($ctx, $n.res, $k.res)}
	| SQRT latex_cmd_arg {$res = Ast.Root($ctx, $latex_cmd_arg.res, None) }
	| SQRT (LBRACKET root_index = a_expr RBRACKET)? latex_cmd_arg {$res = Ast.Root($ctx, $latex_cmd_arg.res, $root_index.res)
		}
	| CONJUGATE latex_cmd_arg {$res = Ast.Conjugate($ctx, $latex_cmd_arg.res)}
	| VEC_UNIT latex_cmd_arg {$res = Ast.VecUnit($ctx, $latex_cmd_arg.res)};


matrix_row
	returns[res: list[Ast.Expr]]:
	| a_expr {$res = [$a_expr.res]} (ENV_EL_SEP a_expr {$res.append($a_expr.res)})* ;
matrix_body
	returns[res: list[list[Ast.Expr]] = []]:
	| matrix_row {$res = [$matrix_row.res]} (ENV_ROW_SEP matrix_row {$res.append($matrix_row.res)})* ENV_ROW_SEP*;

matrix
	returns[res: Ast.Matrix]:
	(beg=BEGIN_MATRIX matrix_body end=END_MATRIX | beg=BEGIN_ARRAY matrix_body end=END_ARRAY) {$res = Ast.Matrix($ctx, $matrix_body.res, $beg.text, $end.text)};


expr_system_expr: a_expr {$expr_system_body::res.append($a_expr.res)};
expr_system_body returns[res: list[Ast.Expr] = []]: | expr_system_expr (ENV_ROW_SEP expr_system_expr)* ENV_ROW_SEP*;
expr_system returns[res: Ast.ExprSystem]: BEGIN_ENV body=expr_system_body END_ENV {$res = Ast.ExprSystem($ctx, $body.res)};

