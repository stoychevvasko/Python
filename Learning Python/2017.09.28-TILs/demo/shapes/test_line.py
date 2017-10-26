"""Unit tests for the Line class."""

from line import Line
from point import Point
# pylint:disable=unused-import
from test_fixtures import point_zero, point_1_2_3, line_1

# pylint: disable=no-self-use
class TestLine(object):
    """Tests the Line class."""

    # pylint:disable=redefined-outer-name
    def test_line__init__(self, line_1):
        """Tests the constructor."""
        assert line_1 is not None
        assert isinstance(line_1, Line)
        assert line_1.start.x_coord == 0
        assert line_1.start.y_coord == 0
        assert line_1.start.z_coord == 0
        assert line_1.end.x_coord == 1
        assert line_1.end.y_coord == 2
        assert line_1.end.z_coord == 3

    # pylint:disable=redefined-outer-name
    def test_get_length(self, line_1):
        """Tests the get_length() method."""
        assert line_1.get_length() > 0

    def test_start_get(self, line_1):
        """Tests the start getter."""
        assert line_1.start is not None
        assert isinstance(line_1.start, Point)

    def test_start_set(self, line_1, point_1_2_3):
        """Tests the start setter."""
        test_line = line_1
        test_line.start = point_1_2_3
        assert test_line.start is not None
        assert isinstance(test_line.start, Point)

    def test_end_get(self, line_1):
        """Tests the end getter."""
        assert line_1.end is not None
        assert isinstance(line_1.end, Point)

    def test_end_set(self, line_1, point_1_2_3):
        """Tests the end setter."""
        test_line = line_1
        test_line.end = point_1_2_3
        assert test_line.end is not None
        assert isinstance(test_line.end, Point)
