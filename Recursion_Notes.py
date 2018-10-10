# Factorials
# 1 != 1 -> 1 ----- Base Cases
# 2 != 2 -> 1*2
# 3 != 6 -> 1*2*3
# 4 != 24 -> 1*2*3*4
# 5 != 120 -> 1*2*3*4*5
# 6 != 720 -> 1*2*3*4*5*6
n=0
n = int(input("find factorial of number "))
def factorial(n):
	if n is 0 or n is 1:
		return 1

	return n*factorial(n-1)

print(factorial(n))


f = int(input("type in the number you want to know for the fibonacci sequence "))
def c(f):
	if f is 0 or f is 1 or f is 2:
		return f

	return c(f-1)+c(f-2)

print(c(f))


# c(f-1)+c(f-2)



