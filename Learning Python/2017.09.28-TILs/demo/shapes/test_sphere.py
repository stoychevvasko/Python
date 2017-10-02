"""Unit tests for the Sphere class."""

from sphere import Sphere
# pylint:disable=unused-import
from test_fixtures import sphere_sm, sphere_bg

def test_sphere__init__():
    """Tests the constructor."""
    sphe = Sphere(1, 2, 3, 42)
    assert sphe is not None
    assert sphe.center.x_coord == 1
    assert sphe.center.y_coord == 2
    assert sphe.center.z_coord == 3
    assert sphe.radius == 42

# pylint:disable=redefined-outer-name
def test_sphere_get_volume(sphere_sm, sphere_bg):
    """Tests get_volume() method."""
    assert sphere_sm.get_volume() > 0
    assert sphere_bg.get_volume() > 0
    assert sphere_sm.get_volume() < sphere_bg.get_volume()

# pylint:disable=redefined-outer-name
def test_sphere_get_area(sphere_sm, sphere_bg):
    """Test get_area() method."""
    assert sphere_sm.get_area() > 0
    assert sphere_bg.get_area() > 0
    assert sphere_sm.get_area() < sphere_bg.get_area()