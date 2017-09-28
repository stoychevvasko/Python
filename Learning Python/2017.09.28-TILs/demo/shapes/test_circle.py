"""Unit tests for the Circle class."""

import circle

def test_circle__init__():
    """Tests the constructor."""
    circ = circle.Circle(1, 2, 3, 42)
    assert circ is not None
    assert circ.center.x_coord == 1
    assert circ.center.y_coord == 2
    assert circ.center.z_coord == 3
    assert circ.radius == 42
