#Argsort on Numpy array
import numpy as np


#sample NumPy array
arr = np.array([0,1,2,3,4,5])

# Ascending
sorted_arr = np.argsort(arr)
print("ascending order:", sorted_arr)

# Descending
sorted_arr_desc = np.argsort(arr)[::-1]
print("escending order:", sorted_arr_desc)
