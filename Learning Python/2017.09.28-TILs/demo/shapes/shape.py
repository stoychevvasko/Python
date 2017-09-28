"""Shape class."""

import point

class Shape():
    """Models an abstract shape."""

    def __init__(self, x, y, z):
        """Shape constructor."""
        self._center = point.Point(x, y, z)

    @property
    def center(self):
        """Getter for self._center"""
        return self._center

    @center.setter
    def center(self, value):
        """Setter for self._center"""
        self._center = value
