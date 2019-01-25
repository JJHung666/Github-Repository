# Sympy_Test

from sympy import *
from sympy.geometry import *

x = Point(0,0)
y = Point(1,1)
z = Point(4,4)
w = Point(-1, 2)
print(Point.is_collinear(x,y,z))
print(Point.is_collinear(x,y,w))
