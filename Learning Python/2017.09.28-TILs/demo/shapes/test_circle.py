"""Unit tests for the Circle class."""

from circle import Circle
# pylint:disable=unused-import
from test_fixtures import circ_sm, circ_bg

# pylint:disable=redefined-outer-name
def test_circle__init__(circ_sm, circ_bg):
    """Tests the constructor."""
    circ = Circle(1, 2, 3, 42)
    assert circ is not None
    assert circ.center.x_coord == 1
    assert circ.center.y_coord == 2
    assert circ.center.z_coord == 3
    assert circ.radius == 42

    assert circ_sm is not None
    assert circ_sm.center.x_coord == 0
    assert circ_sm.center.y_coord == 0
    assert circ_sm.center.z_coord == 0
    assert circ_sm.radius == 1

    assert circ_bg is not None
    assert circ_bg.center.x_coord == 0
    assert circ_bg.center.y_coord == 0
    assert circ_bg.center.z_coord == 0
    assert circ_bg.radius == 2

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