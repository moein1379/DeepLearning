import numpy as np
import matplotlib as plt
import scipy as sy
from PIL import Image
Hx = [[1,0,-1],[2,0,-2],[1,0,-1]]
Hy = [[1,2,1],[0,0,0],[-1,-2,-1]]
image = Image.open("lena.png")
arr = 