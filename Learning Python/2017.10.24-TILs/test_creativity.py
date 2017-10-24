"""Unit tests for creativity exercises."""

from creativity import list_out_of_bounds, count_vowels, remove_punctuation, \
    factors
import pytest

def test_list_out_of_bounds():
    """C-1.23."""
    test_list = [0, 1, 2, 3, 4]
    test_index = 10
    test_element = 'foo'

    with pytest.raises(Exception) as e_info:
        list_out_of_bounds(test_list, test_element, test_index)
        assert e_info == 'Don’t try buffer overflow attacks in Python!'

def test_count_vowels():
    """C-1.24."""
    test_word = 'foobar'
    assert count_vowels(test_word) == 3

def test_remove_punctuation():
    """C-1.25."""
    test_sentence = "Let's try, Mike."
    expected = "Lets try Mike"
    assert remove_punctuation(test_sentence) == expected

def test_factors():
    """C-1.27."""
    test_value = 100
    expected = [1, 2, 4, 5, 10, 20, 25, 50, 100]
    actual = list(factors(test_value))
    # actual.sort()
    assert actual == expected
