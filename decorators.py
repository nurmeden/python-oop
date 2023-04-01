class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    #classmethod -
    @classmethod
    def validated(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if Vector.validated(x) and Vector.validated(y):
            self.x = x
            self.y = y

        print(self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x*x + y*y


s = Vector(1, 200)
print(Vector.norm2(5, 6))
# res = Vector.get_coord(s)
# print(res)
