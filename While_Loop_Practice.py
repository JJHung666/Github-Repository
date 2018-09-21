while True:
	try:
		num = int(input("pick a number between 1 through 5 "))
		if num<1 or num>5:
			num = int(input("That ain't right. put a number between 1 through 5 please. "))
		else:
			print("success")
			break
	except ValueError:
		print("Yeah, thats not right. Please input a number with your number keys")


