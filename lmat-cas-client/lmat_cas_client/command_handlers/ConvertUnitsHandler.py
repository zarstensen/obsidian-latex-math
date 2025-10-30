from sympy import *
from sympy.physics.units import convert_to

import lmat_cas_client.math_lib.UnitsUtils as UnitsUtils

from .EvalHandlerBase import EvalHandlerBase, EvaluateMessage, EvaluateResult


class ConvertMessage(EvaluateMessage):
    target_units: list[str]


# Tries to convert the sympy expressions units to the provided units in message.target_units.
class ConvertUnitsHandler(EvalHandlerBase):
    def handle(self, message: ConvertMessage) -> EvaluateResult:
        message = ConvertMessage.model_validate(message)
        message.environment.unit_system = "SI"
        return super().handle(message)

    def evaluate(self, sympy_expr: Expr, message: ConvertMessage):
        target_units = []

        for target_unit_str in message.target_units:
            target_unit = UnitsUtils.str_to_unit(target_unit_str)

            if target_unit is not None:
                target_units.append(target_unit)

        sympy_expr = convert_to(sympy_expr, target_units)

        return sympy_expr
