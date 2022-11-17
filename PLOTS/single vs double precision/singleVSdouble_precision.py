"""
Evaluate g(t) = e^(−t) * (sin(2πt)+2) at 501 equidistant points between 0 and 1, using
the usual double precision as well as single precision and plotting the differences.
"""

import numpy as np
import matplotlib.pyplot as plt
from math import exp, pi, sin 


points = []
i = 0
while i <= 1:
    points.append(i)
    i += .002

single_x_axis = np.array(points, dtype="float32")
double_x_axis = np.array(points, dtype="float64")

g_t_single = [ (exp(-t) * (sin(2*pi*t) + 2)) for t in single_x_axis ]
g_t_double = [ (exp(-t) * (sin(2*pi*t) + 2)) for t in double_x_axis ]

round_error_list = []
for y_double, y_single in zip(g_t_double, g_t_single):
    round_err = (y_double - y_single) / (y_double)
    round_error_list.append(round_err)




plt.plot(double_x_axis, round_error_list)
plt.title("Error in sampling exp(−t)(sin(2π t)+2) in single precision")
plt.xlabel("t")
plt.ylabel("round error")
plt.show()
