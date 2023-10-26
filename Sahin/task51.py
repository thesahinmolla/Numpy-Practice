#Min, Max, Sum
import numpy as np

a = np.arange(9).reshape(3,3)
print(a)

a += 1
print(a)

min = np.min(a)
print(f"The min is {min}")

max = np.max(a)
print(f"The max is {max}")

sum = np.sum(a)
print(f"The sum is {sum}")