# Find unique intersection
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 5, 6, 7])
arr3 = np.array([5, 3, 8, 9, 1])


unique_intersection = np.intersect1d(arr1, np.intersect1d(arr2, arr3))

print("Unique intersection:", unique_intersection)
