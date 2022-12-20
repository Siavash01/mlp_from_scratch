import sys
sys.path.append('./neuralnetwork')
from neuralnetwork import NeuralNetwork


if __name__ == "__main__":
    nn = NeuralNetwork(nu_inps = 2, num_outs = 2)
    nn.add_layer(activation = 'sigmoid', num_of_neurans = 4, num_of_inp_weights_to_each_neuran = 2)
    nn.add_layer(activation = 'sigmoid', num_of_neurans = 2, num_of_inp_weights_to_each_neuran = 4)