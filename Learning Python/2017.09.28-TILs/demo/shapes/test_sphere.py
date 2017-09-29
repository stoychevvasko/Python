"""Unit tests for the Sphere class."""

import sphere
import pytest

@pytest.fixture
def sph_sm():
    """Generates a small sphere."""
    return sphere.Sphere(0, 0, 0, 1)

@pytest.fixture
def sph_bg():
    """Generates a big sphere."""
    return sphere.Sphere(0, 0, 0, 2)

def test_sphere__init__():
    """Tests the constructor."""
    sphe = sphere.Sphere(1, 2, 3, 42)
    assert sphe is not None
    assert sphe.center.x_coord == 1
    assert sphe.center.y_coord == 2
    assert sphe.center.z_coord == 3
    assert sphe.radius == 42

# pylint:disable=redefined-outer-name
def test_sphere_get_volume(sph_sm, sph_bg):
    """Tests get_volume() method."""
    assert sph_sm.get_volume() > 0
    assert sph_bg.get_volume() > 0
    assert sph_sm.get_volume() < sph_bg.get_volume()

# pylint:disable=redefined-outer-name
def test_sphere_get_area(sph_sm, sph_bg):
    """Test get_area() method."""
    assert sph_sm.get_area() > 0
    assert sph_bg.get_area() > 0
    assert sph_sm.get_area() < sph_bg.get_area()
