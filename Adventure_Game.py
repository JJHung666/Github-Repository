# Name: Justin Lin -- Title of game:
# Date: 9/18/2018
# Description: 
# Source: CPU-club--->Jerry Wang

import sys
import math
import random
import datetime


y = 0
m = 0
d = 0
now = datetime.datetime.now()
y1 = int(now.year)
m1 = int(now.month)
d1 = int(now.day)


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
	gender = input("what is your gender ")
	print("\n\nplease input the birth date and today's date.")
	y = int(input("year of birth "))
	m = int(input("month "))
	d = int(input("day "))
	

	if m >= 1 and d >= 20 and m <= 2 and d <= 18:
		print("\n\nHmmm \nAn aquarius, I see the progress")
#6,7 day
	elif m >= 2 and d >= 19 and m <= 3 and d <= 20:
		print("\n\nHmmm \n,Pisces huh. Interesting")
#1,4 day
	elif m >= 3 and d >= 21 and m <= 4 and d <= 19:
		print("\n\nDaring \nAn Aries, I see possiblities")
#2 day
	elif m >= 4 and d >= 20 and m <= 5 and d <= 20:
		print("\n\nHmmm \nA Taurus, how strong and loyal")	
#5 day
	elif m >= 5 and d >= 21 and m <= 6 and d <= 21:
		print("\n\nAhh \nA Gemini, quite the Cheerful one aren't you")
#3 day
	elif m >= 6 and d >= 22 and m <= 7 and d <= 22:
		print("\n\nHow Ironic \nA Cancer, insecure and unpredictable")
#1,4 day
	elif m >= 7 and d >= 23 and m <= 8 and d <= 22:
		print("\n\nWow! \nA Leo, fiery and majestic")
#7 day
	elif m >= 8 and d >= 23 and m <= 9 and d <= 22:
		print("\n\nHmmm \nA Virgo, diligent aren't you")
#3 day
	elif m >= 9 and d >= 23 and m <= 10 and d <= 23:
		print("\n\nAhh \nA Libra, quite charming")
#5 day
	elif m >= 10 and d >= 24 and m <= 11 and d <= 21:
		print("\n\nHmmm \nAn Scorpio, mysterious")	
#2 day
	elif m >= 11 and d >= 22 and m <= 12 and d <= 21:
		print("\n\nHmmm \nA Sagitarius, courage and generous")
#4 day
	elif m >= 12 and d >= 22 and m <= 1 and d <= 19:
		print("\n\nHmmm \na Capricorn, Determined like my creator it seems.")
#6 day
	
	cfortune()

def nfortune():
	print("That is a shame")
	res = ("would you like to know the fortune of someone else. Yes or No ").lower()
	if res == yes:
		afortune()
	else:
		print("Then this is where we part.")
def cfortune():
	y0  =  y  -  (14  -  m)  //  12 
	x  =  y0  +  y0//4  -  y0//100  +  y0//400
	m0  =  m  +  12  *  ((14  -  m)  /  12)  -  2
	d0  =  (d  +  x  +  (31*m0)//  12)  %  7 

	y2  =  y1  -  (14  -  m1)  //  12 
	x  =  y2  +  y2//4  -  y2//100  +  y2//400
	m2  =  m1  +  12  *  ((14  -  m1)  /  12)  -  2
	d2  =  (d1  +  x  +  (31*m2)//  12)  %  7 

	d3 = abs(d0-d2)
	print(int(d3))

fortune()