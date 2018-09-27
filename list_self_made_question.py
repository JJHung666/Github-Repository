import random as r
b = []
c = []
for x in range(1,101):
	x *= r.randrange(2,11,1)
	b.append(x)
	c.append(x**2)
print(b, len(b))
print(c, len(c))