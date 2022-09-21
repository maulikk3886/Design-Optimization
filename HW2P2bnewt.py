import numpy as np
import matplotlib.pyplot as mpl
def f(x):
    return ((2 - (2*x[0]) - (3*x[1]))**2) + (x[0]**2) + ((x[1]-1)**2)
def gradient(x):
    return np.array([10*x[0] + 12*x[1] - 8, 12*x[0] + 20*x[1] - 14])
def hessian(x):
    return np.array([[10,12],[12,20]])

t = 0.5
x_ini = np.array([1,1])
newt_values = [] # output value list

# Indirect line search
def backtrack(x):
    a1 = np.matmul(gradient(x).T,np.linalg.inv(hessian(x)))
    a2 = np.matmul(a1,gradient(x))
    alpha = 1
    while f(x - alpha*gradient(x)) > (f(x) - (t* a2*alpha)): # Newton's method
        alpha = 0.5 * alpha
    return alpha
#print(f(x_ini - alpha*gradient(x_ini)))
#print((f(x_ini) - (t*np.matmul(gradient(x_ini).T,(np.matmul(np.linalg.inv(hessian(x_ini)),gradient(x_ini)))) *alpha)))

while np.linalg.norm(gradient(x_ini)) > 0.0001:  # epsilon  = 0.0001
    alpha = backtrack(x_ini) #step size
    x_ini = x_ini + alpha *(-gradient(x_ini))
    newt_values.append(f(x_ini))

print(x_ini)
print(newt_values)
#print(len(newt_values))
y_ax = []
for i in range(len(newt_values)-1):
    j = np.log10(newt_values[i] - newt_values[-1])
    y_ax.append(j)

x_ax = range(1,len(newt_values))
mpl.plot(x_ax,y_ax)
mpl.show()
