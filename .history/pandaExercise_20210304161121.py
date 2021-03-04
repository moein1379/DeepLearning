import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def q2(n):
    x = np.random.randn(n)
    y = np.random.randn(n)
    color = []
    for i in range(n):
        if(1<x[i]<3 and 1<y[i]<3):
            color.append(1)
        if(3<x[i]<5 and 3<y[i]<5):
            color.append(1)
        if
    plt.scatter(x,y,c=logic_res)
    plt.show()
q2(100)