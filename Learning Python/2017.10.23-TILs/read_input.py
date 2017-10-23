"""Data Structures and Algorithms in Python - Goodrich, M. et al., page 52"""
# C-1.21 Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D).

def read_input():
    """Reads lines from input until EOFError is raised."""
    output_lines = []
    line_num = 0
    while True:
        try:
            line_num += 1
            item = input(str(line_num) + ': ')
            if item == '':
                raise EOFError
            output_lines.insert(0, item)
            print('>>', output_lines[0])
        except EOFError:
            print(output_lines)
            break

read_input()
