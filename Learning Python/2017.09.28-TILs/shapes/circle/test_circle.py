"""Unit tests for the Circle class."""

from shapes import circle

def test_circle__init__():
    """Tests the constructor."""
    circ = circle.Circle()
    assert circ is not None
    assert isinstance(circ, circle.Circle), "invalid type exception was raised!"
