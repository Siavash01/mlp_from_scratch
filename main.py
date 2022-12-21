import sys
sys.path.append('./neuralnetwork')
from neuralnetwork import NeuralNetwork


if __name__ == "__main__":
    nn = NeuralNetwork(nu_inps = 2, num_outs = 2)
    nn.fit(x = [1,2,3], y = [])
    nn.add_layer(activation = 'sigmoid', num_of_neurans = 2, num_of_inp_weights_to_each_neuran = 3)
    #nn.add_layer(activation = 'sigmoid', num_of_neurans = 2, num_of_inp_weights_to_each_neuran = 4)
    print(nn.layers[0].neurans)
    print("*****************")
    print(nn.x)
    print("*****************")
    print(nn.layers[0].weights)
    print("*****************")
    nn.forward()
    print(nn.layers[0].neurans)