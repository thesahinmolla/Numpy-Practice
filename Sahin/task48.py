#Shuffle
import numpy as np

a = np.arange(5)
print("Before:\n", a)

np.random.shuffle(a)
print("After:\n", a)