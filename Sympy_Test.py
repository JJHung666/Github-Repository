# pprint
import math as m
from sympy import *
# the numbers are printed differently
def sympy_printing_vs_normal_print():
    pprint(sqrt(8))
    print(sqrt(8))
    print(m.sqrt(8)) 

sympy_printing_vs_normal_print()
# this example is a function that shows the difference in symbolic and non symbolic math. It also shows the difference in printing.