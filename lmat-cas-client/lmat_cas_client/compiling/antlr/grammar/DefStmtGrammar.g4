parser grammar DefStmtGrammar;

options {
	tokenVocab = DefStmtLexer;
	language = Python3;
}

import AlgStmtGrammar;

@header {
from lmat_cas_client.compiling.antlr.ast import DefStmtAst as DefAst
}

debug returns[res = rule_t(DefAst.BindingStmts)]: bindings {$res = $bindings.res};

bindings returns[res = rule_t(DefAst.BindingStmts)]: 
	binding {$res = (*$binding.res,) } ((DEF_SEP | SET_DEF_SEP) binding {$res = (*$res, *$binding.res)})* EOF;

binding returns[res = rule_t(tuple[DefAst.BindingStmt])]: 
	definition 
		{$res = ($definition.res,)}
	| symbol_assumptions
		{$res = $symbol_assumptions.res}
	| function_assumption
		{$res = ($function_assumption.res,)}
	;

symbol_signature returns[res = rule_t(DefAst.SignatureStmt)]:
	symbol {$res = DefAst.SignatureStmt($ctx, $symbol.res, None, None)}
	| symbol UNDERSCORE subscript_arg {$res = DefAst.SignatureStmt($ctx, $symbol.res, $subscript_arg.res, None)}
	;

function_signature returns[res = rule_t(DefAst.SignatureStmt)]:
	symbol_signature LPAREN func_args RPAREN {$res = DefAst.SignatureStmt($ctx, $symbol_signature.res.head, $symbol_signature.res.subscript, $func_args.res)}
	;

signature returns[res = rule_t(DefAst.SignatureStmt)]:
	symbol_signature {$res = $symbol_signature.res}
	| function_signature {$res = $function_signature.res}
	;

definition returns[res = rule_t(DefAst.Definition)]: 
	signature DEF_OP def_body
		{$res = DefAst.Definition($ctx, $signature.res, $def_body.res) }
	;

def_body returns[res = rule_t(Ast.AExpr | None)]:
	a_expr {$res = $a_expr.res}
	| {$res = None}
	;

symbol_assumptions
	returns[res = rule_t(tuple[DefAst.Assumption])]
	locals[sigs = rule_t(list[DefAst.SignatureStmt])]:
	symbol_signature {$sigs = [$symbol_signature.res]} (COMMA symbol_signature {$sigs.append($symbol_signature.res)})* VAR_ASSUME_OP assum_body
		{$res = tuple(DefAst.Assumption($ctx, sig, $assum_body.res) for sig in $sigs)}
	;


function_assumption returns[res = rule_t(DefAst.Assumption)]:
	function_signature FUN_ASSUME_OP assum_body
		{$res = DefAst.Assumption($ctx, $function_signature.res, $assum_body.res)}
	;

assum_body returns[res = rule_t(DefAst.Set | None)]:
	set {$res = $set.res}
	| {$res = None}
	;

set returns[res = rule_t(DefAst.Set)]:
	ordered_set {$res = $ordered_set.res }
	| unordered_set {$res = $unordered_set.res }
	| algebraic_set {$res = $algebraic_set.res } 
	| positive_set {$res = $positive_set.res } 
	| nonnegative_set {$res = $nonnegative_set.res } 
	| negative_set {$res = $negative_set.res } 
	| nonpositive_set {$res = $nonpositive_set.res } 
	| nonzero_natural_set {$res = $nonzero_natural_set.res }
	;

complex_set returns[res = rule_t(DefAst.SetType)]: 
	(SET_COMPLEX | SET_FORMATTER SET_LBRACE SET_COMPLEX SET_RBRACE)
	{$res = DefAst.SetType.COMPLEX};
real_set returns[res = rule_t(DefAst.SetType)]: 
	(SET_REAL | SET_FORMATTER SET_LBRACE SET_REAL SET_RBRACE)
	{$res = DefAst.SetType.REAL};
imaginary_set returns[res = rule_t(DefAst.SetType)]: 
	(SET_IMAGINARY | SET_FORMATTER SET_LBRACE SET_IMAGINARY SET_RBRACE)
	{$res = DefAst.SetType.IMAGINARY};
rational_set returns[res = rule_t(DefAst.SetType)]: 
	(SET_RATIONAL | SET_FORMATTER SET_LBRACE SET_RATIONAL SET_RBRACE)
	{$res = DefAst.SetType.RATIONAL};
integer_set returns[res = rule_t(DefAst.SetType)]: 
	(SET_INTEGER | SET_FORMATTER SET_LBRACE SET_INTEGER SET_RBRACE)
	{$res = DefAst.SetType.INTEGER};
natural_set returns[res = rule_t(DefAst.SetType)]: 
	(SET_NATURAL | SET_FORMATTER SET_LBRACE SET_NATURAL SET_RBRACE)
	{$res = DefAst.SetType.NATURAL};
even_set returns[res = rule_t(DefAst.SetType)]: 
	(SET_EVEN | SET_FORMATTER SET_LBRACE SET_EVEN SET_RBRACE)
	{$res = DefAst.SetType.EVEN};
odd_set returns[res = rule_t(DefAst.SetType)]: 
	(SET_ODD | SET_FORMATTER SET_LBRACE SET_ODD SET_RBRACE)
	{$res = DefAst.SetType.ODD};
prime_set returns[res = rule_t(DefAst.SetType)]: 
	(SET_PRIME | SET_FORMATTER SET_LBRACE SET_PRIME SET_RBRACE)
	{$res = DefAst.SetType.PRIME};

algebraic_set returns[res = rule_t(DefAst.SetType)]:
	SET_OVERLINE SET_LBRACE rational_set SET_RBRACE
	{$res = DefAst.SetType.ALGEBRAIC};
ext_real_set returns[res = rule_t(DefAst.SetType)]: 
	SET_OVERLINE SET_LBRACE real_set SET_RBRACE
	{$res = DefAst.SetType.EXT_REAL};

unordered_set
	returns[res = rule_t(DefAst.Set)]
	locals[set_type = rule_t(DefAst.SetType)]: 
	(complex_set {$set_type = $complex_set.res}
	| imaginary_set{$set_type = $imaginary_set.res}) 
		{$res = DefAst.Set($ctx, $set_type, DefAst.SetBound.NONE) }
	;

ordered_set 
	returns[res = rule_t(DefAst.Set)]
	locals[set_type = rule_t(DefAst.SetType)]:
	(real_set {$set_type = $real_set.res }
	| ext_real_set {$set_type = $ext_real_set.res }
	| rational_set {$set_type = $rational_set.res }
	| integer_set {$set_type = $integer_set.res }
	| even_set {$set_type = $even_set.res }
	| odd_set {$set_type = $odd_set.res }
	| prime_set {$set_type = $prime_set.res })
		{$res = DefAst.Set($ctx, $set_type, DefAst.SetBound.NONE)}
	;

// additional bounds one can apply to ordered sets.
positive_set returns[res = rule_t(DefAst.Set)]: 
	ordered_set SET_UNDERSCORE (SET_ADD | SET_LBRACE (SET_ADD | SET_GT SET_ZERO) SET_RBRACE)
		{$res = DefAst.Set($ctx, $ordered_set.res.set_type, DefAst.SetBound.POSITIVE)};
nonnegative_set returns[res = rule_t(DefAst.Set)]:
	ordered_set SET_UNDERSCORE SET_LBRACE SET_GTE SET_ZERO SET_RBRACE
		{$res = DefAst.Set($ctx, $ordered_set.res.set_type, DefAst.SetBound.NONNEGATIVE)};
negative_set returns[res = rule_t(DefAst.Set)]:
	ordered_set SET_UNDERSCORE (SET_ADD | SET_LBRACE (SET_SUB | SET_LT SET_ZERO) SET_RBRACE)
		{$res = DefAst.Set($ctx, $ordered_set.res.set_type, DefAst.SetBound.NEGATIVE)};
nonpositive_set returns[res = rule_t(DefAst.Set)]:
	ordered_set SET_UNDERSCORE SET_LBRACE SET_LTE SET_ZERO SET_RBRACE
		{$res = DefAst.Set($ctx, $ordered_set.res.set_type, DefAst.SetBound.NONPOSITIVE)};
nonzero_natural_set returns[res = rule_t(DefAst.Set)]: 
	natural_set SET_UNDERSCORE (SET_ZERO | SET_LBRACE SET_ZERO SET_RBRACE)
		{$res = DefAst.Set($ctx, $natural_set.res.set_type, DefAst.SetBound.NONZERO)};
