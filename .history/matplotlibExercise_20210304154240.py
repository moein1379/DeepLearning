import numpy as np
x = np.random.randn(100)
y = np.random.randn(100)
logic_res = []
for i in range(100):
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
        logic_res.append()
    