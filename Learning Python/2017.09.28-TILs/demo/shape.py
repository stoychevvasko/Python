"""Shape class."""

class Shape():
    """Models an abstract shape."""

    def __init__(self, **kwargs):
        """Shape constructor."""
        self._center = (kwargs.get('center_x', 0), kwargs.get('center_y', 0))

    @property
    def center(self):
        """Getter for self._center"""
        return self._center

    @center.setter
    def center(self, value):
        """Setter for self._center"""
        self._center = value
