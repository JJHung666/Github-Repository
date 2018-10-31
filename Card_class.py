# Name: Justin Lin
# Date: 10/31/2018
# Description: Classes ----> Card
# Source(s): 

class Card():
	def __init__(self, value, suit):
		self.card = value
		self.suit = suit
	def c():
		return "card number"+str(self.card)+"\nsuit"+str(self.suit)

mydeck = []
for x in range(54):
	mydeck.append(x)
	suit = (x+1)%4
	if suit == 0:
		suit = 4
	mydeck[x] = Card(((x//4)+1), suit)
	print(mydeck[x].c)

# floor division + 1 = ceiling division

# class deck():
# 	def __init__(self):
# 		self.hearts
# 		self.diamonds
# 		self.spades
# 		self.clubs
# 		self.joker

# 	def shuffle(self):

# 	def deal(self): #order

# 	def choose(self): #random

# 	def add_card(self): # think of adding the card to a hand (new deck)

# 	def display(self):