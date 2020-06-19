from matplotlib import rc
import matplotlib.pyplot as plt
import numpy as np
import random as rd

from arrays import Arrays
SIZE = 1000
STD_DEV = 50


def rand_data(size, std_dev):
    # x = np.random.normal(0, std_dev, size)
    x = Arrays.generateNormalArray(size, 0, std_dev)
    x_int = [int(element) for element in x]
    return x_int


X_INT = rand_data(SIZE, STD_DEV)


def makeHistogram(data_batch, nbins, plt_label, filename):
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.title('The histogram for the normally distributed random data')
    count = 1
    calpha = 1
    for data_set in data_batch:
        data_label = plt_label+'-'+str(count)
        count = count+1
        plt.hist(data_set, nbins, density=True, label=data_label, alpha=calpha)
        calpha = calpha-0.1
    plt.legend(loc='best')
    plt.savefig(filename, bbox_inches='tight')
    plt.close()
