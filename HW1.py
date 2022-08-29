# minimization problem
from scipy.optimize import minimize
import numpy as np
# equation to minimize
def func(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    x5 = x[4]
    return ((x[0] - x[2])**2)+((x[1] + x[2] - 2)**2)+((x[3] - 1)**2)+((x[4] - 1)**2)
# subject to  equations
# defining constraints
def constraint1(x):
    return x[0] + (3 * x[1])
def constraint2(x):
    return x[2] + x[3] - (2 * x[4])
def constraint3(x):
    return x[1] - x[4]
x0 = [1,2,3,4,5]
print(func(x0))
# domain of xi is from -10 to 10
limits = (-10.0,10.0)
boundary = (limits,limits,limits,limits,limits)
cons1 = {'type':'eq', 'fun': constraint1}
cons2 = {'type':'eq', 'fun': constraint2}
cons3 = {'type':'eq', 'fun': constraint3}
const = [cons1,cons2,cons3]

Solution = minimize(func,x0,bounds = boundary,constraints = const)
print(Solution)
