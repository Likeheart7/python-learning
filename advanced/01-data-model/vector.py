import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"  # !r 就是f-string里的%r，表示用repr处理, string就会使Vector('3','4')

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self):
        # return math.sqrt(self.x ** 2 + self.y ** 2)
        return math.hypot(self.x, self.y)   # hypot 计算三角形斜边长度

    def __bool__(self):
        return bool(abs(self))


if __name__ == '__main__':
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    v3 = Vector(3, 4)
    print(v1)
    print(v1 + v2)
    print(v3 * 3)
    print(abs(v3 * 3))
    print((bool(v1)))