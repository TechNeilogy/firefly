import matplotlib
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use("TkAgg")

from firefly.fire_fly.Config import Config
from firefly.fire_fly.Environment import Environment

color_highlight = False

config_2d = Config(
    donation_level=5,
    color_highlight=color_highlight
)

config_3d = Config(
    two_d=False,
    color_highlight=color_highlight
)

config = config_3d

env = Environment(
    config
)

width = 1.0

dark = (0.2, 0.2, 0.2, 1)

if config.two_d:
    fig = plt.figure(1, figsize=(5, 5))
    fig.set_facecolor(dark)
    fig.patch.set_facecolor((0.1, 0.1, 0.1, 1))
    ax = plt.axes(xlim=(0, width), ylim=(0, width))
    ax.set_facecolor((0.0, 0.0, 0.0, 1))
else:
    fig = plt.figure(figsize=(6, 6))
    fig.set_facecolor(dark)
    ax = fig.add_subplot(projection='3d')
    ax.set_facecolor(dark)
    for axis in ['x', 'y', 'z']:
        ax.tick_params(axis=axis, colors=(0.4, 0.4, 0.4))
    for axis in [ax.w_xaxis, ax.w_yaxis, ax.w_zaxis]:
        axis.set_pane_color((0.0, 0.0, 0.0, 1.0))    
        axis._axinfo['grid']['color'] = (0.4, 0.4, 0.4)

env.update()

if config.color_highlight:
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
        "",
        [(0.8, 0.0, 0.0), "black", "black", (0.8, 1.0, 0.2)],
        N=100
    )
else:
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
        "",
        ["black", "black", (0.8, 1.0, 0.2)],
        N=100
    )

if config.two_d:
    graph = ax.scatter(
        env.points[:,0],
        env.points[:,1],
        s=env.d,
        c=env.f,
        cmap=cmap
    )
else:
    graph = ax.scatter(
        env.points[:,0],
        env.points[:,1],
        env.points[:,2],
        s=env.d,
        c=env.f,
        cmap=cmap
    )

def animate(_frame):

    global two_d
    global graph
    global env

    env.update()

    graph.set_array(
        env.f
    )

    return graph,


anim = animation.FuncAnimation(
    fig,
    animate,
    frames=env.count,
    interval=1,
    blit=True,
    repeat=True
)

plt.show()