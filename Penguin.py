from Animal import *
class Penguin(Animal):

    def __init__(self, name, age):
        super().__init__(name, age, "Hishnik", ["Riba"], 10, "Kurlik-Kurlik")

    def swim(self, value):
        if type(value) is int:
            if value>0:
                print(self.Name, "Poplaval",value, "sekund")
            else:
                print("nelsa plavat otrizatelnoe kol-vo vremeni")
        else:
            print("vremia doljno bit chislom")
