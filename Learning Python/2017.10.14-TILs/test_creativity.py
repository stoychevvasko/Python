"""Unit tests for creativity exercises."""

from creativity import my_reverse, check_for_pair_of_odd_product, \
    check_if_all_distinct

def test_my_reversed():
    """C-1.13."""
    my_list = [0, 1, 2, 3, 4, 5, 6, 7]
    my_list.reverse()
    standard_rev = my_list

    second_list = [0, 1, 2, 3, 4, 5, 6, 7]
    my_rev = my_reverse(second_list)

    assert standard_rev == my_rev
    assert standard_rev is not my_rev

def test_for_pair_odd_product():
    """C-1.14."""
    has = (1, 2, 3)
    has_not = (2, 4, 6)

    assert check_for_pair_of_odd_product(has) is True
    assert check_for_pair_of_odd_product(has_not) is False

def test_for_distinct():
    """C-1.15."""
    distinct = ('a', 'b', 'c', 1, 1000, -666)
    non_distinct = ('a', 1, 'a', 2, 3, 1)

    assert check_if_all_distinct(distinct) is True
    assert check_if_all_distinct(non_distinct) is False
