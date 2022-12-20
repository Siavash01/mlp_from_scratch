import numpy as np

def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))

def sigmoid_deriative(x):
    return x * (1 - x)

def tanh_deriative():
    pass

def ReLU():
    pass

def ReLU_deriative():
    pass