"""Unit tests for creativity exercises."""

from creativity import reverse_list, check_for_odd_product

def test_reverse_list():
    """C-1.13."""
    test_list = [1, 2, 3, 4, 5]
    assert reverse_list(test_list) == [5, 4, 3, 2, 1]

def test_odd_product():
    """C-1.14."""
    true_list = [1, 2, 3, 4, 5]
    false_list = [2, 4, 6, 8, 10]
    assert check_for_odd_product(true_list) is True
    assert check_for_odd_product(false_list) is False
