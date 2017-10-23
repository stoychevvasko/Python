"""Data Structures and Algorithms in Python - Goodrich, M. et al., page 52"""

# C-1.13 Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.

def reverse_list(original_list):
    """Reverses a list manually."""
    new_list = []
    i = 0
    while i < len(original_list):
        new_list.insert(0, original_list[i])
        i += 1
    return new_list

# C-1.14 Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.

def check_for_odd_product(sequence):
    """Checks a sequence of integers for a distinct pair with odd product."""
    for i in sequence:
        for j in sequence:
            if i is j:
                continue
            elif (i * j) & 1 == 1:
                return True
    return False
