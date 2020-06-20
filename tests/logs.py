import random as rd
import uuid
from datetime import datetime
import platform as os
import sys
import numpy as np
import matplotlib.pyplot as plt


OS_VERSION = os.system()
PROC_INFO = os.uname().processor
AARCH = os.uname().machine
SYSTEM_INFO = os.uname().version

PY_MAJ = sys.version_info.major
PY_MIN = sys.version_info.minor

PYTHON_BUILD = str(PY_MAJ)+'.'+str(PY_MIN)

log_name = 'test-'+str(int(datetime.utcnow().timestamp()))
ext = '.log'

plot_name = 'histogram.pdf'

data = [np.random.normal(0, std, 1000) for std in range(5)]


def MakeHistogram(data_batch, filename, label):
    fig, ax = plt.subplots()
    unique_id = uuid.uuid4()
    unix = str(int(datetime.utcnow().timestamp()))
    plt.xlabel('x')
    plt.text(0.03, 0.95, f'@ {unix}',
             transform=ax.transAxes)
    plt.ylabel('Frequency')
    plt.title(f'Histogram-{unique_id}')
    plt.violinplot(data_batch, showextrema=True, showmeans=True,
                   showmedians=True, vert=True)
    # for data in data_batch:
        # plt.hist(data, bins=120, density=False, histtype='bar', label=label,stacked=True,orientation='vertical',align='mid')
    # plt.legend(loc='best')
    plt.savefig(filename, bbox_inches='tight')
    plt.close()


def GenerateLogFile(filename, id):
    filename = filename+'-'+str(id)+ext
    log_file = open(filename, 'w')

    for log_line in range(100):
        unique_id = uuid.uuid4().hex
        log_info = 'LOG_ID: '+str(log_line+1)+'-'+str(unique_id) + ' GET_TIME: @'+str(
            datetime.utcnow()) + ' OS: '+OS_VERSION+' AARCH: ' + AARCH + ' SYS_INFO: ' + PROC_INFO+' PY_VER: '+PYTHON_BUILD+'\n'
        log_file.write(log_info)

    log_file.close()


MakeHistogram(data, plot_name, 'data-1')

# GenerateLogFile(log_name, 1)
