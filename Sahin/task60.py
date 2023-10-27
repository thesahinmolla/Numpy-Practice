#Cross correlation
import numpy as np

x = np.array([1, 0, 2])
y = np.array([3, 4, 1])
print('x:')
print(x)
print('\ny:')
print(y)

print('\nnp.corrcoef(x, y): ')
print(np.corrcoef(x, y))