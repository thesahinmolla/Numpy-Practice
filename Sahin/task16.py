#Reshape with -1 (lazy option)
import numpy as np

original_array = np.array([1, 2, 3, 4, 5, 6])

reshaped_array = original_array.reshape(2, 3)
print(reshaped_array)

# Reshape the array using -1
reshaped_lazy = original_array.reshape(3, -1)
print(reshaped_lazy)