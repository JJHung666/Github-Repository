# Name: Justin Lin -- Title of game: Constellation fortune
# Date: 9/18/2018
# Description: This is a fortune teller game, that will tell you if you're lucky today based on your birthdate and gender
# Source: none

import sys
import math
import random
import datetime

a = 0
y = 0
m = 0
d = 0
now = datetime.datetime.now()
y1 = int(now.year)
m1 = int(now.month)
d1 = int(now.day)
d2 = 0
d3 = 0
h = 0
ho = 0


def fortune():
	response = input("\n\nSalutations, my precious customer!!! This is a fortune teller game. would you like to know what your fortune is today? \n\n\nYes or No? ").lower()
	if response == "yes":
		afortune()
	elif response == "no":
		nfortune()
	else:
		print("you must type yes or no. Please try again.")
		fortune()
def afortune():
	global y
	global m
	global d
	global y1
	global m1
	global d1
	global a
	global h
	global ho
	gender = input("what gender, or other ").lower()
	print("\n\nplease input the birthdate.")
	y = int(input("\nyear of birth "))
	m = int(input("month "))
	d = int(input("day "))
	
	if gender == "male":
		a = int(1)
	elif gender == "female":
		a = int(-1)
	elif gender == "other":
		a = int(0)
	else:
		print("please type either male, female or other")


	if m == 1:
		d == d
	elif m == 2:
		d = d + 31
	elif m == 3:
		d = d + 59
	elif m == 4:
		d = d + 90
	elif m == 5:
		d = d + 120
	elif m == 6:
		d = d + 151
	elif m == 7:
		d = d + 181
	elif m == 8:
		d = d + 212
	elif m == 9:
		d = d + 243
	elif m == 10:
		d = d + 273
	elif m == 11:
		d = d + 304
	elif m == 12:
		d = d + 334
	

	if m >= 1 and d >= 20 and m <= 2 and d <= 49:
		print("\n\nHmmm \nAn aquarius, I see the progress")
		h = 6
		ho = 7
	elif m >= 2 and d >= 50 and m <= 3 and d <= 79:
		print("\n\nHmmm \nPisces huh. Interesting")
		ho = 1
		h = 4
	elif m >= 3 and d >= 80 and m <= 4 and d <= 109:
		print("\n\nDaring \nAn Aries, I see possiblities")
		h = 2
	elif m >= 4 and d >= 110 and m <= 5 and d <= 140:
		print("\n\nHmmm \nA Taurus, how strong and loyal")	
		h = 5
	elif m >= 5 and d >= 141 and m <= 6 and d <= 172:
		print("\n\nAhh \nA Gemini, quite the Cheerful one aren't you")
		h = 3
	elif m >= 6 and d >= 173 and m <= 7 and d <= 203:
		print("\n\nHow Ironic \nA Cancer, insecure and unpredictable")
		h = 1
		ho = 4
	elif m >= 7 and d >= 204 and m <= 8 and d <= 234:
		print("\n\nWow! \nA Leo, fiery and majestic")
		h = 7
	elif m >= 8 and d >= 235 and m <= 9 and d <= 265:
		print("\n\nHmmm \nA Virgo, diligent aren't you")
		h = 3
	elif m >= 9 and d >= 266 and m <= 10 and d <= 296:
		print("\n\nAhh \nA Libra, quite charming")
		h = 5
	elif m >= 10 and d >= 297 and m <= 11 and d <= 325:
		print("\n\nHmmm \nAn Scorpio, mysterious")	
		h = 2
	elif m >= 11 and d >= 326 and m <= 12 and d <= 355:
		print("\n\nHmmm \nA Sagitarius, courage and generous")
		h = 4
	elif m >= 12 and d >= 356:
		print("\n\nHmmm \na Capricorn, Determined like my creator it seems.")
		h = 6
	elif m == 1 and d <= 19:
		print("\n\nHmmm \na Capricorn, Determined like my creator it seems.")
		h = 6
	
	cfortune()

def nfortune():
	print("That is a shame")
	res = input("would you like to know the fortune of someone else. Yes or No ").lower()
	if res == "yes":
		afortune()
	else:
		print("Then this is where we part.")
def cfortune():
	global y
	global m
	global d
	global y1
	global m1
	global d1
	global a

	if m == 1:
		d == d
	elif m == 2:
		d = d - 31
	elif m == 3:
		d = d - 59
	elif m == 4:
		d = d - 90
	elif m == 5:
		d = d - 120
	elif m == 6:
		d = d - 151
	elif m == 7:
		d = d - 181
	elif m == 8:
		d = d - 212
	elif m == 9:
		d = d - 243
	elif m == 10:
		d = d - 273
	elif m == 11:
		d = d - 304
	elif m == 12:
		d = d - 334

	y0  =  y  -  (14  -  m)  //  12 
	x  =  y0  +  y0//4  -  y0//100  +  y0//400
	m0  =  m  +  12  *  ((14  -  m)  /  12)  -  2
	d0  =  (d  +  x  +  (31*m0)//  12)  %  7 

	y2  =  y1  -  (14  -  m1)  //  12 
	x  =  y2  +  y2//4  -  y2//100  +  y2//400
	m2  =  m1  +  12  *  ((14  -  m1)  /  12)  -  2
	d2  =  (d1  +  x  +  (31*m2)//  12)  %  7 

	d3 = abs((d2+d0)-a)//2
#	print(int(d3))
	if d3 == h or d3 == ho:
		print("\n\nit is your lucky day")
	else:
		print("\n\nlooks like today isn't your lucky day")





#	while True:
#		try:
#			if d3 < 1 or d3 > 13:
#				d3 += 1
			#elif d3 == h:
			#	pass
#				break
#		except ValueError:
#			pass



fortune()