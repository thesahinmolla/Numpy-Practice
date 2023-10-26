#Flip a numpy array by using flipud without sharing the memory
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

f_arr = np.flipud(arr.copy())

print("Original Array:")
print(arr)

print("\nFlipped Array:")
print(f_arr)
