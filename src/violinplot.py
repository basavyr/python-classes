import matplotlib.pyplot as plt
from datetime import datetime


class ViolinPlot:
    def __init__(self, data_batch, filename, label):
        self.filename = filename
        self.label = label
        self.data_batch = data_batch

    def _makeViolinPlot(self):
        fig, ax = plt.subplots()
        plt.xlabel('Sample data')
        plt.xlabel('Observed Values')
        plt.title(f'Violin Plot for {self.label}')
        for data in self.data_batch:
            print(data)
        plt.violinplot(self.data_batch, showmedians=True,
                       showmeans=True, showextrema=True)
        plt.savefig(self.filename, bbox_inches='tight')
        plt.close()

    @staticmethod
    def makeViolinPlot(data_bach, filename, label):
        fig, ax = plt.subplots()
        plt.xlabel('Sample data')
        plt.xlabel('Observed Values')
        plt.title(f'Violin Plot for {label}')
        for data in data_bach:
            print(data)
        plt.violinplot(data_bach, showmedians=True,
                       showmeans=True, showextrema=True)
        plt.savefig(filename, bbox_inches='tight')
        plt.close()


my_data = [[1, 2, 3], [1, 2, 2, 3, 4, 5, 3, 2, 2], [1, 2, 2, 3, 4, 5, 3, 2, 2]]
my_file = 'my_vp.pdf'
my_label = 'data-'+str(int(datetime.utcnow().timestamp()))

my_vp = ViolinPlot(my_data, my_file, my_label)
my_vp._makeViolinPlot()
