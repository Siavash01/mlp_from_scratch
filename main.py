import random
import numpy as np

class Layer:
    def __init__(self, activation : str, num_of_neurans : int):
        self.activation : str = activation
        self.num_of_neurans : int = num_of_neurans
        self._initial_weights()

class NeuralNetwork:
    def __init__(self, nu_inps, nu_nau_in_hid, num_outs):
        self.layers = list()
        self.nu_inps = nu_inps # number of inputs
        self.nu_nau_in_hid = nu_nau_in_hid # number of neurans in hidden layer
        self.num_outs = num_outs # number of outputs

    def add_layer(self, activation : str, num_of_neurans : int):
        self.layers.append(Layer(activation = activation, num_of_neurans = num_of_neurans))



# Initialize a network
def initialize_network(n_inputs, n_hidden, n_outputs):
	network = list()
	hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	network.append(hidden_layer)
	output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(output_layer)
	return network