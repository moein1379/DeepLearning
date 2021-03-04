import numpy as np
from datetime import datetime
finalMatrix = []
def vectorProduct(vector1,vector2):
    result1 = 0
    for i,j in zip(vector1,vector2):
        result1+=i*j
    return result1
matrixA = np.random.random((100,100))
matrixB = np.random.random((100,100))
for rowA,rowB in zip(matrixA,matrixB.T):
    finalMatrix.append(vectorProduct(rowA,rowB))
print(finalMatrix)