"""Data Structures and Algorithms in Python - Goodrich, M. et al., page 53"""

# C-1.26 Write a short program that takes as input three integers, a, b, and c, from
# the console and determines if they can be used in a correct arithmetic
# formula (in the given order), like “a+b = c,” “a = b−c,” or “a * b = c.”

def three_integers():
    """Check if integers meet conditions."""
    num_a = int(input('a = '))
    num_b = int(input('b = '))
    num_c = int(input('c = '))
    cond_1 = (num_a + num_b == num_c)
    print('a+b=c', cond_1)
    cond_2 = (num_a == num_b - num_c)
    print('a=b-c', cond_2)
    cond_3 = (num_a * num_b == num_c)
    print('a*b=c', cond_3)
    print('end result: ', cond_1 & cond_2 & cond_3)

three_integers()
