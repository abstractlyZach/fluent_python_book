import math


class Vector(object):
    """
    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)
    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0
    >>> v * 3
    Vector(9, 12)
    >>> abs(v * 3)
    15.0
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, right):
        return Vector(self.x + right.x, self.y + right.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __mul__(self, right):
        return Vector(self.x * right, self.y * right)
