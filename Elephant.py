from Animal import *
class Elephant(Animal):

    def __init__(self, name, age):
        super().__init__(name, age, "Травоядный", ["листики","сено"], 50, 100, "*ГРОМКИЕ ЗВУКИ ТРУБЫ*")
        self._whoIsAnimal = "Слон"
        self._Biom = "саванна"
        self._Square = 50

    def pour(self):
        print(self._Name,": облил тебя")
