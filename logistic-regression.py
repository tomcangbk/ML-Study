from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt
np.random.seed(2)

X = np.array([[0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50, 
              2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50]])
y = np.array([[-1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1]])
y = y.T
X = np.concatenate((np.ones((1, X.shape[1])), X), axis = 0)
X = X.T
np.dot(w.T, X[1])

# Sigmoid function
def sigmoid(s):
    return 1/(1 + np.exp(-s))
    
def logistic_regression(X, y, iters = 10000, eta = 0.05):
    w = np.array([[0.0],
             [0.0]])
    N = X.shape[0]
    
    for j in range(iters):
        E_gradient = np.array([[0.],
                              [0.]])
        for i in range(N):
            temp = y[i] * X[i] / (1 + np.exp(y[i] * np.dot(w.T, X[i])))
            temp = np.array([temp])
            temp = temp.T

            E_gradient += temp

        E_gradient = - E_gradient / N
        
        w -= eta * E_gradient

    return w
w = logistic_regression(X, y)

# Result w of training data
# array([[-4.07629178],[ 1.50416419]])
