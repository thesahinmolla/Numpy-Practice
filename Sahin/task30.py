#Convert numpy array to list
import numpy as np

arr = np.array([1, 2, 3, ])
list = arr.tolist()

print("Array:")
print(arr)
print(type(arr))

print("List:")
print(list)
print(type(list))
