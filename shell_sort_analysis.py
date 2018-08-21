from numpy import *
from numpy.core.tests.test_mem_overlap import xrange
import numpy.random as rd
from collections import OrderedDict
from timeit import default_timer as timer
import time
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

    list_of_dict = []

    for increment in new_increment(a):
        dict = {}
        for i in xrange(increment, len(a)):
            t = 0
            for j in xrange(i, increment - 1, -increment):
                if a[j - increment] < a[j]:
                    break
                a[j], a[j - increment] = a[j - increment], a[j]
                t+=1
            v = dict.get(t)
            if v==None:
                v = 0
            dict.update({t: v+1})
        dict = sorted(dict.items(), key=lambda t: t[0])
        list_of_dict.append(dict)
        get_splot(list_of_dict)

    plt.show()


def get_array(size):
    return rd.sample(size)

def print_hist(array):
    shellsort(array)

def get_splot(dict_list):
    fig, axs = plt.subplots(2,1)
    i = 0
    for ax in fig.axes:
        keys, values = zip(*dict_list[i])
        i += 1
        ax.bar(keys, values, width=0.5)








print_hist(get_array(100))