import numpy as np

g = 9.81

m = 1.0
k = 100
gamma = k / m
dt = 0.05
L = 2

# v_0 = np.array([0, 3, 5])
# r_0 = np.array([0.2, 0, np.sqrt((L+g/gamma) * (L+g/gamma) - 0.04)])

v_0 = np.array([2, 2, -0.5])
r_0 = np.array([1, 0, 2.3])

x_lim = [-3, 3]
y_lim = [-3, 3]
z_lim = [-15, 0]