# Name: Justin Lin -- Title of simulation: coin head count
# Date: 1/7/2019
# Description:
# Source: none
import random as r
import matplotlib.pyplot as mat 

stored = []
z = 0
for x in range(1000):
	for y in range(11):
		if r.randint(0,1) == 1:
			z += 1
	stored.append(z)
	z = 0
a = 0
num = []
for y in range(11):
	for x in range(len(stored)):
		if stored[x] == y:
			a += 1
	# num.append((a, y))
	num.append(a)
	a = 0
# print(num)
r = [x for x in range(11)]

# mat.plot(r, num)
mat.bar(r, num, color=(.6,.2,.4,1.0))
mat.ylabel("Number of Trials")
mat.xlabel("Number of Heads")
mat.show()