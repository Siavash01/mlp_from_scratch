import random

class NeuralNetwork:
    def __init__(self, nu_inps, nu_nau_in_hid, num_outs):
        self.layers = list()
        self.nu_inps = nu_inps # number of inputs
        self.nu_nau_in_hid = nu_nau_in_hid # number of neurans in hidden layer
        self.num_outs = num_outs # number of outputs
        self._initialize_hidden_layer() # initialize hidden layer (random weights)
        self._initialize_output_layer() # initialize output layer (random weights)

    def _initialize_hidden_layer(self):
        self.layers.append([{'weights': [random.random() for i in range(self.nu_inps + 1)]} for j in range(self.nu_nau_in_hid)])

    def _initialize_output_layer(self):
        self.layers.append([{'weights': [random.random() for i in range(self.nu_nau_in_hid + 1)]} for j in range(self.num_outs)])



# Initialize a network
def initialize_network(n_inputs, n_hidden, n_outputs):
	network = list()
	hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	network.append(hidden_layer)
	output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(output_layer)
	return network