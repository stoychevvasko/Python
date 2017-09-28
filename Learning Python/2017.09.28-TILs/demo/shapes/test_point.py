"""Unit tests for the Point class."""

import point

def test_point__init__():
    """Tests constructor."""
    pnt = point.Point(1, 2, 3)
    assert pnt is not None
    assert isinstance(pnt, point.Point), 'invalid type exception was raised!'
    assert pnt.x_coord == 1
    assert pnt.y_coord == 2
    assert pnt.z_coord == 3
