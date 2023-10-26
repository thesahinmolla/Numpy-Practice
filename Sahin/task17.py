#Numpy with precision
import numpy as np

a = np.random.random(15)

print('Original Array:')
print(a)

print('\nAfter setting presicion to 5')
np.set_printoptions(precision = 5)
print(a)
print("\nanother one with precision 2")
# resetting precision to default (8)
np.set_printoptions(precision = 2)
print(a)