#List to numpy array
import numpy as np

a = [1,2,3,4,5]
print(f"{a} is a {type(a)}")

b = np.array(a)
print(f"{b} is a {type(b)}")