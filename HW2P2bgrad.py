import numpy as np
import matplotlib.pyplot as mpl
def f(x):
    return ((2 - (2*x[0]) - (3*x[1]))**2) + (x[0]**2) + ((x[1]-1)**2)
def gradient(x):
    return np.array([10*x[0] + 12*x[1] - 8, 12*x[0] + 20*x[1] - 14])
#def hessian(x):
    #return np.matrix([[10,12],[12,20]])

t = 0.5
x_ini = np.array([1,1])
gr_values = [] # output value list

# Indirect line search
def backtrack(x):
    alpha = 1
    while f(x - alpha*gradient(x)) > f(x) - (t * np.matmul(gradient(x).T,gradient(x)) * alpha): # Gradient descent algorithm
        alpha = 0.5 * alpha
    return alpha


while np.linalg.norm(gradient(x_ini)) > 0.0001:  # epsilon  = 0.0001
    alpha = backtrack(x_ini) #step size
    x_ini = x_ini + alpha * (-gradient(x_ini))
    gr_values.append(f(x_ini))

#print(x_ini)
#print(gr_values)
#print(len(gr_values))
y_ax = []
for i in range(len(gr_values)-1):
    j = np.log10(gr_values[i] - gr_values[-1])
    y_ax.append(j)

x_ax = range(1,len(gr_values))
mpl.plot(x_ax,y_ax)
