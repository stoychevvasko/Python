"""Unit tests for the Line class."""

from line import Line
# pylint:disable=unused-import
from test_fixtures import point_zero, point_1_2_3

# pylint:disable=redefined-outer-name
def test_line__init__(point_zero, point_1_2_3):
    """Tests the constructor."""
    line1 = Line(point_zero, point_1_2_3)
    assert line1 is not None
    assert isinstance(line1, Line)
    assert line1.start.x_coord == 0
    assert line1.start.y_coord == 0
    assert line1.start.z_coord == 0
    assert line1.end.x_coord == 1
    assert line1.end.y_coord == 2
    assert line1.end.z_coord == 3
