from Penguin import *
from Tiger import *
from Elephant import *
from jail import *
from Zoo import *


E1=Elephant("Олег",17)
t1=Tiger("Дмитрий",2)
v1=Jail(100,"саванна",1)
p1=Penguin("Гоша",3)
E2 = Elephant("Григорий",19)

z1 = Zoo("Одинцово", 500)

v1.addPrisoner(E1)
v1.addPrisoner(E2)

z1.addJail(v1)

print(z1._Jails)

z1.addFoodToJails("листики", 75)
z1.addFoodToJails("сено", 75)

print(v1.feeder)

z1.feedAllAnimals()

print(v1.feeder)

