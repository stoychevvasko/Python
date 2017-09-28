"""Unit tests for the Sphere class."""

import sphere
import pytest

@pytest.fixture
def sph_sm():
    """Generates a small sphere."""
    return sphere.Sphere(0, 0, 0, 1)

def test_sphere__init__():
    """Tests the constructor."""
    sph = sphere.Sphere(1, 2, 3, 42)
    assert sph is not None
    assert sph.center.x_coord == 1
    assert sph.center.y_coord == 2
    assert sph.center.z_coord == 3
    assert sph.radius == 42
