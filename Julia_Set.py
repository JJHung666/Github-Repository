# Name: Justin Lin
# Date: 10/17/2018
# Description: Julia
# Source(s): 

from PIL import Image as i
import random as r

xa, xb = -1.5, 1.5
ya, yb = -1.5, 1.5

img_sizex = 1000
img_sizey = 1000


pixeled = []

maxtries = 256

image = i.new("RGB", (img_sizex, img_sizex))

for y in range(img_sizey):
	yz = y * (yb-ya)/(img_sizey-1) + ya
	for x in range(img_sizex):
		xz = x * (xb-xa)/(img_sizex-1) + xa
		z = complex(xz, yz)
		c = complex( -0.334,0.626)
		for i in range(maxtries):
			if abs(z) >= 2.0:
				break
			z = z**2 + c
		r = i
		g = i
		b = i
		if i < 200:
			image.putpixel((x,y),(r, g, b))
		else:
			image.putpixel((x,y), (x//3,y//3,(x*y)//7))
		
image.show("Julia", "PNG")
image.save("Julia.png", "PNG")