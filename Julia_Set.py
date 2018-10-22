# Name: Justin Lin
# Date: 10/17/2018
# Description: Julia set
# Source(s): googled what the julia set was

# For each pixel (x, y) on the screen, do:
import random as r
from PIL import Image as i

x = 0
y = 0

tries = 0
max_tries = 256

while (x*x + y*y < 4  and  tries < max_tries) 
    xtemp = zx*zx - zy*zy

    zy = 2*zx*zy  + cy 

    zx = xtemp + cx
    
    tries = tries + 1 
  
    if (tries == max_tries)
        return a = (0, 0, 0)
    else
        return tries
        for i in range(maxtries):
			if abs(z) >= 2.0:
				break
    r = 256//i
	g = i//255
	b = i



image.putpixel((x,y),(r,g,b))

image.show("Julia_Set.png", "PNG")