import numpy as np

a = np.arange(1,13)
print(a)

a = [a[i:len(a):2] for i in np.arange(2)]
a = [item for sublist in a for item in sublist]
print(a)