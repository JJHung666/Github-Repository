from sympy import *
def sympy_symbols():
    a = Symbol('a')
    b = Symbol('b')
    c = Symbol('c')
    e = (a*b + 2*a*b)**(c**2)
    pprint(e)
sympy_symbols()