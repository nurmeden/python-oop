class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

    # old = property()
    # old = old.getter(get_old)
    # old = old.setter(set_old)


p = Person("Dulat", 20)
p.old = 35
print(p.old, p.__dict__)
