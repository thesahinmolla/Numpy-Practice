#Find the nearest element in the array
import numpy as np

a = np.arange(10, 60, 7)
print(a)

b = int(input("Enter a number"))
c = a.flat[np.abs(a - b).argmin()]
print(f'Elemenet near by {b} : {c}')