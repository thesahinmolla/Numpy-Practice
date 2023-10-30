#Shuffling by permutation
import numpy as np

a = np.arange(10)

print('a Before shuffling (using permutation:')
print(a)

print('\na After shuffling (using permutation:')
print(np.random.permutation(10))