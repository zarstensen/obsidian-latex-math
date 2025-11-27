import pytest
from lmat_cas_client.math_lib.setup import setup_mathlib


@pytest.fixture(scope="session", autouse=True)
def mathlib_setup():
    setup_mathlib()
