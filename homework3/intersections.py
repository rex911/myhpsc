from numpy import nan
from numpy import sqrt
from numpy import sin, cos
from scipy.optimize import fsolve

epsilon = 10**(-14)
max_iter = 20
def solve(fvals, x0, debug=False):
    if x0 < 0: return nan
    if x0 == 0: return 0
    x = x0
    if debug:
        print 'Initial guess: x = %22.15e' %x
    for i in range(max_iter):
        if abs(x - fsolve(lambda x: sin(x)-1+x**2, x0)) < epsilon:
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
    f = sin(x)-1+x**2
    fp = cos(x) + 2*x
    return f, fp

def test1(debug_solve=False):
    """
    Test Newton iteration for the square root with different initial
    conditions.
    """
    for x0 in [-0.5, 0.5]:
        print " "  # blank line
        x,iters = solve(fvals_sqrt, x0, debug=debug_solve)
        print "solve returns x = %22.15e after %i iterations " % (x,iters)
        fx,fpx = fvals_sqrt(x)
        print "the value of f(x) is %22.15e" % fx
        assert abs(x-2.) < 1e-14, "*** Unexpected result: x = %22.15e"  % x


if __name__ == '__main__':
    test1()
