# Name: Justin Lin
# Date: 10/24/2018
# Source(s): None
	
def mandlebrot_1():
	from PIL import Image as i
	xa, xb = -0.3111, -0.2790
	ya, yb = -0.6723, -0.6402

	img_sizex = 1000
	img_sizey = 1000 

	maxtries = 256
	b = 0
	c = 0

	image = i.new("RGB", (img_sizex, img_sizex))

	for y in range(img_sizey):
		yc = y * (yb-ya)/(img_sizey-1) + ya
		for x in range(img_sizex):
			xc = x * (xb-xa)/(img_sizex-1) + xa
			c = complex(xc, yc)
			z = 0
			for i in range(maxtries):
				if abs(z) >= 2.0:
					break
				z = z**2 + c

			r = 256-i
			b = i+256
			if b >= 256:
				b = b - i
			g = 256-i
			image.putpixel((x,y),(r, g, b))
			if i < 100:
				image.putpixel((x,y), (x,y,x-y))
	image.show("Mandlebrot_1", "PNG")
	image.save("Mandlebrot_1.png", "PNG")

def mandlebrot_2():
	from PIL import Image as i
	xa, xb = -0.9084, -0.9103
	ya, yb = 0.2396, 0.2415

	img_sizex = 1000
	img_sizey = 1000 

	maxtries = 256
	b = 0
	c = 0

	image = i.new("RGB", (img_sizex, img_sizex))

	for y in range(img_sizey):
		yc = y * (yb-ya)/(img_sizey-1) + ya
		for x in range(img_sizex):
			xc = x * (xb-xa)/(img_sizex-1) + xa
			c = complex(xc, yc)
			z = 0
			for i in range(maxtries):
				if abs(z) >= 2.0:
					break
				z = z**2 + c

			r = i
			b = 256-i
			g = 256-i
			image.putpixel((x,y),(r, g, b))
			if i < 150:
				image.putpixel((x,y), (y,x,y-x))
	image.show("Mandlebrot_2", "PNG")
	image.save("Mandlebrot_2.png", "PNG")

def julia():
	from PIL import Image as i
	import random as r

	xa, xb = -1.5, 1.5
	ya, yb = -1.5, 1.5

	img_sizex = 1000
	img_sizey = 1000

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

mandlebrot_1()

mandlebrot_2()

julia()