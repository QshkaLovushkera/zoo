class Jail:

    def __init__(self,square,biom,number):
        self._prisoners = []
        self._listOfTipesOfAnimals = ["Тигр","Пингвин","Слон"]
        self._maxSquare = square
        self._square=0
        self._biom = biom
        self.__listOfBioms = ["пустыня","джунгли","антарктика","саванна","тайга",]
        self._number = number
        self._feeder = {}

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

    @property
    def feeder(self):
        return self._feeder

    def addFood(self,typeOfFood,mass):
        if not (type(mass) is int):
            print("Масса должна быть числом")
        elif mass<=0:
            print("Масса должна быть положительной")
        elif not (type(typeOfFood) is str):
            print("Тип еды должен быть буквами")
        elif not(typeOfFood in self._feeder.keys()):
            print("Нельзя добавить такую еду")
        else:
            self._feeder[typeOfFood] += mass

    def howFeed(self,object):
        sumOfAvailibleFood = 0
        for i in object._Food:
            sumOfAvailibleFood += self._feeder[i]
        return sumOfAvailibleFood
    @property
    def isAllPrisonersNotHunger(self):
        flag=True
        for i in self._prisoners:
            flag=i.isFeed
        return flag

    def feedAllAnimals(self):
        for i in self._prisoners:
            if i._HungerNorm - i._HungerLevel < 0:
                print(i._Name, "не хочет есть")
            elif i._HungerNorm - i._HungerLevel>self.howFeed(i):
                print(i._Name,": недостаточно еды для кормёжки")
            else:
                k = i._HungerNorm - i._HungerLevel
                if i._HungerMax <= self.howFeed(i):
                    i._HungerLevel = i._HungerMax
                else:
                    i._HungerLevel = self.howFeed(i)
                i._HungerLevel += i._HungerMax
                for x in i._Food:
                    if self._feeder[x]>=k:
                        self._feeder[x] -= k
                        break
                    else:
                        k -= self._feeder[x]
                        self._feeder[x] -= k

    def addTypeFood(self, object):
        for i in object._Food:
            if i not in self._feeder.keys():
                a={i:0}
                self._feeder.update(a)

    def addPrisoners(self,newBedolaga):
        if newBedolaga._Biom == self._biom:
            if newBedolaga._Square+self._square<=self._maxSquare:
                if newBedolaga._whoIsAnimal in self._listOfTipesOfAnimals:
                    f=0
                    if newBedolaga.Type=="Хищник":
                        for i in self._prisoners:
                            if i._whoIsAnimal!=newBedolaga._whoIsAnimal:
                                f = 1
                                break
                        if f == 0:
                            self._prisoners.append(newBedolaga)
                            self.addTypeFood(newBedolaga)
                        else:
                            print("Нельзя сажать хищников вместе с другими животными")
                    else:
                        for i in self._prisoners:
                            if i.Type!=newBedolaga._Type:
                                f = 1
                                break
                        if f == 0:
                            self._prisoners.append(newBedolaga)
                            self.addTypeFood(newBedolaga)
                        else:
                            print("Травоядных нельзя сажать вметсе с хищниками")
                else:
                    print("Нельзя сажать таких животных")
            else:
                print("Нет места для нового животного")
        else:
            print("Это животное не может жить в данном биоме")







