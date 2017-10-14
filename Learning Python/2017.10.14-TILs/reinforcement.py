"""Data Structures and Algorithms in Python - Goodrich, M. et al., page 51"""

from random import randrange

# R-1.8 Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for index
# −n≤k<0, what is the equivalent index j ≥0 such that s[j] references
# the same element?

def get_pos_index_from_neg_index(str_value, neg_index):
    """Returns the positive integer equivalent of a given negative index."""
    return len(str_value) + neg_index

# R-1.9 What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?

def use_range_constructor():
    """Returns (50, 60, 70, 80)."""
    return tuple(range(50, 81, 10))

# R-1.10 What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

def descending_range():
    """Returns (8, 6, 4, 2, 0, −2, −4, −6, −8)."""
    return tuple(range(8, -9, -2))

# R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

def get_powers():
    """Returns [1, 2, 4, 8, 16, 32, 64, 128, 256]."""
    return list(2 ** val for val in range(9))

# R-1.12 Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module includes
# a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function.

def my_choice(sequence):
    """Implement your own choice() function to return random element from sequence."""
    return sequence[randrange(len(sequence) - 1)]
