#Find median
import numpy as np

a = np.arange(9).reshape(3,3)
print(a)

med = np.median(a)
print(f"The median is {med}")