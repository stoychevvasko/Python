"""Circle class."""

import math
from round import Round

class Circle(Round):
    """Models a circle shape."""

    def __init__(self, x, y, z, r):
        """Initialzes a new Circle instance."""
        super(Circle, self).__init__(x, y, z, r)

    def get_surface(self):
        """Calculates surface area."""
        return math.pi * self.radius * self.radius

    def get_perimeter(self):
        """Calculates perimeter length."""
        return math.pi * self.radius * 2
