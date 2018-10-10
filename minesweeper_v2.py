# Name: Justin Lin
# Date: 9/27/2018
# Discription:
# Sources: Zhi 

import random as r 
import sys


width = 0
height = 0
bombse = 0
bombs = 0


while True:
	try:
		width = int(input("input the width please "))
		height = int(input("input the height please "))
		bombse = int(input("input the amount of bombs please "))
		if width < 0 and height < 0 and bombse < 0:
			width = int(input("That ain't right. put a number for width "))
			height = int(input("That ain't right. put a number for height "))
			bombse = int(input("That ain't right. put a number for bombs "))
		elif width >= 1 and height >= 0 and bombs >=0:
			w = width + 2
			h = height + 2
			bombs = bombse
			break
	except ValueError:
		print("Yeah, thats not right. Please input a number with your number keys")

e = 0
Q = 0
z = 0

bomb_count = 0
bomb = []

grid_size = [[0]*w for x in range(h)]
second = [[0]*w for x in range(h)]
for x in range(bombs):
	b = r.randint(1,h-2)
	c = r.randint(1,w-2)
	while grid_size[b][c] is "æ":
		b = r.randint(1,h-2)
		c = r.randint(1,w-2)
	grid_size[b][c] = "æ"
	if grid_size[(b-1)][(c-1)] != "æ":
		grid_size[(b-1)][(c-1)] += 1

	if grid_size[(b-1)][(c)] != "æ":
		grid_size[(b-1)][(c)] += 1

	if grid_size[(b-1)][(c+1)] != "æ":
		grid_size[(b-1)][(c+1)] += 1

	if grid_size[(b)][(c+1)] != "æ":
		grid_size[(b)][(c+1)] += 1

	if grid_size[(b)][(c-1)] != "æ":
		grid_size[(b)][(c-1)] += 1

	if grid_size[(b+1)][(c-1)] != "æ":
		grid_size[(b+1)][(c-1)] += 1

	if grid_size[(b+1)][(c)] != "æ":
		grid_size[(b+1)][(c)] += 1

	if grid_size[(b+1)][(c+1)] != "æ":
		grid_size[(b+1)][(c+1)] += 1



for x in range(1,len(grid_size)-1):
	for y in range (1, len(grid_size[0])-1):
		second[x][y] = grid_size[x][y]
		if grid_size[x][y] == "æ":
			bomb_count += 1

		if second[x][y] == grid_size[x][y]:
			second[x][y] = "•"

		print(grid_size[x][y],end=" ")
	print("")
print("there are", bomb_count, "bombs")
# print(len(grid_size))
# print(len(grid_size[0]))#0 could be subbed for any number within the width

def reveal9(f,g): 
	for x in range(-1,2):
		for y in range(-1,2):
			#print((f+x, g+y))
			second[f+x][g+y] = grid_size[f+x][g+y]



# Zhi guided me through a lot of the code here
visited = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def inbounds(x,y):
	return y >= 1 and y <= w-2 and x >= 1 and x <= h-2

def visit(x,y):
	visited.append((x,y))
	for i in range(4):
		if inbounds(x+dx[i], y+dy[i]) and grid_size[x+dx[i]][y+dy[i]] == 0 and (x+dx[i], y+dy[i]) not in visited:
			visit(x+dx[i],y+dy[i])
		else:
			reveal9(x,y)
z = 1
flagging = 0
while z:
	m = int(input("type 1, for marking, 2 for flagging, 3 for deflagging, and type 4 for the game to check if you won "))
	if m == 1:
		g = int(input("mark for row "))
		f = int(input("mark for column "))
		if f <= height and g <= width:
			if grid_size[f][g] == "æ":
				print("Game Over")
				for x in range(1,len(grid_size)-1):
					for y in range (1, len(grid_size[0])-1):
						print(grid_size[x][y],end=" ")
					print("")
				break

			elif grid_size[f][g] >= 1:
				second[f][g] = grid_size[f][g]

			elif grid_size[f][g] == 0:
				second[f][g] = grid_size[f][g]
				visit(f, g)
		else:
			print("please input the right number")

			

	elif m == 3:
		k = int(input("flagging for row "))
		j = int(input("flagging for column ")) 
		if k <= height and j <= width:

			if second[j][k] == "!":
				second[j][k] = "•"
			else:
				pass
				


	elif m == 2:
		k = int(input("flagging for row "))
		j = int(input("flagging for column ")) 
		if k <= height and j <= width:
			if grid_size[j][k] == "æ":
				second[j][k] = "!"
			elif grid_size[j][k] >= 0:
				second[j][k] = "!"


		else:
			print("please input the right number")		
	

	for x in range(1,len(second)-1):
		for y in range (1, len(second[0])-1):
			if m == 4:
				if second[x][y] != "•":
					e += 1
				else:
					e = e
				if second[x][y] == "!":
					flagging += 1
				if flagging == bomb_count:
					z = 0
			print(second[x][y],end=" ")
		print("")

print("You win")


