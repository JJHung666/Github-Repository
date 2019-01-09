# Name: Justin Lin -- Title of simulation: coin head count
# Date: 1/7/2019
# Description:
# Source: none
import random as r
stored = []
z = 0
for x in range(1000):
	for y in range(10):
		if r.randint(0,1) == 1:
			z += 1
	stored.append(z)
	z = 0
a = 0
num = []
for y in range(10):
	for x in range(len(stored)):
		if stored[x] == y:
			a += 1
	num.append((a, y))
	a = 0
print(num)