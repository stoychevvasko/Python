"""Round class."""

from shape import Shape

class Round(Shape):
    """Models a round figure."""

    def __init__(self, x: float, y: float, z: float, r: float):
        """Initializes a new Round instance."""
        super(Round, self).__init__(x, y, z)
        self._radius = r

    @property
    def radius(self) -> float:
        """Getter for self._radius."""
        return self._radius

    @radius.setter
    def radius(self, value: float):
        """Setter for self._radius."""
        self._radius = value

    def __str__(self) -> str:
        """Returns this Round instance as a str value."""
        return 'Round(c: ' + str(self.center) + ', r:' + str(self.radius) + ')'
