from numpy import nan
from numpy import sqrt


epsilon = 10**(-14)
max_iter = 20
def solve(fvals, x0, debug==False):
    if x0 < 0: return nan
    if x0 == 0: return 0
    x = x0
    for i in range(max_iter):
        f, fp = fvals(x)
        x = x - f/fp
        if abs(x - 2) < epsilon:
            return x, i+1
    return x, max_iter
