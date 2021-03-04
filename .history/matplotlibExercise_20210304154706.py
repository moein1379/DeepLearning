import numpy as np
import matplotlib.pyplot as plt
def q2(x):
    x = np.random.randn(x)
    y = np.random.randn(x)
    logic_res = []
    for i in range(x):
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
    plt.scatter(x,y,c=logic_res)
    plt.show()
q2(100000)