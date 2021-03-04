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

print(finalMatrix)
print(matrixA.dot(matrixB))