"""
Plots graphs with different sequences for Shell Sort compared.

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


def collect_names(how='', path_to_dir='C:\\Users\\Sergei\\Desktop\\data'):
    onlyfiles = [f for f in listdir(path_to_dir) if isfile(join(path_to_dir, f))]
    if how == 'all':
        return onlyfiles
    elif how == 'without1':
        for file in onlyfiles:
            if file.find(r'without_1') == -1:
                onlyfiles.remove(file)
        return onlyfiles
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


def plot_together(list_of_files):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    add_inscriptions(ax)

    for item in ax.get_xticklabels() + ax.get_yticklabels():
        item.set_fontsize(20)

    plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0),fontsize = 30)



    set_limits(ax,list_of_files)

    for file in list_of_files:
        el_num, eff_coef = get_data(file)
        if file.find('_2') != -1:
            if file.find('without') != -1:
                plt.plot(el_num, eff_coef, label='N/2 without k=1', color='#ff3333', linestyle='--')
            else:
                plt.plot(el_num, eff_coef, label='N/2', color='#ff3333')
        if file.find('_s') != -1:
            if file.find('without') != -1:
                plt.plot(el_num, eff_coef, label="Sedgewick without k=1", color='#4da6ff', linestyle='--')
            else:
                plt.plot(el_num, eff_coef, label="Sedgewick", color='#4da6ff')
        if file.find('_f') != -1:
            if file.find('without') != -1:
                plt.plot(el_num, eff_coef, label="Febonacci without k=1", color='#180c29', linestyle='--')
            else:
                plt.plot(el_num, eff_coef, label="Febonacci", color='#180c29')
        if file.find('_p') != -1:
            if file.find('without') != -1:
                plt.plot(el_num, eff_coef, label='Pratt without k=1', color='#47d147', linestyle='--')
            else:
                plt.plot(el_num, eff_coef, label='Pratt', color='#47d147')
        if file.find('_h') != -1:
            if file.find('without') != -1:
                plt.plot(el_num, eff_coef, label='Hibbard without k=1', color='#ff751a', linestyle='--')
            else:
                plt.plot(el_num, eff_coef, label='Hibbard', color='#ff751a')


    plt.legend(loc='lower right',ncol = 2,fontsize=18)
    plt.show()


def add_inscriptions(ax):
    ax.axes.set_xlabel('Число элементов',size = 30)
    ax.axes.set_ylabel('Эффективность векторизации',size = 30)


def set_limits(ax,list_of_files):
    if list_of_files[0].find('without_1') != -1:
        ax.set_ylim(0, 4)
    else:
        ax.set_ylim(0, 4)

def plot_with_params(file_name, subplot, elem_num, effic_coef):
    subplot.set_title(file_name)
    subplot.axes.set_xlabel('Число элементов',size = 15)
    subplot.axes.set_ylabel('Эффективность векторизации')
    subplot.set_ylim(0, 3)
    subplot.plot(elem_num, effic_coef)

plot_together(collect_names('all'))
