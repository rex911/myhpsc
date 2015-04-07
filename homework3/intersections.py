import numpy as np
from numpy import nan
from numpy import sqrt
from numpy import sin, cos, pi
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


epsilon = 10**(-14)
max_iter = 20
def solve(fvals, x0, debug=False):
    x = x0
    if debug:
        print 'Initial guess: x = %22.15e' %x
    for i in range(max_iter):
        if abs(x - fsolve(lambda x: x*cos(pi*x)-1+0.6*x**2, x0)) < epsilon:
            return x, i
        f, fp = fvals(x)
        x = x - f/fp
        if debug:
            print 'After %d iterations, x = %22.15e' %(i+1, x)
    return x, max_iter
# $UWHPSC/codes/homework3/test_code.py 
# To include in newton.py

def fvals_sqrt(x):
    """
    Return f(x) and f'(x) for applying Newton to find a square root.
    """
    f = x*cos(pi*x)-1+0.6*x**2
    fp = cos(pi*x)-sin(pi*x)*pi*x + 1.2*x
    return f, fp

def test1(debug_solve=False):
    """
    Test Newton iteration for the square root with different initial
    conditions.
    """
    for x0 in [-2,-1.5,-1,1.5]:
        print " "  # blank line
        #import pdb; pdb.set_trace()
        x,iters = solve(fvals_sqrt, x0, debug=debug_solve)
        print "solve returns x = %22.15e after %i iterations " % (x,iters)
        fx,fpx = fvals_sqrt(x)
        print "the value of f(x) is %22.15e" % fx
        assert abs(x-fsolve(lambda x: x*cos(pi*x)-1+0.6*x**2, x0)) < 1e-14, "*** Unexpected result: x = %22.15e"  % x
        plt.plot(x, 1-0.6*x**2, 'ko')

    # plot curves of the 2 functions
    x = np.linspace(-5,5,1000)
    f = x*np.cos(np.pi*x)
    g=1-0.6*x**2
    plt.plot(x,f, 'r')
    plt.plot(x,g, 'b')


if __name__ == '__main__':
    test1()
