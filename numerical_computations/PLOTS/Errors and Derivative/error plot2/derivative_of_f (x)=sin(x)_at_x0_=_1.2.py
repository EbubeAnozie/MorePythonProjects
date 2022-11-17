"""
Question:
Carry out calculations for approximating the
derivative of the function f (x)= sin(x) evaluated at x0 = 1.2
using method derived from Taylor's series.
Plot the graph of increasing point interval, h,
against the corresponding absolute errors.
"""

import matplotlib.pyplot as plt
from math import sin, cos


Yprime = cos(1.2)

array_h = []
i = -20
while i <= 0:
    array_h.append(10**i)
    i += 0.5


error_arr = []
for h in array_h:
    Y1prime = (sin(1.2 + h) - sin(1.2))/h
    error_arr.append(abs(Yprime - Y1prime))


d_error = [(sin(1.2) / 2) * h for h in array_h]
y_arr = [error_arr, [cos(1.2) for i in error_arr], d_error]
label_arr = ["absolute error", "exact value", "discretization error"]



for y, label in zip(y_arr, label_arr):
    plt.loglog(array_h, y, label=label)

gragh = plt.loglog(array_h, [(sin(1.2 + h) - sin(1.2))/h for h in array_h],\
                 label="approximation", linestyle="dashed")

plt.xlabel("log(h)")
plt.title("log-log graph: derivative of the function f (x)= sin(x) evaluated at x0 = 1.2 for decreasing h")
plt.legend()
plt.show()
