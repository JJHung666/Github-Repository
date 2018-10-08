# Name: Justin Lin
# Date: 9/27/2018
# Discription:
# Sources: Zhi 

import random as r 
import sys

w = int(input("input the width please ")) + 2
h = int(input("input the height please ")) + 2
bombs = int(input("input the amount of bombs please "))
f = 0
g = 0
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
			print((f+x, g+y))
			second[f+x][g+y] = grid_size[f+x][g+y]



# Zhi guided me through a lot of the code here
visited = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def inbounds(x,y):
	return x >= 1 and x <= w-1 and y >= 1 and y <= h-1

def visit(x,y):
	visited.append((x,y))
	for i in range(4):
		if inbounds(x+dx[i], y+dy[i]) and grid_size[x+dx[i]][y+dy[i]] == 0 and (x+dx[i], y+dy[i]) not in visited:
			visit(x+dx[i],y+dy[i])
		else:
			reveal9(x,y)


while 1:
	g = int(input("check for row "))
	f = int(input("check for column "))
	#j = int(input("check for row flagging"))
	#k = int(input("check for column flagging"))

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

	for x in range(1,len(second)-1):
		for y in range (1, len(second[0])-1):
			print(second[x][y],end=" ")
		print("")
