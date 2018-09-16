# date: 9/15/2018
# description: this is a program that will tell you your grade depending on the number you input
# sources:

import sys

x = float(sys.argv[1])

if x>5 or x<=0:
	print("your number is not within the range of the the grades")
if x>0 and x<1:
	print("your grade is a F")
if x>=1 and x<1.5:
	print("your grade is a D-")
if x>=1.5 and x<2:
	print("your grade is a D")
if x>=2 and x<2.5:
	print("your grade is a D+")
if x>=2.5 and x<2.85:
	print("your grade is a C-")
if x>=2.85 and x<3.2:
	print("your grade is a C")
if x>=3.2 and x<3.5:
	print("your grade is a C+")
if x>=3.5 and x<3.85:
	print("your grade is a B-")
if x>=3.85 and x<4.2:
	print("your grade is a B")
if x>4.2 and x<4.5:
	print("your grade is a B+")
if x>=4.5 and x<4.7:
	print("your grade is a A-")
if x>=4.7 and x<4.85:
	print("your grade is a A")
if x>=4.85 and x<=5:
	print("your grade is a A+")