from Animal import *
class Tiger(Animal):

    def __init__(self, name, age):
        super().__init__(name,age,"Хищник",["Мясо"], 25, 50,"РРРРРРРРРРРРРРРРРР!!!!!!!!!")
        self._whoIsAnimal = "Тигр"
        self._Biom = "саванна"
        self._Square = 20

    def bite(self):
        print(self._Name,"сделал кусь")