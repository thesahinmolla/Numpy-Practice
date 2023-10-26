#Print without truncation
import numpy as np
import sys
x = np.arange(10000)

print('Before setting print options : ')
print(x) 

a = np.set_printoptions(threshold = sys.maxsize)

print('\nAfter setting print options : ')
print(a)