"""Unit tests for the Circle class."""

import circle
import pytest

@pytest.fixture
def circ_sm():
    """Generates a small circle."""
    return circle.Circle(0, 0, 0, 1)

@pytest.fixture
def circ_bg():
    """Generates a small circle."""
    return circle.Circle(0, 0, 0, 2)

def test_circle__init__():
    """Tests the constructor."""
    circ = circle.Circle(1, 2, 3, 42)
    assert circ is not None
    assert circ.center.x_coord == 1
    assert circ.center.y_coord == 2
    assert circ.center.z_coord == 3
    assert circ.radius == 42

# pylint:disable=redefined-outer-name
def test_circle_get_surface(circ_sm, circ_bg):
    """Tests get_surface() method."""
    assert circ_sm.get_surface() > 0
    assert circ_bg.get_surface() > 0
    assert circ_sm.get_surface() < circ_bg.get_surface()

# pylint:disable=redefined-outer-name
def test_circle_get_perimeter(circ_sm, circ_bg):
    """Tests get_perimeter() method."""
    assert circ_sm.get_perimeter() > 0
    assert circ_bg.get_perimeter() > 0
    assert circ_sm.get_perimeter() < circ_bg.get_perimeter()
