# Trying to inverse a singular matrix
import numpy as np

a = np.array([[2,3],[4,6]])

try:
    np.linalg.inv(a)
except Exception as err:
    print('Error : ', err)
    