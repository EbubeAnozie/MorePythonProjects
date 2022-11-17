"""
Question:
Carry out calculations for approximating the
derivative of the function f (x)= e−2x evaluated at x0 = 0.5
using method derived from Taylor's series.
Plot the graph of increasing point interval, h,
against the corresponding absolute errors.
"""

import matplotlib.pyplot as plt
from math import exp, log


Yprime = -2*exp(-2*0.5)  # at x=0.5

array_h = []
i = -20
while i <= 0:
    array_h.append(10**i)
    i += 0.5

array_log_h = [log(i) for i in array_h]

error_arr = []
for h in array_h:
   Y1prime = (exp(-2*(0.5 + h)) - exp(-2*0.5))/h
   abs_error = abs(Yprime - Y1prime)
   error_arr.append(abs_error)

##for index in range(len(error_arr)):
##                     print(f"{array_h[index]:>5} | {error_arr[index]:>5}")


y_arr = [error_arr, [Yprime for occurence in error_arr]]
label_arr = ["absolute error", "exact value"]

for y, label in zip(y_arr, label_arr):
    plt.plot(array_log_h, y, label=label)

approx_gragh = plt.plot(array_log_h, [(exp(-2*(0.5 + h)) - exp(-2*0.5))/h for h in array_h],\
                 label="approximation", linestyle="dashed")
plt.title("numerical errors and approximations of the gradient of exp(-2x) at x=0.5")
plt.xlabel("log(h)")
plt.legend()
plt.show()
