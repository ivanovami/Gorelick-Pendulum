import numpy as np

g = 9.81

m = 1.0
k = 200
gamma = k / m
dt = 0.05
L = 1

v_0 = np.array([4, 0, 0])
r_0 = np.array([0, 0, L+g/gamma])

x_lim = [-2, 2]
y_lim = [-2, 2]
z_lim = [-2, 0]