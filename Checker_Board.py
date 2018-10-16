# Name: Justin Lin
# Date: 10/15/2018
# Description: 
# Source(s): 

from PIL import Image as i
import random

img_sizex = 512
img_sizey = 512
a = 10
limit = 8
z = [i for i in range(1, limit+2, 2)]
c = [h for h in range(0, limit+3, 2)]
imag = i.new("RGB", (img_sizex, img_sizey))



while a > 0:
	a -= 2
	b = a-1
	if a-1 < 0:
		b = 0
	for g in range(int(limit//2)):
		for x in range(b*(int(img_sizex/8)), a*(int(img_sizex/8))):
			for y in range(int(img_sizey/8)*int(c[g]), int(img_sizey/8)*int(z[g])):
				imag.putpixel((x,y),(255,0,0))
		for y in range(b*(int(img_sizex/8)), a*(int(img_sizex/8))):
			for x in range(int(img_sizey/8)*int(c[g]), int(img_sizey/8)*int(z[g])):
				imag.putpixel((x,y),(255,0,0))

imag.save("Checker_Board.png", "PNG")
