import numpy as np

g = 9.81

m = 1.0
k = 20
gamma = k / m
dt = 0.05
L = 2

v_0 = np.array([2, 2, 1])
r_0 = np.array([1, 0, 2.5])

x_lim = [-3, 3]
y_lim = [-3, 3]
z_lim = [-4, 0]