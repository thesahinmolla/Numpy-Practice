#Swap rows
import numpy as np
a = np.arange(4).reshape(2, 2)
print('Before : ')
print(a)

a[[0,1]] = a[[1, 0]]

print('\nAfter : ')
print(a)