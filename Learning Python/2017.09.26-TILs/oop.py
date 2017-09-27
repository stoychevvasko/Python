"""OOP in Python"""

class Human(object):
    """Models a human being."""

    def __init__(self, **kwargs):
        assert self is not False
        self._name = kwargs.get('name', 'default_name')
        self._height = kwargs.get('height', None)
        self._sex = kwargs.get('sex', 'male')

    #use @ decorators
    @property
    def height(self):
        """Getter for self._height"""
        return self._height

    @height.setter
    def height(self, value):
        """Setter for self._height"""
        self._height = value

    @property
    def name(self):
        """Getter for self._name"""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for self._name"""
        self._name = value

    @property
    def sex(self):
        """Getter for self._sex"""
        return self._sex

    @sex.setter
    def sex(self, value):
        """Setter fpr self._sex"""
        self._sex = value

HUMAN_PROPERTIES = {
    'name': 'default_human',
    'height': 170,
    'sex': 'male'
}

HUMAN_01 = Human(**HUMAN_PROPERTIES) #** unpacks dict
print('human object: ', HUMAN_01)
print('human.name: ', HUMAN_01.name)
print('human.height', HUMAN_01.height)
print('human.sex: ', HUMAN_01.sex)
