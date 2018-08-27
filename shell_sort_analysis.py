from numpy import *
from numpy.core.tests.test_mem_overlap import xrange
import numpy.random as rd
import matplotlib.pyplot as plt


def shellsort(a, v, Show_dict=False, Show_Maximized_Dict=False, Show_Itarations=False, Show_Hist = False):
    def new_increment2(a):
        N = int(len(a))
        h = 1
        while h < N / 3:
            h = 3 * h + 1
        while h >= 1:
            yield h
            h //= 3

    dict = {}
    ks = []
    list_of_dicts = []
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
        ks.append(increment)
        dict.update({increment: values})
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
        maximized_dict.update({key: find_maxs_in_subsets(value, v)})
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

def number_of_el_I_depend():
    a = [10**i for i in range(1000,1000000,5000)]
    b = [shellsort(get_array(size),16,Show_Itarations=True) for size in a]
#    plt.scatter(a, b)
    plt.plot(a,b, '-o')
    plt.show()


number_of_el_I_depend()