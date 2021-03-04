import numpy as np
from datetime import datetime
result1 = 0
result2 = 0
def vectorProduct(vector1,vector2):
    for i,j in zip(vector1,vector2):
        result1+=i*j
    return result1
matrixA = np.random.random((100,100))
matrixB = np.random.random((100,100))
for rowA,rowB in zip(matrixA,matrixB.T):
    result2+=vect