#Numpy compare with nonzero count
import numpy as np

a = np.arange(12).reshape((3, 4))
print('Before : ')
print(a)

print(a % 3 == 1)
print(np.count_nonzero(a % 3 == 1))