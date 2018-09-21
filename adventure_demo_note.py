import sys
import math as m
import random as r


# \n ---> backslash N is just hitting enter basically
def start():
	response = input("\n\n\n\nGreetings young hero! \nYou are looking for treasure. Your map says that the treasure can be found northerly. However, your friend says he heard someone talking about treasure in the south. \n\nDo you 1) Trust your friend, or 2) trust the Map?")
	if response == "1":
		friend()
	elif response == "2":
		map()
	else:
		print("you must type 1 or 2. Please try again.")
		start()
#		response = str(r.randrange(3))

def map():
	routeM = input("You have correctly chosen the path to your next journey. Your map now brings you to the doorway of the dungeon. \n\n\n1) call your 'friend' \nor \n2)go in alone")
	if routeM == "1":
		Jfriend()
	elif routeM == "2":
		beater()
	else:
		print("you must type 1 or 2. Please try again.")
		map()
def Jfriend():
	pass

def beater():
	pass

def friend():
	routef = input("You have chosen the incorrect path to your next journey. Your friend now brings you to the doorway of the dungeon, and kills you out of jealousy. \n\n\n1) revive \nor \n2)become part of the dungeon")
	if routef == "1":
		revive()
	elif routef == "2":
		dungeon()
	else:
		print("you must type 1 or 2. Please try again.")
		friend()
def revive():
	pass
def dungeon():
	print("you lost.")
	res = input("there was a revive program for heroes, would you like to use revive to play again, Yes or No").lower()
	if res == "yes" or res == "Yes":
		start()
	else:
		exit() # quits program
def exit():
	pass
start()