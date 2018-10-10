import re
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

"""
Call `plot_linear_graph` to plot the information in the linear format.
Call `plot_bar_graph` to plot the information like a bar.




"""

def get_data():
    file = open('C:\\Users\\Sergei\\Desktop\\data\\result.txt')
    speedups = []

    for line in file:
        if line.find('speedup') != -1:
            result = re.search(r'speedup = (\d*\.\d*)', line)
            speedups.append(float(result.group(1)))
    print(speedups)
    return speedups


def create_df(speedups):

    methods = ['OLD VECT','OLD VECT','OLD VECT','OLD VECT',
               'FULL UNROLL','FULL UNROLL','FULL UNROLL','FULL UNROLL',
               'NEW VECT','NEW VECT','NEW VECT','NEW VECT',]
    functions = ['mul_8x8','mul_7x7','mul_6x6','mul_5x5',
                 'mul_8x8','mul_7x7','mul_6x6','mul_5x5',
                 'mul_8x8', 'mul_7x7', 'mul_6x6', 'mul_5x5']
    import pandas as pd
    df = pd.DataFrame({'Методы':methods,
                      'Функции':functions,
                      'Ускорение':speedups[0:12]})
    return df


def plot_linear_graph():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    data = get_data()

    plt.plot(data[0:4],label = 'OLD VECT 100',marker = 'o')
    plt.plot(data[4:8],label = 'FULL UNROLL 100',marker = 'o')
    plt.plot(data[8:12],label = 'NEW VECT 100',marker = 'o')
    plt.plot(data[12:16],label = 'NEW VECT 1000',marker = 'o')

    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(14)

    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(14)

    labels = ['om_mult_mm_8x8','om_mult_mm_7x7','om_mult_mm_6x6','om_mult_mm_5x5',]
    ax.set_xticks([0,1,2,3])
    ax.set_xticklabels(labels)

    plt.legend(loc='upper right',ncol = 2,fontsize=20)
    plt.show()


def plot_seaborn_bar_graph():
    import seaborn as sns
    sns.set_style('darkgrid')
    sns.set(font_scale=1.4)
    fig = plt.figure()
    ax = fig.add_subplot(111)

    g = sns.catplot(x='Функции',y='Ускорение',hue='Методы',data=create_df(get_data()),
                       kind='bar',height=5,legend=False)
    plt.legend(loc='best')
    ax.add_patch(Polygon([[0,0],[0,1],[4,1],[4,0]],closed=True))



    g.set_axis_labels("Функции", "Ускорение")

    plt.show()

def regroup_list(a,k):
    """
    Regroup the list.
    :param k:
    """
    a = [a[i:len(a):k] for i in np.arange(k)]
    a = [item for sublist in a for item in sublist]


def plot_bar_graph():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    data = get_data()[0:12]
    ax.bar(np.arange(len(data)), data)

    plt.show()




if __name__=='__main__':
    plot_seaborn_bar_graph()