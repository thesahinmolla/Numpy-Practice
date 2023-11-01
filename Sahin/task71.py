# Find the diff
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 5, 6, 7])


setdiff = np.setdiff1d(arr1, arr2)

print("diff :", setdiff)