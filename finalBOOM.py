import re
from genericpath import isfile
from macpath import join
from os import listdir
import matplotlib.pyplot as plt
########################################################################################################################
"""
Launch plot() and plot()





"""
def get_data(seq):
    eff_norm = []
    eff_wo_k = []

    for file in collect_names():
        fil = open('C:/Users/Sergei/Desktop/data/TheoreticalEfficiency/' + file)

        for line in fil:
            result = re.search(r'(\d*\.\d*)', line)
            if result is not None:
                if file.find('без') != -1:
                    eff_wo_k.append(float(result.group(1)))
                else:
                    eff_norm.append(float(result.group(1)))

    if seq == '2':
        return eff_norm[::5], eff_wo_k[::5]
    elif seq == 's':
        return eff_norm[2::5], eff_wo_k[2::5]
    elif seq == 'f':
        return eff_norm[4::5], eff_wo_k[4::5]
    elif seq == 'p':
        return eff_norm[3::5], eff_wo_k[3::5]
    elif seq == 'h':
        return eff_norm[1::5], eff_wo_k[1::5]


def collect_names(path_to_dir='C:/Users/Sergei/Desktop/data/TheoreticalEfficiency/'):
    files = [f for f in listdir(path_to_dir)]
    return files

def plot():
    ns = range(10000,2000001,10000)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(ns,get_data('s')[0],label='Sedgwick sequence',color='black',linestyle=':',linewidth=3)
    ax.plot(ns,get_data('h')[0],label='Hibbard sequence',color='black',linewidth=4)
    ax.plot(ns,get_data('2')[0],label='Pratt sequence',color='black')
    make_legend(ax)
    ax.grid()
    set_fontsize(ax)
    add_inscriptions(ax)
    plt.show()


def add_inscriptions(ax):
    ax.axes.set_xlabel('Number of elements', size=30)
    ax.axes.set_ylabel('Vectorization efficiency', size=30)



def set_fontsize(ax):
    for item in ax.get_xticklabels() + ax.get_yticklabels():
        item.set_fontsize(20)

def make_legend(ax):
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.14,
                     box.width, box.height])

    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.11),
              fancybox=True, ncol=2, fontsize=24,handlelength=6)
    alter_tick_labels(ax)


def alter_tick_labels(ax):
    # ax.xaxis.set_major_formatter(ticker.FormatStrFormatter(">%d<"))
    # ax.xaxis.set_major_formatter(major_formatter)
    ticks = ['0', '0', '$0.25\cdot10^{6}$', '$0.5\cdot10^{6}$', '$0.75\cdot10^{6}$', '$1.0\cdot10^{6}$',
             '$1.25\cdot10^{6}$', '$1.5\cdot10^{6}$', '$1.75\cdot10^{6}$', '$2.0\cdot10^{6}$']
    ax.set_xticklabels(ticks)


def get_data2(filename):
    file = open('C:\\Users\\Sergei\\Desktop\\data\\' + filename)
    speedups = []

    for line in file:
        if line.find('speedup') != -1:
            result = re.search(r'(\d*\.\d*) times', line)
            speedups.append(float(result.group(1)))
    return speedups

def plot2():
    ns = range(10000, 2000001, 10000)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(ns, get_data2('result_s.txt'), label='Sedgwick sequence', color='black', linestyle=':',linewidth=3)
    ax.plot(ns, get_data2('result_h.txt'), label='Hibbard sequence', color='black',linewidth=4)
    ax.plot(ns, get_data2('result_2.txt'), label='Pratt sequence', color='black')
    ax.grid()
    make_legend(ax)
    set_fontsize(ax)
    add_inscriptions(ax)
    plt.show()


if __name__ == '__main__':
    plot()
    plot2()