import numpy

class Network:

    """
    Initializing the Network. layer_sizes is a vector which contains a list of the number of nodes
    in each layer of the neural network.
    """
    def __init__(self,layer_sizes):

        self.num_of_layers = size(layer_sizes)
        self.layer_sizes   = layer_sizes
        self.weights = [numpy.random.rand(x,y) for x,y in zip(layer_sizes[:-1],layer_sizes[1:])]
        self.biases  = [numpy.random.rand(x,1) for x in layer_sizes[1:]]


    """
    Returns output based on the trained neural network. The input is a n-space vector a, which contains all
    the input features from the first layer.
    """
    def feedforward_output(self,a):

        for w,b in zip(self.weights,self.biases):
            a = sigmoid(numpy.dot(w,a) + b);

        return a
    
    """
    Trains the neural netowrk by dividing training set into batches and then updating the neural network by
    calling the update_neural_network function on all batches for epoch times. 'eta' is the learning rate.
    """
    def neural_network_trainer(self,training_instances, epochs, eta,batch_size):

        for e in xrange(epochs):

            random.shuffle(training_instances)
            batches = [training_instances[i:i+batch_size]
                       for i in xrange(0,n,batch_size)]

            for batch in batches:

                self.update_neural_network(batch, eta)

    """
    Updates the neural network for each batch, instance by instance. It updates the biases and the weights.
    """
    def update_neural_network(self,batch,eta):

        delta_b = [numpy.zeros(i.shape) for i in self.biases]
        delta_w = [numpy.zeros(i.shape) for i in self.weights]

        for x,y in batch:

            temp_delta_b, temp_delta_w = self.back_propogate(x,y)
            delta_b = [i+j for i,j in zip(delta_b,temp_delta_b)]
            delta_w = [i+j for i,j in zip(delta_w,temp_delta_w)]

        self.biases  = [b-(eta/len(batch)*db) for b,dw in zip(self.biases,delta_b)]
        self.weights = [w-(eta/len(batch))*dw for w,dw in zip(self.weights,delta_w)]


    """
    Implements the back propogating algorithm and returns the deltas for the weights and biases for a
    single training example.x is the feature vector,i.e., the vector consisting of the input to the first
    layer of the neural network. y is the label of the instance that x represents.
    """
    def back_propogate(self,x,y):

        delta_b = [numpy.zeros(i.shape) for i in self.biases]
        delta_w = [numpy.zeros(i.shape) for i in self.weights]

        activation = x
        activation_values = [x]
        zs = []

        for b,w in zip(self.biases,self.weights):

            z = numpy.dot(w,x) + b
            zs.append(z)
            activation = sigmoid(z)
            activation_values.append(activation)

        delta = self.cost_derivative(activation_values[-1],y) * self.sigmoid_derivative_vectorize(zs[-1])

        delta_b[-1] = delta
        delta_w[-1] = numpy.dot(delta, activation_values[-2].transpose())

        for i in xrange(2,self.num_of_layers):

            z = zs[-i]
            sdv = sigmoid_derivative_vectorize(z)
            delta = numpy.dot(self.weights[-i+1].transpose(),delta) * sdv
            delta_b[-i] = delta
            delta_w[-i] = numpy.dot(delta,activation_values[-i-1].transpose())

        return (delta_b,delta_w)

    """
    Derivative of the cost function used. Depends on the problem the neural net is trying to solve.
    Basically, the only thing that needs to change.
    """
    def cost_derivative(self,activation_values,y):

        return activation_values - y;

    """
    Basic sigmoid function
    """
    def sigmoid(self,z):

        return 1.0/(1.0+numpy.exp(-z))


    def sigmoid_prime(self,z):

        return sigmoid(z)*(1-sigmoid(z))

    sigmoid_derivative_vectorize = numpy.vectorize(sigmoid_prime)

    """Return the number of test inputs for which the neural
    network outputs the correct result. Note that the neural
    network's output is assumed to be the index of whichever
    neuron in the final layer has the highest activation."""
    
    def evaluate(self, test_data):
    
        test_results = [(numpy.argmax(self.feedforward(x)), y)
                    for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)


def main():
    print "Hello"


main()




