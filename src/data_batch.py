import numpy as np
import random as rd
import matplotlib.pyplot as plt


class DataBatch:
    def __init__(self, batch_size, left_limit, right_limit, data_size, mean, std_dev, init_type):
        self.batch_size = batch_size
        self.batch_type = 'normal'
        self.left_limit = left_limit
        self.right_limit = right_limit
        self.mean = mean
        self.std_dev = std_dev
        self.data_size = data_size
        if(init_type == 'verbose'):
            print(
                f'The class {DataBatch.__name__} has a size of: {self.batch_size}')

    poisson_tp = 'poisson'
    normal_tp = 'normal'
    random_tp = 'random'
    gamma_tp = 'gamma'
    student_tp = 'standard_t'

    def _createDB(self, distribution_type):
        db = []
        self.batch_type = distribution_type
        error = 'The data batch structure is not a valid type!'
        if(self.batch_type == 'random'):
            for _ in range(self.batch_size):
                rand_data = list(np.random.randint(
                    self.left_limit, self.right_limit, self.data_size))
                db.append(rand_data)
            return db
        if(self.batch_type == 'normal'):
            for _ in range(self.batch_size):
                rand_normal_data = [int(x) for x in np.random.normal(
                    self.mean, self.std_dev, self.data_size)]
                db.append(rand_normal_data)
            return db
        if(self.batch_type == 'gamma'):
            for _ in range(self.batch_size):
                rand_gamma_data = [int(x) for x in np.random.gamma(
                    self.std_dev, 1, self.data_size)]
                db.append(rand_gamma_data)
            return db
        if(self.batch_type == 'poisson'):
            for _ in range(self.batch_size):
                rand_possion_data = [int(x) for x in np.random.poisson(
                    self.std_dev, self.data_size)]
                db.append(rand_possion_data)
            return db
        if(self.batch_type == 'standard_t'):
            for _ in range(self.batch_size):
                rand_student_data = [int(x) for x in np.random.standard_t(
                    self.std_dev, self.data_size)]
                db.append(rand_student_data)
            return db
        return (error, db)
