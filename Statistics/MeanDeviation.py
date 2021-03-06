import numpy as np
from Calculator.Subtraction import subtraction

class MeanDeviation():
    @staticmethod
    def mean_deviation(data):
        return np.mean(np.absolute(data - np.mean(data)))