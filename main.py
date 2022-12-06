from Penguin import *
from Tiger import *
from Elephant import *
from jail import *


E1=Elephant("Oleg",17)
t1=Tiger("Dmitiy",2)
v1=Jail(100,"savanna",1)
p1=Penguin("Gosha",3)

v1.addPrisoners(E1)
v1.addPrisoners(t1)
v1.addPrisoners(p1)

print(v1.prisoners)