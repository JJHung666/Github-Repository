# Name: Justin Lin -- Title of simulation: random walk simulation
# Date: 1/9/2019
# Description:
# Source: none
import random as r

trials = 1000
n = 10
percentage = 100
def walk_dis(n):
	a,b = (0, 0)
	for x in range(n):
		if r.randint(0,1) == 0:
			a += r.randrange(-1,2,2)
		else:
			b += r.randrange(-1,2,2)
	dis = (abs(a)+abs(b))

	return dis

while percentage >= 50:
	walk_home = 0
	for x in range(trials):	
		result = walk_dis(n)
		if result <= 4:
			walk_home += 1
		percentage = ((walk_home/trials)*100)
	print(percentage)
	n += 1
print(n-1)