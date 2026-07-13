parser grammar DefExprGrammar;
options {
	tokenVocab = DefExprLexer;
	language = Python3;
}

import AlgExprGrammar;

@header {
from lmat_cas_client.compiling.antlr.ast import DefStmtAst as DefAst
}

debug returns[res = rule_t(DefAst.BindingStmts)]: bindings EOF {$res = $bindings.res};

bindings returns[res = rule_t(DefAst.BindingStmts)]: 
	binding {$res = ($binding.res,) } ((DEF_SEP | SET_DEF_SEP) binding {$res = (*$res, $binding.res)})*;

binding returns[res = rule_t(DefAst.BindingStmt)]: 
	definition 
		{$res = $definition.res}
	| symbol_assumption 
		{$res = $symbol_assumption.res}
	| function_assumption
		{$res = $function_assumption.res}
	;

definition returns[res = rule_t(DefAst.Definition)]: 
	symbol DEF_OP def_body
		{$res = DefAst.Definition($ctx, $symbol.res, None, None, $def_body.res) }
	| symbol UNDERSCORE subscript_arg DEF_OP def_body
		{$res = DefAst.Definition($ctx, $symbol.res, $subscript_arg.res, None, $def_body.res) }
	| symbol LPAREN func_args RPAREN DEF_OP def_body
		{$res = DefAst.Definition($ctx, $symbol.res, None, $func_args.res, $def_body.res) }
	| symbol UNDERSCORE subscript_arg LPAREN func_args RPAREN DEF_OP def_body
		{$res = DefAst.Definition($ctx, $symbol.res, $subscript_arg.res, $func_args.res, $def_body.res) }
	;

def_body returns[res = rule_t(Ast.AExpr | None)]:
	a_expr {$res = $a_expr.res}
	| {$res = None}
	;

symbol_assumption returns[res = rule_t(DefAst.Assumption)]:
	symbol VAR_ASSUME_OP assum_body
		{$res = DefAst.Assumption($ctx, $symbol.res, None, None, $assum_body.res)}
	| symbol UNDERSCORE subscript_arg VAR_ASSUME_OP assum_body
		{$res = DefAst.Assumption($ctx, $symbol.res, $subscript_arg.res, None, $assum_body.res)}
	;


function_assumption returns[res = rule_t(DefAst.Assumption)]:
	symbol LPAREN func_args RPAREN FUN_ASSUME_OP assum_body
		{$res = DefAst.Assumption($ctx, $symbol.res, None, $func_args.res, $assum_body.res)}
	| symbol UNDERSCORE subscript_arg LPAREN func_args RPAREN FUN_ASSUME_OP assum_body
		{$res = DefAst.Assumption($ctx, $symbol.res, $subscript_arg.res, $func_args.res, $assum_body.res)}
	;

assum_body returns[res = rule_t(DefAst.Set | None)]:
	set {$res = $set.res}
	| {$res = None}
	;

set returns[res = rule_t(DefAst.Set)]:
	signed_set {$res = $signed_set.res }
	| unsigned_set {$res = $unsigned_set.res }
	| algebraic_set {$res = $algebraic_set.res } 
	| positive_set {$res = $positive_set.res } 
	| nonnegative_set {$res = $nonnegative_set.res } 
	| negative_set {$res = $negative_set.res } 
	| nonpositive_set {$res = $nonpositive_set.res } 
	| natural0_set {$res = $natural0_set.res }
	;

set_complex returns[res = rule_t(DefAst.SetType)]: 
	(SET_COMPLEX | SET_FORMATTER SET_LBRACE SET_COMPLEX SET_RBRACE)
	{$res = DefAst.SetType.COMPLEX};
set_real returns[res = rule_t(DefAst.SetType)]: 
	(SET_REAL | SET_FORMATTER SET_LBRACE SET_REAL SET_RBRACE)
	{$res = DefAst.SetType.REAL};
set_imaginary returns[res = rule_t(DefAst.SetType)]: 
	(SET_IMAGINARY | SET_FORMATTER SET_LBRACE SET_IMAGINARY SET_RBRACE)
	{$res = DefAst.SetType.IMAGINARY};
set_rational returns[res = rule_t(DefAst.SetType)]: 
	(SET_RATIONAL | SET_FORMATTER SET_LBRACE SET_RATIONAL SET_RBRACE)
	{$res = DefAst.SetType.RATIONAL};
set_integer returns[res = rule_t(DefAst.SetType)]: 
	(SET_INTEGER | SET_FORMATTER SET_LBRACE SET_INTEGER SET_RBRACE)
	{$res = DefAst.SetType.INTEGER};
set_natural returns[res = rule_t(DefAst.SetType)]: 
	(SET_NATURAL | SET_FORMATTER SET_LBRACE SET_NATURAL SET_RBRACE)
	{$res = DefAst.SetType.NATURAL};
set_even returns[res = rule_t(DefAst.SetType)]: 
	(SET_EVEN | SET_FORMATTER SET_LBRACE SET_EVEN SET_RBRACE)
	{$res = DefAst.SetType.EVEN};
set_odd returns[res = rule_t(DefAst.SetType)]: 
	(SET_ODD | SET_FORMATTER SET_LBRACE SET_ODD SET_RBRACE)
	{$res = DefAst.SetType.ODD};
set_prime returns[res = rule_t(DefAst.SetType)]: 
	(SET_PRIME | SET_FORMATTER SET_LBRACE SET_PRIME SET_RBRACE)
	{$res = DefAst.SetType.PRIME};

algebraic_set returns[res = rule_t(DefAst.SetType)]:
	SET_OVERLINE SET_LBRACE set_rational SET_RBRACE
	{$res = DefAst.SetType.ALGEBRAIC};
ext_real_set returns[res = rule_t(DefAst.SetType)]: 
	SET_OVERLINE SET_LBRACE set_real SET_RBRACE
	{$res = DefAst.SetType.EXT_REAL};

unsigned_set
	returns[res = rule_t(DefAst.Set)]
	locals[set_type = rule_t(DefAst.SetType)]: 
	(set_complex {$set_type = $set_complex.res}
	| set_imaginary{$set_type = $set_imaginary.res}) 
		{$res = DefAst.Set($ctx, $set_type, DefAst.SetBound.NONE) }
	;

signed_set 
	returns[res = rule_t(DefAst.Set)]
	locals[set_type = rule_t(DefAst.SetType)]:
	(set_real {$set_type = $set_real.res }
	| ext_real_set {$set_type = $ext_real_set.res }
	| set_rational {$set_type = $set_rational.res }
	| set_integer {$set_type = $set_integer.res }
	| set_even {$set_type = $set_even.res }
	| set_odd {$set_type = $set_odd.res }
	| set_prime {$set_type = $set_prime.res })
		{$res = DefAst.Set($ctx, $set_type, DefAst.SetBound.NONE)}
	;

positive_set returns[res = rule_t(DefAst.Set)]: 
	signed_set SET_UNDERSCORE (SET_ADD | SET_LBRACE (SET_ADD | SET_GT SET_ZERO) SET_RBRACE)
		{$res = DefAst.Set($ctx, $signed_set.res.set_type, DefAst.SetBound.POSITIVE)};
nonnegative_set returns[res = rule_t(DefAst.Set)]:
	signed_set SET_UNDERSCORE SET_LBRACE SET_GTE SET_ZERO SET_RBRACE
		{$res = DefAst.Set($ctx, $signed_set.res.set_type, DefAst.SetBound.NONNEGATIVE)};
negative_set returns[res = rule_t(DefAst.Set)]:
	signed_set SET_UNDERSCORE (SET_ADD | SET_LBRACE (SET_SUB | SET_LT SET_ZERO) SET_RBRACE)
		{$res = DefAst.Set($ctx, $signed_set.res.set_type, DefAst.SetBound.NEGATIVE)};
nonpositive_set returns[res = rule_t(DefAst.Set)]:
	signed_set SET_UNDERSCORE SET_LBRACE SET_LTE SET_ZERO SET_RBRACE
		{$res = DefAst.Set($ctx, $signed_set.res.set_type, DefAst.SetBound.NONPOSITIVE)};
natural0_set returns[res = rule_t(DefAst.Set)]: 
	set_natural SET_UNDERSCORE (SET_ZERO | SET_LBRACE SET_ZERO SET_RBRACE)
		{$res = DefAst.Set($ctx, $set_natural.res.set_type, DefAst.SetBound.NONZERO)};
