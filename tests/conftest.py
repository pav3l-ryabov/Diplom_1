import pytest

from data.test_data import BUN_VALID_NAME, BUN_VALID_FLOAT_PRICE
from praktikum.bun import Bun

@pytest.fixture
def bun():
    return Bun(BUN_VALID_NAME, BUN_VALID_FLOAT_PRICE)