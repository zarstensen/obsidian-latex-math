from sympy.core.parameters import global_parameters as sympy_gp


#
def setup_mathlib():
    """
    Configure sympy to work as expected with this mathlib and the various sympy parsers + transformers.
    This has to run before any kind of work with the mathlib, and thus also parsers + transformers happen.
    """
    # configure exp(x) and e^x to be interpreted as e^x (opposite behaviour is default).
    # This solve some issues with units not working in the exponent of e.
    sympy_gp.exp_is_pow = True
