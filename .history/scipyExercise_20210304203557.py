import numpy as np
import matplotlib as plt
from scipy.signal import convolve2d
from PIL import Image
Hx = [[1,0,-1],[2,0,-2],[1,0,-1]]
Hy = [[1,2,1],[0,0,0],[-1,-2,-1]]
Image = Image.open("lena.png")
ImageArr = np.array(Image)
grayImage = ImageArr.mean(axis=2)
Gx = convolve2d(garyImageArr,Hx)
Gy = convolve2d(garyImageArr,Hy)
print(Gx)