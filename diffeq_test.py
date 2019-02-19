# diffeq_test.py
#
# Anders Poirel
# apoirel@ucsc.edu
# 18-02-2019
#
# Tests implementation of the fourth-order Runge-Kotta method

from runge_kotta import solve_runge_kotta
import math

solve_runge_kotta(lambda x, y: y, 0, 10, 1, 50);

