#Flipping the numpy array using slices
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# using slices
f_arr = arr[::-1, ::-1]

print("Original Array:")
print(arr)

print("\nFlipped Array (both vertical and horizontal):")
print(f_arr)
