import numpy as np

g = 9.81

m = 1.0
k = 10
gamma = k / m
dt = 0.05
L = 1

v_0 = np.array([0, 0, 3])
r_0 = np.array([0, 0, L+g/gamma])

x_lim = [-5, 5]
y_lim = [-5, 5]
z_lim = [-5, 0]