# Name: Justin Lin
# Date: 11/12/2018
# Description: Image Filter
# Source(s): (https://www.youtube.com/watch?v=6Qs3wObeWwc&t=811s), 

from PIL import Image as i
import colorsys as c
import sys
# l = i.open(sys.argv[1])

# l.save('image1.png', "PNG")

# size_x_y = (2048, 1536)
fn = sys.argv[1]
for x in range(len(fn)):
	if fn[x] == '.':
		if fn[x+1] == 'j' or fn[x+1] == 'p':
			file_name = fn[:x] + 'filtered'
# l.thumbnail(size_x_y)


# # l.save('im/{}.png'.format(file_name, "png"))
# l.save("Image.png", "png")

# img_sizex = 700
# img_sizey = 989
# img_sizex = 678
# img_sizey = 960
# img_sizex = 2048
# img_sizey = 1536

H = i.open(sys.argv[1])
img_sizex, img_sizey = H.size

recorded_color1 = [[(255,255,255) for x in range(img_sizex)] for y in range(img_sizey)]
recorded_color2 = [[(255,255,255) for x in range(img_sizex)] for y in range(img_sizey)]
recorded_color3 = [[(255,255,255) for x in range(img_sizex)] for y in range(img_sizey)]
recorded_color4 = [[(255,255,255) for x in range(img_sizex)] for y in range(img_sizey)]

def dark1():
	for x in range(img_sizex):
		a = 0
		r,g,b = 255,255,255
		if x <= img_sizey-1:
			recorded_color1[x][x] = ((0,0,0))
		while a < img_sizex:
			y = x+a
			y1 = x-a
			if y < img_sizey:
				recorded_color1[y][x] = ((0,0,0))

			if y1 >= 0 and y1 < img_sizey:
				recorded_color1[y1][x] = ((0,0,0))
			a += 5

def dark2():
	for x in range(img_sizex):
		a = 0
		r,g,b = 255,255,255
		if x <= img_sizey-1:
			recorded_color2[x][x] = ((0,0,0))
		while a < img_sizex:
			y = x+a
			y1 = x-a
			x1 = x-3
			if y < img_sizey:
				recorded_color2[y][x] = ((0,0,0))

			if y1 >= 0 and y1 < img_sizey:
				recorded_color2[y1][x] = ((0,0,0))

			if x1 >= 0 and y < img_sizey:
				recorded_color2[y][x1] = ((0,0,0))

			if x1 >= 0 and y1 >= 0 and y1 < img_sizey:
				recorded_color2[y1][x1] = ((0,0,0))

			a += 5

def dark3():
	for x in range(img_sizex):
		a = 0
		r,g,b = 255,255,255
		if x <= img_sizey-1:
			recorded_color3[x][x] = ((0,0,0))
		while a < img_sizex:
			y = x+a
			y1 = x-a
			x1 = x-3
			if y < img_sizey:
				recorded_color3[y][x] = ((0,0,0))
				d = img_sizex-(x+1)
				# y = d+a
				recorded_color3[y][d] = ((0,0,0))

			if y1 >= 0 and y1 < img_sizey:
				recorded_color3[y1][x] = ((0,0,0))
				d = img_sizex-(x+1)
				recorded_color3[y1][d] = ((0,0,0))
			a += 5


def dark4():
	for x in range(img_sizex):
		a = 0
		r,g,b = 255,255,255
		if x <= img_sizey-1:
			recorded_color4[x][x] = ((0,0,0))
		while a < img_sizex:
			y = x+a
			y1 = x-a
			x1 = x-3
			if y < img_sizey:
				recorded_color4[y][x] = ((0,0,0))
				d = img_sizex-(x+1)
				recorded_color4[y][d] = ((0,0,0))
			
			if y1 >= 0 and y1 < img_sizey:
				recorded_color4[y1][x] = ((0,0,0))
				d = img_sizex-(x+1)
				recorded_color4[y1][d] = ((0,0,0))

			if x1 >= 0 and y < img_sizey:
				recorded_color4[y][x1] = ((0,0,0))
				e = img_sizex-(x1+1)
				recorded_color4[y][e] = ((0,0,0))

			if x1 >= 0 and y1 >= 0 and y1 < img_sizey:
				recorded_color4[y1][x1] = ((0,0,0))
				e = img_sizex-(x1+1)
				recorded_color4[y1][e] = ((0,0,0))
			a += 5

			
dark1()
dark2()
dark3()
dark4()


for x in range(img_sizex):
	for y in range(img_sizey):
		r,g,b = H.getpixel((x,y))
		average_rgb = ((r+g+b)//3)
		if average_rgb <= 51:
			H.putpixel((x,y),(r,g,b))
		elif average_rgb > 51 and average_rgb <= 102 and recorded_color4[y][x] == ((0,0,0)):
			H.putpixel((x,y),((r,g,b)))
		elif average_rgb > 102 and average_rgb <= 153 and recorded_color3[y][x] == ((0,0,0)):
			H.putpixel((x,y),((r,g,b)))
		elif average_rgb > 153 and average_rgb <= 204 and recorded_color2[y][x] == ((0,0,0)):
			H.putpixel((x,y),((r,g,b)))
		elif average_rgb > 204 and average_rgb <= 255 and recorded_color1[y][x] == ((0,0,0)):
			H.putpixel((x,y),((r,g,b)))
		else:
			H.putpixel((x,y),(255,255,255))
	print(x)

H.show("x", "PNG")
H.save(file_name+'.png', "png")