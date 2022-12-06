class Jail:

    def __init__(self,square,biom,number):
        self._prisoners = []
        self._listOfTipesOfAnimals = ["Tiger","Penguin","Elephant"]
        self._maxSquare = square
        self._square=0
        self._biom = biom
        self.__listOfBioms = ["pustina","jungli","antarktika","savanna","taiga",]
        self._number = number

    @property
    def Biom(self):
        return self._biom

    @Biom.setter
    def Biom(self,newBiom):
        if type(newBiom) is str:
            if newBiom in self._listOfBioms:
                self._biom = newBiom
            else:
                print("Нельзя создать такой биом")
        else:
            print("Биом должен являться типом str")

    @property
    def prisoners(self):
        return self._prisoners

    @property
    def square(self):
        return self._maxSquare

    @square.setter
    def square(self,value):
        if type(value) is int:
            self._maxSquare+=value
        else:
            print("Новое значение площади должно быть числом")

    def addPrisoners(self,newBedolaga):
        if newBedolaga._Biom == self._biom:
            if newBedolaga._Square+self._square<=self._maxSquare:
                if newBedolaga._whoIsAnimal in self._listOfTipesOfAnimals:
                    f=0
                    if newBedolaga.Type=="Hishnik":
                        for i in self._prisoners:
                            if i._whoIsAnimal!=newBedolaga._whoIsAnimal:
                                f = 1
                                break
                        if f == 0:
                            self._prisoners.append(newBedolaga)
                        else:
                            print("Нельзя сажать хищников вместе с другими животными")
                    else:
                        for i in self._prisoners:
                            if i.Type!=newBedolaga._Type:
                                f = 1
                                break
                        if f == 0:
                            self._prisoners.append(newBedolaga)
                        else:
                            print("Травоядных нельзя сажать вметсе с хищниками")
                else:
                    print("Нельзя сажать таких животных")
            else:
                print("Нет места для нового животного")
        else:
            print("Это животное не может жить в данном биоме")







