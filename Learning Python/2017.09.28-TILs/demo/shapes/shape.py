"""Shape class."""

import math
from point import Point

class Shape():
    """Models an abstract shape."""

    def __init__(self, x: float, y: float, z: float):
        """Shape constructor."""
        self._center = Point(x, y, z)

    @property
    def center(self) -> Point:
        """Getter for self._center"""
        return self._center

    @center.setter
    def center(self, value: Point):
        """Setter for self._center"""
        self._center = value

    def get_distance_to_origin(self) -> float:
        """Calculates distance from center to origin point of coordinate system."""
        return math.sqrt(
            math.pow(self.center.x_coord, 2)
            + math.pow(self.center.y_coord, 2)
            + math.pow(self.center.z_coord, 2))

    def __str__(self):
        """Returns this Shape instance as a str value."""
        return 'Shape(' + str(self.center) + ')'
