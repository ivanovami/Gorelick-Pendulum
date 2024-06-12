import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np


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
g = 9.81

# config
m = 1.0
k = 600
gamma = k / m
dt = 0.05
L = 2

# number of frames
frame_num = 1000

# define initial position
r = np.zeros(frame_num * 3)
r.shape = (frame_num, 3)
#r[0] = np.array([0, 0, L+g/gamma])
r[0] = np.array([0.2, 0, np.sqrt((L+g/gamma) * (L+g/gamma) - 0.04)])


# define initial velocities
v = np.zeros(frame_num * 3)
v.shape = (frame_num, 3)
v[0] = np.array([0, 0.3, 0.5])

# define initial acceleration
a = np.zeros(frame_num * 3)
a.shape = (frame_num, 3)

a[0] = find_acceleration(r[0])


# create a figure

sp = np.array([[0, 0, 0], r[0]])
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.set(xlim3d=[-1, 1], ylim3d=[-1, 1], zlim3d=[-10, 0])
line, = ax.plot(r[0, 0], r[0, 1], -r[0, 2], color="darkred", markersize=0.2)
spring, = ax.plot(sp[:, 0], sp[:, 1], -sp[:, 2], color="grey", markersize=0.2)
scat, = ax.plot(r[0, 0], r[0, 1], -r[0, 2], color="gold", marker="o", markersize=3)
ax.scatter(0, 0, -L-g/gamma, color="darkgreen", s=5)

print(r[0])

def update(frame, r, v, a):
    r[frame + 1] = r[frame] + v[frame] * dt + a[frame] * dt * dt / 2
    a[frame + 1] = find_acceleration(r[frame + 1])
    v[frame + 1] = v[frame] + (a[frame] + a[frame + 1]) * dt / 2

    # update line
    line.set_data(r[:frame, 0], r[:frame, 1])
    line.set_3d_properties(-r[:frame, 2])

    sp = np.array([[0, 0, 0], r[frame]])
    spring.set_data(sp[:, 0], sp[:, 1])
    spring.set_3d_properties(-sp[:, 2])

    # update point
    scat.set_data(r[frame:frame+1, 0], r[frame:frame+1, 1])
    scat.set_3d_properties(-r[frame:frame+1, 2])

    return line, scat


ani = animation.FuncAnimation(fig=fig, func=update, frames=frame_num-1, interval=30, fargs=(r, v, a))
#
# # Set up formatting for the movie files
# Writer = animation.writers['ffmpeg']
# writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=4000)
#
# # Save animation
# ani.save("Pendul.mp4", writer=writer)

plt.show()
