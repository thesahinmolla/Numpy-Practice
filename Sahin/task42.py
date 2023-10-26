#Between two Dates
import numpy as np

a = np.arange('2023-12-23', '2024-01-02', dtype='datetime64[D]')
print(f"Between two dates : 2023-12-23 and 2024-01-02: \n{a}")

a = np.arange('2023-11', '2023-12', dtype='datetime64[D]')
print(f"Between 2 months : 2023-11 and 2023-12: \n{a}")
