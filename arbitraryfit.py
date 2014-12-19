import numpy as np
import math
import mpmath as mp
import pickle
import sys
import matplotlib.pyplot as plt
from scipy.optimize import fmin
from scipy.stats import norm

def arbitraryfit(x,y,color,function_of_parameter_array_and_variable_x,parameters_guess):
    
    y = np.array(y)    
    x = np.array(x)

    # error function to minimize
    error = lambda parameters, x, y: ((function_of_parameter_array_and_variable_x(parameters,x)-y)**2).sum()

    # fitting the data with fmin
    parameters = fmin(error, parameters_guess, args=(x,y))

    print 'estimator parameters: ', parameters

    #change this so that your function fits nicely on screen... start, stop, count
    xx = np.linspace(0,16,1000)
    plt.plot(x,y,'bo')
    plt.plot(xx, function_of_parameter_array_and_variable_x(parameters,xx),color, label = 'fit')
    plt.legend()
    return parameters


if __name__ == "__main__":

  #An example!  choose some arbitrary x values, y is normal with noise, fit a normal pdf to those values
  x = np.random.uniform(0,16,100)
  y = norm.pdf(x,loc=8,scale=2) + np.random.normal(loc=0, scale=0.01, size=100) #gaussian + noise

  fitparams = arbitraryfit(x,y, 'r', lambda c,x: norm.pdf(x,loc=c[0],scale=c[1]), np.random.rand(2))

  plt.show()
