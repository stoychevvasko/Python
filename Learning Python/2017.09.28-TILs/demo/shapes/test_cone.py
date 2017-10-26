"""Unit tests for the Cone class."""

from circle import Circle
from cone import Cone
from point import Point
# pylint:disable=unused-import
from test_fixtures import cone_sm, cone_bg, circ_sm, circ_bg, point_1_2_3

# pylint:disable=no-self-use
class TestCone(object):
    """Tests the Cone class."""

    # pylint:disable=redefined-outer-name
    def test_cone__init__(self, cone_sm, cone_bg):
        """Tests constructor."""
        assert cone_sm is not None
        assert cone_bg is not None
        assert isinstance(cone_sm, Cone)
        assert isinstance(cone_sm, Cone)

    # pylint:disable=redefined-outer-name
    def test_cone_base_property_get(self, cone_sm, cone_bg):
        """Tests the base property getter."""
        assert cone_sm.base is not None
        assert cone_bg.base is not None
        assert isinstance(cone_sm.base, Circle)
        assert isinstance(cone_bg.base, Circle)

    # pylint:disable=redefined-outer-name
    def test_cone_base_property_set(self, cone_sm, cone_bg, circ_sm, circ_bg):
        """Tests the base property setter."""
        test_cone_sm = cone_sm
        test_cone_sm.base = circ_sm
        assert isinstance(test_cone_sm.base, Circle)
        test_cone_bg = cone_bg
        test_cone_bg.base = circ_bg
        assert isinstance(test_cone_bg.base, Circle)

    def test_cone_apex_property_get(self, cone_sm, cone_bg):
        """Tests the apex (vertex) property getter."""
        assert cone_sm.apex is not None
        assert cone_bg.apex is not None
        assert isinstance(cone_sm.apex, Point)
        assert isinstance(cone_bg.apex, Point)

    def test_cone_apex_property_set(self, cone_sm, cone_bg, point_1_2_3):
        """Tests the apex (vertex) property setter."""
        test_cone_sm = cone_sm
        test_cone_sm.apex = point_1_2_3
        assert isinstance(test_cone_sm.apex, Point)
        test_cone_bg = cone_bg
        test_cone_bg.apex = point_1_2_3
        assert isinstance(test_cone_bg.apex, Point)

    # pylint:disable=redefined-outer-name
    def test_cone_get_volume(self, cone_sm, cone_bg):
        """Tests the get_volume() method."""
        assert cone_sm.get_volume() > 0
        assert cone_bg.get_volume() > 0
