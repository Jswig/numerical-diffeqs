# runge_kotta.py
#
# Anders Poirel
# apoirel@ucsc.edu
# 17-02-2019
#
# approximates solution to diff. eq. y'= f(t, y) given an initial value using the fourth-order Runge-Kotta method. Plots and prints table of solution

from matplotlib import pyplot


def solve_runge_kotta(f, a, b, c, n): 
    """  returns a list where the first item the t-values and as second item 
    the approximated y-values. Plots the approximation over the given interval and
    prints table of approximations up to 3 decimal places\n
    Parameters: f: numeric-valued function taking 2 parameters, a: , b: endpoint of interval, c: initial value, n: number of points to approximate
    """           
    h = (a + b)/n
    t = [a]
    y = [c]

    for i in range(0, n):
        t.append(t[i] + h)
        
        # intermediary calculations
        u1 = y[i]
        u2 = y[i] + 0.5 * h * f(t[i], y[i])
        u3 = y[i] + 0.5 * h * f(t[i] + 0.5 * h, u2)
        u4 = y[i] + h * f(t[i] + 0.5 * h, u3) 
        
        y.append(y[i] + (1/6) * h * (f(t[i], u1) + 2 * f(t[i] + 0.5 * h,  u2) \
            + 2 * f(t[i] + 0.5 * h, u3) + f(t[i] + h,  u4)) )

    pyplot.scatter(t,y)
    
    print("t-values    y-values")
    for i in range(0, len(t)):
        print("%10.3f    %10.3f" % (t[i], y[i]))    
    
    return [t, y]
