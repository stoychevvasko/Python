"""Flower class."""

# R-2.4 Write a Python class, Flower, that has three instance variables of type str,
# int, and float, that respectively represent the name of the flower, its number
# of petals, and its price. Your class must include a constructor method
# that initializes each variable to an appropriate value, and your class should
# include methods for setting the value of each type, and retrieving the value
# of each type.

class Flower(object):
    """Models a flower."""

    def __init__(self, name: str, number_of_petals: int, price: float):
        """Initializes a new instance of the Flower class."""
        self._name = name
        self._number_of_petals = number_of_petals
        self._price = price

    @property
    def name(self) -> str:
        """Getter for self._name."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Setter for self._name."""
        self._name = str(value)

    @property
    def number_of_petals(self) -> int:
        """Getter for self._number_of_petals."""
        return self._number_of_petals

    @number_of_petals.setter
    def number_of_petals(self, value: int):
        """Setter for self._number_of_petals."""
        self._number_of_petals = int(value)

    @property
    def price(self) -> float:
        """Getter for self._price."""
        return self._price

    @price.setter
    def price(self, value: float):
        """Setter for self._price."""
        self._price = float(value)
