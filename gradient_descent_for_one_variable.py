import math
import numpy as np
# Function is f(x) = x^2 + 5sinx
def derivative(x):
      return 2*x + 5*np.cos(x)

def var_of_function(x):
      return x**2 + 5*np.sin(x)

def GD(x0, alpha):
      t = 0
      x = x0
      while True:
            f1 = var_of_function(x)
            x = x - alpha*derivative(x)
            f2 = var_of_function(x)
            print(x, f1)
            t+=1
            print(t)
            if abs(f1 - f2) <= 1e-3:
                  break
      return val_of_function(x), t
val, times = GD(-5, 0.05)

print(val, times)
