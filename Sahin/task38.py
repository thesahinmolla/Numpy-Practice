#Convert list to float numpy array
import numpy as np

a = [[1.2,2.3,3.4],[4.5,5.6,6.7]]
print(a)
print(type(a))

b = np.array(a)
print(b)
print(b.dtype)