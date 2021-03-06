from numpy import nan
from numpy import sqrt
from scipy.optimize import fsolve

epsilon = 10**(-14)
max_iter = 20
def solve(fvals, x0, debug=False):
    if x0 < 0: return nan
    if x0 == 0: return 0
    x = x0
    if debug:
        print 'Initial guess: x = %f' %x
    for i in range(max_iter):
        if abs(x - fsolve(lambda x: x**2-4, x0)) < epsilon:
            return x, i
        f, fp = fvals(x)
        x = x - f/fp
        if debug:
            print 'After %d iterations, x = %f' %(i+1, x)
    return x, max_iter
# $UWHPSC/codes/homework3/test_code.py 
# To include in newton.py

def fvals_sqrt(x):
    """
    Return f(x) and f'(x) for applying Newton to find a square root.
    """
    f = x**2 - 4.
    fp = 2.*x
    return f, fp

def test1(debug_solve=False):
    """
    Test Newton iteration for the square root with different initial
    conditions.
    """
    from numpy import sqrt
    for x0 in [1., 2., 100.]:
        print " "  # blank line
        x,iters = solve(fvals_sqrt, x0, debug=debug_solve)
        print "solve returns x = %22.15e after %i iterations " % (x,iters)
        fx,fpx = fvals_sqrt(x)
        print "the value of f(x) is %22.15e" % fx
        assert abs(x-2.) < 1e-14, "*** Unexpected result: x = %22.15e"  % x


if __name__ == '__main__':
    test1()
