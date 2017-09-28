"""Point class."""

class Point(object):
    """Models a point in 3D space."""

    def __init__(self, x, y, z):
        """Initializes a new Point instance."""
        self.__x = int(x)
        self.__y = int(y)
        self.__z = int(z)

    @property
    def x_coord(self):
        """Getter for self.__x."""
        return self.__x

    @x_coord.setter
    def x_coord(self, value):
        """Setter for self.__x."""
        self.__x = value

    @property
    def y_coord(self):
        """Getter for self.__y."""
        return self.__y

    @y_coord.setter
    def y_coord(self, value):
        """Setter for self.__y."""
        self.__y = value

    @property
    def z_coord(self):
        """Getter for self.__z."""
        return self.__z

    @z_coord.setter
    def z_coord(self, value):
        """Setter for self.__z."""
        self.__z = value
