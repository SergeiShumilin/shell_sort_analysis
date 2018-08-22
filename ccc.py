import numpy as np
from numpy.core.tests.test_mem_overlap import xrange
import numpy.random as rd
from collections import OrderedDict
from timeit import default_timer as timer
import time
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

mu, sigma = 10, 15
x = mu + sigma*np.random.randn(1000)


n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)
y = mlab.normpdf( bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=1)

plt.show()
