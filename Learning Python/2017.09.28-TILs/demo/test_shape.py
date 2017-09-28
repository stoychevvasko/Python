"""Unit tests for the Shape class."""

import shape

def test_shape__init__():
    """Tests constructor."""
    shp = shape.Shape()
    assert shp is not None
    assert isinstance(shp, shape.Shape), 'invalid type exception was raised!'
    assert shp.center == (0, 0)

def test_shape_init_w_center():
    """Tests constructor with parameters."""
    shp = shape.Shape(center_x=1, center_y=1)
    assert shp.center == (1, 1), 'invalid center coords exception was raised!'
