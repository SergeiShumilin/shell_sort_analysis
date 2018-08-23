from numpy import *
from numpy.core.tests.test_mem_overlap import xrange
import numpy.random as rd
import matplotlib.pyplot as plt
import time


def ddd(array):
    N = int(len(array))
    h = 1
    res = [1]
    while h < N / 3:
        h = 3 * h + 1
        res.append(h)
    return res


def shellsort(a):

    def new_increment2(a):
        N = int(len(a))
        h = 1
        while h < N / 3:
            h = 3 * h + 1
        while h >= 1:
            yield h
            h //= 3

    dict = {}
    for increment in new_increment2(a):
        values = []
        for i in xrange(increment, len(a)):
            iter = 0
            for j in xrange(i, increment - 1, -increment):
                iter += 1
                if a[j - increment] < a[j]:
                    break
                a[j], a[j - increment] = a[j - increment], a[j]
            values.append(iter)
        dict.update({increment:values})
    print(dict)
    print_maxim_dict(maximize(dict,3))



def get_array(size):
    return rd.sample(size)


def print_hist(array):
    shellsort(array)


def get_splot(dict_list, list_of_ks):
    print('the length of the dict is ' + str(len(dict_list)))
    if len(dict_list) % 2 != 0:
        fig, axs = plt.subplots(2, (len(dict_list) // 2) + 1, sharey='row')
        axs[-1, -1].axis('off')
    else:
        fig, axs = plt.subplots(2, len(dict_list) // 2, sharey='row')
    i = 0
    for ax in fig.axes:
        if i < len(dict_list):
            keys, values = zip(*dict_list[i])
            ax.set_title('k =' + str(list_of_ks[i]))
            i += 1
            ax.bar(keys, values, width=0.5)
        else:
            break


def maximize(dict, t):
    maximized_dict = {}
    for key, value in dict.items():
        summed_array = []
        for i in range(0, len(value), t):
            for j in range(i, i + t):
                max = value[j]
                if value[j]>max : max = value[j]
            summed_array.append(value[j])
        maximized_dict.update({key: summed_array})
    return maximized_dict


def print_maxim_dict(max_dict):
    for key, value in max_dict.items():
        print('k = ' + str(key)+': '+str(value))


shellsort(get_array(10))