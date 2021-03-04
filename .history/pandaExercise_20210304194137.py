import numpy as np
import matplotlib.pyplot as plt
x1 = np.random.randn(1000)
x2 = np.random.randn(1000)
x1Squar = x1**2
x2Squar = x2**2
x1INx2 = x1*x2
dict = {"x1" : x1,"x2":x2,"x1^2" : x1Squar,"x2^2":x2Squar,"x1*x2":x1INx2}
df = pd.DataFrame{dict}