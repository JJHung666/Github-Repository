# Name: Justin Lin
# Date: 10/17/2018
# Description: Mandlebrot
# Source(s): 

from PIL import Image as i

xa, xb = -1.0, 0.0
ya, yb = -1.0, 0.0

img_sizex = 1000
img_sizey = 1000

maxtries = 256 #because there are 255 color shades

image = i.new("RGB", (img_sizex, img_sizex))

for y in range(img_sizey):
	yc = y * (yb-ya)/(img_sizey-1) + ya
	cy = -2 + ((2/(img_sizey//2))*y)
	for x in range(img_sizex):
		cx = -2 + ((2/(img_sizex//2))*x)
		xc = x * (xb-xa)/(img_sizex-1) + xa
		c = complex(xc, yc)
		# c = complex(cx, cy)
		z = 0
		for i in range(maxtries):
			if abs(z) >= 2.0:
				break
			z = z**2 + c

		r = 256//i
		g = i//255
		b = i

		image.putpixel((x,y),(r,g,b))

image.show("Mandlebrot_inclass.png", "PNG")
# image.save("Mandlebrot_inclass.png", "PNG")