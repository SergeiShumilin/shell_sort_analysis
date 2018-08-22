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






def shellsort(a, seq_num):
    def new_increment1(a):
        i = int(len(a) / 2)
        yield i
        while i != 1:
            if i == 2:
                i = 1
            else:
                i = int(round(i / 2))
            yield i

    def new_increment2(a):
        N = int(len(a))
        h = 1
        while h < N / 3:
            h = 3 * h + 1
        while h >= 1:
            yield h
            h //= 3

    list_of_dict = []
    list_of_k = []

    if seq_num == 1:
        for increment in new_increment1(a):
            dict = {}
            for i in xrange(increment, len(a)):
                t = 0
                for j in xrange(i, increment - 1, -increment):
                    if a[j - increment] < a[j]:
                        break
                    a[j], a[j - increment] = a[j - increment], a[j]
                    t += 1
                v = dict.get(t)
                if v == None:
                    v = 0
                dict.update({t: v + 1})
            dict = sorted(dict.items(), key=lambda t: t[0])
            list_of_dict.append(dict)
            list_of_k.append((increment))
        print(list_of_dict)
        #get_splot(list_of_dict, list_of_k)
    else:
        for increment in new_increment2(a):
            dict = {}
            for i in xrange(increment, len(a)):
                t = 0
                for j in xrange(i, increment - 1, -increment):
                    if a[j - increment] < a[j]:
                        break
                    a[j], a[j - increment] = a[j - increment], a[j]
                    t += 1
                v = dict.get(t)
                if v == None:
                    v = 0
                dict.update({t: v + 1})
            dict = sorted(dict.items(), key=lambda t: t[0])
            list_of_dict.append(dict)
            list_of_k.append((increment))
        #print(list_of_dict)
        get_splot(list_of_dict, list_of_k)

    plt.show()


def get_array(size):
    return rd.sample(size)


def print_hist(array, seq_num):
    shellsort(array, seq_num)


def get_splot(dict_list, list_of_ks):
    print('the length of the dict is '+str(len(dict_list)))
    if len(dict_list)%2!=0:
        fig, axs = plt.subplots(2, (len(dict_list) // 2)+1, sharey='row')
    else: fig, axs = plt.subplots(2, len(dict_list) // 2, sharey='row')
    i = 0
    for ax in fig.axes:
        if i<=len(dict_list):
            keys, values = zip(*dict_list[i])
            ax.set_title('k =' + str(list_of_ks[i]))
            i += 1
            ax.bar(keys, values, width=0.5)
        else: break


def count_time(use_seq):
    t1 = time.time()
    print_hist(get_array(100000), use_seq)
    t2 = time.time()
    print('The work time of the Shell algorithms when using ' + str(use_seq) + ' is ' + str(t2 - t1))
    return t2 - t1

def time_mean(use_seq, iterations):
    total_time = 0
    for i in range(0,iterations):
        total_time += count_time(use_seq)
    print('Mean of work of Shell alg. with '+ str(iterations) + ' iterations is ' + str(total_time/iterations)
          + ' using '+ str(use_seq)+' sequence')
    return total_time



