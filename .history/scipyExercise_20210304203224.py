import numpy as np
import matplotlib as plt
from scipy.signal import convolve2d
from PIL import Image
Hx = [[1,0,-1],[2,0,-2],[1,0,-1]]
Hy = [[1,2,1],[0,0,0],[-1,-2,-1]]
grayImage = Image.open("lena.png").convert('LA')
grayImageArr = np.array(grayImage)
Gx = convolve2d(grayImageArr,Hx)
