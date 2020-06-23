import matplotlib.pyplot as plt
from datetime import datetime


class ViolinPlot:
    def __init__(self, data_batch, filename, label, u_id):
        self.filename = filename+'.pdf'
        self.label = label
        self.data_batch = data_batch
        self.uid = u_id
        print(
            f'The class {ViolinPlot.__name__} has been initialzed with values: {self.data_batch} | {self.label} | {self.filename}')

    def _makeViolinPlot(self):
        fig, ax = plt.subplots()
        plt.xlabel('Sample data')
        plt.xlabel('Observed Values')
        plt.title(f'Violin Plot for {self.label}')
        plt.text(0.08, 0.90, self.uid, {
                 'color': 'b', 'fontsize': 7, 'fontstyle': 'italic'}, transform=ax.transAxes)
        plt.violinplot(self.data_batch, showmedians=True,
                       showmeans=True, showextrema=True)
        plt.savefig(self.filename, bbox_inches='tight')
        plt.close()

    @staticmethod
    def makeBatchViolinPlot(data_bach, filename, label, uid):
        filename = filename+'.pdf'
        fig, ax = plt.subplots()
        plt.xlabel('Sample data')
        plt.xlabel('Observed Values')
        plt.title(f'Violin Plot for {label}')
        plt.text(0.08, 0.90, uid, {
                 'color': 'b', 'fontsize': 7, 'fontstyle': 'italic'}, transform=ax.transAxes)
        for data in data_bach:
            plt.violinplot(data_bach, showmedians=True,
                           showmeans=True, showextrema=True)
        plt.savefig(filename, bbox_inches='tight')
        plt.close()

    @staticmethod
    def makeViolinPlot(data_bach, filename, label,uid):
        filename = filename+'.pdf'
        fig, ax = plt.subplots()
        plt.xlabel('Sample data')
        plt.xlabel('Observed Values')
        plt.title(f'Violin Plot for {label}')
        plt.text(0.08, 0.08, uid, {
                 'color': 'b', 'fontsize': 7, 'fontstyle': 'italic'}, transform=ax.transAxes)
        plt.violinplot(data_bach, showmedians=True,
                       showmeans=True, showextrema=True)
        plt.savefig(filename, bbox_inches='tight')
        plt.close()
