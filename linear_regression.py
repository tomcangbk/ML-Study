from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt

# height (cm)
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# weight (kg)
y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w_0 = w[0][0]
w_1 = w[1][0]
# Theo cac gia tri w_0, w_1 da tinh =>muon du doan gia tri dau(x) vao thi su dung:
# y = w_1*x + w_0; vd tinh y khi x = 167
y_167 = w_1*167 +w_0
