class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        print(isinstance(args[0], str))
        if not isinstance(args[0], str):
            raise TypeError("Аргумент должен быть строкой")
        return args[0].strip(self.__chars)


s1 = StripChars("?:!.,; ")
s2 = StripChars("ell")
res = s1(" Hello World! ")

# def outer_function(x):
#     print("x: ", x)
#
#     def inner_function(y):
#         print("x: ", x)
#         print("y: ", y)
#         return x + y
#     return inner_function

# closure = outer_function(10)
# print(closure(5))
