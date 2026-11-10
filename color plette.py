from PIL import Image
width=500
height=100
image=Image.new("RGB",(width,height))
pixels=image.load()
for y in range(height):
    for x in range(width):
        r=x
        pixels[x,y]=(r,r,r)
image.save("color_palette.png")
image.show()
print("Color palette created and saved as color_palette.png")        