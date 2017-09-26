"""OOP in Python"""

HUMAN_PROPS = {
    'name':'default_human',
    'height':170,
    'sex':'male'
}

class Human():
    """Models a human being."""

    def __init__(self, **kwargs):
        assert self is not False
        self._name = kwargs.get('name', '')
        self._sex = kwargs.get('sex', 'male')

    @property #@ decorates
    def name(self):
        """Getter for self._name"""
        return self._name

    @name.setter
    def name(self, value):
        """Setter fpr self._name"""
        self._name = value

    @property #@ decorates
    def sex(self):
        """Getter for self._sex"""
        return self._sex

    @sex.setter
    def sex(self, value):
        """Setter fpr self._sex"""
        self._sex = value

HUMAN_01 = Human(**HUMAN_PROPS)
print('human object: ', HUMAN_01)
print('human.name: ', HUMAN_01.name)
print('human.sex: ', HUMAN_01.sex)
