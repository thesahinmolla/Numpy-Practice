#Numpy Where
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
filtered_arr = arr[np.where(arr % 2 != 0)]

print(filtered_arr)
