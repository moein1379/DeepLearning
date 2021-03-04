import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
from PIL import Image
Hx = [[1,0,-1],[2,0,-2],[1,0,-1]]
Hy = [[1,2,1],[0,0,0],[-1,-2,-1]]
image = Image.open("lena.png")
ImageArr = np.array(image)
grayImageArr = ImageArr.mean(axis=2)
Gx = convolve2d(Hx,grayImageArr)
Gy = convolve2d(Hy,grayImageArr)
plt.imshow(np.sqrt(np.power(Gx,2) + np.power(Gy,2)))
plt.show()