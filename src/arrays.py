import numpy as np
import random as rd


class Arrays:
    def __init__(self, size, left, right):
        self.size = size
        self.left = left
        self.right = right
    LEFT = 0
    RIGHT = 100
    SIZE = 120

    def giveArray(self):
        rand_list = [rd.randrange(self.left, self.right)
                     for id in range(self.size+1)]
        return rand_list

    @staticmethod
    def generateArray(size, left, right):
        rand_list = []
        for x in range(size+1):
            rnd_number = rd.randrange(left, right+1)
            rand_list.append(rnd_number)
        return rand_list

    @staticmethod
    def generateNormalArray(size, mean, std_dev):
        data = np.random.normal(mean, std_dev, size)
        return data
