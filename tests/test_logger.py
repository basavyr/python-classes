from datetime import datetime
import uuid

import sys
sys.path.append('src/')
sys.path.append('../src/')

import logger

path = '../out/logs/'
filename = path+'text_log-'+str(int(datetime.utcnow().timestamp()))

log = logger.Logger(filename)


def now():
    return datetime.utcnow()


def u_id():
    return uuid.uuid4()


def createLogData(data_batch, id):
    log_data = [str(now().timestamp())+'-'+str(id), u_id(), now()]
    data_batch.append(log_data)


log_data_batch = []

for _id in range(1000):
    createLogData(log_data_batch, _id)

log.writeLogData(log_data_batch)
