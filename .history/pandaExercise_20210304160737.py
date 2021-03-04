import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def q2(n):
    x = np.random.randn(n)
    y = np.random.randn(n)
    logic_res = []
    for i in range(n):
        X1 = 0
        X2 = 0
        if x[i] <= 0:
            X1 = 0
        else:
            X1 = 1
        if y[i] <= 0:
            X2 = 0
        else:
            X2 = 1
        if(X1+X2 == 2 or X1+X2==0):
            logic_res.append(0)
        else:
            logic_res.append(1)
    plt.scatter(x,y,c)
    plt.show()
q2(100)