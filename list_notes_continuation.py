# empty list
a = []

# add 2 to our list?
a += [2]
a.append(4)
a.append(7)
a.append(1)
a.append(3)
a = [2,1,2,3,4,5] + a
print(a)

# updates value
a[4] = 7

# print the list
print(a)

# removing from the list
del a[1:5] # the fifth digit is not deleted
# del a[5] is only deleting the fifth digit
# del a[5:] del everything after five
# del a[:5] del everything before five


print(a)

print(a.pop()) # it just switches the places of the last number
print(a)

a.remove(2) # it only deletes the first 2 --- first matching occurence
print(a)

print(a[3])
print(a[len(a)-1]) # or just type this --> print(a[-1]) a[-1]=last digit on the list
# a[-2] gives you the second last number/value on the list
# this counts from backwards


# how to swap values on different spots on the list

#a.replace(a[3],a[5]) -- failure

# c = a, a = b, b = c

c,b = 1,5
c,b = b,c
print(c,b)

# same works for list

a[3],a[4]=a[4],a[3]
print(a)

for seven in range(100):
	b = []
	seven *= 7
	b.append(seven)
print(b, len(b))


# ms. healey's way
sevens = []
count = 0
while count < 700:
	sevens.append(count)
	count += 7
print (sevens,len(sevens))

# way #2
sevenss = []
for x in range(0,700,7):
	sevenss.append(x)
print (sevenss, len(sevenss))

# way #3
seve = [x for x in range(0,700,7)]
print(seve, len(seve))

