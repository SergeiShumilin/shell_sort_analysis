import numpy as np

arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 1, 2, 2]

arr2 = np.arange(100)

import itertools
def find_maxs_in_subsets(array,v):
    print(array)
    res = [max(array[i:i+v]) for i in range(0,len(array),v)]
    return res


print(find_maxs_in_subsets(arr,3))