# Пример Паттерна Singleton
class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance  #Возвращаем созданный обьект

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"connect to db: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("close connection this db")

    def read(self):
        return "data in db"

    def write(self, data):
        print(f"write in db {data}")

db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '1234', 80)
print(id(db), id(db2))
