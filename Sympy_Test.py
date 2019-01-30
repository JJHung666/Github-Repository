from sympy import *
from sympy.geometry import *
x = Point(0,0) 
y = Point(1,1) 
z = Point(3,0) 
w = Point(0, 0.5)
t = Polygon(w,x,y,z)
print(Polygon(w,x,y,z).area)