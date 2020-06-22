from datetime import datetime
import sys
sys.path.append('../src/')
sys.path.append('src/')

import data_batch
import violinplot
import logger

path = '../out/violins/'
log_path = '../out/logs/'
filename = path+'violin-'+str(int(datetime.utcnow().timestamp()))
log_filename = log_path+'violin-'+str(int(datetime.utcnow().timestamp()))

# self, batch_size, left_limit, right_limit, data_size, mean, std_dev, init_type
silent = ' '
# db = data_batch.DataBatch(3, 0, 100, 100, 0, 10, silent)._createDB(
#     data_batch.DataBatch.normal_tp)

lg=logger.Logger(log_filename)
log_data_batch=[]

for _id in range(10):
    violinplot.ViolinPlot.makeViolinPlot(data_batch.DataBatch(5, 0, 100, 100, 0, 10, silent)._createDB(data_batch.DataBatch.normal_tp), filename+'-'+str(_id), str(_id)+str(int(datetime.utcnow().timestamp())))
    lg.createLogData(log_data_batch,_id)

lg.writeLogData(log_data_batch)