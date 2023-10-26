#Dataframe to Numpy
import pandas as pd 

a = pd.DataFrame({'a1': [1, 2, 3], 'a2': [4, 5, 6]}, index = ['X', 'Y', 'Z'])

print('Dataframe:')
print(a)

x = a.to_numpy()

print('\nDataframe to Numpy:')
print(x)

y = a.index.to_numpy()
print('\nDataframe Indices to Numpy:')
print(y)

z = a['a1'].to_numpy()
print('\nDataframe Series to Numpy:')
print(z)