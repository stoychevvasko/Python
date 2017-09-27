"""Example class for simple calculations."""

class Calculator():
    """Models a simple calculator."""

    def __init__(self):
        assert self is not False

    @classmethod
    def add(cls, *args):
        """Addition."""
        accumulator = 0
        for arg in args:
            accumulator += arg
        return accumulator

    @classmethod
    def subtract(cls, minuend, subtrahend):
        """Subtraction."""
        return minuend - subtrahend

    @classmethod
    def multiply(cls, *args):
        """Multiplication."""
        accumulator = 1
        for arg in args:
            accumulator *= arg
        return accumulator

    @classmethod
    def divide(cls, dividend, divisor):
        """Division."""
        return dividend / divisor
