import re
import matplotlib.pyplot as plt

def plot_effic(filename):
    file = open('C:\\Users\\Sergei\\Desktop\\'+filename+'.txt')
    el_numbers = []
    speedups = []
    for line in file:

        if line.find('begin')!=-1:
            result = re.search(r'begin (\d*)',line)
            el_numbers.append(int(result.group(1)))
        if line.find('speedup')!=-1:
            result = re.search(r'(\d*\.\d*) times',line)
            speedups.append(float(result.group(1)))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title(filename)
    ax.axes.set_xlabel('Number of elements')
    ax.axes.set_ylabel('Vectorization efficiency')
    ax.set_ylim(0,10)
    plt.plot(el_numbers,speedups)
    plt.show()

names = ['result_2','result_f','result_h','result_p','result_s']

for name in names:
    plot_effic(name)