"""Unit tests for the Point class."""

from point import Point
# pylint:disable=unused-import
from test_fixtures import point_zero, point_1_2_3, point_invalid
import pytest

# pylint:disable=redefined-outer-name
def test_point__init__(point_zero, point_1_2_3, point_invalid):
    """Tests constructor."""
    assert isinstance(point_zero, Point), 'invalid type exception was raised!'
    assert point_zero.x_coord == 0
    assert point_zero.y_coord == 0
    assert point_zero.z_coord == 0

    assert point_1_2_3 is not None
    assert isinstance(point_1_2_3, Point), 'invalid type exception was raised!'
    assert point_1_2_3.x_coord == 1
    assert point_1_2_3.y_coord == 2
    assert point_1_2_3.z_coord == 3

    assert point_invalid is None

# pylint:disable=redefined-outer-name
def test_get_distance(point_zero, point_1_2_3):
    """Tests the get_distance() method."""
    dist = point_1_2_3.get_distance(point_zero)
    assert dist > 0

# pylint:disable=redefined-outer-name
def test_get_projection(point_zero, point_1_2_3):
    """Tests the get_projection() method."""
    assert isinstance(point_zero.get_projection('x'), Point)
    assert point_zero.get_projection('x').x_coord == 0
    assert isinstance(point_zero.get_projection('y'), Point)
    assert point_zero.get_projection('y').y_coord == 0
    assert isinstance(point_zero.get_projection('z'), Point)
    assert point_zero.get_projection('z').z_coord == 0

    assert isinstance(point_1_2_3.get_projection('x'), Point)
    assert point_1_2_3.get_projection('x').x_coord == 0
    assert point_1_2_3.get_projection('x').y_coord == 2
    assert point_1_2_3.get_projection('x').z_coord == 3

    assert isinstance(point_1_2_3.get_projection('y'), Point)
    assert point_1_2_3.get_projection('y').x_coord == 1
    assert point_1_2_3.get_projection('y').y_coord == 0
    assert point_1_2_3.get_projection('y').z_coord == 3

    assert isinstance(point_1_2_3.get_projection('z'), Point)
    assert point_1_2_3.get_projection('z').x_coord == 1
    assert point_1_2_3.get_projection('z').y_coord == 2
    assert point_1_2_3.get_projection('z').z_coord == 0
