# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import math
import os
import sys

from numerical_integration import (left_right_sum, simpson_18rule,
                                   trapezoid_sum, trapezoid_sum_error,
                                   simpson18_error)
from accounting import build_future_income_function, build_present_value_function

# %%
A = lambda t: 10000
f = build_future_income_function(A, 10, 0.05)
trapezoid = trapezoid_sum(f, (0, 10), 10)
f_2nd_derived = lambda t: 41.218 * math.exp(-0.05 * t)
epsilon = trapezoid_sum_error(f_2nd_derived, (0, 10), 10)
print(trapezoid)
print(epsilon)
simpsons = simpson_18rule(f, (0, 10), 10)
print(simpsons)
f_4th_derived = lambda t: 0.103045 * math.exp(-0.05 * t)
simpson_error = simpson18_error(f_4th_derived, (0,10), 10)
print(simpson_error)

# %%
A = lambda t: 10000 - 200 * t ** 2
f = build_present_value_function(A, 0.05)
trapezoid = trapezoid_sum(f, (0, 10), 10)
f_2nd_derived = lambda t: math.exp(-0.05 * t) * (-0.5 * t ** 2 + 40 * t - 375)
epsilon = trapezoid_sum_error(f_2nd_derived, (0, 10), 10)
print(trapezoid)
print(epsilon)
simpsons = simpson_18rule(f, (0, 10), 10)
print(simpsons)
f_4th_derived = lambda t: math.exp(-0.05 * t) * (-0.00125 * t ** 2 + 0.2 * t - 5.9375)
simpson_error = simpson18_error(f_4th_derived, (0,10), 10)
print(simpson_error)


# %%
