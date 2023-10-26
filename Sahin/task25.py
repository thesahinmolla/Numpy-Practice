#Flip a numpy array by using flipud
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Fliping the array using np.flipud
f_arr = np.flipud(arr)

print("Original Array:")
print(arr)

print("\nFlipped Array:")
print(f_arr)
