from Animal import *
class Penguin(Animal):

    def __init__(self, name, age):
        super().__init__(name, age, "Hishnik", ["Riba"], 10, "Kurlik-Kurlik")
        self._whoIsAnimal = "Penguin"
        self._Biom = "antarktika"
        self._Square = 10

    def swim(self, value):
        if type(value) is int:
            if value>0:
                print(self._Name, "Poplaval",value, "sekund")
            else:
                print("nelsa plavat otrizatelnoe kol-vo vremeni")
        else:
            print("vremia doljno bit chislom")
