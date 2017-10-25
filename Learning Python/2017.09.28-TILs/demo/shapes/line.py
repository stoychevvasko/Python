"""Line class."""

from shape import Shape
from point import Point

class Line(Shape):
    """Models a line."""

    def __init__(self, start: Point, end: Point):
        """Initializes a new instance of the Line class."""
        super(Line, self).__init__(
            (start.x_coord + end.x_coord)/2.0,
            (start.y_coord + end.y_coord)/2.0,
            (start.z_coord + end.z_coord)/2.0)
        self._start = Point(start.x_coord, start.y_coord, start.z_coord)
        self._end = Point(end.x_coord, end.y_coord, end.z_coord)

    @property
    def start(self) -> Point:
        """Getter for self._start."""
        return self._start

    @start.setter
    def start(self, value: Point):
        """Setter for self._start."""
        self._start = value

    @property
    def end(self) -> Point:
        """Getter for self._end."""
        return self._end

    @end.setter
    def end(self, value: Point):
        """Setter for self._end."""
        self._end = value

    def get_length(self) -> float:
        """Returns the length of the line."""
        return self.end.get_distance(self.start)
