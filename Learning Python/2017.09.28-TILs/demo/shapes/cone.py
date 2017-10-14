"""Cone class."""

# import math
from circle import Circle
from point import Point
from shape import Shape

class Cone(Shape):
    """Models a cone shape."""

    def __init__(self, c_base, r_radius, apex):
        """Initializes a new Cone instance."""
        c_x = c_base.x_coord
        c_y = c_base.y_coord
        c_z = c_base.z_coord
        super(Cone, self).__init__(c_x, c_y, c_z)
        self._apex = Point(apex.x_coord, apex.y_coord, apex.z_coord)
        self._base = Circle(c_x, c_y, c_z, r_radius)
