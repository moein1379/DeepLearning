import numpy as np
import matplotlib as plt
from scipy.signal import convolve2d
from PIL import Image
Hx = [[1,0,-1],[2,0,-2],[1,0,-1]]
Hy = [[1,2,1],[0,0,0],[-1,-2,-1]]
Image = Image.open("lena.png")
ImageArr = np.array(Image)
Gx = convolve2d(ImageArr,Hx)
Gy = convolve2d(ImageArr,Hy)
print(Gx)
