#Numpy where with multiple conditions - apply only on matching conditions
import numpy as np

a = np.arange(10).reshape((2, 5))
print('Before : ')
print(a)

print('\nAfter : ')
b = np.where((a > 3) & (a < 6), 999, a)
print(b)