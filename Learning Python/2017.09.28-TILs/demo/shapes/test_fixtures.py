"""Test fixtures."""

from circle import Circle
from line import Line
from point import Point
from round import Round
from shape import Shape
from sphere import Sphere
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

### Line class. ###
@pytest.fixture
def line_1():
    """Generates line ab where a=[0,0,0] and b=[1,2,3]."""
    point_a = Point(0, 0, 0)
    point_b = Point(1, 2, 3)
    return Line(point_a, point_b)

### Round class. ###
@pytest.fixture
def round_sm():
    """Generates a small round."""
    return Round(0, 0, 0, 1)

@pytest.fixture
def round_bg():
    """Generates a bigger round."""
    return Round(0, 0, 0, 2)

### Circle class. ###
@pytest.fixture
def circ_sm():
    """Generates a small circle."""
    return Circle(0, 0, 0, 1)

@pytest.fixture
def circ_bg():
    """Generates a bigger circle."""
    return Circle(0, 0, 0, 2)

### Sphere class. ###
@pytest.fixture
def sphere_sm():
    """Generates a small sphere."""
    return Sphere(0, 0, 0, 1)

@pytest.fixture
def sphere_bg():
    """Generates a bigger sphere."""
    return Sphere(0, 0, 0, 2)
