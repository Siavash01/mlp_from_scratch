import random
import numpy as np

class Layer:
    def __init__(self, activation : str, num_of_neurons : int, num_of_inp_weights_to_each_neuran : int):
        self.activation : str = activation
        self.num_of_neurons : int = num_of_neurons
        self.num_of_inp_weights_to_each_neuran : int = num_of_inp_weights_to_each_neuran
        self.neurons = [None for i in range(num_of_neurons)]
        self._initial_weights()

    def _initial_weights(self):
        # self.weights = [[random.random() for i in range(self.num_of_neurons + 1)] for j in range(self.num_of_inp_weights_to_each_neuran)]
        self.weights = [[random.random() for i in range(self.num_of_neurons)] for j in range(self.num_of_inp_weights_to_each_neuran)] # no bias

class NeuralNetwork:
    def __init__(self, nu_inps : int, num_outs : int, alpha : int = 0.1):
        self.layers = list()
        self.nu_inps = nu_inps # number of inputs
        self.num_outs = num_outs # number of outputs
        self.alpha = alpha # learning rate

    def add_layer(self, activation : str, num_of_neurons : int, num_of_inp_weights_to_each_neuran : int):
        self.layers.append(Layer(activation = activation, num_of_neurons = num_of_neurons, num_of_inp_weights_to_each_neuran = num_of_inp_weights_to_each_neuran))

    def fit(self, x, y, epochs = 1000):
        self.x = x
        self.y = y
        self.epochs = epochs

    def forward(self):
        '''
        matrix multipication of inputs and first hidden layer weigts witch does the job of creating first hidden layer neurons
        '''
        self.layers[0].neurons = np.dot(self.x, self.layers[0].weights)
        for i in range(1, len(self.layers)):
            self.layers[i].neurons = np.dot(self.layers[i-1].neurons, self.layers[i].weights)

    def gradient_descent(self):
        pass

    def train(self):
        for i in range(self.epochs):
            pass