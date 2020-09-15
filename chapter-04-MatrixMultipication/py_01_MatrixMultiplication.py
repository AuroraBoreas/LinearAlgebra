import sys
sys.path.append('.')
from libraries.vector import Vector

class Matrix(Vector):
    def __init__(self, *args):
        self.a, self.b, self.c, self.d = args
    def __str__(self):
        return 'Matrix({}, {}, {}, {})'.format(self.a, self.b, self.c, self.d)
    def __add__(self, other):
        pass
    def __mul__(self, other):
        _i = Vector(self.a, self.b)
        _j = Vector(self.c, self.d)

        _v1 = _i * other.a
        _v2 = _j * other.b
        _v3 = _i * other.c
        _v4 = _j * other.d

        _I = _v1 + _v2
        _J = _v3 + _v4
        return Matrix(_I.x, _I.y, _J.x, _J.y)


m1 = Matrix(0, 1, 2, 0)
m2 = Matrix(1, 1, -2, 0)
print(m1 * m2)