"""Unit tests for the Sphere class."""

from point import Point
from sphere import Sphere
# pylint:disable=unused-import
from test_fixtures import sphere_sm, sphere_bg

# pylint:disable=no-self-use
class TestSphere(object):
    """Tests the Sphere class."""

    def test_sphere__init__(self):
        """Tests the constructor."""
        sphe = Sphere(1, 2, 3, 42)
        assert sphe is not None
        assert sphe.center.x_coord == 1
        assert sphe.center.y_coord == 2
        assert sphe.center.z_coord == 3
        assert sphe.radius == 42

    # pylint:disable=redefined-outer-name
    def test_sphere_get_volume(self, sphere_sm, sphere_bg):
        """Tests get_volume() method."""
        assert sphere_sm.get_volume() > 0
        assert sphere_bg.get_volume() > 0
        assert sphere_sm.get_volume() < sphere_bg.get_volume()

    # pylint:disable=redefined-outer-name
    def test_sphere_get_area(self, sphere_sm, sphere_bg):
        """Tests get_area() method."""
        assert sphere_sm.get_area() > 0
        assert sphere_bg.get_area() > 0
        assert sphere_sm.get_area() < sphere_bg.get_area()

    # pylint:disable=redefined-outer-name
    def test_sphere_get_center(self, sphere_sm):
        """Tests the get_center() method."""
        assert isinstance(sphere_sm.get_center(), Point)

    def test_sphere__str__(self, sphere_sm, sphere_bg):
        """Tests the self.__str__() ovrload method."""
        expected_sm = 'sphere(c:Point(x: 0.0, y: 0.0, z: 0.0), r:1)'
        assert sphere_sm.__str__() == expected_sm
        assert str(sphere_sm) == expected_sm
        expected_bg = 'sphere(c:Point(x: 0.0, y: 0.0, z: 0.0), r:2)'
        assert sphere_bg.__str__() == expected_bg
        assert str(sphere_bg) == expected_bg
