# pyright: reportOperatorIssue=false, reportArgumentType=false
from typing import cast

import sympy as sp
from lmat_cas_client.math_lib import MatrixUtils

from .. import Ast

LocRange = tuple[int, int]

ExprEntry = tuple[sp.Basic, LocRange]

CasExprV2 = tuple[ExprEntry, ...]

def evalExprToSympy(expr: Ast.AExpr, scope: None) -> ExprEntry:
    def ev(expr: Ast.AExpr, scope: None):
        match expr:
            case Ast.Symbol(_, s):
                return sp.Symbol(s)
            case Ast.Number(_, n_str):
                if "." in n_str:
                    return sp.Float(n_str)
                else:
                    return sp.Integer(n_str)
            case Ast.ExpOp(_, base, exp):
                return ev(base, scope) ** ev(exp, scope)
            case Ast.YEE(_, lhs, rhs):
                return ev(lhs, scope) * ev(rhs, scope)
            case Ast.DivOp(_, lhs, rhs):
                return ev(lhs, scope) / ev(rhs, scope)
            case Ast.AddOp(_, lhs, rhs):
                return ev(lhs, scope) + ev(rhs, scope)
            case Ast.SubOp(_, lhs, rhs):
                return ev(lhs, scope) - ev(rhs, scope)
            case Ast.UPlusOp(_, op):
                return +ev(op, scope)
            case Ast.UMinusOp(_, op):
                return -ev(op, scope)
            # case Ast.AppliedBuiltinFunc(_, f):
            #     pass
                # return evalAppliedBuiltingFuncToSympy(f, scope)

    match expr:
        case Ast.AstNode(ctx):
            start_token = ctx.start
            end_token = ctx.stop

            assert start_token is not None and end_token is not None

            return (ev(expr, scope)[0], (start_token.start, end_token.stop))

    # TODO: what to do here...
    assert False

