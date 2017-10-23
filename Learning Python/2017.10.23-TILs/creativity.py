"""Data Structures and Algorithms in Python - Goodrich, M. et al., page 52"""

from random import randint

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

# C-1.15 Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).

def check_for_distinct(sequence):
    """Checks if a all numbers in a sequence are different (distinct)."""
    as_set = set(sequence)
    return len(as_set) == len(sequence)

# C-1.18 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

def create_list_like_seq(length):
    """Returns [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]."""
    result = []
    for i in range(length):
        result.append(i * (i + 1))
    return result

# C-1.19 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.

def produce_alphabet():
    """Create the list [a, b, c...]."""
    result = []
    for i in range(26):
        result.append(chr(ord('a') + i))
    return result

# C-1.20 Python’s random module includes a function shuffle(data) that accepts a
# list of elements and randomly reorders the elements so that each possible
# order occurs with equal probability. The random module includes a
# more basic function randint(a, b) that returns a uniformly random integer
# from a to b (including both endpoints). Using only the randint function,
# implement your own version of the shuffle function.

def my_shuffle(data):
    """Shuffles data sequence using the randint() method."""
    new_data = []
    for item in data:
        rand = randint(0, 1)
        if rand == 0:
            new_data.insert(0, item)
        else:
            new_data.append(item)
    return new_data
