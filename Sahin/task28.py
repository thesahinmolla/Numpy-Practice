#Flip a numpy array by using flip (both horizontally and vertically)
import numpy as np

# Create a sample NumPy array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# upside down without
f_arr = np.flipud(arr.copy())

print("Original Array:")
print(arr)

print("\nFlipped Array(Vartical):")
print(f_arr)

# Horizontal
f_arr = np.fliplr(arr.copy())

print("\nFlipped Array(Horizontal):")
print(f_arr)
