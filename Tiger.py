from Animal import *
class Tiger(Animal):

    def __init__(self, name, age):
        super().__init__(name,age,"Hishnik",["Miaso"], 25,"RRRRRRRRRRRRRRRRRRRRRR!!!!!!!!!")

    def bite(self):
        print(self.Name,"sdelal kus")