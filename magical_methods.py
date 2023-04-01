class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MIN_COORD:
            self.x = x
            self.y = y

    # def set_bound(self, left):
    #     self.MIN_COORD = left  # новый аттрибут добавляется на экземпляр

    # @classmethod
    # def set_bound(cls, left):
    #     cls.MIN_COORD = left  # изменяет атрибут из класса

    def __getattribute__(self, item): # автоматически вызывается при получении свойства класса с именем item
        print("__getattribute__")
        if item == "x":
            raise ValueError("доступ запрещен")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value): # автоматически вызывается при изменении свойства key класса
        if key == 'z':
            raise AttributeError("недопустимое имя атрибута")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item): # автоматически вызывается при получении несуществующего свойства item класса
        return False

    def __delattr__(self, item): # автоматически вызывается при удалении свойства item(не важно существует оно или нет)
        print("__delattr__ " + item)
        object.__delattr__(self, item)


pt = Point(1, 2)
del pt.y
print(pt.__dict__)
