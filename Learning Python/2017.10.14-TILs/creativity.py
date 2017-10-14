"""Data Structures and Algorithms in Python - Goodrich, M. et al., page 52"""

# C-1.13 Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.

def my_reverse(original):
    """Reverses the order of a list of items."""
    return original[::-1]

# C-1.14 Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.

def check_for_pair_of_odd_product(integers):
    """Checks for existing pair where product is odd."""
    for outer in integers:
        for inner in integers:
            if outer is inner:
                continue
            elif (outer * inner) & 1 == 1:
                # print('C-1.14. (exercise)', outer, '*', inner, '=', outer * inner)
                return True
    return False

# C-1.15 Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).

def check_if_all_distinct(values):
    """Checks if all values are different from each other."""
    return len(values) == len(set(values))
