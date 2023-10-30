#Shuffle
import numpy as np

a = np.arange(10)

print('a Before shuffling:')
print(a)

print('\na After shuffling:')
np.random.shuffle(a)
print(a)