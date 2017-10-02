"""Unit tests for the Round class."""

# pylint:disable=unused-import
from test_fixtures import round_sm

# pylint:disable=redefined-outer-name
def test_round__init__(round_sm):
    """Tests the constructor."""
    assert round_sm.center.x_coord == 0
    assert round_sm.center.y_coord == 0
    assert round_sm.center.z_coord == 0
    assert round_sm.radius == 1
