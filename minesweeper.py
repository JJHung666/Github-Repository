# Name: Justin Lin
# Date: 9/27/2018
# Discription:
# Sources: Zhi 

import random as r 
import math

w = int(input("input the width please "))
h = int(input("input the height please "))

grid_size = [[0]*w for x in range(h)]
for x in range(len(grid_size)):
	b = r.randint(0,h-1)
	c = r.randint(0,w-1)
	grid_size[b][c] = "æ"

bomb_count = 0

for x in range(h):
	for y in range(w): #zhi explained what a nested for loop does to me
		if grid_size[x-1][y-1] == "æ":
			bomb_count += 1
			height = x-1
			width = y -1
			grid_size[(height-1)][(width-1)] = "1"
			grid_size[(height-1)][(width)] = "1"
			grid_size[(height-1)][(width+1)] = "1"
			grid_size[(height)][(width+1)] = "1"
			grid_size[(height)][(width-1)] = "1"
			grid_size[(height+1)][(width-1)] = "1"
			grid_size[(height+1)][(width)] = "1"
			grid_size[(height+1)][(width+1)] = "1"




for x in range(len(grid_size)):
	print(*grid_size[x])

print("there are", bomb_count, "bombs")