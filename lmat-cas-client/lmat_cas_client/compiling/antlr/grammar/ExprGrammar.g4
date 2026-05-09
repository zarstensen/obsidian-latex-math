parser grammar ExprGrammar;
options {
	tokenVocab = ExprLexer;
	language = Python3;
}

@header {
import lmat_cas_client.compiling.antlr.Ast as Ast
}

@members {
func_set: set[str] = set()
}

debug
	returns[res: Ast.AstNode]: (expr_system {$res = $expr_system.res} | a_expr {$res = $a_expr.res}) EOF ;

rel_op: EQ | NEQ | LT | LTE | GT | GTE;
relation: a_expr (rel_op a_expr)*;

// TODO: different name, dont know what this is called
deriv_arg locals[deg: Expr | None = None]:
	DIFFERENTIAL a_expr POW latex_cmd_arg {$deriv_args::res.append(($a_expr.res, $latex_cmd_arg.res))}
	| DIFFERENTIAL a_expr {$deriv_args::res.append(($a_expr.res, None))};

deriv_args returns[res: list[tuple[Expr, Expr | None]] = []]: deriv_arg+;

//TODO:
// - [x] matrices / environments - [x] derivatives (physics + frac) - [x] integrals - [x] optional
// latex arg (\\sqrt[...]{}) - [ ] abs + norm + maybe other things i have missed? - [x]
// combinatorics special notation {_n C ^k} - [x] differential grammar, this maybe depends on
// optional latex arg?
// - [x] how to handle args to derivatives VERY IMPORTANT!!!!!!
//   SOLUTION: has to be done during evaluation, so the derivatives first go through all their function children and differentiate, and *then* apply their arguments during evaluation,
//   so nothing parser specific, should be fine

int_bounds returns[bounds: tuple[Expr, Expr] | None]: 
	POW upper=latex_cmd_arg UNDERSCORE lower=latex_cmd_arg {$bounds = ($lower.res, $upper.res)}
	| UNDERSCORE lower=latex_cmd_arg POW upper=latex_cmd_arg {$bounds = ($lower.res, $upper.res)}
	| {$bounds = None}
	;

// TODO: should probably begin implementing the visitor / transformer now that way tests can be set
// up and stuff like that, and also seems to not really have any reamining glaring problems which
// have not been covered.
a_expr
	returns[res: Expr]
	locals[node_t: type]:
	<assoc = right> base = a_expr POW exp = pow_arg
	{$res=Ast.ExpOp($ctx, $base.res, $exp.res)}                                                                                                              # ExponentialOp
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
	) {$res = $node_t($ctx, $op.res)}                                                                                                                        # Prefix
	// \dv{...}{...} cases
	| PHYS_PARTIAL_DERIVATIVE (LBRACKET a_expr RBRACKET)? latex_cmd_arg LBRACE diff_l=a_expr RBRACE LBRACE diff_r=a_expr RBRACE
	{$res = Ast.Differential($ctx, $latex_cmd_arg.res, [($diff_l.res, None), ($diff_r.res, None)])}                                                          # Deriv
	| (PHYS_DERIVATIVE | PHYS_PARTIAL_DERIVATIVE) (LBRACKET deg=a_expr RBRACKET)? latex_cmd_arg LBRACE a_expr RBRACE
	{$res = Ast.Differential($ctx, $latex_cmd_arg.res, [($a_expr.res, $deg.res)])}                                                                           # Deriv
	| (PHYS_DERIVATIVE | PHYS_PARTIAL_DERIVATIVE) (LBRACKET deg=a_expr RBRACKET)? latex_cmd_arg diffand_last=a_expr
	{$res = Ast.Differential($ctx, $a_expr.res, [($latex_cmd_arg.res, $deg.res)])}                                                                           # Deriv
	// \frac{\dd ...}{\dd .. \dd ..} cases
	| FRAC LBRACE DIFFERENTIAL (LBRACKET diff=a_expr RBRACKET)? a_expr RBRACE LBRACE deriv_args RBRACE    
	{$res = Ast.Differential($ctx, $a_expr.res, $deriv_args.res)}                                                                                            # Deriv
	| FRAC LBRACE DIFFERENTIAL (LBRACKET diff=a_expr RBRACKET)? RBRACE LBRACE deriv_args RBRACE a_expr    
	{$res = Ast.Differential($ctx, $a_expr.res, $deriv_args.res)}                                                                                            # Deriv
	| FUNCTION LPAREN (a_expr (COMMA a_expr)*)? RPAREN                                                                                                       # Function
	| FUNCTION LBRACE a_expr RBRACE                                                                                                                          # Function // Only allow these alternatives if function
	| FUNCTION a_expr                                                                                                                                        # Function // was from a command? this *could* be stored in the AST
	| LIMIT UNDERSCORE LBRACE lim_var=symbol LIMIT_ARROW lim_poa=a_expr limit_dir RBRACE a_expr
	{$res = Ast.Limit($a_expr.res, $lim_var.res, $lim_poa.res, $limit_dir.res)}                                                                              # Limit
	| lhs = a_expr (
		MULT {$node_t = Ast.MultOp}
		| DIV {$node_t = Ast.DivOp}
	) rhs = a_expr {$res = $node_t($ctx, $lhs.res, $rhs.res)}                                                                                                # MultiplicativeOp
	// dissallow if rhs is number (maybe should be toh number?) or if the following token is a PLUS / MINUS (i.e. a -b does should never be seen as a * (-b)).
	|  lhs = a_expr {((self._input.LA(-1), self._input.LA(1)) != (self.NUMBER, self.NUMBER) and self._input.LA(1) not in (self.PLUS, self.MINUS))}? rhs = a_expr 
		{$res = Ast.MultOp($ctx, $lhs.res, $rhs.res)}                                                                                                        # MultiplicativeOp
	| (SUM {$node_t = Ast.Sum} | PRODUCT {$node_t = Ast.Product}) series_range_args LPAREN a_expr RPAREN
	{$res = $node_t($ctx, $a_expr.res, $series_range_args.symb, ($series_range_args.start, $series_range_args.end))} # Series
	| (SUM {$node_t = Ast.Sum} | PRODUCT {$node_t = Ast.Product}) series_range_args a_expr
	{$res = $node_t($ctx, $a_expr.res, $series_range_args.symb, ($series_range_args.start, $series_range_args.end))} # Series
	| lhs = a_expr (
		PLUS {$node_t = Ast.AddOp}
		| MINUS {$node_t = Ast.SubOp}
	) rhs = a_expr {$res = $node_t($ctx, $lhs.res, $rhs.res)}                                                                                                # AdditiveOp
	| (
		PLUS {$node_t = Ast.UPlusOp}
		| MINUS {$node_t = Ast.UMinusOp}
	) a_expr {$res = $node_t($ctx, $a_expr.res)}                                                                                                             # UAdditiveOp

	| LBRACE (UNDERSCORE|POW) lhs=a_expr op=symbol POW rhs=a_expr RBRACE {$res = Ast.Number($ctx, '1')}
{
#$res = Ast.tryMakeComb($lhs.res, $rhs.res, $op.res)
}# Comb

	| LPAREN a_expr RPAREN {$res = $a_expr.res.mut_ctx($ctx)}                                                                                                # Stub
	| BAR a_expr BAR {$res = Ast.Abs($ctx, $a_expr.res)}                                                                                                     # Abs
	| builtin_func {$res = $builtin_func.res}                                                                                                                # Stub
	| matrix {$res = $matrix.res }                                                                                                                           # Stub
	| subscript_symbol {$res = $subscript_symbol.res}                                                                                                        # Stub
	| atom {$res = $atom.res }                                                                                                                               # Stub;


atom
	returns[res: Expr]:
	// TODO: if symbol is in func_set, return function instead.
	symbol {$res = $symbol.res}
	| NUMBER {$res = Ast.Number($ctx, $NUMBER.text)};

symbol returns[res: Expr]:
	ID {$res = Ast.Symbol($ctx, $ID.text)}
	| COMMAND {$res = Ast.Symbol($ctx, $COMMAND.text)};

subscript_arg returns[res: list[Expr] = []]:
	atom {$res = [$atom.res]}
	| builtin_func {$res = [$builtin_func.res]}
	| LBRACE  first=a_expr {$res = [$a_expr.res]} (COMMA rem=a_expr {$res.append($rem.res)})* RBRACE;

subscript_symbol returns[res: Expr]: symbol UNDERSCORE subscript_arg {$res = Ast.SubscriptSymbol($ctx, $symbol.res, $subscript_arg.res)};


// argument to a latex command, so can either be an atom (singular digit, letter or command, this is handled by the lexer), or a brace surrounded expression.
latex_cmd_arg
	returns[res: Expr]:
	atom {$res = $atom.res }
	| LBRACE a_expr RBRACE {$res = $a_expr.res};

pow_arg
	returns[res: Expr]:
	atom {$res = $atom.res }
	| builtin_func {$res = $builtin_func.res}
	| LBRACE a_expr RBRACE {$res = $a_expr.res};

limit_dir returns[res: Ast.LimitDir]:
	{$res = Ast.LimitDir.BOTH}
	| POW LBRACE (PLUS | MINUS) RBRACE {$res = Ast.LimitDir.BOTH}
	| POW PLUS {$res = Ast.LimitDir.POSITIVE}
	| POW MINUS {$res = Ast.LimitDir.NEGATIVE};

series_range_args
	returns[symb: Ast.Symbol, start: Ast.Expr, end: Ast.Expr]:
	UNDERSCORE LBRACE symbol EQ a_expr RBRACE POW latex_cmd_arg {
$symb = $symbol.res
$start = $a_expr.res
$end = $latex_cmd_arg.res
}
	| POW latex_cmd_arg UNDERSCORE LBRACE symbol EQ a_expr RBRACE {
$symb = $symbol.res
$start = $a_expr.res
$end = $latex_cmd_arg.res
};

// these are exclusively built in math functions accessed via. latex commands,
// as in \sqrt .., but not .. ! as this is *not* a command.
builtin_func
	returns[res: Ast.BuiltinFunc]:
	FRAC num = latex_cmd_arg den = latex_cmd_arg {$res = Ast.DivOp($ctx, $num.res, $den.res)}
	| BINOM n = latex_cmd_arg k = latex_cmd_arg {$res = Ast.Binom($ctx, $n.res, $k.res)}
	| SQRT latex_cmd_arg {$res = Ast.Root($ctx, $latex_cmd_arg.res, None) }
	| SQRT (LBRACKET index = a_expr RBRACKET)? latex_cmd_arg {$res = Ast.Root($ctx, $latex_cmd_arg.res, $index.res)
		}
	| CONJUGATE latex_cmd_arg {$res = Ast.Conjugate($ctx, $latex_cmd_arg.res)}
	| VEC_UNIT latex_cmd_arg {$res = Ast.VecUnit($ctx, $latex_cmd_arg.res)};


matrix_el: a_expr {$matrix_row::res.append($a_expr.res) };
matrix_row
	locals[res: list[Ast.Expr] = []]:
	| matrix_el (ENV_EL_SEP matrix_el)* {$matrix_body::res.append($res)};
matrix_body
	returns[res: list[list[Ast.Expr]] = []]:
	| matrix_row (ENV_ROW_SEP matrix_row)* ENV_ROW_SEP*;

matrix
	returns[res: Ast.Matrix]:
	BEGIN_MATRIX matrix_body END_MATRIX {$res = Ast.Matrix($ctx, $matrix_body.res, $BEGIN_MATRIX.text, $END_MATRIX.text)};


expr_system_expr: a_expr {$expr_system_body::res.append($a_expr.res)};
expr_system_body returns[res: list[Expr] = []]: | expr_system_expr (ENV_ROW_SEP expr_system_expr)* ENV_ROW_SEP*;
expr_system returns[res: Ast.ExprSystem]: BEGIN_ENV body=expr_system_body END_ENV {$res = Ast.ExprSystem($ctx, $body.res)};

