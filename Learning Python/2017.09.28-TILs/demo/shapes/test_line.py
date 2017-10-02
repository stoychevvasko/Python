"""Unit tests for the Line class."""

from line import Line
# pylint:disable=unused-import
from test_fixtures import point_zero, point_1_2_3, line_1

# pylint:disable=redefined-outer-name
def test_line__init__(line_1):
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
def test_get_length(line_1):
    """Tests the get_length() method."""
    assert line_1.get_length() > 0
