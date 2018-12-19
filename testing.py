import sympy as sp
import sympy.geometry as gm

a = gm.Point(1, 1)
b = gm.Point(2, 1)
z = gm.Point(2, 2)
t = gm.Triangle(a,b,z)
print(t.area)