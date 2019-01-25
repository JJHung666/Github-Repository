# Sympy_Test

from sympy import *
a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
e = (a*b + 2*a*b)**(c**2)
print(e)

x,y,z = symbols('x,y,z')
print(x,y,z)
