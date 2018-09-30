# making a 2 dimentional list
i = [[1,2,3],[4,5,6],[7,8,9]]
i[1][0]
#[n for e in i for n in e]
print(i)

i = [0 for x in range(12)]
print(i)

j=[0]*12
print(j)

i = [[0]*10 for x in range(10)]
print(i)

x = 20

a = [[0]*20 for x in range(10)]

#how to make it more organized when printed

for x in range(len(a)):
	print(*a[x])