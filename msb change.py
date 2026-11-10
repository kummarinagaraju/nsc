from PIL import Image
import numpy as np
img = Image.open("me.png").convert("RGB")
pixels = img.load()
a=img.convert("L")
matrix=np.array(a)
print("Image matrix is:",matrix)
for y in range(img.height):
    for x in range(img.width):
        r, g, b = pixels[x, y]
        r = r^128
        pixels[x, y] = (r, g, b)
matrix1=matrix^128
print("Image matrix after msb bit changed:",matrix1)
img.save("msb_modified.bmp")
img.show()
print("MSB modification completed")