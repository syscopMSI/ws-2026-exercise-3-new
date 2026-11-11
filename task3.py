"""
This is the template for coding tasks in exercise sheet 3.

Everywhere you see "YOUR CODE", it means a playground for you :P

WARNING: do not rename variables as this will break the tests.
=============================================================================================================================

Eventually you will explore the powerful least squares estimation formulated with linear algebra!
And as usual here are two functions that might be helpful to you.

- to stack vectors as columns to form a matrix:
    <https://numpy.org/doc/stable/reference/generated/numpy.column_stack.html>

- to calculate x = A^(-1) b with specifying A, b:
    <https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html>

- to extract the diagonal of a matrix:
    <https://numpy.org/doc/stable/reference/generated/numpy.diagonal.html>

Have fun!
"""


import os
import matplotlib.pyplot as plt
import numpy as np



## load data
filepath = os.path.join(os.path.dirname(__file__), "exercise3_task3_dataset.npz")
data = np.load(filepath)
print(data.files)
i = data['i']
u = data['u']
N = 2000


## a) Plot each dataset in a corresponding plot
plt.figure(1)
# YOUR CODE: plot dataset i, u




## b) only PAPER questions :)


## c) 
# Use the least squares estimator to find the experimental values of R and E for each of the two datasets individually.
# YOUR CODE: least squares with dataset i, u
# ============================================
# "None" is just to pass the syntax check. Replace them with your code. Don't need to stick to a single line.
# (The same holds for all the following cases)
Phi = None
theta_star = None



# Plot the linear fits through the respective measurement data
plt.figure(1)
# YOUR CODE: linear fits with dataset i, u




## d) 
# YOUR CODE: calculate the residuals
r = None


# plot the histograms of them
plt.figure(2)
# YOUR CODEgit


## f)
## YOUR CODE : Calculate the covariance matrix and  1-sigma standard deviation estimate
# "None" is just to pass the syntax check. Replace them with your code. Don't need to stick to a single line.
cov_mat = None
standard_deviation = None

print(f"theta 1 estimate = {theta_star[0]} +- {standard_deviation[0]}")
print(f"theta 2 estimate = {theta_star[1]} +- {standard_deviation[1]}")

# show all plots
# ===============
# If you don't see any plots but also no errors, it is very likely because a non-interactive backend is chosen by default.
# One possible solution you can try is to manually select another backend via "matplotlib.use()" function at the beginning.
# Here gives more details: <https://matplotlib.org/stable/users/explain/backends.html>
plt.show()
