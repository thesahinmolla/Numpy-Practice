#Save Numpy to CSV
import numpy as np

a = np.asarray([ [1,2,3], [4,5,6]])
print(a)
np.savetxt("sahin.csv", a, delimiter=",")