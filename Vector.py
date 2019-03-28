# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 13:34:55 2019

@author: batuhan
"""

from math import hypot

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def __repr__(self):     # str olarak döndürmek için, print edebilmek için
        return "Vector(%r, %r)" %(self.x, self.y) # __str__ ile __repr__ arasındaki fark nedir
    
    def __abs__(self):      # 2 vektörün magnitutesini almak
        return hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, skaler):
        return Vector(self.x * skaler, self.y * skaler)
    
v1 = Vector(3, 5)
v2 = Vector(1, 2)
v3 = Vector(5, 2)
v4 = Vector(8, 10)

x = v1 + v2
x2 = abs(x)
x3 = bool(x)

print(x, x2, x3)
