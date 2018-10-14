# Name: Justin Lin
# Date: 10/14/2018
# Description: 
# Source(s): 

from PIL import Image as i
import random

img_sizex = 512
img_sizey = 512

imag = i.new("RGB", (img_sizex, img_sizey))

count = img_sizey/2
counts = 10



for x in range(int(count/5)):
	for y in range(int(img_sizey)):
		imag.putpixel((int(y/2),x*5),(25,130,100))
		imag.putpixel((x*10,y),(255,0,0))
for x in range(30,70):
	for y in range(30,70):
		imag.putpixel((x, y),(0,255,0))
for x in range(120,140):
	for y in range(120,140):
		imag.putpixel((x, y),(0,255,255))
for x in range(60,80):
	for y in range(120,140):
		imag.putpixel((x, y),(185,185,185))
for x in range(60,70):
	for y in range(60,80):
		imag.putpixel((x*2, y),(175,105,175))
while counts > 0:
	for x in range(random.randint(0,512)):
		for y in range(random.randint(0,512)):
			imag.putpixel((x, y),(x,y,(x-y)))
	counts -= 1


imag.save("HW_image.png", "PNG")