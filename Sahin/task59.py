#Pearson product-moment correlation
import numpy as np

a = np.array([0, 1, 3])
b = np.array([2, 4, 5])
print('x:')
print(a)
print('\ny:')
print(b)

print('\nnp.corrcoef(x, y): ')
print(np.corrcoef(a, b))
