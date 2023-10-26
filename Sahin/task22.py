#Numpy Inverse
import numpy as np

a = np.array([[2,3],[4,5]])
print('Before Inverse : ')
print(a)

b = np.linalg.inv(a)
print('After Inverse : ')
print(b)