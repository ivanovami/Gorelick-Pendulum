import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

from the_best import *

def find_acceleration(vect):
    x = vect[0]
    y = vect[1]
    z = vect[2]
    theta = np.arctan2(np.sqrt(x * x + y * y), z)
    phi = np.arctan2(y, x)

    delta_L = np.sqrt(x * x + y * y + z * z) - L
    delta_x = delta_L * np.sin(theta) * np.cos(phi)
    delta_y = delta_L * np.sin(theta) * np.sin(phi)
    delta_z = delta_L * np.cos(theta)

    return np.array([-gamma * delta_x, -gamma * delta_y, g-gamma * delta_z])



# constants
#g = 9.81

# # constants
# m = 1.0
# k = 30
# gamma = k / m
# dt = 0.05
# L = 1

# number of frames
frame_num = 1000

# define initial position
r = np.zeros(frame_num * 3)
r.shape = (frame_num, 3)
r[0] = r_0


# define initial velocities
v = np.zeros(frame_num * 3)
v.shape = (frame_num, 3)
v[0] = v_0
# define initial acceleration
a = np.zeros(frame_num * 3)
a.shape = (frame_num, 3)

a[0] = find_acceleration(r[0])


# create a figure

sp = np.array([[0, 0, 0], r[0]])
fig = plt.figure()
ax = fig.add_subplot()
ax.set(xlim=x_lim, ylim=z_lim)
line, = ax.plot(r[0, 0], -r[0, 2], color="darkred", markersize=0.5)
spring, = ax.plot(sp[:, 0], -sp[:, 2], color="grey", markersize=0.2)
scat, = ax.plot(r[0, 0], -r[0, 2], color="gold", marker="o", markersize=5)
ax.scatter(0, -L-g/gamma, color="darkgreen", s=10)

print(r[0])
print(a[0])


def update(frame, r, v, a):
    r[frame + 1] = r[frame] + v[frame] * dt + a[frame] * dt * dt / 2
    a[frame + 1] = find_acceleration(r[frame + 1])
    v[frame + 1] = v[frame] + (a[frame] + a[frame + 1]) * dt / 2

    # update line
    line.set_data(r[:frame+1, 0], -r[:frame+1, 2])

    # update spring
    sp = np.array([[0, 0], [r[frame][0], -r[frame][2]]])
    spring.set_data(sp[:, 0], sp[:, 1])

    # update point
    scat.set_data(r[frame:frame+1, 0], -r[frame:frame+1, 2])

    return line, scat


ani = animation.FuncAnimation(fig=fig, func=update, frames=frame_num-1, interval=30, fargs=(r, v, a))
plt.grid(which='major')
plt.grid(which='minor', linestyle=':')

plt.show()

# # Set up formatting for the movie files
# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=4000)
#
# # Save animation
# ani.save("interesting.mp4", writer=writer)
