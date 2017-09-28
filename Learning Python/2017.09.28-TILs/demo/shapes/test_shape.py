"""Unit tests for the Shape class."""

import shape

def test_shape__init__():
    """Tests constructor."""
    shp = shape.Shape(0, 0, 0)
    assert shp is not None
    assert isinstance(shp, shape.Shape), 'invalid type exception was raised!'

def test_shape_init_w_center():
    """Tests constructor with parameters."""
    shp = shape.Shape(1, 2, 3)
    assert shp is not None
    assert isinstance(shp, shape.Shape), 'invalid type exception was raised!'
    assert shp.center.x_coord == 1
    assert shp.center.y_coord == 2
    assert shp.center.z_coord == 3
