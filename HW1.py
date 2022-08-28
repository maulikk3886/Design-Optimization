# minimization problem
import scipy as sp
import numpy as np
# equation to minimize
func = ((x1 - x3)**2)+((x2 + x3 - 2)**2)+((x4 - 1)**2)+((x5 - 1)**2)
# subject to  equations
x1 + (3 * x2) = 0
x3 + x4 - (2 * x5) = 0
x2 - x5 = 0
# domain of xi is from -10 to 10
sp.optimize()
