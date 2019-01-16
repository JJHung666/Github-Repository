# Name: Justin Lin -- Title of simulation: excess holiday calories
# Date: 1/11/2019
# Description:
# Source: none
import random as r
from collections import Counter
import matplotlib.pyplot as mat

def desert_eating(parties):
	c=0
	for x in range(parties):
		servings = r.randint(1,30)
		for y in range(servings):
			calories = r.randint(50,500)
			c += calories
	return c

desert_calories = []
for x in range(1000000):
	parties = r.randint(0,8)
	desert_calories.append(desert_eating(parties))

results = sorted(Counter(desert_calories).items())
a = []
b = []
for tuples in results:
	a.append(tuples[0])
	b.append(tuples[1])
mat.plot(a,b)
mat.show()