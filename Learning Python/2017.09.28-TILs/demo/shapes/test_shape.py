"""Unit tests for the Shape class."""

from point import Point
from shape import Shape
# pylint:disable=unused-import
from test_fixtures import shape_zero, shape_1_2_3, point_1_2_3

# pylint:disable=no-self-use
class TestShape(object):
    """Tests the Shape class."""

    # pylint:disable=redefined-outer-name
    def test_shape__init__(self, shape_zero):
        """Tests constructor."""
        assert shape_zero is not None
        assert isinstance(shape_zero, Shape), 'invalid type exception was raised!'

    def test_shape_center_get(self, shape_zero, shape_1_2_3):
        """Tests the center getter."""
        assert shape_zero.center is not None
        assert shape_1_2_3.center is not None
        assert isinstance(shape_zero.center, Point)
        assert isinstance(shape_1_2_3.center, Point)

    def test_shape_center_set(self, shape_zero, point_1_2_3):
        """Tests the center setter."""
        test_shape = shape_zero
        test_shape.center = point_1_2_3
        assert test_shape.center is not None
        assert isinstance(test_shape.center, Point)

    # pylint:disable=redefined-outer-name
    def test_shape_init_w_center(self, shape_1_2_3):
        """Tests constructor with parameters."""
        assert shape_1_2_3 is not None
        assert isinstance(shape_1_2_3, Shape), 'invalid type exception was raised!'
        assert shape_1_2_3.center.x_coord == 1
        assert shape_1_2_3.center.y_coord == 2
        assert shape_1_2_3.center.z_coord == 3

    # pylint:disable=redefined-outer-name
    def test_get_distance_to_origin(self, shape_1_2_3):
        """Tests get_distance_to_origin() method."""
        assert shape_1_2_3.get_distance_to_origin() > 0

    def test_shape__str__(self, shape_1_2_3):
        """Tests the self.__str__() overload method."""
        expected = 'Shape(Point(x: 1.0, y: 2.0, z: 3.0))'
        assert shape_1_2_3.__str__() == expected
        assert str(shape_1_2_3) == expected
