import unittest
from Penguin import *
from Tiger import *
from Elephant import *
from jail import *
from Zoo import *

class Test_Jail(unittest.TestCase):

    def setUp(self):
        self.e1 = Elephant("Григорий",11)
        self.t1 = Elephant("Виктор", 4)
        self.p1 = Elephant("Шкипер", 2)
        self.e2 = Elephant("Борис", 11)
        self.t2 = Elephant("Дмитрий", 4)
        self.p2 = Elephant("Ковальски", 2)
        self.k =[self.e1,self.t1,self.p1,self.e2,self.t2,self.p2]
        self.v1 = Jail(100,"саванна",1)
        self.v2 = Jail(100, "саванна", 2)



if __name__ == "__main__":
    unittest.main()

