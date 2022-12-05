class Animal:

    def __init__(self, name, age, type, foodType, hungerNorm, sound):
        self.Name = name
        self.__Age = age
        self.__Type = type
        self.__Food = foodType
        self.__HungerLevel=0
        self.__HungerNorm=hungerNorm
        self.__Sound=sound

    def eat(self,food,mass):
        if type(food) is str:
            if food in self.__Food:
                if type(mass) is int:
                    if mass>0:
                        self.__HungerLevel+=mass
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
                self.__Age = value
            else:
                print("Vozrast doljen bit bolshe 0")
        else:
            print("Vozrast doljen bit cifroi")

    def play(self):
        print(self.__Name," : poigral")
