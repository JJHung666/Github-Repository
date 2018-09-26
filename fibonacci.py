f = int(input("type in the number you want to know for the fibonacci sequence"))

def c(f):
#	for x in range(f):
	if f == 1:
		return 0
	elif f == 2:
		return 1
	else:
		return c(f-1)+c(f-2)
res = c(f)
print(res)