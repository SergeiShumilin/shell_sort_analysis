from numpy import *
from numpy.core.tests.test_mem_overlap import xrange
import numpy.random as rd
from timeit import default_timer as timer

import pandas as pd
import matplotlib.pyplot as plt


def shellsort(a):
    def new_increment(a):
        i = int(len(a) / 2)
        yield i
        while i != 1:
            if i == 2:
                i = 1
            else:
                i = int(round(i / 2.2))
            yield i

    dict = {}
    for increment in new_increment(a):
        i = 0
        for i in xrange(increment, len(a)):
            for j in xrange(i, increment - 1, -increment):
                if a[j - increment] < a[j]:
                    break
                a[j], a[j - increment] = a[j - increment], a[j]
                i+=i
        dict.update({increment: i})
    print(dict)
    return dict


def get_array(size):
    return rd.sample(size)

def print_change_freq(array):

    shellsort(array).plt.hist(grid=True, bins=20, rwidth=0.9,
                   color='#607c8e')
    plt.show()



print_change_freq(get_array(100))
