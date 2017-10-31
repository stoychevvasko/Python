"""Circle class."""

import math
from round import Round

class Circle(Round):
    """Models a circle shape."""

    def __init__(self, x: float, y: float, z: float, r: float):
        """Initialzes a new Circle instance."""
        super(Circle, self).__init__(x, y, z, r)

    def get_surface(self) -> float:
        """Calculates surface area."""
        return math.pi * self.radius * self.radius

    def get_perimeter(self) -> float:
        """Calculates perimeter length."""
        return math.pi * self.radius * 2

    def __str__(self) -> str:
        """Returns a string representation of this circle instance."""
        return 'circle(c: ' + str(self.center) + ', r:' + str(self.radius) + ')'
