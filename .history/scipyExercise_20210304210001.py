import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
from PIL import Image
Hx = [[1,0,-1],[2,0,-2],[1,0,-1]]
Hy = [[1,2,1],[0,0,0],[-1,-2,-1]]
image = Image.open("lena.png").convert("LA")
ImageArr = np.array(image)
grayImageArr = ImageArr.mean(axis=1)
Gx = convolve2d(grayImageArr,Hx)
Gy = convolve2d(grayImageArr,Hy)
plt.imshow(np.sqrt(Gx.dot(Gy) + Gy.dot(Gy)))
plt.show()