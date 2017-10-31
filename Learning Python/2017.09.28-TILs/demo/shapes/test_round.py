"""Unit tests for the Round class."""

# pylint:disable=unused-import
from test_fixtures import round_sm, round_bg

# pylint: disable=no-self-use, too-few-public-methods
class TestRound(object):
    """Tests the Round class."""

    # pylint:disable=redefined-outer-name
    def test_round__init__(self, round_sm):
        """Tests the constructor."""
        assert round_sm.center.x_coord == 0
        assert round_sm.center.y_coord == 0
        assert round_sm.center.z_coord == 0
        assert round_sm.radius == 1

    def test_round_radius_get(self, round_sm, round_bg):
        """Tests the radius getter."""
        assert round_sm.radius is not None
        assert round_bg.radius is not None
        assert round_sm.radius > 0
        assert round_bg.radius > 0

    def test_round_radius_set(self, round_sm):
        """Tests the radius setter."""
        test_round = round_sm
        test_round.radius = 15
        assert test_round.radius is not None
        assert test_round.radius == 15

    def test_round__str__(self, round_sm, round_bg):
        """Tests the self.__str__() overload method."""
        expected_sm = 'Round(c: Point(x: 0.0, y: 0.0, z: 0.0), r:1)'
        assert round_sm.__str__() == expected_sm
        assert str(round_sm) == expected_sm
        expected_bg = 'Round(c: Point(x: 0.0, y: 0.0, z: 0.0), r:2)'
        assert round_bg.__str__() == expected_bg
        assert str(round_bg) == expected_bg
