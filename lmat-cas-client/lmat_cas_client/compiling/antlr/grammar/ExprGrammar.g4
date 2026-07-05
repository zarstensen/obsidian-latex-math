parser grammar ExprGrammar;
options {
	tokenVocab = ExprLexer;
	language = Python3;
}

@header {
import lmat_cas_client.compiling.antlr.Ast as Ast
from typing import cast, Type, Callable

def rule_t[T](_t: Type[T], v: T | None = None) -> T:
	return cast(T, v)
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
// - [x] inner product, floor, ceil, norm
// - [x] modulo
// - [x] matrix indexing
// - [x] determinant matrix
// - [x] degangements special syntax {! ...}
// - [x] Delta?
// - [x] Eval At
// - [x] cross product
// - [x] organize
// - [ ] primes (for symbols, and derivatives)

debug returns[res = rule_t(Ast.AlgStmt)]:
	alg_statement {$res = $alg_statement.res};

alg_statement returns[res = rule_t(Ast.AlgStmt)]: (a_expr {$res = $a_expr.res} | relation {$res = $relation.res} | system {$res = $system.res}) EOF;

system_el returns[res = rule_t(Ast.SystemEntry)]:
	a_expr {$res = Ast.AExprEntry($ctx, $a_expr.res)} | relation {$res = Ast.RelEntry($ctx, $relation.res)};
system_body returns[res = rule_t(list[Ast.SystemEntry], [])]:
	system_el {$res.append($system_el.res)} (ENV_ROW_SEP system_el {$res.append($system_el.res)})* ENV_ROW_SEP*;
system_env returns[res = rule_t(Ast.SystemEnv)]:
	BEGIN_ENV system_body {$res = Ast.SystemEnv($ctx, $system_body.res)} END_ENV;

system_and_chain
	returns[res = rule_t(Ast.AndChain)]
	locals[elems = rule_t(list[Ast.SystemEntry], [])]:
	system_el {$elems.append($system_el.res)} (AND system_el {$elems.append($system_el.res)})+
		{$res = Ast.AndChain($ctx, $elems)};

system returns[res = rule_t(Ast.System)]: system_env {$res = $system_env.res} | system_and_chain {$res = $system_and_chain.res};

rel_op returns[op = rule_t(type)]: EQ {$op = Ast.Eq} | NEQ {$op = Ast.Neq} | LT {$op = Ast.Lt} | LTE {$op = Ast.Lte} | GT {$op = Ast.Gt} | GTE {$op = Ast.Gte};
relation returns[res = rule_t(Ast.Rel)]:
	a_expr rel_op relation {$res = $rel_op.op ($ctx, $a_expr.res, $relation.res)}
	| lhs=a_expr rel_op rhs=a_expr {$res = $rel_op.op ($ctx, $lhs.res, $rhs.res)};


// TODO: should probably begin implementing the visitor / transformer now that way tests can be set
// up and stuff like that, and also seems to not really have any reamining glaring problems which
// have not been covered.
a_expr
    returns[res = rule_t(Ast.AExpr)]
    locals[node_t = rule_t(type)]:
	<assoc = right> base=a_expr postfix_op {$res = $postfix_op.op ($ctx, $base.res)}

	// \int \frac{\dd ...} {...} case
	| INT int_bounds FRAC LBRACE DIFFERENTIAL diff=a_expr RBRACE recip_integrand=latex_cmd_arg
		{$res = Ast.Integral($ctx, Ast.DivOp($recip_integrand.ctx, Ast.Number($recip_integrand.ctx, "1"), $recip_integrand.res), $diff.res, $int_bounds.bounds)}
	// \int ... \dd ... case
	| INT int_bounds integrand=a_expr DIFFERENTIAL diff=a_expr
		{$res = Ast.Integral($ctx, $integrand.res, $diff.res, $int_bounds.bounds)}

	// \dv{...}{...} cases
	| PHYS_PARTIAL_DERIVATIVE (LBRACKET a_expr RBRACKET)? latex_cmd_arg LBRACE diff_l=a_expr RBRACE LBRACE diff_r=a_expr RBRACE
		{$res = Ast.Differential($ctx, $latex_cmd_arg.res, [($diff_l.res, None), ($diff_r.res, None)])}
	| (PHYS_DERIVATIVE | PHYS_PARTIAL_DERIVATIVE) (LBRACKET degree=a_expr RBRACKET)? latex_cmd_arg LBRACE a_expr RBRACE
		{$res = Ast.Differential($ctx, $latex_cmd_arg.res, [($a_expr.res, $degree.res)])}
	| (PHYS_DERIVATIVE | PHYS_PARTIAL_DERIVATIVE) (LBRACKET degree=a_expr RBRACKET)? latex_cmd_arg diffand_last=a_expr
		{$res = Ast.Differential($ctx, $a_expr.res, [($latex_cmd_arg.res, $degree.res)])}

	// \frac{\dd ...}{\dd .. \dd ..} cases
	| FRAC LBRACE DIFFERENTIAL (LBRACKET degree=a_expr RBRACKET)? a_expr RBRACE LBRACE diff_vars RBRACE    
		{$res = Ast.Differential($ctx, $a_expr.res, $diff_vars.res)}
	| FRAC LBRACE DIFFERENTIAL (LBRACKET degree=a_expr RBRACKET)? RBRACE LBRACE diff_vars RBRACE a_expr    
		{$res = Ast.Differential($ctx, $a_expr.res, $diff_vars.res)}

	| lhs = a_expr LPAREN func_args RPAREN
		{$res = Ast.AmbigApplyFunc($ctx, Ast.ApplyFunc($ctx, $lhs.res, $func_args.res))}
	| lhs = a_expr DIV rhs = a_expr {$res = Ast.DivOp($ctx, $lhs.res, $rhs.res)}
	| lhs = a_expr 
		(
		MULT {$node_t = Ast.MultOp}
		| DOT_PROD {$node_t = Ast.MultOp}
		| MOD {$node_t = Ast.ModOp}
		| TIMES {$node_t = Ast.XProdOp}
		| XPROD {$node_t = Ast.XProdOp}
		) rhs = a_expr
		{$res = $node_t($ctx, $lhs.res, $rhs.res)}
	// dissallow if rhs is number (maybe should be toh number?) or if the following token is a PLUS / MINUS (i.e. a -b does should never be seen as a * (-b)).
	// also cases like ... (...) should not be matched by this rule, this is instead handled by the ApplyFunc production
	// 	{$res = Ast.AmbigApplyFunc($ctx, Ast.ApplyFunc($ctx, $a_expr.res, $func_args.res))}
	// so i *could* do this, or its just like a manual thing i guess for the IR stuff.
	// maybe its best to split stuff into unary binary ternary and so on then...
	// probably that yes
	| lhs = a_expr {((self._input.LA(-1), self._input.LA(1)) != (self.NUMBER, self.NUMBER) and self._input.LA(1) not in (self.PLUS, self.MINUS, self.LPAREN))}? rhs = a_expr
		{$res = Ast.MultOp($ctx, $lhs.res, $rhs.res)}

	// this probably makes the most sense anyway with presedence?
	// feels more consistent atleast, that all of this acts on the remaining term, instead of just the factor?
	// and the other way around is quite conveluted to implement?


	| LIMIT UNDERSCORE LBRACE lim_var=symbol LIMIT_ARROW lim_poa=a_expr limit_dir RBRACE a_expr
		{$res = Ast.Limit($ctx, $a_expr.res, $lim_var.res, $lim_poa.res, $limit_dir.res)}
	| (SUM {$node_t = Ast.Sum} | PRODUCT {$node_t = Ast.Product}) series_range_args LPAREN a_expr RPAREN
		{$res = $node_t($ctx, $a_expr.res, $series_range_args.symb, ($series_range_args.start, $series_range_args.end))}
	| (SUM {$node_t = Ast.Sum} | PRODUCT {$node_t = Ast.Product}) series_range_args a_expr
		{$res = $node_t($ctx, $a_expr.res, $series_range_args.symb, ($series_range_args.start, $series_range_args.end))}

	| lhs = a_expr (PLUS {$node_t = Ast.AddOp} | MINUS {$node_t = Ast.SubOp}) rhs = a_expr
		{$res = $node_t($ctx, $lhs.res, $rhs.res)}
	| (PLUS {$node_t = Ast.UPlusOp} | MINUS {$node_t = Ast.UMinusOp}) a_expr
		{$res = $node_t($ctx, $a_expr.res)}
	| LPAREN expr=a_expr RPAREN PIPE eval_at_arg
		{$res = Ast.EvalAt($ctx, $expr.res, $eval_at_arg.subs_start, $eval_at_arg.subs_end)}
	| LBLANK expr=a_expr PIPE eval_at_arg
		{$res = Ast.EvalAt($ctx, $expr.res, $eval_at_arg.subs_start, $eval_at_arg.subs_end)}
	| LBRACKET expr=a_expr RBRACKET eval_at_arg 
		{$res = Ast.EvalAt($ctx, $expr.res, $eval_at_arg.subs_start, $eval_at_arg.subs_end)}
	| expr=a_expr PIPE eval_at_arg 
		{$res = Ast.EvalAt($ctx, $expr.res, $eval_at_arg.subs_start, $eval_at_arg.subs_end)}

	| combinatorial {$res = $combinatorial.res}
	| delim_expr {$res = $delim_expr.res}
	| cmd_func {$res = $cmd_func.res}
	| matrix {$res = $matrix.res }
	| det_matrix {$res = $det_matrix.res}
	| symbol {$res = $symbol.res}
	| NUMBER {$res = Ast.Number($ctx, $NUMBER.text) };

// matches an atom value, provided the preceeding token,
// pushed the COMM_ARG lexer mode.
// an atom is either a singular letter, or a singular digit.
atom
    returns[res = rule_t(Ast.AExpr)]:
	// TODO: if symbol is in func_set, return function instead.
	primary_symbol {$res = $primary_symbol.res}
	| NUMBER {$res = Ast.Number($ctx, $NUMBER.text)};

// \cmd [[..]]
//      ^ matches the arguments to a latex command
//
// can either be an atom (singular digit, letter or command, this is handled by the lexer), or a brace surrounded expression.
latex_cmd_arg
    returns[res = rule_t(Ast.AExpr)]:
	atom {$res = $atom.res }
	| LBRACE a_expr RBRACE {$res = $a_expr.res};

// .. ^ [[..]]
//      ^ matches the rhs argument to a exponential operation
pow_arg returns[res = rule_t(Ast.AExpr)]:
	atom {$res = $atom.res }
	| cmd_func {$res = $cmd_func.res}
	| LBRACE a_expr RBRACE {$res = $a_expr.res};

// make thingy part of thingy...
postfix_op returns[op = rule_t(Callable[[ParserRuleContext, Ast.AExpr], Ast.PostfixOp])]:
	POW exp = pow_arg UNDERSCORE subscript = subscript_arg
		{$op=lambda ctx, base: Ast.ExpOp(ctx, Ast.SubscriptOp(ctx, base, $subscript.res), $exp.res)}
	| POW exp = pow_arg
		{$op=lambda ctx, base: Ast.ExpOp(ctx, base, $exp.res)}
	| UNDERSCORE subscript = subscript_arg
		{$op = lambda ctx, target: Ast.SubscriptOp(ctx, target, $subscript.res)}
	| BANG {$op = lambda ctx, target: Ast.Factorial(ctx, target)}
	| PERCENT {$op = lambda ctx, target: Ast.Percent(ctx, target)}
	| PERMILLE {$op = lambda ctx, target: Ast.Permille(ctx, target)};

func_args returns[res = rule_t(list[Ast.AExpr], [])]: 
	a_expr {$res.append($a_expr.res)} (COMMA a_expr {$res.append($a_expr.res)})*;

range_slot returns[res = rule_t(tuple[Ast.AExpr | None, Ast.AExpr | None])]:
    beg=a_expr? (delim=COLON|delim=DOTS) end=a_expr? {$res = ($beg.res, $end.res)};
all_slot: MULT | STAR;

slot_entry returns[res = rule_t(Ast.IndexEntry)]:
    a_expr {$res = $a_expr.res}
    | range_slot {$res = $range_slot.res}
    | all_slot {$res = None}
    | {$res = None};

// .. _ [[{..}]]
//      ^ matches the argument to a subscript
// must be a comma separated list of slot_entry
subscript_arg 
	returns[res = rule_t(Ast.Subscript)]
	locals[slots = [], seps = []]:
    atom {$res = Ast.Subscript($ctx, ($atom.res,), Ast.SubscriptForm((None, None), ()))}
    | cmd_func {$res = Ast.Subscript($ctx, ($cmd_func.res,), Ast.SubscriptForm((None, None), ()))}
    | LBRACE (ldelim=LBRACKET|ldelim=LPAREN)?
	a_expr {$slots.append($a_expr.res)}	
	(
		(sep=COMMA | sep=SEMICOLON) slot_entry
{
$res.append($slot_entry.res)
$seps.append($sep.text)
}
	)*
	(rdelim=LBRACKET|rdelim=LPAREN)? RBRACE {$res = Ast.Subscript($ctx, tuple($slots), Ast.SubscriptForm(($ldelim.text, $rdelim.text), tuple($seps)))};

// \int [[_a^b]] .. \dd ..
//      ^ int_bounds matches the bounds of a bounded integral
int_bounds returns[bounds = rule_t(tuple[Ast.AExpr, Ast.AExpr] | None)]: 
    POW upper=latex_cmd_arg UNDERSCORE lower=latex_cmd_arg {$bounds = ($lower.res, $upper.res)}
    | UNDERSCORE lower=latex_cmd_arg POW upper=latex_cmd_arg {$bounds = ($lower.res, $upper.res)}
    | {$bounds = None};
	
diff_var locals[deg: Ast.AExpr | None = None]:
	DIFFERENTIAL a_expr POW latex_cmd_arg {$diff_vars::res.append(($a_expr.res, $latex_cmd_arg.res))}
	| DIFFERENTIAL a_expr {$diff_vars::res.append(($a_expr.res, None))};

// \frac{\dd ..}{[[\dd .. ^ ..]]...}
//               ^ matches all the differential variables + optionally their degree in a
//                 partial derivative.
diff_vars returns[res = rule_t(list[tuple[Ast.AExpr, Ast.AExpr | None]], [])]: diff_var+;

// \lim_{ .. \to .. [[^(+|-)]] }
//                  ^ limit_dir matches the direction for which the limit should be considered
limit_dir returns[res = rule_t(Ast.LimitDir)]:
    {$res = Ast.LimitDir.BOTH}
    | POW LBRACE (PLUS | MINUS) RBRACE {$res = Ast.LimitDir.BOTH}
    | POW PLUS {$res = Ast.LimitDir.POSITIVE}
    | POW MINUS {$res = Ast.LimitDir.NEGATIVE};

// \sum [[_{..=..}^..]] ..
//      ^ matches the range arguments to a series
//        including the inverted alternative, where the superscript is first.
series_range_args
    returns[symb = rule_t(Ast.AExpr), start = rule_t(Ast.AExpr), end = rule_t(Ast.AExpr)]:
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

eval_at_sub_vars returns[res = rule_t(list[tuple[Ast.AExpr, Ast.AExpr], ...], [])]:
	var=a_expr EQ sub=a_expr {$res.append(($var.res, $sub.res))} (COMMA var=a_expr EQ sub=a_expr {$res.append(($var.res, $sub.res))})*;

// .. | [[_{x=.., y=..}^{x=..,y=..}]]
//		^ matches the variables to substitute for an evaluate at expression.
eval_at_arg returns[
	subs_start = rule_t(tuple[tuple[Ast.AExpr, Ast.AExpr], ...]),
	subs_end = rule_t(tuple[tuple[Ast.AExpr, Ast.AExpr], ...] | None)
	]:
	UNDERSCORE LBRACE eval_at_sub_vars RBRACE {$subs_start = tuple($eval_at_sub_vars.res)}
	| UNDERSCORE LBRACE sstart=eval_at_sub_vars RBRACE POW LBRACE send=eval_at_sub_vars RBRACE {
$subs_start = tuple($sstart.res)
$subs_end=tuple($send.res)
}
	| POW LBRACE send=eval_at_sub_vars RBRACE UNDERSCORE LBRACE sstart=eval_at_sub_vars RBRACE {
$subs_start = tuple($sstart.res)
$subs_end=tuple($send.res)
};

// matches a symbol from a lone ID or COMMAND token
primary_symbol returns[res = rule_t(Ast.AExpr)]:
    ID {$res = Ast.Symbol($ctx, $ID.text)}
    | COMMAND {$res = Ast.Symbol($ctx, $COMMAND.text)};

// matches a symbol prefixed with a \Delta symbol.
// e.g. \Delta x
delta_symbol returns[res = rule_t(Ast.AExpr)]:
    DELTA primary_symbol {$res = Ast.Symbol($ctx, f"{$DELTA.text} {$primary_symbol.res.symbol}")};


// need to also allow for indexing here, *except* if symbol itself evaluates to a matrix / indexable value?
// thats prob fine? its just a predicate
symbol returns[res = rule_t(Ast.AExpr)]:
    primary_symbol {$res = $primary_symbol.res}
    | delta_symbol {$res = $delta_symbol.res};

// function_call 
// 	returns[res = rule_t(Ast.ApplyFunc)]
// 	locals[args = rule_t(list[Ast.AExpr], [])]:
// 	a_expr {isinstance($a_expr.res, Ast.Symbol)}? LPAREN RPAREN;


// ok, time to rewrite this so it also support indexing i guess...
// function 
// 	returns[res = rule_t(Ast.ApplyFunc)]
// 	locals[args = rule_t(list[Ast.AExpr], [])]:
// 	(func=FUNC_ID|func=FUNC_CMD) LPAREN (a_expr {$args.append($a_expr.res)} (COMMA a_expr {$args.append($a_expr.res)})*)? RPAREN
// 		{$res = Ast.ApplyFunc($ctx, Ast.Function($func.text), tuple($args))}
// 	| FUNC_CMD LBRACE a_expr RBRACE
// 		{$res = Ast.ApplyFunc($ctx, Ast.Function($FUNC_CMD.text), ($a_expr.res,))}
// 	| FUNC_CMD a_expr
// 		{$res = Ast.ApplyFunc($ctx, Ast.Function($FUNC_CMD.text), ($a_expr.res,))};

// func_call returns[res = rule_t(Ast.AExpr)]:
// 	func=primary_symbol LPAREN RPAREN {$res = Ast.Symbol($ctx, $func.res.symbol)};

// matches operators which are notated via. surrounding an expression with delimiters.
// e.g. (..), |..|
delim_expr returns[res = rule_t(Ast.AExpr)]:
    LPAREN a_expr RPAREN {$res = Ast.Parens($ctx, $a_expr.res)}
    | LBRACKET a_expr RBRACKET {$res = Ast.Parens($ctx, $a_expr.res)}
    | PIPE a_expr PIPE {$res = Ast.Abs($ctx, $a_expr.res)}
    | DOUBLE_PIPE a_expr DOUBLE_PIPE {$res = Ast.Norm($ctx, $a_expr.res)}
    | LFLOOR a_expr RFLOOR {$res = Ast.Floor($ctx, $a_expr.res)}
    | LCEIL a_expr RCEIL {$res = Ast.Ceil($ctx, $a_expr.res)}
    | LANGLE lhs=a_expr (PIPE|COMMA) rhs=a_expr RANGLE {$res = Ast.DotProd($ctx, $lhs.res, $rhs.res)};

combinatorial returns[res = rule_t(Ast.AExpr)]: 
    (LBRACE (UNDERSCORE|POW) n=a_expr op=ID {$ID.text == 'C'}? {($op.text in Ast.CombOpId)}? POW k=a_expr RBRACE
    {$res = Ast.combOpFromId($ctx, $n.res, $k.res, Ast.CombOpId($op.text))}
    | LBRACE ID {$ID.text == 'D'}? POW n=a_expr RBRACE) // TODO this should not be here maybe?
    {$res = Ast.Derangements($ctx, $n.res)}
    | LBRACE BANG n=a_expr RBRACE {$res = Ast.Derangements($ctx, $n.res)};

// these are exclusively built in math functions accessed via. latex commands,
// as in \sqrt .., but not .. ! as this is *not* a command.
cmd_func
    returns[res = rule_t(Ast.AExpr)]:
    FRAC num = latex_cmd_arg den = latex_cmd_arg {$res = Ast.DivOp($ctx, $num.res, $den.res)}
    | BINOM n = latex_cmd_arg k = latex_cmd_arg {$res = Ast.Binom($ctx, $n.res, $k.res)}
    | SQRT latex_cmd_arg {$res = Ast.Root($ctx, $latex_cmd_arg.res, None) }
    | SQRT (LBRACKET root_index = a_expr RBRACKET)? latex_cmd_arg {$res = Ast.Root($ctx, $latex_cmd_arg.res, $root_index.res)
        }
    | CONJUGATE latex_cmd_arg {$res = Ast.Conjugate($ctx, $latex_cmd_arg.res)}
    | VEC_UNIT latex_cmd_arg {$res = Ast.VecUnit($ctx, $latex_cmd_arg.res)};


matrix_row
    returns[res = rule_t(list[Ast.AExpr])]:
    | a_expr {$res = [$a_expr.res]} (ENV_EL_SEP a_expr {$res.append($a_expr.res)})* ;
matrix_body
    returns[res = rule_t(list[list[Ast.AExpr]], [])]:
    | matrix_row {$res = [$matrix_row.res]} (ENV_ROW_SEP matrix_row {$res.append($matrix_row.res)})* ENV_ROW_SEP*;

// matches a matrix, ==> expressions delimited by & and \\ in any matrix or array environment
matrix
    returns[res = rule_t(Ast.Matrix)]:
    (beg=BEGIN_MATRIX matrix_body end=END_MATRIX | beg=BEGIN_ARRAY matrix_body end=END_ARRAY) {$res = Ast.Matrix($ctx, $matrix_body.res, $beg.text, $end.text)};

// special case of matrix for the vmatrix environment
det_matrix returns[res = rule_t(Ast.AExpr)]: BEGIN_V_MATRIX matrix_body END_V_MATRIX {$res = Ast.DetMatrix($ctx, $matrix_body.res)};
