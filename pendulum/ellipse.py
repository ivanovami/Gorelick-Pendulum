import numpy as np

g = 9.81

m = 1.0
k = 600
gamma = k / m
dt = 0.05
L = 2

v_0 = np.array([0.0, 0.5, 0])
# v_0 = np.array([0.3, 0.5, 0])
r_0 = np.array([0.2, 0, np.sqrt((L+g/gamma) * (L+g/gamma) - 0.04)])

x_lim = [-1, 1]
y_lim = [-1, 1]
z_lim = [-3, 0]