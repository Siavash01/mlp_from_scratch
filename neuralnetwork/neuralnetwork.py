import random
import numpy as np

class Layer:
    def __init__(self, activation : str, num_of_neurans : int, num_of_input_weights : int):
        self.activation : str = activation
        self.num_of_neurans : int = num_of_neurans
        self.num_of_input_weights : int = num_of_input_weights
        self._initial_weights()

    def _initial_weights(self):
        self.weights = [[random.random() for i in range(self.num_of_neurans + 1)] for j in range(self.num_of_input_weights)]

class NeuralNetwork:
    def __init__(self, nu_inps, nu_nau_in_hid, num_outs, output_activation : str):
        self.layers = list()
        self.nu_inps = nu_inps # number of inputs
        self.nu_nau_in_hid = nu_nau_in_hid # number of neurans in hidden layer
        self.num_outs = num_outs # number of outputs
        self.output_activation : str = output_activation

    def add_layer(self, activation : str, num_of_neurans : int):
        self.layers.append(Layer(activation = activation, num_of_neurans = num_of_neurans))
