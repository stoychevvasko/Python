"""Unit tests for the Flower class."""

from flower import Flower

# pylint:disable=no-self-use
class TestFlower(object):
    """Tests the Flower class."""

    def test_flower__init__(self):
        """Tests the constructor."""
        test_name = 'rose'
        test_petals = 8
        test_price = 3.50

        test_flower = Flower(test_name, test_petals, test_price)

        assert test_flower is not None
        assert isinstance(test_flower, Flower)

    def test_flower_name_getter(self):
        """Tests the self._name getter."""
        test_flower = Flower('rose', 8, 3.50)

        assert test_flower.name == 'rose'

    def test_flower_name_setter(self):
        """Tests the self._name setter."""
        test_flower = Flower('rose', 8, 3.50)
        test_flower.name = 'changed'

        assert test_flower.name == 'changed'

    def test_number_of_petals_getter(self):
        """Tests the self._number_of_petals getter."""
        test_flower = Flower('rose', 8, 3.50)

        assert test_flower.number_of_petals == 8

    def test_number_of_petals_setter(self):
        """Tests the self._number_of_petals setter."""
        test_flower = Flower('rose', 8, 3.50)
        test_flower.number_of_petals = 13

        assert test_flower.number_of_petals == 13

    def test_price_getter(self):
        """Tests the self._price getter."""
        test_flower = Flower('rose', 8, 3.50)

        assert test_flower.price == 3.50

    def test_price_setter(self):
        """Tests the self._price setter."""
        test_flower = Flower('rose', 8, 3.50)
        test_flower.price = 5.55

        assert test_flower.price == 5.55
