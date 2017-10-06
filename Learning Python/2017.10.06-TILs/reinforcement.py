"""Data Structures and Algorithms in Python - Goodritch, M. et al., page 51"""

# R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.

def multiple(number_n, number_m):
    """Returns boolean evaluation if n is multiple of m."""
    return number_n % number_m == 0

# R-1.2 Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

def is_even(number_k):
    """Returns boolean evaluation if k is even."""
    return number_k & 1 == 1

# R-1.3 Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

def minmax(*data):
    """Returns tuple (min, max) from sequence of numbers."""
    min_num, max_num = data[0], data[0]
    for num in data:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return (min_num, max_num)

# R-1.4 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def sum_of_squares(num):
    """Returns sum of squares of all positive integers smaller than n."""
    acc = 0
    for val in range(num):
        acc += val ** 2
    return acc

# R-1.5 Give a single command that computes the sum from Exercise R-1.4, relying
# on Python’s comprehension syntax and the built-in sum function.

def sum_of_squares_short(num):
    """Returns sum of squares of all positive integers smaller than n."""
    return sum(val * val for val in range(0, num))

# R-1.6 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def sum_of_odd_squares(num):
    """Returns sum of squares of all odd positive integers smaller than n."""
    return sum(val ** 2 for val in range(1, num, 2))
