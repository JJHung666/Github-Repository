from PIL import Image as i

imgx = 512
imgy = 512

imag = i.new("RGB", (imgx, imgy))

imag.putpixel((0,0),(255,0,0))

imag.save("demo_image.png", "PNG")