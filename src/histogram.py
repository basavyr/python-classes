from matplotlib import rc
import matplotlib.pyplot as plt
import numpy as np
import random as rd


class Histogram:
    def __init__(self, data_batch, nbins, filename, label, u_id):
        self.label = label
        self.filename = filename+'.pdf'
        self.nbins = nbins
        self.data_batch = data_batch
        self.uid = u_id
        # print( f'Class {Histogram.__name__} was initialized with the arguments: {self.label} | {self.data_batch} | {self.nbins}')

    def _makeHistogram(self):
        fig, ax = plt.subplots()
        plt.xlabel('x')
        plt.ylabel('P(x)')
        plt.title('The histogram for the normally distributed random data')
        plt.text(0.05, 0.9, self.uid, {
                 'color': 'b', 'fontsize': 7,'fontstyle': 'italic'}, transform=ax.transAxes)
        count = 1
        calpha = 1
        for data in self.data_batch:
            data_label = self.label+'-'+str(count)
            plt.hist(data, self.nbins, density=True,
                     label=data_label, alpha=calpha)
            count = count+1
            calpha = calpha-0.1
        plt.legend(loc='best')
        plt.savefig(self.filename, bbox_inches='tight')
        plt.close()

    @staticmethod
    def makeHistogram(data_batch, nbins, plt_label, filename):
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
