#List to numpy array with explicit dtype
import numpy as np

a = [0, 1, 2, 3, 4, 5]
print('Before : ')
print(a)
print(type(a))

print('\nAfter : ')
b = np.array(a)
print(b)
print(b.dtype)