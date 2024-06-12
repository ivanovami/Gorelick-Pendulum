import numpy as np

g = 9.81

m = 1.0
k = 2
gamma = k / m
dt = 0.05
L = 2

v_0 = np.array([2, 0, 2])
r_0 = np.array([0, 0, L+g/gamma])

x_lim = [-3, 3]
y_lim = [-2, 3]
z_lim = [-15, 0]