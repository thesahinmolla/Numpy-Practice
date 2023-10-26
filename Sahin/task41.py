#Get today in numpy and deltas
import numpy as np

today = np.datetime64('today', 'D')
print('today          : ', today)

after2days = np.datetime64('today', 'D') + np.timedelta64(2, 'D')
print('after 2 days   : ', after2days)

before3days = np.datetime64('today', 'D') - np.timedelta64(3, 'D')
print('before 3 days  : ', before3days)

after1week = np.datetime64('today', 'D') + np.timedelta64(1, 'W')
print('after 1 week   : ', after1week)

after10weeks = np.datetime64('today', 'D') + np.timedelta64(10, 'W')
print('after 10 weeks : ', after10weeks)

after1years = np.datetime64('today', 'D') + np.timedelta64(365, 'D')
print('after 1 years : ', after1years)