#2D list to numpy array
import numpy as np

a = [[1,2,3],
     [4,5,6]]
print(a)
print(type(a))

b = np.array(a)
print(b)
print(b.dtype)