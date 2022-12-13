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
                        print("Масса еды должна быть положительной")
                else:
                    print("Масса еды должна быть написана числом")
            else:
                print("Этого животного нельзя кормить этим")
        else:
            print("Тип еды должен быть написан буквами")

    @property
    def Age(self):
        return self._Age

    @Age.setter
    def Age(self,value):
        if type(value) is int:
            if value>0:
                self._Age = value
            else:
                print("Возраст должен быть положительным")
        else:
            print("Возраст должен быть написан цифрой")

    @property
    def Type(self):
        return self._Type

    def play(self):
        print(self._Name," : поиграл")
