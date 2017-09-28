"""Sphere class."""

import math
from shape import Shape

class Sphere(Shape):
    """Models a sphere shape."""

    def __init__(self, x, y, z, r):
        """Initialzes a new Sphere instance."""
        super(Sphere, self).__init__(x, y, z)
        self._radius = r

    @property
    def radius(self):
        """Getter for self._radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter for self._radius."""
        self._radius = value
