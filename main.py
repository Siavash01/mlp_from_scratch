import sys
sys.path.append('./neuralnetwork')
from neuralnetwork import NeuralNetwork


if __name__ == "__main__":
    nn = NeuralNetwork(nu_inps = 2, num_outs = 2)