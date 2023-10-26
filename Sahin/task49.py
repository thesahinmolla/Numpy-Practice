#Get specific element
import numpy as np

a = np.arange(9).reshape(3,3)
print(a)
print(f"specific number at (0,2) is {a[0,2]}")

b = np.arange(27).reshape(3,3,3)
print(b)
print(f"specific number at (2,1,2) is {b[2,1,2]}")