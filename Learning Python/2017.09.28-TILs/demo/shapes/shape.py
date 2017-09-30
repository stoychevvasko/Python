"""Shape class."""

from point import Point

class Shape():
    """Models an abstract shape."""

    def __init__(self, x, y, z):
        """Shape constructor."""
        self._center = Point(x, y, z)

    @property
    def center(self):
        """Getter for self._center"""
        return self._center

    @center.setter
    def center(self, value):
        """Setter for self._center"""
        self._center = value

    def get_distance_to_origin(self):
        """Calculates distance from center to origin point of coordinate system."""
        return 0
