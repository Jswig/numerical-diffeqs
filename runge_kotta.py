# runge_kotta.py
#
# Anders Poirel
# apoirel@ucsc.edu
# 17-02-2019


import math
from matplotlib import pyplot

def solve_runge_kotta(f, a, b, c, h):            
    step = (a+b) / h
    t = [a]
    y = [c]

    for i in range(0, h):
        t.append(t[i] + h)
        u1 = y[i]
        u2 = y[i] + 0.5*h * f(t[i], y[i])
        u3 = y[i] + 0.5*h * f(t[i]) + 0.5*h, u2)
        u4 = y[i] + h *f(t[i]+ 0.5*h, u3) 
        y.append(y[i] + (1/6)*h * (f(t[i], u1) + 2*f(t[i] + 0.5*h,  u2) \
            + 2 * f(t[i] + 0.5*h, z3) + f(t[i] + h,  u4)) )
            
    return [t, y]

def plot_approx():
    pass
    # FIXME