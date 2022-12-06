class Animal:

    def __init__(self, name, age, type, foodType, hungerNorm, sound):
        self._Name = name
        self._Age = age
        self._Type = type
        self._Food = foodType
        self._HungerLevel=0
        self._HungerNorm=hungerNorm
        self._Sound=sound
        self._Square=0

    def eat(self,food,mass):
        if type(food) is str:
            if food in self._Food:
                if type(mass) is int:
                    if mass>0:
                        self._HungerLevel+=mass
                    else:
                        print("Massa edi doljna bit bolshe 0")
                else:
                    print("Massa edi doljna bit chislom")
            else:
                print("Ia takoe ne em")
        else:
            print("Tip edi doljen bit bukvami")

    @property
    def Age(self):
        return self.__Age

    @Age.setter
    def Age(self,value):
        if type(value) is int:
            if value>0:
                self._Age = value
            else:
                print("Vozrast doljen bit bolshe 0")
        else:
            print("Vozrast doljen bit cifroi")

    @property
    def Type(self):
        return self._Type


    def play(self):
        print(self._Name," : poigral")
