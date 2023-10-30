#Create 4 different integers from 0, 4. (It will throw error as we can't get 5 unique integers from 4)
import numpy as np

try:
    x = np.random.choice(4, 5, replace = False)
    
    print('np.random.choice(4, 5, replace = False):\n')
    print(x)
except Exception as err:
    print('Error : ', err)

# output
# Error :  Cannot take a larger sample than population when 'replace=False'