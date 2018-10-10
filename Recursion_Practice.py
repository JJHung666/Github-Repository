# Given a string, compute recursively (no loops) the 
# number of lowercase 'x' chars in the string.

# countX("xxhixx") → 4
# countX("xhixhix") → 3
# countX("hi") → 0

a = input("type any amount of x with words in between ")
x = len(a)
y = 0

	

def countX(a):
	global x
	if "x" not in a:
		return 0
	if "x"  in (a[0], (a[x-1])):
		y += 1




print(y)
print(countX(a))