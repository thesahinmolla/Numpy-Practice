#Numpy where with multiple conditions
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

#Even
even = arr[np.where(arr % 2 == 0)]
print(f"Filtering even number\n {even}")

#Odd
odd = arr[np.where(arr % 2 != 0)]
print(f"Filtering odd number\n {odd}")
