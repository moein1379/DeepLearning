import numpy as np
from datetime import datetime
matrixA = np.random.random((100,100))
matrixB = np.random.random((100,100))
res = [[0 for x in range(len(matrixB[0]))] for y in range(len(matrixA))] 
for i in range(len(matrixA)): 
    for j in range(len(matrixB[0])): 
        for k in range(len(matrixB)):
            res[i][j] += matrixA[i][k] * matrixB[k][j] 
print (res)
print(matrixA.dot(matrixB))