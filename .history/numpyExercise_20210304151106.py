import numpy as np
from datetime import datetime
finalMatrix = [][]
def vectorProduct(vector1,vector2):
    result1 = 0
    for i,j in zip(vector1,vector2):
        result1+=i*j
    return result1
matrixA = np.random.random((100,100))
matrixB = np.random.random((100,100))
for rowA,rowB in zip(matrixA,matrixB.T):
    finalMatrix.append(vectorProduct(rowA,rowB))
for i in range(len(matrix1)): 
    for j in range(len(matrix2[0])): 
        for k in range(len(matrix2)): 
  
            # resulted matrix 
            res[i][j] += matrix1[i][k] * matrix2[k][j] 
  
print (res)
print(finalMatrix)
print(matrixA.dot(matrixB))