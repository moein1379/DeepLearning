import numpy as np
from datetime import datetime
matrixA = np.random.random((100,100))
matrixB = np.random.random((100,100))
t0 = datetime.now()
res = [[0 for x in range(len(matrixB[0]))] for y in range(len(matrixA))] 
for i in range(len(matrixA)): 
    for j in range(len(matrixB[0])): 
        for k in range(len(matrixB)):
            res[i][j] += matrixA[i][k] * matrixB[k][j] 
print (res)
t1 = datetime.now - 
print(matrixA.dot(matrixB))