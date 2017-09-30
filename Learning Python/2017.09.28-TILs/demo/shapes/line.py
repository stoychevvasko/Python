"""Line class."""

from shape import Shape
from point import Point

class Line(Shape):
    """Models a line."""

    def __init__(self, start, end):
        """Initializes a new instance of the Line class."""
        super(Line, self).__init__(start.x_coord, start.y_coord, start.z_coord)
        self._start = Point(start.x_coord, start.y_coord, start.z_coord)
        self._end = Point(end.x_coord, end.y_coord, end.z_coord)

    @property
    def start(self):
        """Getter for self._start."""
        return self._start

    @start.setter
    def start(self, value):
        """Setter for self._start."""
        self._start = value

    @property
    def end(self):
        """Getter for self._end."""
        return self._end

    @end.setter
    def end(self, value):
        """Setter for self._end."""
        self._end = value
