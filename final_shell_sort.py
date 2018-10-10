from genericpath import isfile
from macpath import join
from os import listdir
import re
import matplotlib.pyplot as plt

def collect_names(path_to_dir='C:/Users/Sergei/Desktop/data/TheoreticalEfficiency/'):
    files = [f for f in listdir(path_to_dir)]
    return files


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


def get_name(seq):
    if seq == '2':
        return 'Шелла'
    elif seq == 's':
        return 'Сэджвика'
    elif seq == 'f':
        return 'Фибоначчи'
    elif seq == 'p':
        return 'Пратта'
    elif seq == 'h':
        return 'Хиббарда'



def plot_theor_eff(seq):

    ns = range(10000,2000001,10000)
    plt.plot(ns,get_data(seq)[0],label='теор. ускорение',color='#0052cc',linewidth=2)
    plt.plot(ns,get_data(seq)[1],label='теор. ускорение без k=1',color='#66a3ff',linewidth=2)

if __name__=='__main__':
    plot_theor_eff('h')