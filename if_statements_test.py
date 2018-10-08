w = 5
h = 4

grid_size = [[0]*w for x in range(h)]

for x in range(1,len(grid_size)-1):
	for y in range (1, len(grid_size[0])-1):
		if grid_size[x][y]==0:
			print("hi")
		else:
			print("no")
