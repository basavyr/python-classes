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

import histogram as hst

def GenerateDataBatch(N):
    data_batch = []
    for n_id in range(N):
        current_data = hst.X_INT
        data_batch.append(current_data)
        importlib.reload(hst)
    return data_batch


path = '../out/'
ext = '.pdf'
log_ext = '.log'
log_name = path+'histogram-build-process-'+str(os.system())+log_ext

OS_VERSION = os.system()
PROC_INFO = os.uname().processor
AARCH = os.uname().machine
SYSTEM_INFO = os.uname().version
PY_MAJ = sys.version_info.major
PY_MIN = sys.version_info.minor
PYTHON_BUILD = str(PY_MAJ)+'.'+str(PY_MIN)

log_file = open(log_name, 'w')
total_time=0.0
for plot_id in range(3):
    start=time.time()
    unique_id = uuid.uuid4().hex
    data_batch = GenerateDataBatch(3)
    filename = path+'hist-'+str(plot_id+1)+ext
    label = 'data-id'+str(plot_id)
    hst.makeHistogram(data_batch, 75, label, filename)
    end=time.time()
    total_time=total_time+(end-start)
    log_info = 'PLOT_ID: '+str(plot_id+1)+'-'+str(unique_id) + ' GET_TIME: @'+str(
        datetime.utcnow()) + ' OS: '+OS_VERSION+' AARCH: ' + AARCH + ' SYS_INFO: ' + PROC_INFO+' PY_VER: '+PYTHON_BUILD+' PROC_TIME: '+str(end-start)+'\n'
    log_file.write(log_info)

log_file.close()
print(f'All histograms have been generated. Process took {round(total_time,3)} seconds...')