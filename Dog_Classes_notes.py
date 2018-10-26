# Name: Justin Lin
# Date: 10/25/2018
# Description: Classes ----> Tamagotchi
# Source(s): 

# Properties
# #---------------
# stamina - energy
# Name - 
# hunger
# Height/Weight
# appearance
# happiness
# #----------
# Methods
# #--------------
# bark
# eat
# sleep
# play
# poop


class Dog: #the first letter of the class is better off being capitalized
	# Constructor is going to initialize all the properties of the dog
	def __init__(self, energy, names):
		self.stamina = energy
		self.hunger = 5
		self.weight = 30
		self.happiness = 5
		#this will make every constructed dog named Fido
		self.name = names


		# methods - functions ----> difference is that methods are in classes
	def eat(self): # the self in eat is from __init__
		status = ""
		if (self.hunger > 0):
			self.weight+= 1
			self.hunger-= 1
			self.stamina += 1
			self.happiness +=1
			status = self.name+" just ate."
			if self.weight > 40:
				self.happiness -= 3
				status += "\n for your info, this dog is unhappy because it's getting fat"
		else:
			status = "Nope, not eating. Not hungry."
		return status

	def play(self):
		current_status = ""
		if self.stamina >= 3:
			self.weight -= 1
			self.hunger += 1
			self.stamina -= 2
			self.happiness += 1
			current_status = self.name+" has finished playing"
			if self.happiness >= 10:
				happiness = 10
			if self.hunger >= 7:
				current_status += "\n your dog is getting very hungry"
		else:
			current_status = "your dog is almost too tired to do anything else"
		return current_status

	def death(self):
		autopsy = ""



	def status_report(self):
		# print("Name",self.name)
		# print("Hunger",self.hunger)
		# print("Stamina",self.stamina)
		# print("Hapiness",self.happiness)
		# print("Weight",self.weight)

		# or you could write it like this
		return "Name:"+self.name+"\nHunger:"+str(self.hunger)+"\nStamina:"+str(self.stamina)+"\nhappiness:"+str(self.happiness)+"\nweight:"+str(self.weight)



myDog = Dog(3, "Tim")
mySecondDog = Dog(8, "Annabelle")
print(myDog.eat()) #myDog was called earlier, that is why this works
print(myDog.eat())
print(myDog.eat())
print(myDog.eat())
print(myDog.eat())
print(myDog.play())
print(myDog.status_report())
