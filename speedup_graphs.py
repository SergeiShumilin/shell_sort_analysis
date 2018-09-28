"""
Plots graphs with different sequences for Shell Sort compared.

How to use this module
======================
use `plot_linear_graph` with this letters:
        s
        p
        2
        h
Examples:
plot_together(collect_names())
plot_together(collect_names('without1'))
plot_together(collect_names('all'))

"""

import re
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
import seaborn as sb
import matplotlib.ticker as tick
from matplotlib import ticker
import new_shell_sort_analysis as nssa


def collect_names(how='', path_to_dir='C:\\Users\\Sergei\\Desktop\\data'):
    onlyfiles = [f for f in listdir(path_to_dir) if isfile(join(path_to_dir, f))]
    res = []
    if how == 'all':
        return onlyfiles
    elif how == 'without1':
        for file in onlyfiles:
            if file.find(r'without_1') == -1:
                onlyfiles.remove(file)
        return onlyfiles

    elif how == '2':
        for file in onlyfiles:
            if file.find('2') != -1:
                res.append(file)
        return res

    elif how == 's':
        for file in onlyfiles:
            if file.find(r'_s') != -1:
                res.append(file)
        return res
    elif how == 'f':
        for file in onlyfiles:
            if file.find(r'_f') != -1:
                res.append(file)
        return res
    elif how == 'p':
        for file in onlyfiles:
            if file.find(r'_p') != -1:
                res.append(file)
        return res
    elif how == 'h':
        for file in onlyfiles:
            if file.find(r'_h') != -1:
                res.append(file)
        return res

    else:
        for file in onlyfiles:
            if file.find(r'without_1') != -1:
                onlyfiles.remove(file)
        return onlyfiles




def get_data(filename):
    file = open('C:\\Users\\Sergei\\Desktop\\data\\' + filename)
    el_numbers = []
    speedups = []

    for line in file:
        if line.find('begin') != -1:
            result = re.search(r'begin (\d*)', line)
            el_numbers.append(int(result.group(1)))
        if line.find('speedup') != -1:
            result = re.search(r'(\d*\.\d*) times', line)
            speedups.append(float(result.group(1)))

    return el_numbers, speedups


def plot_on_subplots(list_of_files):
    if len(list_of_files) % 2 != 0:
        fig, axs = plt.subplots(2, (len(list_of_files) // 2) + 1, sharey='row')
        axs[-1, -1].axis('off')
    else:
        fig, axs = plt.subplots(2, len(list_of_files) // 2, sharey='row')

    for pair in zip(list_of_files, fig.axes):
        elements_number, efficiency_coef = get_data(pair[0])
        plot_with_params(pair[0], pair[1], elements_number, efficiency_coef)
    plt.show()



def plot_together(s,list_of_files):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    add_inscriptions(ax)

    for item in ax.get_xticklabels() + ax.get_yticklabels():
        item.set_fontsize(20)

  #  plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0),fontsize = 30)
    set_limits(s,ax)

    for file in list_of_files:
        el_num, eff_coef = get_data(file)
        if file.find('_2') != -1:
            if file.find('without') != -1:
                plt.plot(el_num, eff_coef, label='послед. Шелла (N/2) без k=1', color='r')
                nssa.plot_theor_eff(1)
            else:
                plt.plot(el_num, eff_coef, label='послед. Шелла (N/2)', color='g')
        if file.find('_s') != -1:
            if file.find('without') != -1:
                plt.plot(el_num, eff_coef, label="послед. Седжвика без k=1", color='r')
                nssa.plot_theor_eff(4)
            else:
                plt.plot(el_num, eff_coef, label="послед. Седжвика", color='g')
        if file.find('_f') != -1:
            if file.find('without') != -1:
                plt.plot(el_num, eff_coef, label="Фибоначчи без k=1", color='r')
            else:
                plt.plot(el_num, eff_coef, label="Фибоначчи", color='g')
        if file.find('_p') != -1:
            if file.find('without') != -1:
                plt.plot(el_num, eff_coef, label='послед. Пратта без k=1', color='r' )
                nssa.plot_theor_eff(2)
            else:
                plt.plot(el_num, eff_coef, label='послед. Пратта', color='g')
        if file.find('_h') != -1:
            if file.find('without') != -1:
                plt.plot(el_num, eff_coef, label='послед. Хиббарда без k=1', color='r')
                nssa.plot_theor_eff(5)
            else:
                plt.plot(el_num, eff_coef, label='послед. Хиббарда', color='g')

    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.2,
                     box.width, box.height])

    # Put a legend below current axis
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12),
              fancybox=True, ncol=2,fontsize=24)
    alter_tick_labels(ax)
 #   plt.legend(loc='upper right',ncol = 2,fontsize=30)
    plt.show()



def alter_tick_labels(ax):
#ax.xaxis.set_major_formatter(ticker.FormatStrFormatter(">%d<"))
#ax.xaxis.set_major_formatter(major_formatter)
    ticks = ['0','0','$0.25\cdot10^{6}$','$0.5\cdot10^{6}$','$0.75\cdot10^{6}$','$1.0\cdot10^{6}$',
             '$1.25\cdot10^{6}$','$1.5\cdot10^{6}$','$1.75\cdot10^{6}$','$2.0\cdot10^{6}$']
    ax.set_xticklabels(ticks)

def major_formatter(x,pos):
    return '[%.2f]' % x


def add_inscriptions(ax):
    ax.axes.set_xlabel('Число элементов',size = 30)
    ax.axes.set_ylabel('Эффективность векторизации',size = 30)


def set_limits(s,ax):
    if s == '2':
        ax.set_ylim(0.5, 6)
    elif s == 's':
        ax.set_ylim(1, 7)
    elif s == 'f':
        ax.set_ylim(0, 4)
    elif s == 'p':
        ax.set_ylim(1, 10)
    elif s == 'h':
        ax.set_ylim(0.8, 8)

def plot_with_params(file_name, subplot, elem_num, effic_coef):
    subplot.set_title(file_name)
    subplot.axes.set_xlabel('Число элементов',size = 15)
    subplot.axes.set_ylabel('Эффективность векторизации')
    subplot.set_ylim(0, 3)
    subplot.plot(elem_num, effic_coef)


def plot_graph(seq):
    plot_together(seq, collect_names(seq))



if __name__ == '__main__':

#    plot_graph('s')
#    plot_graph('2')
#   plot_graph('p')
    plot_graph('h')
