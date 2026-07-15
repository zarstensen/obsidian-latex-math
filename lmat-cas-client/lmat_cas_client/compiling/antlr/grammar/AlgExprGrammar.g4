parser grammar AlgExprGrammar;
options {
	tokenVocab = AlgExprLexer;
	language = Python3;
}

@header {
from lmat_cas_client.compiling.antlr.ast import AlgStmtAst as Ast
from typing import cast, Type, Callable

def rule_t[T](_t: Type[T], v: T | None = None) -> T:
	return cast(T, v)
}

//TODO:
// - [x] matrices / environments - [x] derivatives (physics + frac) - [x] integrals - [x] optional
// latex arg (\\sqrt[...]{}) - [x] abs + norm + maybe other things i have missed? - [x]
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
// - [ ] trigonometric functions

debug returns[res = rule_t(Ast.AlgStmt)]:
	alg_statement {$res = $alg_statement.res};

// matches any complete algebraic expression, relation, or system
// e.g. 1 + 1, 2 < 3, \begin{cases} x + y = 2 \end{cases}
alg_statement returns[res = rule_t(Ast.AlgStmt)]: (a_expr {$res = $a_expr.res} | relation {$res = $relation.res} | system {$res = $system.res}) EOF;

// matches a single element within a system — either an expression or a relation
// e.g. x^2 + 1  or  x > 1
system_el returns[res = rule_t(Ast.SystemEntry)]:
	a_expr {$res = Ast.AExprEntry($ctx, $a_expr.res)} | relation {$res = Ast.RelEntry($ctx, $relation.res)};
// matches one or more system elements separated by \\ row separators
// e.g. x + y = 2 \\ x - y = 1
system_body returns[res = rule_t(list[Ast.SystemEntry], [])]:
	system_el {$res.append($system_el.res)} (ENV_ROW_SEP system_el {$res.append($system_el.res)})* ENV_ROW_SEP*;
system_env returns[res = rule_t(Ast.SystemEnv)]:
	BEGIN_ENV system_body {$res = Ast.SystemEnv($ctx, $system_body.res)} END_ENV;

// matches relations chained by and operators,
// e.g. 2 < 3 \land x = y
system_and_chain
	returns[res = rule_t(Ast.AndChain)]
	locals[elems = rule_t(list[Ast.SystemEntry], [])]:
	system_el {$elems.append($system_el.res)} (AND system_el {$elems.append($system_el.res)})+
		{$res = Ast.AndChain($ctx, $elems)};

// matches either an environment-based system or an \land-chained system
// e.g. \begin{cases} x = 2 \end{cases}  or  x < 3 \land y > 1
system returns[res = rule_t(Ast.System)]: system_env {$res = $system_env.res} | system_and_chain {$res = $system_and_chain.res};

rel_op returns[op = rule_t(type)]: EQ {$op = Ast.Eq} | NEQ {$op = Ast.Neq} | LT {$op = Ast.Lt} | LTE {$op = Ast.Lte} | GT {$op = Ast.Gt} | GTE {$op = Ast.Gte};
// matches a binary relation with a relational operator, supporting chaining
// e.g. 2 < 3, x = y, a < b < c
relation returns[res = rule_t(Ast.Rel)]:
	a_expr rel_op relation {$res = $rel_op.op ($ctx, $a_expr.res, $relation.res)}
	| lhs=a_expr rel_op rhs=a_expr {$res = $rel_op.op ($ctx, $lhs.res, $rhs.res)};


// TODO: should probably begin implementing the visitor / transformer now that way tests can be set
// up and stuff like that, and also seems to not really have any reamining glaring problems which
// have not been covered.
a_expr
    returns[res = rule_t(Ast.AExpr)]
    locals[node_t = rule_t(type)]:
	// matches postfix operators: power/subscript/factorial/etc.
	// e.g. a^2, a_i, n!
	<assoc = right> base=a_expr postfix_op {$res = $postfix_op.op ($ctx, $base.res)}

	// \int \frac{\dd ...} {...} case
	| INT int_bounds ADJ_OP FRAC LBRACE DIFFERENTIAL diff=a_expr RBRACE ADJ_OP recip_integrand=latex_cmd_arg
		{$res = Ast.Integral($ctx, Ast.DivOp($recip_integrand.ctx, Ast.Number($recip_integrand.ctx, "1"), $recip_integrand.res), $diff.res, $int_bounds.bounds)}
	// \int ... \dd ... case
	| INT int_bounds ADJ_OP integrand=a_expr DIFFERENTIAL diff=a_expr
		{$res = Ast.Integral($ctx, $integrand.res, $diff.res, $int_bounds.bounds)}

	// \dv{...}{...} cases
	| PHYS_PARTIAL_DERIVATIVE ADJ_OP (LBRACKET a_expr RBRACKET ADJ_OP)?  latex_cmd_arg ADJ_OP LBRACE diff_l=a_expr RBRACE ADJ_OP LBRACE diff_r=a_expr RBRACE
		{$res = Ast.Differential($ctx, $latex_cmd_arg.res, [($diff_l.res, None), ($diff_r.res, None)])}
	| (PHYS_DERIVATIVE | PHYS_PARTIAL_DERIVATIVE) ADJ_OP (LBRACKET degree=a_expr RBRACKET ADJ_OP)? latex_cmd_arg ADJ_OP LBRACE a_expr RBRACE
		{$res = Ast.Differential($ctx, $latex_cmd_arg.res, [($a_expr.res, $degree.res)])}
	| (PHYS_DERIVATIVE | PHYS_PARTIAL_DERIVATIVE) ADJ_OP (LBRACKET degree=a_expr RBRACKET ADJ_OP)? latex_cmd_arg ADJ_OP diffand_last=a_expr
		{$res = Ast.Differential($ctx, $a_expr.res, [($latex_cmd_arg.res, $degree.res)])}

	// \frac{\dd ...}{\dd .. \dd ..} cases
	| FRAC ADJ_OP LBRACE DIFFERENTIAL (LBRACKET degree=a_expr RBRACKET ADJ_OP)? a_expr RBRACE ADJ_OP LBRACE diff_vars RBRACE
		{$res = Ast.Differential($ctx, $a_expr.res, $diff_vars.res)}
	| FRAC ADJ_OP LBRACE DIFFERENTIAL (LBRACKET degree=a_expr RBRACKET)? RBRACE ADJ_OP LBRACE diff_vars RBRACE ADJ_OP a_expr
		{$res = Ast.Differential($ctx, $a_expr.res, $diff_vars.res)}

	// matches expr(args) — ambiguous between function application and implicit multiplication
	// resolved at evaluation time: if expr is a known function, becomes ApplyFunc; otherwise, MultOp
	// e.g. f(x, y)  or  (1+1)(x)
	| lhs = a_expr ADJ_OP LPAREN func_args RPAREN
		{$res = Ast.AmbigApplyFunc($ctx, Ast.ApplyFunc($ctx, $lhs.res, $func_args.res))}
	// matches division operator
	// e.g. a / b
	| lhs = a_expr DIV rhs = a_expr {$res = Ast.DivOp($ctx, $lhs.res, $rhs.res)}
	// matches explicit multiplication, dot product, modulo, and cross product operators
	// e.g. a * b, a \cdot b, a \bmod b, a \times b
	| lhs = a_expr 
		(
		MULT {$node_t = Ast.MultOp}
		| ADJ_OP {$node_t = Ast.MultOp}
		| DOT_PROD {$node_t = Ast.MultOp}
		| MOD {$node_t = Ast.ModOp}
		| TIMES {$node_t = Ast.XProdOp}
		| XPROD {$node_t = Ast.XProdOp}
		) rhs = a_expr
		{$res = $node_t($ctx, $lhs.res, $rhs.res)}
	// matches implicit multiplication (juxtaposition without an explicit operator)
	// e.g. 2x, a b
	// TODO: should probably just split it up here..., so have one rule which matches things which can be implicitly multiplied,
	// and also things which cannot...
	// otherwise performance is completely broken
	// the only thing here is basically that rhs just must not be a unary plus or minus 

	// matches a limit expression
	// e.g. \lim_{x \to 0} x
	| LIMIT UNDERSCORE LBRACE lim_var=symbol LIMIT_ARROW lim_poa=a_expr limit_dir RBRACE ADJ_OP a_expr
		{$res = Ast.Limit($ctx, $a_expr.res, $lim_var.res, $lim_poa.res, $limit_dir.res)}
	// matches a sum (\sum) or product (\prod) with range arguments
	// e.g. \sum_{i=1}^n i^2
	| (SUM {$node_t = Ast.Sum} | PRODUCT {$node_t = Ast.Product}) series_range_args ADJ_OP LPAREN a_expr RPAREN
		{$res = $node_t($ctx, $a_expr.res, $series_range_args.symb, ($series_range_args.start, $series_range_args.end))}
	| (SUM {$node_t = Ast.Sum} | PRODUCT {$node_t = Ast.Product}) series_range_args ADJ_OP a_expr
		{$res = $node_t($ctx, $a_expr.res, $series_range_args.symb, ($series_range_args.start, $series_range_args.end))}

	// matches addition and subtraction operators
	// e.g. a + b, a - b
	| lhs = a_expr (PLUS {$node_t = Ast.AddOp} | MINUS {$node_t = Ast.SubOp}) rhs = a_expr
		{$res = $node_t($ctx, $lhs.res, $rhs.res)}
	// matches unary plus and minus
	// e.g. -a, +5
	| (PLUS {$node_t = Ast.UPlusOp} | MINUS {$node_t = Ast.UMinusOp}) a_expr
		{$res = $node_t($ctx, $a_expr.res)}
	// matches an "evaluate at" expression with variable substitution
	// e.g. \left. x^2 \right|_{x=1}
	| LPAREN expr=a_expr RPAREN ADJ_OP PIPE eval_at_arg
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

// matches postfix operators applied to an expression
// e.g. a^2, a_i, n!
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

// matches comma-separated function arguments
// e.g. x, y + 1
func_args returns[res = rule_t(list[Ast.AExpr], [])]: 
	a_expr {$res.append($a_expr.res)} (COMMA a_expr {$res.append($a_expr.res)})*;

// matches a range slice for matrix/array indexing (beg:end or beg...end)
// e.g. 1:10, :5, 3:
range_slot returns[res = rule_t(tuple[Ast.AExpr | None, Ast.AExpr | None])]:
    beg=a_expr? (delim=COLON|delim=DOTS) end=a_expr? {$res = ($beg.res, $end.res)};
// matches a wildcard slot (*) for selecting all elements in a dimension
all_slot: MULT | STAR;

// matches a single slot entry in a subscript: an index, a range, a wildcard, or empty
// e.g. 3, 1:10, *, (empty)
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
	
// matches a single differential variable with an optional degree
// e.g. \dd x^2, \dd y
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

// matches comma-separated variable substitutions (var = expr)
// e.g. x=1, y=2
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
    DELTA primary_symbol {$res = Ast.Symbol($ctx, f"{$DELTA.text} {$primary_symbol.res.name}")};


// matches any symbol: a plain identifier, a \command, or a \Delta-prefixed symbol
// e.g. x, \alpha, \Delta x
symbol returns[res = rule_t(Ast.AExpr)]:
    primary_symbol {$res = $primary_symbol.res}
    | delta_symbol {$res = $delta_symbol.res};

// matches operators which are notated via. surrounding an expression with delimiters.
// e.g. (..), |..|
delim_expr returns[res = rule_t(Ast.AExpr)]:
    LPAREN a_expr RPAREN {$res = Ast.Parens($ctx, $a_expr.res)}
    | LBRACKET a_expr RBRACKET {$res = Ast.Parens($ctx, $a_expr.res)}
    | PIPE a_expr PIPE {$res = Ast.Abs($ctx, $a_expr.res)}
    | DOUBLE_PIPE a_expr DOUBLE_PIPE {$res = Ast.Norm($ctx, $a_expr.res)}
    | LFLOOR a_expr RFLOOR {$res = Ast.Floor($ctx, $a_expr.res)}
    | LCEIL a_expr RCEIL {$res = Ast.Ceil($ctx, $a_expr.res)}
    | LANGLE lhs=a_expr (ADJ_OP PIPE|COMMA) rhs=a_expr RANGLE {$res = Ast.DotProd($ctx, $lhs.res, $rhs.res)};

// matches combinatorial notation: combinations ({_n C^k}) and derangements ({!n})
// e.g. {_n C^k}, {!n}
// TODO: permutations?
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
    FRAC ADJ_OP num = latex_cmd_arg ADJ_OP den = latex_cmd_arg {$res = Ast.DivOp($ctx, $num.res, $den.res)}
    | BINOM ADJ_OP n = latex_cmd_arg ADJ_OP k = latex_cmd_arg {$res = Ast.Binom($ctx, $n.res, $k.res)}
    | SQRT ADJ_OP (LBRACKET root_index = a_expr RBRACKET ADJ_OP)? latex_cmd_arg {$res = Ast.Root($ctx, $latex_cmd_arg.res, $root_index.res)
        }
    | CONJUGATE ADJ_OP latex_cmd_arg {$res = Ast.Conjugate($ctx, $latex_cmd_arg.res)}
    | VEC_UNIT ADJ_OP latex_cmd_arg {$res = Ast.VecUnit($ctx, $latex_cmd_arg.res)};


// matches a single row of a matrix (expressions separated by &)
// e.g. a & b & c
matrix_row
    returns[res = rule_t(list[Ast.AExpr])]:
    | a_expr {$res = [$a_expr.res]} (ENV_EL_SEP a_expr {$res.append($a_expr.res)})*;
// matches the full body of a matrix (rows separated by \\)
// e.g. a & b \\ c & d
matrix_body
    returns[res = rule_t(list[list[Ast.AExpr]], [])]:
    | matrix_row {$res = [$matrix_row.res]} (ENV_ROW_SEP matrix_row {$res.append($matrix_row.res)})* ENV_ROW_SEP*;

// matches a matrix, ==> expressions delimited by & and \\ in any matrix or array environment
matrix
    returns[res = rule_t(Ast.Matrix)]:
    (beg=BEGIN_MATRIX matrix_body end=END_MATRIX | beg=BEGIN_ARRAY matrix_body end=END_ARRAY) {$res = Ast.Matrix($ctx, $matrix_body.res, $beg.text, $end.text)};

// special case of matrix for the vmatrix environment
det_matrix returns[res = rule_t(Ast.AExpr)]: BEGIN_V_MATRIX matrix_body END_V_MATRIX {$res = Ast.DetMatrix($ctx, $matrix_body.res)};
