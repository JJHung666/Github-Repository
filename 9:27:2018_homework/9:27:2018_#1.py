# Name: Justin Lin
# Date: 9/27/2018
# Description: Generate  a  list  of  10  random  numbers  between  0  and  100.  Get  them  in order  from  largest  to  smallest,  removing  numbers  divisible  by  3.  (Ms.  Healey)
# Source: none

import sys
import math
import random as r


n = []
count = 0

while len(n) < 10:
	n.append(count)
	count = r.randint(0, 100)
	while count%3 ==  0:
		count = r.randint(0, 100)

print (n,len(n))
