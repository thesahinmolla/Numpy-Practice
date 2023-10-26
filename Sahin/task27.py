#Flip a numpy array by using fliplr (horizontally)
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

f_arr = np.fliplr(arr.copy())

print("Original Array:")
print(arr)

print("\nFlipped Array (without sharing memory):")
print(f_arr)
