"""Unit tests for the Point class."""

from point import Point
# pylint:disable=unused-import
from test_fixtures import point_zero, point_1_2_3, point_invalid
import pytest

# pylint: disable=no-self-use
class TestPoint(object):
    """Tests the Point class."""

    # pylint:disable=redefined-outer-name
    def test_point__init__(self, point_zero, point_1_2_3, point_invalid):
        """Tests constructor."""
        assert isinstance(point_zero, Point)
        assert point_zero.x_coord == 0
        assert point_zero.y_coord == 0
        assert point_zero.z_coord == 0

        assert point_1_2_3 is not None
        assert isinstance(point_1_2_3, Point)
        assert point_1_2_3.x_coord == 1
        assert point_1_2_3.y_coord == 2
        assert point_1_2_3.z_coord == 3

        assert point_invalid is None

    # pylint:disable=redefined-outer-name
    def test_get_distance(self, point_zero, point_1_2_3):
        """Tests the get_distance() method."""
        dist = point_1_2_3.get_distance(point_zero)
        assert dist > 0

    # pylint:disable=redefined-outer-name
    def test_get_projection(self, point_zero, point_1_2_3):
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

        with pytest.raises(ValueError):
            point_1_2_3.get_projection('invalid')

    def test_x_coord_get(self, point_1_2_3):
        """Tests the x_coord getter."""
        assert point_1_2_3.x_coord is not None
        assert point_1_2_3.x_coord == 1

    def test_x_coord_set(self, point_1_2_3):
        """Tests the x_coord setter."""
        test_point = point_1_2_3
        test_point.x_coord = 15
        assert test_point.x_coord is not None
        assert test_point.x_coord == 15

    def test_y_coord_get(self, point_1_2_3):
        """Tests the y_coord getter."""
        assert point_1_2_3.y_coord is not None
        assert point_1_2_3.y_coord == 2

    def test_y_coord_set(self, point_1_2_3):
        """Tests the y_coord setter."""
        test_point = point_1_2_3
        test_point.y_coord = 15
        assert test_point.y_coord is not None
        assert test_point.y_coord == 15

    def test_z_coord_get(self, point_1_2_3):
        """Tests the z_coord getter."""
        assert point_1_2_3.z_coord is not None
        assert point_1_2_3.z_coord == 3

    def test_z_coord_setter(self, point_1_2_3):
        """Tests the z_coord setter."""
        test_point = point_1_2_3
        test_point.z_coord = 15
        assert test_point.z_coord is not None
        assert test_point.z_coord == 15

    def test_point__str__(self, point_zero, point_1_2_3):
        "Tests the __str__() overload method."""
        expected_zero = 'Point(x: 0.0, y: 0.0, z: 0.0)'
        assert point_zero.__str__() == expected_zero
        assert str(point_zero) == expected_zero
        expected_1_2_3 = 'Point(x: 1.0, y: 2.0, z: 3.0)'
        assert point_1_2_3.__str__() == expected_1_2_3
        assert str(point_1_2_3) == expected_1_2_3
