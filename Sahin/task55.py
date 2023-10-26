#Get min of axis = 0
import numpy as np

a = np.arange(9).reshape(3,3)
print(a)

min = np.min(a , axis=0)
print(f"The min is {min}")