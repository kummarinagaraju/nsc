
from PIL import Image
import numpy as np
img = Image.open("me.png").convert("RGB")
matrix=np.array(img)
print("Image matrix is:",matrix)


