"""Unit tests for the Point class."""

from point import Point
# pylint:disable=unused-import
from test_fixtures import point_zero, point_1_2_3, point_invalid
import pytest

# pylint:disable=redefined-outer-name
def test_point__init__(point_zero, point_1_2_3, point_invalid):
    """Tests constructor."""
    pntz = point_zero
    assert isinstance(pntz, Point), 'invalid type exception was raised!'
    assert pntz.x_coord == 0
    assert pntz.y_coord == 0
    assert pntz.z_coord == 0

    pnt = point_1_2_3
    assert pnt is not None
    assert isinstance(pnt, Point), 'invalid type exception was raised!'
    assert pnt.x_coord == 1
    assert pnt.y_coord == 2
    assert pnt.z_coord == 3

    assert point_invalid is None
