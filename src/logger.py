import platform as os
from datetime import datetime
import uuid
import sys


class Logger:
    ext = '.log'

    def __init__(self, filename):
        self.filename = filename+Logger.ext
        self.logfile = open(self.filename, 'w')
        print(f'File {self.filename} opened successfully...')

    def __del__(self):
        self.logfile.close()
        print(f'File {self.filename} closed successfully...')

    def now(self):
        return datetime.utcnow()

    def u_id(self):
        return uuid.uuid4()

    def createLogData(self, data_batch, id):
        log_data = [str(int(self.now().timestamp()))+'-' +
                    str(id), self.u_id(), self.now()]
        data_batch.append(log_data)

    def writeLine(self, content):
        self.logfile.write(content)
        self.logfile.write('\n')

    def writeLog(self, log_data):
        log_line = f'ID: {log_data[0]} UUID: {log_data[1]} GEN_TIME @{log_data[2]} OS: {os.system()} SYSTEM: {os.machine()} AARCH: {os.uname().processor}'
        self.writeLine(log_line)

    def writeLogData(self, log_batch_data):
        for log_data in log_batch_data:
            self.writeLog(log_data)
        print('The log file content was generated...')
