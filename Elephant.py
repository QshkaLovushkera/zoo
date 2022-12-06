from Animal import *
class Elephant(Animal):

    def __init__(self, name, age):
        super().__init__(name, age, "Travoyadny", ["listiki","seno"], 50, "GROMKIE ZVUKI TRUBI")
        self._whoIsAnimal = "Elephant"
        self._Biom = "savanna"
        self._Square = 50

    def pour(self):
        print(self._Name,": oblil tebia")
