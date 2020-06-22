import matplotlib.pyplot as plt
from datetime import datetime


class ViolinPlot:
    def __init__(self, data_batch, filename, label):
        self.filename = filename+'.pdf'
        self.label = label
        self.data_batch = data_batch
        print(
            f'The class {ViolinPlot.__name__} has been initialzed with values: {self.data_batch} | {self.label} | {self.filename}')

    def _makeViolinPlot(self):
        fig, ax = plt.subplots()
        plt.xlabel('Sample data')
        plt.xlabel('Observed Values')
        plt.title(f'Violin Plot for {self.label}')
        plt.violinplot(self.data_batch, showmedians=True,
                       showmeans=True, showextrema=True)
        plt.savefig(self.filename, bbox_inches='tight')
        plt.close()

    @staticmethod
    def makeBatchViolinPlot(data_bach, filename, label):
        filename=filename+'.pdf'
        fig, ax = plt.subplots()
        plt.xlabel('Sample data')
        plt.xlabel('Observed Values')
        plt.title(f'Violin Plot for {label}')
        for data in data_bach:
            plt.violinplot(data_bach, showmedians=True,
                           showmeans=True, showextrema=True)
        plt.savefig(filename, bbox_inches='tight')
        plt.close()

    @staticmethod
    def makeViolinPlot(data_bach, filename, label):
        filename=filename+'.pdf'
        fig, ax = plt.subplots()
        plt.xlabel('Sample data')
        plt.xlabel('Observed Values')
        plt.title(f'Violin Plot for {label}')
        plt.violinplot(data_bach, showmedians=True,
                       showmeans=True, showextrema=True)
        plt.savefig(filename, bbox_inches='tight')
        plt.close()
