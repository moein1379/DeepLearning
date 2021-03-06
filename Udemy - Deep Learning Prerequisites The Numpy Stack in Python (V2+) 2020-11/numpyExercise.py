import numpy as np
from datetime import date, datetime
def q1(x):
    matrixA = np.random.random((x,x))
    matrixB = np.random.random((x,x))
    t0 = datetime.now()
    res = [[0 for x in range(len(matrixB[0]))] for y in range(len(matrixA))] 
    for i in range(len(matrixA)): 
        for j in range(len(matrixB[0])): 
            for k in range(len(matrixB)):
                res[i][j] += matrixA[i][k] * matrixB[k][j]  
    dt1 = datetime.now() - t0
    t0 = datetime.now()
    matrixA.dot(matrixB)
    dt2 = datetime.now()-t0
    print(dt1.total_seconds()," | ",dt2.total_seconds())
for i in range(50,200):
    q1(i)
