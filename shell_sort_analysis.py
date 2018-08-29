from numpy import *
from numpy.core.tests.test_mem_overlap import xrange
import numpy.random as rd
import matplotlib.pyplot as plt


def shellsort(a, v, seq, Show_dict=False, Show_Maximized_Dict=False, Show_Itarations=False, Show_Hist=False):
    """

    :param a: array with constant distribution
    :param v:
    :param seq: 1 - shell
                2 - pratt1
                3 - pratt2
                4 - fibonacci
    :param Show_dict:
    :param Show_Maximized_Dict:
    :param Show_Itarations:
    :param Show_Hist:
    :return:
    """
    dict = {}
    ks = []
    list_of_dicts = []

    gaps = choose_seq(seq,a)

    for gap in gaps:
        values = []
        for i in xrange(gap, len(a)):
            iter = 0
            for j in xrange(i, gap - 1, -gap):
                iter += 1
                if a[j - gap] < a[j]:
                    break
                a[j], a[j - gap] = a[j - gap], a[j]

            values.append(iter)

        ks.append(gap)
        dict.update({gap: values})

    list_of_dicts.append(dict)

    max_dic = maximize(dict, v)

    if Show_dict is True: print(dict)
    if Show_Maximized_Dict is True: print_maxim_dict(max_dic)

    if Show_Itarations is True:
        Ivect = sum_up(max_dic)
        Iorigin = sum_up(dict)
        I = Iorigin / Ivect
        print('Кол-во итераций внутр. цикла в невекторизованном коде: Iorigin = ' + str(Iorigin))
        print('Кол-во итераций внутр. цикла в векторизованном коде: Ivect = ' + str(Ivect))
        print('Отношение числа итераций Iorigin/Ivect = ' + str(I))

    if Show_Hist is True:
        get_splot(max_dic, ks)

    return I

def shell(array):
    """
    Worst case complexity: O(n^2)
    :param array:
    :return:
    """
    res = []
    i = int(len(array) / 2)
    yield i
    while i != 1:
        if i == 2:
            i = 1
        else:
            i = int(round(i / 2))
        res.append(i)
    return res

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
    return res

def fibonacci(array):
    res = []

    def fib(n):
        a, b = 1, 1
        while (a < n / 2):
            yield a
            a, b = b, a + b

    for i in fib(len(array)):
        res.append(i)
    res.remove(1)
    return list(reversed(res))


def sedgewick(array):
    res = []
    i = 0
    el = 0
    while el < (len(array) // 3):
        if i % 2 == 0:
            el = (9 * (2 ** i - 2 ** (i // 2)) + 1)
            i += 1
        else:
            el = 8 * 2 ** i - 6 * 2 ** ((i + 1) // 2) + 1
            i += 1
        res.append(el)
    return list(reversed(res))

def choose_seq(n, array):
    if n == 1:
        return shell(array)
    elif n == 2:
        return pratt1(array)
    elif n == 3:
        return pratt2(array)
    elif n == 4:
        return fibonacci(array)
    elif n == 5:
        return sedgewick(array)


def get_array(size):
    return rd.sample(size)


def get_splot(dict_list, list_of_ks):
    if len(dict_list) % 2 != 0:
        fig, axs = plt.subplots(2, (len(dict_list) // 2) + 1, sharey='row')
        axs[-1, -1].axis('off')
    else:
        fig, axs = plt.subplots(2, len(dict_list) // 2, sharey='row')
    i = 0
    for ax, dict in zip(fig.axes, dict_list):
        values = dict_list.get(dict)
        row = arange(len(values))
        ax.set_title('k =' + str(list_of_ks[i]))
        i += 1
        ax.axhline(y=16, color='r', linestyle='--', lw=0.5)
        ax.bar(row, values, width=0.3)
    plt.show()


def maximize(dict, v):
    maximized_dict = {}
    for key, value in dict.items():
        if key<16: maximized_dict.update({key: find_maxs_in_subsets(value, key)})
        else: maximized_dict.update({key: find_maxs_in_subsets(value, v)})
    return maximized_dict


def find_maxs_in_subsets(array, v):
    res = [max(array[i:i + v]) for i in range(0, len(array), v)]
    return res


def sum_up(maxim_dict):
    I = 0
    for key, value in maxim_dict.items():
        I += sum(value)
    return I


def print_maxim_dict(max_dict):
    for key, value in max_dict.items():
        print('k = ' + str(key) + ': ' + str(value))


def number_of_el_I_depend(seq):
    x = [i for i in range(50000, 1000000, 50000)]
    y = [shellsort(get_array(size),16,seq, Show_Itarations=True) for size in x]
    a, b, c = polyfit(x, y, 2)
    x_out = linspace(0, max(x), 1000)  # choose 20 points, 10 in, 10 outside original range
    y_pred = polyval([a, b, c], x_out)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.axes.set_xlabel('Number of elements')
    ax.axes.set_ylabel('Vectorization efficiency')
    plt.plot(x, y, '-o')
    plt.plot(x, y, 'g.', x_out, y_pred, 'b-')

    plt.show()

number_of_el_I_depend(5)