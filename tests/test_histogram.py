import importlib
import numpy as np

import sys
sys.path.append('src/')
sys.path.append('../src/')

import histogram as hst

def GenerateDataBatch(N):
    data_batch = []
    for n_id in range(N):
        current_data = hst.X_INT
        data_batch.append(current_data)
        importlib.reload(hst)
    return data_batch


path = 'out/'
ext = '.pdf'

for plot_id in range(10):
    data_batch = GenerateDataBatch(3)
    filename = path+'hist-'+str(plot_id+1)+ext
    label = 'data-id'+str(plot_id)
    hst.makeHistogram(data_batch, 75, label, filename)
