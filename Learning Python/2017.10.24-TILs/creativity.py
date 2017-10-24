"""Data Structures and Algorithms in Python - Goodrich, M. et al., page 53"""

# C-1.23 Give an example of a Python code fragment that attempts to write an element
# to a list based on an index that may be out of bounds. If that index
# is out of bounds, the program should catch the exception that results, and
# print the following error message:
# “Don’t try buffer overflow attacks in Python!”

def list_out_of_bounds(a_list, element, index):
    """Attempts to write element at index position within the list."""
    try:
        a_list[index] = element
    except:
        raise Exception('Don’t try buffer overflow attacks in Python!')

# C-1.24 Write a short Python function that counts the number of vowels in a given
# character string.

def count_vowels(string):
    """Counts the number of vowels in a string."""
    # vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y']
    vowels = 'aeiouy'
    counter = 0
    for character in string:
        if character.lower() in vowels:
            counter += 1
    return counter

# C-1.25 Write a short Python function that takes a string s, representing a sentence,
# and returns a copy of the string with all punctuation removed. For example,
# if given the string "Let s try, Mike.", this function would return
# "Lets try Mike".

def remove_punctuation(sentence):
    """Removes all punctuation from a sentence string."""
    result = ''
    punctuation = ["'", '"', ':', ';', '.', ',', '!', '?', '-']
    for letter in sentence:
        if letter not in punctuation:
            result += letter
    return result

# C-1.27 In Section 1.8, we provided three different implementations of a generator
# that computes factors of a given integer. The third of those implementations,
# from page 41, was the most efficient, but we noted that it did not
# yield the factors in increasing order. Modify the generator so that it reports
# factors in increasing order, while maintaining its general performance advantages.

def factors(num):
    """Generator that computes factors."""
#     k = 1
#     while k * k < num: # while k < sqrt(n)
#         if num % k == 0:
#             yield k
#             yield num // k
#         k += 1
#     if k * k == num:
#         yield k
    for k in range(1, num + 1):
        if num % k == 0:
            yield k
