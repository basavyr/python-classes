import importlib
import numpy as np


import sys
import platform as os
from datetime import datetime
import random as rd
import uuid
import time

sys.path.append('src/')
sys.path.append('../src/')

import data_batch
import histogram as hst
import logger 


path = '../out/hists/'
log_path='../out/logs/'
ext = '.pdf'
log_ext = '.log'
log_name = log_path+'histogram-build-process-'+str(int(datetime.utcnow().timestamp()))+'-'+str(os.system())
plot_name=path+'hist-'+str(int(datetime.utcnow().timestamp()))+'-'+str(os.system())

log_data=[]
logfile=logger.Logger(log_name)

for id in range(50):
    logfile.createLogData(log_data,id)
    plot_label=log_data[id][1]
    db = data_batch.DataBatch(4, 0, 100, 100, 0, 6, 'silent')._createDB(data_batch.DataBatch.poisson_tp)
    my_hist=hst.Histogram(db,30,plot_name+'-'+str(id),'hist-'+str(id),plot_label)
    my_hist._makeHistogram()

logfile.writeLogData(log_data)