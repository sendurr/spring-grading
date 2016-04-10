'''Question 1: Make a function class.'''

from math import *

class F:
    def __init__(self, a, w):
        self.a = a
        self.w = w

    def value(self, x):
        a = self.a
        w = self.w
        return exp(-a * x) * sin(w * x)

from math import *
f = F(a=1.0, w=0.1)
print f.value(x=pi)
f.a = 2
print f.value(pi)