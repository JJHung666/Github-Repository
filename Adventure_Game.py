# Name: Justin Lin -- Title of game:
# Date: 9/18/2018
# Description: 
# Source: CPU-club--->Jerry Wang

import sys
import math
import random

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
	gender = input("what is your gender")
	print("\n\nplease input the birth date and today's date.")
	y = float(input("year of birth "))
	m = float(input("month "))
	d = float(input("day "))
	year = float(input("current year "))
	month = float(input("current month "))
	day = float(input("today "))

	if m = 1 and d >= 20 or m = 2 and d <= 18:
		print("\n\nHmmm \nAn aquarius, I see")

	y0  =  y  -  (14  -  m)  //  12 
	x  =  y0  +  y0//4  -  y0//100  +  y0//400
	m0  =  m  +  12  *  ((14  -  m)  /  12)  -  2
	d0  =  (d  +  x  +  (31*m0)//  12)  %  7 
#	print(int(d0))

def nfortune():
	print("That is a shame")
	res = input("would you like to know the fortune of someone else").lower()
	if res = yes:
		afortune()
	else:
		print("Then this is where we part.")

fortune()