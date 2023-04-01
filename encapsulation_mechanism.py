class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self._x = x
            self._y = y

    # public protected private

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    # getter and setter интерфейсные методы
    def set_cord(self, x, y):  # setter
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")

    def get_cord(self):  # getter
        return self.__y, self.__x


pt = Point(1, 2)
pt.set_cord(4, 20)
for i in dir(pt):
    print(i)
