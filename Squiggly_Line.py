# Name: Justin Lin
# Date: 10/15/2018
# Description: 
# Source(s): 

from PIL import Image as i
import random

img_sizex = 512
img_sizey = 512
n = int(input("amount of lines you want "))
imag = i.new("RGB", (img_sizex, img_sizey))
f = 0
xpos = []


for x in range(1, n-1):
	f = random.randint(0, img_sizex)
	for y in range(0, img_sizey):
		xpos = [f for i in range(0,n)]
		r = random.randint(-1,1)
		imag.putpixel((xpos[x]+r,y),(x+y, y*2, x*y))


imag.save("Squiggly.png", "PNG")