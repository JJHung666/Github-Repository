# Name: Justin Lin
# Date: 9/27/2018
# Discription:
# Sources: Zhi 

import random as r 
import math

w = int(input("input the width please ")) + 2
h = int(input("input the height please ")) + 2

bomb_count = 0


grid_size = [[0]*w for x in range(h)]
for x in range(1,len(grid_size)-1):
	for y in range(1, len(grid_size)-3):
		b = r.randint(1,h-2)
		c = r.randint(1,w-2)
		grid_size[b][c] = "æ"

		if grid_size[(b-1)][(c-1)] != "æ":
			grid_size[(b-1)][(c-1)] += 1
		elif grid_size[(b-1)][(c)] != "æ":
			grid_size[(b-1)][(c)] += 1
		elif grid_size[(b-1)][(c+1)] != "æ":
			grid_size[(b-1)][(c+1)] += 1
		elif grid_size[(b)][(c+1)] != "æ":
			grid_size[(b)][(c+1)] += 1
		elif grid_size[(b)][(c-1)] != "æ":
			grid_size[(b)][(c-1)] += 1
		elif grid_size[(b+1)][(c-1)] != "æ":
			grid_size[(b+1)][(c-1)] += 1
		elif grid_size[(b+1)][(c)] != "æ":
			grid_size[(b+1)][(c)] += 1
		elif grid_size[(b+1)][(c+1)] != "æ":
			grid_size[(b+1)][(c+1)] += 1



for x in range(1,len(grid_size)-1):
	for y in range (1, len(grid_size[0])-1):
		if grid_size[x][y] == "æ":
			bomb_count += 1
		print(grid_size[x][y],end=" ")
	print("")

print("there are", bomb_count, "bombs")