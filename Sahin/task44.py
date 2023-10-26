#Random int array and sorting
import numpy as np

a = np.random.randint(0 , 20 ,2)
print(f"before:\n {a}")

a.sort()
print(f"After:\n {a}")