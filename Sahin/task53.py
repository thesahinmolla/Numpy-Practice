#Using amin function
import numpy as np

x = np.arange(10).reshape((2, 5))
print('x:')
print(x)

print('\nnp.amin(x, 1) : ')
print(np.amin(x, 1))