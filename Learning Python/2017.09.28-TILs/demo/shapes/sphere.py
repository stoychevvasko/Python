"""Sphere class."""

import math
from round import Round

class Sphere(Round):
    """Models a sphere shape."""

    def __init__(self, x, y, z, r):
        """Initialzes a new Sphere instance."""
        super(Sphere, self).__init__(x, y, z, r)

    def get_volume(self):
        """Calculates sphere volume."""
        return (4.0/3.0)*math.pi*math.pow(self.radius, 3)

    def get_area(self):
        """Calculates sphere surface area."""
        return 4*math.pi*math.pow(self.radius, 2)
