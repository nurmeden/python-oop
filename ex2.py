class Point:
    color = 'red' #атрибуты
    circle = 2
    # new() Вызывается перед созданием обьекта класса
    # init()  Вызывается сразу после созданием обьекта класса
    def __init__(self, x, y):
        print("вызов __init__")
        self.x = x
        self.y = y

    def __del__(self):
        print("del")

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return  (self.x, self.y)

pt = Point(1,2)
print(pt.__dict__)
print(Point)