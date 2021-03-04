import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
from PIL import Image
import math as math
Hx = [[1,0,-1],[2,0,-2],[1,0,-1]]
Hy = [[1,2,1],[0,0,0],[-1,-2,-1]]
grayimage = Image.open("lena.png").convert("LA")
#grayImageArr = np.array(image)
#grayImageArr = ImageArr.mean(axis=2)
Gx = convolve2d(grayImage,Hx)
Gy = convolve2d(grayImageArr,Hy)
plt.imshow(np.sqrt(Gx.dot(Gy) + Gy.dot(Gy)))
plt.show()