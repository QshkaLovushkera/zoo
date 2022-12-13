from Animal import *
class Penguin(Animal):

    def __init__(self, name, age):
        super().__init__(name, age, "Хищник", ["Рыба"], 10, 20, "Курлык-Курлык")
        self._whoIsAnimal = "Пингвин"
        self._Biom = "антарктика"
        self._Square = 10

    def swim(self, value):
        if type(value) is int:
            if value>0:
                print(self._Name, "Поплавал",value, "секунд")
            else:
                print("Время плавания должно быть положительным")
        else:
            print("Время должно быть написано числом")
