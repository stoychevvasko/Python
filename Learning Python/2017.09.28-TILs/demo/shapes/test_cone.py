"""Unit tests for the Cone class."""

from cone import Cone
# pylint:disable=unused-import
from test_fixtures import cone_sm, cone_bg

# pylint:disable=no-self-use
class TestCone(object):
    """Tests the Cone class."""

    # pylint:disable=redefined-outer-name
    def test_shape__init__(self, cone_sm, cone_bg):
        """Tests constructor."""
        assert cone_sm is not None
        assert isinstance(cone_sm, Cone), 'invalid type exception was raised!'
        assert cone_bg is not None
        assert isinstance(cone_sm, Cone), 'invalid type exception was raised!'
