import numpy as np

class neuron:
    def __init__(self,n_inputs):
        self.w = np.random.rand(n_inputs)
        self.b = 0.0

    def forward(self, x):
        z = np.dot(x, self.w) + self.b
        y = 1/(1+np.exp(-z))
        return y
    
    def num_params(self):
        return len(self.w) + 1
    
n = neuron(3)
print(n.w)
print(n.w.shape)
print(n.b)