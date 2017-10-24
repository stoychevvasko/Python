"""Cone class (right, circular)."""

# import math
from circle import Circle
from point import Point
from shape import Shape

class Cone(Shape):
    """Models a cone shape."""

    def __init__(self, c_base, r_radius, apex):
        """Initializes a new Cone instance."""
        super(Cone, self).__init__(c_base.x_coord, c_base.y_coord, c_base.z_coord)
        self._apex = Point(apex.x_coord, apex.y_coord, apex.z_coord)
        self._base = Circle(c_base.x_coord, c_base.y_coord, c_base.z_coord, r_radius)

    @property
    def apex(self):
        """Getter for self._apex."""
        return self._apex

    @apex.setter
    def apex(self, value):
        """Setter for self._apex."""
        self._apex = value

    @property
    def base(self):
        """Getter for self._base."""
        return self._base

    @base.setter
    def base(self, value):
        """Setter for self._base."""
        self._base = value

    def get_volume(self):
        """Returns cone volume."""
        return (1.0/3.0)*self.base.get_surface()*Point.get_distance(self.base.center, self.apex)
