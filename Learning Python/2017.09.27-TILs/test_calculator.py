"""Unit tests using the pytest library."""
# '$ pip install pytest'
#make sure to name the file test_module_name.py so test discovery will work
#run unit tests in console
# '$ python -m pytest'
#  ^this one discovers all test_'s recursively by the file name prefix
# '$ python -m pytest -v --color=yes'
#  ^verbose parameter used here, also forces color
# '$ py.test -v --color=yes'
#  ^another way

import calculator
#each file is a module by default in Python

import pytest

@pytest.fixture
def calc():
    """Generates a calculator instance."""
    return calculator.Calculator()

# pylint:disable=redefined-outer-name
def test_calculator__init__(calc):
    """Tests the constructor."""
    assert calc is not None
    assert isinstance(calc, calculator.Calculator), 'invalid type exception was raised!'

# pylint:disable=redefined-outer-name
def test_calculator_add(calc):
    """Tests addition."""
    assert calc.add(2.5, 2.5) == 5
    assert calc.add(2.5, 2.5, 5) == 10

# pylint:disable=redefined-outer-name
def test_calculator_subtract(calc):
    """Tests subtraction."""
    assert calc.subtract(10, 5) == 5

# pylint:disable=redefined-outer-name
def test_calculator_multiply(calc):
    """Tests multiplication."""
    assert calc.multiply(3, 5) == 15
    assert calc.multiply(3, 5, 4) == 60

# pylint:disable=redefined-outer-name
def test_calculator_divide(calc):
    """Tests division."""
    assert calc.divide(50, 10) == 5
    assert calc.divide(18, -3) == -6
