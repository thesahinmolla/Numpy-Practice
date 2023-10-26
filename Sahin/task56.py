#Calculate 90th percentile of an axis
import numpy as np

a = np.arange(12).reshape(4,3)
print(f"a is : \n{a}")

per = np.percentile(a, 90, 0)
print(f"90th percentile of an axis is : \n{per}")