"""Point class."""

import math

class Point(object):
    """Models a point in 3D space."""

    def __init__(self, x: float, y: float, z: float):
        """Initializes a new Point instance."""
        self.__x = float(x)
        self.__y = float(y)
        self.__z = float(z)

    @property
    def x_coord(self) -> float:
        """Getter for self.__x."""
        return self.__x

    @x_coord.setter
    def x_coord(self, value: float):
        """Setter for self.__x."""
        self.__x = value

    @property
    def y_coord(self) -> float:
        """Getter for self.__y."""
        return self.__y

    @y_coord.setter
    def y_coord(self, value: float):
        """Setter for self.__y."""
        self.__y = value

    @property
    def z_coord(self) -> float:
        """Getter for self.__z."""
        return self.__z

    @z_coord.setter
    def z_coord(self, value: float):
        """Setter for self.__z."""
        self.__z = value

    def get_distance(self, other) -> float:
        """Gets the distance between the current point and another."""
        return math.sqrt(
            math.pow(other.x_coord-self.x_coord, 2) +
            math.pow(other.y_coord-self.y_coord, 2) +
            math.pow(other.z_coord-self.z_coord, 2))

    def get_projection(self, option: str):
        """Gets the projectection of this point onto selected axis."""
        if option == 'x':
            return Point(0, self.y_coord, self.z_coord)
        elif option == 'y':
            return Point(self.x_coord, 0, self.z_coord)
        elif option == 'z':
            return Point(self.x_coord, self.y_coord, 0)
        else:
            raise ValueError("invalid axis/dimension - must be 'x', 'y' or 'z'")

    def __str__(self) -> str:
        """Returns the current Point instance as str value."""
        return 'Point(x: ' + str(self.x_coord) + ', y: ' + str(self.y_coord) + \
            ', z: ' + str(self.z_coord) + ')'
