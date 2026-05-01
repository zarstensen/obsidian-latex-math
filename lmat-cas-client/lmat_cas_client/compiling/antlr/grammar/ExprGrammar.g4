parser grammar ExprGrammar;
options {
    tokenVocab = ExprLexer;
    language = Python3;
}

@header {
import Ast
}

@members {
func_set: set[str] = set()
}

debug returns[res: Expr]: expr EOF {$res = $expr.res};

//TODO:
// - [ ] matrices / environments
// - [ ] derivatives (physics + frac)
// - [ ] integrals
// - [ ] optional latex arg (\\sqrt[...]{})
// - [ ] abs + norm + maybe other things i have missed?
// - [ ] combinatorics special notation {_n C ^k}
// - [ ] differential grammar, this maybe depends on optional latex arg?

// TODO: should probably begin implementing the visitor / transformer now that way tests can be set
// up and stuff like that, and also seems to not really have any reamining glaring problems which
// have not been covered.
expr
    returns[res: Expr]
    locals [node_t: type]:
    <assoc = right> base=expr POW exp=latex_cmd_arg {$res=Ast.ExpOp($ctx, $base.res, $exp.res)}                                                     # ExponentialOp
    | op=expr (BANG {$node_t = Ast.Factorial} | PERCENT {$node_t = Ast.Percent} | PERMILLE {$node_t = Ast.Permille}) {$res = $node_t($ctx, $op.res)} # Prefix
    | FUNCTION LPAREN (expr (COMMA expr)*)? RPAREN                                                                                                  # Function
    | FUNCTION LBRACE expr RBRACE                                                                                                                   # Function // Only allow these alternatives if function
    | FUNCTION expr                                                                                                                                 # Function // was from a command? this *could* be stored in the AST
    // TODO: limit should live here?
    | LIMIT UNDERSCORE LBRACE SYMBOL LIMIT_ARROW expr (POW limit_dir)? RBRACE expr                                                                  # Limit
    | lhs = expr (MULT {$node_t = Ast.MultOp} | DIV {$node_t = Ast.DivOp}) rhs = expr {$res = $node_t($ctx, $lhs.res, $rhs.res)}                    # MultiplicativeOp
    // dissallow if rhs is number (maybe should be toh number?) or if the following token is a PLUS / MINUS (i.e. a -b does should never be seen as a * (-b)).
    | lhs = expr {self._input.LA(1) not in (self.PLUS, self.MINUS, self.NUMBER)}? rhs = expr {$res = Ast.MultOp($ctx, $lhs.res, $rhs.res)}          # MultiplicativeOp 
    | (SUM | PRODUCT) series_range_args LPAREN expr RPAREN                                                                                          # Series
    | (SUM | PRODUCT) series_range_args expr                                                                                                        # Series
    | lhs = expr (PLUS {$node_t = Ast.AddOp}| MINUS {$node_t = Ast.SubOp}) rhs = expr {$res = $node_t($ctx, $lhs.res, $rhs.res)}                    # AdditiveOp
    | (PLUS {$node_t = Ast.UPlusOp}| MINUS {$node_t = Ast.UMinusOp}) expr {$res = $node_t($ctx, $expr.res)}                                         # UAdditiveOp
    | INT expr DIFFERENTIAL                                                                                                                         # Int
    | LPAREN expr RPAREN {$res = $expr.res}                                                                                                         # Stub
    | atom {$res = $atom.res }                                                                                                                      # Stub;

atom
    returns[res: Expr]:
	// TODO: if symbol is in func_set, return function instead.
    SYMBOL {$res = Ast.Symbol($ctx, $SYMBOL.text)}
    | COMMAND {$res = Ast.Symbol($ctx, $COMMAND.text)}
    | NUMBER {$res = Ast.Number($ctx, $NUMBER.text)};

// argument to a latex command, so can either be an atom (singular digit, letter or command, this is handled by the lexer), or a brace surrounded expression.
latex_cmd_arg returns[res: Expr]: atom {$res = $atom.res }| LBRACE expr RBRACE {$res = $expr.res};

limit_dir: LBRACE (PLUS|MINUS) RBRACE | PLUS | MINUS;

// NOTE: function cannot be used as symbol? this is probably fine
series_range_args returns [symb: Ast.Symbol, start: Ast.Expr, end: Ast.Expr]:
    UNDERSCORE LBRACE SYMBOL EQUAL expr RBRACE POW latex_cmd_arg
{
$symb = Ast.Symbol($ctx, $SYMBOL.text)
$start = $expr.res
$end = $latex_cmd_arg.res
}
    | POW latex_cmd_arg UNDERSCORE LBRACE SYMBOL EQUAL expr RBRACE
{
$symb = Ast.Symbol($ctx, $SYMBOL.text)
$start = $expr.res
$end = $latex_cmd_arg.res
};

hard_func returns[res: Ast.HardFunc]:
    FRAC latex_cmd_arg latex_cmd_arg
    | BINOM latex_cmd_arg latex_cmd_arg
    | SQRT latex_cmd_arg
    | CONJUGATE latex_cmd_arg
    | VEC_UNIT latex_cmd_arg;


