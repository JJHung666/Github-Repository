# Name: Justin Lin
# Date: 10/17/2018
# Description: Mandlebrot
# Source(s): 

from PIL import Image as i
import random as r

img_sizex = 3

image = i.new("RGB", (img_sizex, img_sizex))
n = img_sizex


def Mandlebrot(z, c, n):
	
	z(0) = 0

	z(1) = c

	z(2) = z(1)**2 + c

	z(n+1) = z(n)**2+c

	xy = z(n) 
	absoluteZ == sqrt((x**2)+(y**2))

#imag.putpixel( (x, y),(255 ,0 ,0 ) )


def z(n)
	for x in range(img_sizex):
		for y in range(img_sizex):

			c == (-2 + ((2/(img_sizex//2))*x), -2 + ((2/(img_sizex//2))*y))

			# while z < img_sizex:

			z(n+1) = z(n)**2 + c
	Mandlebrot(z, c, n)



# Mandlebrot(a, a, a)

image.save("Mandlebrot.png", "PNG")




