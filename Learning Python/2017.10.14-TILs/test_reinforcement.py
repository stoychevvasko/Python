"""Unit tests for reinforcement exercises."""

from reinforcement import get_pos_index_from_neg_index, use_range_constructor, \
    descending_range, get_powers, my_choice

def test_negative_index():
    """R-1.8."""
    literal = '01234'
    neg = -2
    pos = get_pos_index_from_neg_index(literal, neg)
    assert literal[neg] == literal[pos]

def test_range():
    """R-1.9."""
    expected = (50, 60, 70, 80)
    actual = use_range_constructor()
    assert expected == actual

def test_desc_range():
    """R-1.10."""
    expected = (8, 6, 4, 2, 0, -2, -4, -6, -8)
    actual = descending_range()
    assert expected == actual

def test_comprehension_powers():
    """R-1.11."""
    expected = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    actual = get_powers()
    assert expected == actual

def test_my_choice():
    """R-1.12."""
    seq = [1, 2, 3, 4, 5]
    assert my_choice(seq) in seq
