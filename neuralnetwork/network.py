import random
import numpy as np

class Layer:
    def __init__(self, activation : str, num_of_neurans : int, num_of_inp_weights_to_each_neuran : int):
        self.activation : str = activation
        self.num_of_neurans : int = num_of_neurans
        self.num_of_inp_weights_to_each_neuran : int = num_of_inp_weights_to_each_neuran
        self.neurans = [None for i in range(num_of_neurans)]
        self._initial_weights()

    def _initial_weights(self):
        self.weights = [[random.random() for i in range(self.num_of_neurans + 1)] for j in range(self.num_of_inp_weights_to_each_neuran)]

class NeuralNetwork:
    def __init__(self, nu_inps : int, num_outs : int, alpha : int = 0.1):
        self.layers = list()
        self.nu_inps = nu_inps # number of inputs
        self.num_outs = num_outs # number of outputs
        self.alpha = alpha # learning rate

    def add_layer(self, activation : str, num_of_neurans : int, num_of_inp_weights_to_each_neuran : int):
        self.layers.append(Layer(activation = activation, num_of_neurans = num_of_neurans, num_of_inp_weights_to_each_neuran = num_of_inp_weights_to_each_neuran))

    def fit(self, x, y, epochs = 1000):
        self.x = x
        self.y = y
        self.epochs = epochs

    def forward(self):
        for i in range(0, self.layers[0].num_of_neurans):
            self.layers[0].neurans[i] = np.dot(self.x, self.layers[0].weights)
        # for i in np.arange(0, self.nu_inps):
        #     self.layers[0].neurans = np.dot(self.x, self.layers[0].weights)
        # for i in np.arange(0, len(self.layers)):
        #     pass

    def gradient_descent(self):
        pass

    def train(self):
        for i in range(self.epochs):
            pass