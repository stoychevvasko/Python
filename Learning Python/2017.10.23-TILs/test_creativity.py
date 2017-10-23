"""Unit tests for creativity exercises."""

from creativity import reverse_list, check_for_odd_product, check_for_distinct, \
    create_list_like_seq, produce_alphabet, my_shuffle

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

def test_distinct_in_sequence():
    """C-1.15."""
    true_list = [1, 2, 3, 4, 5]
    false_list = [1, 1, 2, 3, 4]
    assert check_for_distinct(true_list) is True
    assert check_for_distinct(false_list) is False

def test_create_list_like_seq():
    """C-1.18."""
    length = 10
    assert create_list_like_seq(length) == [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]

def test_produce_alphabet():
    """C-1.19."""
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', \
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    assert produce_alphabet() == alphabet

def test_my_shuffle():
    """C-1.20."""
    test_data = ['a', 'b', 'c', 'd', 'e']
    assert ['a', 'b', 'c', 'd', 'e'] != my_shuffle(test_data)
