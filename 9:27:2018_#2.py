# Name: Justin Lin
# Date: 9/27/2018
# Description: Generate  a  random  list  of  6  multiples  of  13  that  are  within  270  and  do not  have  any  number  with  the  digit  6  (Eric,  Tilden,  Ethan)
# Source: Oleh

import sys
import math
import random

def check_function (number):
	result = 0
	str_number = str(number)
	for i in range(len(str_number)):
		if str_number[i] == 6:
			result = result+1
	return result

a = []
number = 0
r = random.randrange(20)

#for b in range(0,6,1):
#	a = []
#	a.append(b)



while len(a) < 6:

	number = random.randint(0, 20)*13
	if check_function(number) == 0:
		a.append(number)

print(a, len(a))

