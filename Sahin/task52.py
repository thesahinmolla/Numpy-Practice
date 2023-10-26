#Get min of axis = 1
import numpy as np

a = np.arange(9).reshape(3,3)
print(a)

i = np.min(a,axis=1)
print(f"The min is {i}")