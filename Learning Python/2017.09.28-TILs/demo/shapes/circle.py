"""Circle class."""

from shape import Shape

class Circle(Shape):
    """Models a circle shape."""

    def __init__(self, **kwargs):
        
        super(Circle, self).__init__(kwargs)
        self._radius = kwargs.get('radius', 1)
