from numpy.random import choice
import time as t
from random import randint

class Dummy_bee():

    def travelling(self):
        t.sleep(randint(0,10))
        
    def cross_beam(self, choices):
        return choice(choices)        
        
    def participate(self, choices):
        self.travelling()
        self.cross_beam(choices)
