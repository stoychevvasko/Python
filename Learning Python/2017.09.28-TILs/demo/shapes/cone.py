"""Cone class."""

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
        self.base = Circle(c_base.x_coord, c_base.y_coord, c_base.z_coord, r_radius)

        @property
        def base(self):
            """Getter for self._base."""
            return self._base

        @base.setter
        def base(self, value):
            """Setter for self._base."""
            self._base = value
