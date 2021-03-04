import numpy as np
import matplotlib as plt
from scipy.signal import convolve2d
from PIL import Image
import math as math
Hx = [[1,0,-1],[2,0,-2],[1,0,-1]]
Hy = [[1,2,1],[0,0,0],[-1,-2,-1]]
Image = Image.open("lena.png")
ImageArr = np.array(Image)
grayImageArr = ImageArr.mean(axis=2)
Gx = convolve2d(grayImageArr,Hx)
Gy = convolve2d(grayImageArr,Hy)
print(Gx.dot)
