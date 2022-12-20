class Zoo:

    def __init__(self,name, square):
        self._name = name
        self._square = square
        self._nowSquare = 0
        self._Jails = []


    def addSquare(self,value):
        if type(value) is int:
            if value>0:
                self._square += value
            else:
                print("Нельзя добавить неположительную площадь")
        else:
            print("Площадь должна быть цифрой")

    def addJail(self,jail):
        if jail._maxSquare + self._nowSquare<=self._square:
            self._Jails.append(jail)
        else:
            print("Новый вольер не помещается в зоопарк")

    def addFoodToJails(self, typeFood, value):
        if len(self._Jails)>0:
            if type(typeFood) is str:
                jailNeedThisFood = []
                for i in self._Jails:
                    if typeFood in i._feeder.keys():
                        jailNeedThisFood.append(i)
                if len(jailNeedThisFood)>0:
                    if type(value) is int:
                        if value>0:
                            for i in jailNeedThisFood:
                                i.addFood(typeFood, int(round(value/len(jailNeedThisFood), 0)))
                        else:
                            print("Количество еды должно быть положительным")
                    else:
                        print("Количество еды должно быть написано цифрой")
                else:
                    print("Такой тип еды не нужен ни одному из вольеров")
            else:
                print("Тип еды должен быть написан буквами")
        else:
            print("В зоопарке нет вольеров. Куда еду кидать собрался?")

    def removeJail(self, number):
        if type(number) is int:
            fl= True
            for i in self._Jails:
                if i._number == number:
                    self._Jails.remove(i)
                    fl = False
            if fl:
                print("В зоопарке нет вольера с таким номером")
        else:
            print("Номер вольера должен быть цифрой")