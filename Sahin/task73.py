# Find the union
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print(f"Array 1 is \n{arr1}")

arr2 = np.array([3, 4, 5, 6, 7])
print(f"Array 2 is \n{arr2}")

print(f"Union of 2 array is : \n{np.union1d(arr1, arr2)}")
