import numpy.random as rd
import numpy as np
import matplotlib.pyplot as plt
import shell_sort_analysis as ssa



def plot_main_graph(a,v):

    ax1 = plt.subplot2grid((4, 3), (0, 0), colspan=3)
    bar = ax1.bar(get_linear_seq(a),a*100,color='grey')
    paint_columns(bar,a,v)
    plt.show()


def get_linear_seq(a):
    return np.linspace(1,len(a),len(a))

def paint_columns(bar,a,v):
    colors = ['r','g','b','r','g','b','r','g','b']
    for i in range(0, len(a), v):
        [col.set_color(color) for col in bar[i:i + v] for color in colors]


def get_array(size):
    return rd.sample(size)


plot_main_graph(get_array(100),8)