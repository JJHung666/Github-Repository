import random as r
import math as m

Celsius = float(input("Please enter degrees in Celsius "))
Fahrenheit = Celsius*1.8 + 32
print("The temp for fahrenheit is:",str(Fahrenheit))

F = float(input("Please enter degrees in fahrenheit "))
C = (Fahrenheit - 32) / 1.8
print("The temp for celsius is:",str(C))

theta = r.random()*m.pi*2
trigResult = m.sin(theta)**2 + m.cos(theta)**2
print(trigResult)