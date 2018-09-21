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

	if m = 1 and d >= 20 and m = 2 and d <= 18:
		print("\n\nHmmm \nAn aquarius, I see the progress")
#6,7
	elif m = 2 and d >= 19 and m = 3 and d <= 20:
		print("\n\nHmmm \n,Pisces huh. Interesting")
#1,4
	elif m = 3 and d >= 21 and m = 4 and d <= 19:
		print("\n\nDaring \nAn Aries, I see possiblities")
#2	
	elif m = 4 and d >= 20 and m = 5 and d <= 20:
		print("\n\nHmmm \nA Taurus, how strong and loyal")	
#5
	elif m = 5 and d >= 21 and m = 6 and d <= 21:
		print("\n\nAhh \nA Gemini, quite the Cheerful one aren't you")
#3	
	elif m = 6 and d >= 22 and m = 7 and d <= 22:
		print("\n\nHow Ironic \nA Cancer, insecure and unpredictable")
#1,4
	elif m = 7 and d >= 23 and m = 8 and d <= 22:
		print("\n\nWow! \nA Leo, fiery and majestic")
#7
	elif m = 8 and d >= 23 and m = 9 and d <= 22:
		print("\n\nHmmm \nA Virgo, diligent aren't you")
#3
	elif m = 9 and d >= 23 and m = 10 and d <= 23:
		print("\n\nAhh \nA Libra, quite charming")
#5
	elif m = 10 and d >= 24 and m = 11 and d <= 21:
		print("\n\nHmmm \nAn Scorpio, mysterious")	
#2
	elif m = 11 and d >= 22 and m = 12 and d <= 21:
		print("\n\nHmmm \nA Sagitarius, courage and generous")
#4
	elif m = 12 and d >= 22 and m = 1 and d <= 19:
		print("\n\nHmmm \na Capricorn, Determined like my creator it seems.")
#6
	cfortune()

def nfortune():
	print("That is a shame")
	res = input("would you like to know the fortune of someone else").lower()
	if res = yes:
		afortune()
	else:
		print("Then this is where we part.")
def cfortune():


fortune()