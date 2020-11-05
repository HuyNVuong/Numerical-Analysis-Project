# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import os
import sys
from numerical_integration import left_right_sum, trapezoid_sum, trapezoid_sum_error, simpson_18rule
from accounting import build_netincome_function

# %%
f = lambda x: x ** 2
xs = [1,2,3,4,5]
left_sum, right_sum = left_right_sum(f, (2, 3), 5)
print(left_sum, right_sum)

# %%
trapezoid = trapezoid_sum(f, (2, 3), 5)
print(trapezoid)
f_derived = lambda x : 2
epsilon = trapezoid_sum_error(f, f_derived, (2, 3), 5)
print(epsilon)

#%%
simpsons = simpson_18rule(f, (2, 3), 6)
print(simpsons)

# %%
A = lambda t : 10000 * t - 3000
print('Income stream function 10000 * t - 3000')
f = build_netincome_function(A, 0.05)
net_income = trapezoid_sum(f, (0, 10), 100)
print(net_income)

# %%
