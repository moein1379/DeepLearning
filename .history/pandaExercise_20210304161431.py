import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def q2(n):
    x = np.random.randn(n)
    y = np.random.randn(n)
    color = []
    for i in range(n):
        if(0<x[i]<1 and 0<y[i]<1):
            color.append(1)
        if(3<x[i]<5 and 3<y[i]<5):
            color.append(0)
    plt.scatter(x,y,c=color)
    plt.show()
q2(100)