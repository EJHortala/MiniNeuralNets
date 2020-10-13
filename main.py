from Backpropagation import backpropagation
from Perceptron import *


if __name__ == "__main__":
    training_inputs = np.array([[1, 1, 0, 0],
                                [0, 0, 1, 0],
                                [1, 0, 1, 0],
                                [0, 0, 0, 1],
                                [1, 0, 1, 1],
                                [0, 1, 1, 1]])

    training_outputs = np.array([0, 0, 0, 1, 1, 1])

    nn = Perceptron(activation=sigmoid)
    nn.train(training_inputs, training_outputs, iterations=10000, train_func=backpropagation)

    input_vals = np.array([0, 1, 1, 0])

    _, prediction, error = nn.predict(input_vals)
    print("INPUT \n {}".format(input_vals))
    print("PREDICTION \t\t ERROR \n {} \t\t\t {}".format(prediction, error))
