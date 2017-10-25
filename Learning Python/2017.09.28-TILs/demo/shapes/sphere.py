"""Sphere class."""

import math
from point import Point
from round import Round

class Sphere(Round):
    """Models a sphere shape."""

    def __init__(self, x: float, y: float, z: float, r: float):
        """Initialzes a new Sphere instance."""
        super(Sphere, self).__init__(x, y, z, r)

    def get_volume(self) -> float:
        """Calculates sphere volume."""
        return (4.0/3.0)*math.pi*math.pow(self.radius, 3)

    def get_area(self) -> float:
        """Calculates sphere surface area."""
        return 4*math.pi*math.pow(self.radius, 2)

    def get_center(self) -> Point:
        """Returns the center of the sphere as Point object."""
        return self.center
