#Get unique elements
import numpy as np

arr = np.array([2, 3, 1, 2, 3, 4, 5, 4, 6, 5])
print(f"The array is :{arr}")

unique_elements = np.unique(arr)
print(f"Unique elements in the array are : {unique_elements}")
