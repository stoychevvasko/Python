"""Test fixtures."""

from circle import Circle
from point import Point
from shape import Shape
import pytest

### Shape class. ###
@pytest.fixture
def shape_zero():
    """Generates a shape with center [0, 0, 0]."""
    return Shape(0, 0, 0)

@pytest.fixture
def shape_1_2_3():
    """Generates a shape with center [1, 2, 3]."""
    return Shape(1, 2, 3)

### Point class. ###
@pytest.fixture
def point_zero():
    """Returns Point[0, 0, 0]."""
    return Point(0, 0, 0)

@pytest.fixture
def point_1_2_3():
    """Returns Point[1, 2, 3]."""
    return Point(1, 2, 3)

# pylint:disable=bare-except
@pytest.fixture
def point_invalid():
    """Generates invalid point [x: 'invalid_x', y: 'invalid_y', z: 'invalid_z']."""
    try:
        return Point('invalid_x', 'invalid_y', 'invalid_z')
    except:
        print('<<<invalid point!>>> PointError ..')

### Circle class. ###
@pytest.fixture
def circ_sm():
    """Generates a small circle."""
    return Circle(0, 0, 0, 1)

@pytest.fixture
def circ_bg():
    """Generates a small circle."""
    return Circle(0, 0, 0, 2)
