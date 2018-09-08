print("Hello, my master!")
username = input("what is your name? Please insert to the right. ")
print("Hello, master "+username+"!")
gender = input("are you a male or female? Insert male or female. ")
if gender == "male": 
	print("you have chosen to be a "+gender+"? excellent")
elif gender == "Male":
	print("you have chosen to be a "+gender+"? excellent")
elif gender == "female":
	print("you have chosen to be a "+gender+"? excellent")
elif gender == "Female":
	print("you have chosen to be a "+gender+"? excellent")
race = input("would you like to be a dragonslayer, mage, swordsmen, or healer. Please type in your choice. ")
if race == "dragonslayer":
	print("you are a "+gender+" "+race+"! superb!!! your abilities allow you to eat other's projectile attacks, and allow you to access dragon abilities.")
elif race == "mage":
	print("you are a "+gender+" "+race+"! exquisite!!! your abilities allow you to use mulitple destructive spells.")
elif race == "healer":
	print("you are a "+gender+" "+race+"! admirable!!! your abilities as the name implies allow you to heal. However there is a secret ability you can achieve in the future.")
elif race == "swordsmen":
	print("you are a "+gender+" "+race+"! splendid!!! your abilities are perfect for deafeating numerous amounts of enemies.")
