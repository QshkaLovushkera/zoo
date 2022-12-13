from Penguin import *
from Tiger import *
from Elephant import *
from jail import *


E1=Elephant("Олег",17)
t1=Tiger("Дмитрий",2)
v1=Jail(100,"саванна",1)
p1=Penguin("Гоша",3)

v1.addPrisoners(E1)
v1.addPrisoners(t1)
v1.addPrisoners(p1)
print(v1.prisoners)
v1.addFood("листики", 100)
print(v1.feeder)
v1.feedAllAnimals()
print(v1.isAllPrisonersNotHunger)
print(v1.feeder)
