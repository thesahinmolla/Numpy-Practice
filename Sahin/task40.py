#Find common values between two numpy array
import numpy as np

a = np.random.randint(0,25,17)
b = np.random.randint(0,25,17)
print(a)
print(b)

print(f"the common value is {np.intersect1d(a,b)}")