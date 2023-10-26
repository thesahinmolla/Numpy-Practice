#Repeat an array
import numpy as np

a = np.array([[1, 2, 3]])
print('Before : ')
print(a)

b = np.repeat(a, 5, axis=0)
print('\nAfter : ')
print(b)