# Name: Justin Lin -- Title of simulation: random dart simulation
# Date: 1/10/2019
# Description:
# Source: (https://www.palisade.com/risk/monte_carlo_simulation.asp)

# Question number 1: respond to the following question (from class) in comments at the top of a new coding project: What is the longest walk you can take where you'll be within walking distance of home at least 50% of the time?

# Answer #1: My program resulted in 15 step (16-17 steps rarely), however, the answer the video showed was 22 steps, however this was because I made my program stop on the first number to drop under 50% instead of the last shown 50%

# Question number 2: briefly research Monte Carlo simulations. What are they? What can they be used for? How do they work? Answer these questions as best you can succinctly, also at the top of your coding project.

# Answer #2: The monte Carlos simulation is a computerized mathematical technique that computes a simulation multiple times with a different set of random values to reduce the risk and possible outcomes of a simulation. It can be used to calculate the probablity of different outcomes.

# Question number 3:imagine you are throwing darts at a square dartboard, which has a circle perfectly inscribed in the square. Let's say the location of the center of the dartboard is 0,0, and the side length of the square is 2, giving the circle a radius of 1. Keep track of the number of times that your dart lands within the circle in 100 tries. Now, multiply that number by 4, and divide by the number of darts you threw. What value do you get? Repeat the simulation, but with 1000 darts... and 10,000 darts... and 100,000 darts. What do you notice about the output?

# Answer #3: Code below

import random as r

def Random_Dart_Throws(n):
	a,b = (0, 0) #the middle of the dartboard
	inc, outc = (0,0) # inc means the amount of times hit inside the dartboard circle, and outc means the amount of times hit outside the dartboard circle
	for x in range(n):
		a += r.uniform(-1,1) #the random positions of where it can be hit.
		b += r.uniform(-1,1)
		if abs(a) <= 1 and abs(b) <= 1:  # this statement checks whether the random number is inside or outside of the dartboard circle
			inc += 1
		else:
			outc += 1

	return inc, outc 

a,b = Random_Dart_Throws(1000)
c,d = Random_Dart_Throws(10000)
e,f = Random_Dart_Throws(100000)

print((a*4)/1000)
print((c*4)/10000)
print((e*4)/100000)