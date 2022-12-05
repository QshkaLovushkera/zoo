from Animal import *
class Elephant(Animal):

    def __init__(self,name, age):
        super().__init__(name, age, "Travoyadny", ["listiki","seno"], 50, "GROMKIE ZVUKI TRUBI")

    def pour(self):
        print(self.Name,": oblil tebia")
