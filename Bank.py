# Name: Justin Lin
# Date: 10/25/2018
# Description: Classes ----> Bank accounts
# Source(s):

# Properties
#---------------
# number of the account
# balance
# interest rate
# password
	# security questions
	# Pin
# savings checkings
#---------------

# methods
#---------------
# checkBalance
# Deposit
# Withdraw
# Transfer
# Login/Logout
#---------------


class Bank_Account():
	def __init__(self, interest_rate, a_name, name):
		import random as r
		used = []
		self.balance = 0
		pin_num = r.randrange(1000000000000000, 10000000000000000)
		s_pin = r.randrange(100,1000)
		used.append(pin_num)
		used.append(s_pin)
		if pin_num not in used:
			self.pin_number = pin_num
			self.security_pin = s_pin
		self.type_account = "checkings"
		self.interest = 0.02
		self.account_name = a_name
		self.owner = name

	def checkBalance():
		return "Name:", +self.name+"\nBalance"+str(self.balance)

	def deposit():

	def withdrawal():

	def Transfer():

	def log_in/out():
