import numpy as np
from datetime import datetime
result2 = 0
final
def vectorProduct(vector1,vector2):
    result1 = 0
    for i,j in zip(vector1,vector2):
        result1+=i*j
    return result1
matrixA = np.random.random((100,100))
matrixB = np.random.random((100,100))
for rowA,rowB in zip(matrixA,matrixB.T):
    result2+=vectorProduct(rowA,rowB)
print(result2)