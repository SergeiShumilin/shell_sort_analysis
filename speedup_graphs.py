"""
    USE `plot_speedups` with `names_list` = list of file names with data
"""

import re
import matplotlib.pyplot as plt


def plot_speed_ups(names_list=['result_2', 'result_f', 'result_h', 'result_p', 'result_s']):
    for name in names_list:
        plot_effic(name)


def plot_effic(filename):
    file = open('C:\\Users\\Sergei\\Desktop\\' + filename + '.txt')
    el_numbers = []
    speedups = []

    for line in file:
        if line.find('begin') != -1:
            result = re.search(r'begin (\d*)', line)
            el_numbers.append(int(result.group(1)))
        if line.find('speedup') != -1:
            result = re.search(r'(\d*\.\d*) times', line)
            speedups.append(float(result.group(1)))

    plot_it(el_numbers, speedups, filename)


def plot_it(elements_number, efficiency_coef, filename):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title(filename)
    ax.axes.set_xlabel('Number of elements')
    ax.axes.set_ylabel('Vectorization efficiency')
    ax.set_ylim(0, 10)
    plt.plot(elements_number, efficiency_coef)
    plt.show()

