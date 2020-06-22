from matplotlib import rc
import matplotlib.pyplot as plt
import numpy as np
import random as rd


class Histogram:
    @staticmethod
    def makeHistogram(data, nbins, plt_label, filename):
        plt.xlabel('x')
        plt.ylabel('P(x)')
        plt.title('The histogram for the normally distributed random data')
        plt.hist(data, nbins, density=True, label=plt_label)
        plt.legend(loc='best')
        plt.savefig(filename, bbox_inches='tight')
        plt.close()

    @staticmethod
    def makeBatchHistogram(data_batch, nbins, plt_label, filename):
        plt.xlabel('x')
        plt.ylabel('P(x)')
        plt.title('The histogram for the normally distributed random data')
        count = 1
        calpha = 1
        for data_set in data_batch:
            data_label = plt_label+'-'+str(count)
            count = count+1
            plt.hist(data_set, nbins, density=True,
                     label=data_label, alpha=calpha)
            calpha = calpha-0.1
        plt.legend(loc='best')
        plt.savefig(filename, bbox_inches='tight')
        plt.close()
