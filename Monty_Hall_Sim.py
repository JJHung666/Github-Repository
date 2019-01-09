# Name: Justin Lin -- Title of simulation: Monty Hall Problem
# Date: 1/9/2019
# opinion: I have already heard of the monty hall problem before, so I know that the correct answer is to switch your choice, since you lower your chances by 33% if you don't switch. I try to imagine 1 million doors instead of 3 doors with the same rules.
# Source: none
import random as r

choices = input("choose between 1 through 3 ")
choice = int(choices)
a = 0
b = 0

for x in range(1000):
	car = r.randint(1,3)
	sheep = 0
	while True:
		sheep = r.randint(1,3)
		if sheep != choice and sheep != car:
			break
	
	if choice != car:
		a += 1
	else:
		b += 1
print(str(a)+" cars if you switched.")
print(str(b)+ "cars if you stayed true to your gut.")