from PIL import Image
import numpy as np

img = Image.open("me.png").convert("RGB")
pixels = img.load()
print("matrix of image befor modification")
mat1=np.array(img)
print(mat1)
for y in range(img.height):
    for x in range(img.width):
        r, g, b = pixels[x, y]
        r = r & 254
        pixels[x, y] = (r, g, b)
print("after modify img matrix")
mat2=np.array(img)
print(mat2)
img.save("lsb_modified.bmp")
img.show()
print("LSB modification completed")
