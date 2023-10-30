#Count the number of occurrences
import numpy as np

arr = np.array([1, 2, 3, 4, 2, 2, 3, 1, 5])
value_to_count = 2

occurrences = np.count_nonzero(arr == value_to_count)
print(f"The number of occurrences of {value_to_count} in the array is: {occurrences}")
