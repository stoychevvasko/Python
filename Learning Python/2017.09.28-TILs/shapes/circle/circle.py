"""Circle class."""

class Circle():
    """Models a circle shape."""

    def __init__(self, **kwargs):
        self._radius = kwargs.get('radius', 1)
        self._center_x = kwargs.get('center_x', 0)
        self._center_y = kwargs.get('center_y', 0)
