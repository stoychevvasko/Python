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

def test_calculator__init__():
    """Tests the constructor."""
    calc = calculator.Calculator()
    assert calc is not None
    assert isinstance(calc, calculator.Calculator), 'invalid type exception was raised!'

def test_calculator_add():
    """Tests addition."""
    calc = calculator.Calculator()
    assert calc.add(2.5, 2.5) == 5
    assert calc.add(2.5, 2.5, 5) == 10

def test_calculator_subtract():
    """Tests subtraction."""
    calc = calculator.Calculator()
    assert calc.subtract(10, 5) == 5

def test_calculator_multiply():
    """Tests multiplication."""
    calc = calculator.Calculator()
    assert calc.multiply(3, 5) == 15
    assert calc.multiply(3, 5, 4) == 60

def test_calculator_divide():
    """Tests division."""
    calc = calculator.Calculator()
    assert calc.divide(50, 10) == 5
    assert calc.divide(18, -3) == -6
