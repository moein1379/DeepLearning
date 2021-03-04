import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def q2(n):
    x = np.random.randn(n)
    y = np.random.randn(n)
    color = []
    for i in range(n):
        if(-1<=x[i]<=1 and -1<=y[i]<=1):
            color.append(1)
        #if((1<x[i]<2 and 1<y[i]<2) and (-2<x[i]<-1 and -2<y[i]<-1)):
        else:
            color.append(0)
        
    plt.scatter(x,y,c=color)
    plt.show()
