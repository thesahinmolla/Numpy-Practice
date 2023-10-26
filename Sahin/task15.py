#Get the nth column of an array
import numpy as np
x = np.array([[1, 2], [3, 4], [5, 6]])

print('Numpy array:')
print(x)

y = x[:,0]
print('\nFirst Column')
print(y)

z = x[:, 1]
print('\nSecond Column')
print(z)

a = x[0,:]
print('\nFirst Row')
print(a)

b = x[1,:]
print('\nSecond Row')
print(b)

c = x[2,:]
print('\nThird Row')
print(c)