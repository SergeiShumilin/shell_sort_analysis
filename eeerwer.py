def sedgewick(array):
   res = []
   i = 0
   el = 0
   while el < (len(array)//3):
       if i % 2 == 0:
           el = (9 * (2 ** i - 2 ** (i//2)) + 1)

           i +=1
       else:
           el = 8 * 2 ** i - 6 * 2 ** ((i + 1) // 2) + 1
           i += 1
       res.append(el)
   return list(reversed(res))


from numpy import *
from numpy.core.tests.test_mem_overlap import xrange
import numpy.random as rd
import matplotlib.pyplot as plt


array = rd.sample(10000)
print(sedgewick(array))