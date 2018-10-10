import numpy.random as rd
import numpy as np
import matplotlib.pyplot as plt
import shell_sort_analysis as ssa


def get_array(size):
    return rd.sample(size)

def color_subseq(a,bar,v,colors):

    for i in range(0,len(a),v):
        bar[i].set_color(colors[0])
        bar[i+1].set_color(colors[1])
        bar[i+2].set_color(colors[2])


def plot_unsorted_subseq(a,v):
    plot_them(extract_subseq(a,v))


def plot_them(sub_ss):
    first = sub_ss[0]
    second = sub_ss[1]
    third = sub_ss[2]
    ax2 = plt.subplot2grid((4, 3), (1, 0))
    ax3 = plt.subplot2grid((4, 3), (1, 1))
    ax4 = plt.subplot2grid((4, 3), (1, 2))
    ax2.bar(get_linear_seq(first), first, color='r')
    ax3.bar(get_linear_seq(second),second, color='g')
    ax4.bar(get_linear_seq(third), third, color='b')
    plot_sorted_seq(first,second,third)

def plot_sorted_seq(a1,a2,a3):

    a1 = sorted(a1)
    a2 = sorted(a2)
    a3 = sorted(a3)

    ax5 = plt.subplot2grid((4, 3), (2, 0))
    ax6 = plt.subplot2grid((4, 3), (2, 1))
    ax7 = plt.subplot2grid((4, 3), (2, 2))
    ax5.bar(get_linear_seq(a1), a1, color='r')
    ax6.bar(get_linear_seq(a2),a2, color='g')
    ax7.bar(get_linear_seq(a3), a3, color='b')

def plot_sorted_array(a,v):
    print(a)
    a = part_shell(a,v)
    print(a)
    ax5 = plt.subplot2grid((4, 3), (3, 0), colspan=3)
    bar =  ax5.bar(get_linear_seq(a), a*100, color='grey')
    color_subseq(a, bar,v,['r','g','b'])


def extract_subseq(a,v):
    first = []
    second = []
    third = []
    for i in range(0, len(a), v):
        first.append(a[i]*100)
        if (i+1)<len(a):
            second.append(a[i + 1]*100)
        if (i+2)<len(a):
            third.append(a[i + 2]*100)

    return first,second,third

def get_linear_seq(a):
    return np.linspace(1,len(a),len(a))

def plot_main_graph(a,v):

    ax1 = plt.subplot2grid((4, 3), (0, 0), colspan=3)
    bar = ax1.bar(get_linear_seq(a),a*100,color='grey')
    color_subseq(a,bar,v,['r','g','b'])
    plot_unsorted_subseq(a,v)
    plot_sorted_array(a,v)
    plt.show()

def part_shell(a,v):
        for i in range(96, len(a)):
            for j in range(i, 0, -v):
                if a[j - v] < a[j]:
                    break
                a[j], a[j - v] = a[j - v], a[j]
        return a

def shell_sort_itself(a):
    gaps = ssa.sedgewick(a)
    for gap in gaps:
        for i in range(gap, len(a)):
            for j in range(i, gap - 1, -gap):
                if a[j - gap] < a[j]:
                    break
                a[j], a[j - gap] = a[j - gap], a[j]



if __name__ == '__main__':

    plot_main_graph(get_array(100),16)

