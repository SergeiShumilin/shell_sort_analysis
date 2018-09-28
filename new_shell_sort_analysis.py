import numpy as np
from numpy.core.tests.test_mem_overlap import xrange
import matplotlib.pyplot as plt
import numpy.random as rd
import time
import seaborn as sns

"""
Plots theoretical efficiency of vectorization.

How to use
============
call `plot_theor_eff(seq)` with seq: 

                1 - shell
                2 - pratt1
                3 - pratt2
                4 - sedgewick
                5 - hibbard

The number of elements range is set manually in the `plot_theor_eff(seq)` function (Ns variable)


"""
def plot_theor_eff(seq):
    Ns = range(10000, 1000000, 10000)

    effs = [shellsort(get_array(N), seq) for N in Ns]
    effs_k1 = [shellsort(get_array(N), seq,without_k1=True) for N in Ns]
    plt.plot(Ns,effs, color = 'orange',label = get_label(seq))
    plt.plot(Ns,effs_k1, color = 'blue', label = get_label(seq)+' без k=1')


def get_label(seq):
    s = 'Теор. эффект. послед. '
    if seq == 1:
        return s + 'Шелла'
    elif seq == 2:
        return s + 'Пратта'
    elif seq == 3:
        return s + 'Пратта 2'
    elif seq == 4:
        return s + 'Сэджвика'
    elif seq == 5:
        return s + 'Хиббарда'




def shellsort(a, seq, without_k1 = False, plot_vect = False):
    """
    :param seq: 1 - shell
                2 - pratt1
                3 - pratt2
                4 - sedgewick
                5 - hibbard
    """
    sns.set()
    all_values = []
    all_vect_values = []
    fig = plt.figure()
    for gap in choose_seq(seq, a):
        if without_k1:
            if gap==1:
                break
        values = inner_loop(a, gap)
        all_values += values
        all_vect_values += (vectorize(values,gap))
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)
        sns.distplot(all_vect_values, kde=False,label='Vectorized',ax=ax2)
        sns.set_palette('YlOrRd_r')
#        ax2.title('Vectorized ' + get_name(seq) + ' k = ' + str(gap), size=15)
#        plt.savefig('figures/' + 'Vectorized ' + get_name(seq) + ' k_' + str(gap))
#        plt.clf()
        sns.set_palette('PuBuGn_r')
        sns.distplot(all_values, kde=False,label='Original',ax=ax1)
#        ax1.title(get_name(seq) + ' k = ' + str(gap), size=15)
        plt.legend()
        plt.savefig('figures/' + get_name(seq) + ' k_' + str(gap))
        plt.clf()




    return sum(all_values) / sum(all_vect_values)

def get_name(seq):
    if seq==1:

        return 'N2'
    if seq==2:
        return 'Pratt'
    if seq==4:

        return 'Sedgewick'
    if seq==5:
        return 'Hibbard'

def get_array(size):
    return rd.sample(size)


def inner_loop(a, gap):
    values = []
    for i in xrange(gap, len(a)):
        iter = 0
        for j in xrange(i, gap - 1, -gap):
            iter += 1
            if a[j - gap] < a[j]:
                break
            a[j], a[j - gap] = a[j - gap], a[j]
        values.append(iter)
    return values


def vectorize(values, k):
    return [max(values[i:i + min(16, k)]) for i in range(0, len(values), min(16, k))]


def shell(array):
    """
    Worst case complexity: O(n^2)
    :param array:
    :return:
    """
    res = [int(len(array) / 2)]
    i = int(len(array) / 2)
    while i != 1:
        if i == 2:
            i = 1
        else:
            i = int(round(i / 2))
        res.append(i)
    return list(res)

def pratt1(array):
    """Generate a sorted list of products of powers of 2 and 3 below max_size"""
    res = []
    max_size = len(array) // 2
    pow3 = 1  # start with q = 0
    while pow3 <= max_size:
        # At this point, pow3 = 3**q, so set p = 0
        pow2 = pow3
        while pow2 <= max_size:
            # At this point, pow2 = 2**p * 3**q
            res.append(pow2)
            pow2 = pow2 * 2  # this is like adding 1 to p
        # now that p overflowed the maximum size, add 1 to q and start over
        pow3 = pow3 * 3
    return list(reversed(sorted(res)))

def pratt2(array):
    res = []
    N = int(len(array))
    h = 1
    while h < N / 3:
        h = 3 * h + 1
    while h >= 1:
        res.append(h)
        h //= 3
    del res[0]
    return res


def sedgewick(array):
    res = []
    i = 0
    el = 0
    while el*3<len(array):
        if i % 2 == 0:
            el = (9 * (2 ** i - 2 ** (i // 2)) + 1)
            i += 1
        else:
            el = 8 * 2 ** i - 6 * 2 ** ((i + 1) // 2) + 1
            i += 1
        res.append(el)
    res = list(reversed(res))
    del res[0]
    return res

def hibbard(array):
    i = 1
    res = []
    n = 0
    while 2 ** i - 1 < len(array):
        n = 2 ** i - 1
        res.append(n)
        i += 1
    return list(reversed(res))

def choose_seq(n, array):
    if n == 1:
        return shell(array)
    elif n == 2:
        return pratt1(array)
    elif n == 3:
        return pratt2(array)
    elif n == 4:
        return sedgewick(array)
    elif n == 5:
        return hibbard(array)

if __name__ == '__main__':

    shellsort(get_array(1000000),1)
#    shellsort(get_array(100000),2)
#   shellsort(get_array(100000),4)
    shellsort(get_array(1000000),5)