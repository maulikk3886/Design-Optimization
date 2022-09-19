import numpy as np

def f(x):
    return ((2 - (2*x[0]) - (3*x[1]))**2) + (x[0]**2) + ((x[1]-1)**2)
def gradient(x):
    return np.matrix([10*x[0] + 12*x[1] - 8, 12*x[0] + 20*x[1] - 14])
def hessian(x):
    return np.matrix([[10,12],[12,20]])

t = 0.5
alpha = 0.01

#beta = 0.8
# Indirect line search
def backtrack(x):
    alpha = 1
    while f(x - alpha*gradient(x)) > f(x) - (t * np.matmul(gradient(x).T,-1*gradient(x)) * alpha): # Gradient descent algorithm
        alpha = 0.5 * alpha
    return alpha


while np.linalg.norm(gradient(x)) > 0.001:  # epsilon  = 0.001
    alpha = backtrack(x) #step size
    x = x + alpha * (-gradient(x))
