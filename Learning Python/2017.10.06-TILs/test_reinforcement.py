"""Unit tests for reinforcement exercises."""

from reinforcement import multiple, is_even, minmax, sum_of_squares, sum_of_squares_short, \
sum_of_odd_squares

def test_multiple():
    """R-1.1."""
    assert multiple(9, 3) is True
    assert multiple(9, 4) is False

def test_is_even():
    """R-1.2."""
    assert is_even(5) is True
    assert is_even(-4) is False

def test_minmax():
    """R-1.3."""
    assert minmax(1, 2, 3) == (1, 3)
    assert minmax(5, -10, 20, 100, 3) == (-10, 100)

def test_sum_of_squares():
    """R-1.4."""
    assert sum_of_squares(3) == 5
    assert sum_of_squares(7) == 91

def test_sum_of_squares_short():
    """R-1.4."""
    assert sum_of_squares_short(3) == 5
    assert sum_of_squares_short(7) == 91

def test_sum_of_odd_squares():
    """R-1.5."""
    assert sum_of_odd_squares(3) == 1
    assert sum_of_odd_squares(7) == 35
    assert sum_of_odd_squares(10) == 165
