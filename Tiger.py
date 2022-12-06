from Animal import *
class Tiger(Animal):

    def __init__(self, name, age):
        super().__init__(name,age,"Hishnik",["Miaso"], 25,"RRRRRRRRRRRRRRRRRRRRRR!!!!!!!!!")
        self._whoIsAnimal = "Tiger"
        self._Biom = "savanna"
        self._Square = 20

    def bite(self):
        print(self._Name,"sdelal kus")