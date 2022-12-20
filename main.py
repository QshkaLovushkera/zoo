from Penguin import *
from Tiger import *
from Elephant import *
from jail import *
from Zoo import *


E1=Elephant("Олег",17)
t1=Tiger("Дмитрий",2)
v1=Jail(100,"саванна",1)
p1=Penguin("Гоша",3)

z1 = Zoo("Одинцово", 500)

v1.addPrisoners(E1)

z1.addJail(v1)

print(z1._Jails)
z1.addFoodToJails("листики", 100)
print(v1.prisoners)
print(v1.feeder)
v1.feedAllAnimals()
print(v1.isAllPrisonersNotHunger)
print(v1.feeder)

z1.removeJail(1)

print(z1._Jails)

