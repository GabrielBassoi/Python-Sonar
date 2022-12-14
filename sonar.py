# Importing libraries
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from test import Tests
from arduino import Arduino
from matplotlib.widgets import Button

# Setting up matplotlib
matplotlib.use('TkAgg', force=True)
matplotlib.rcParams['toolbar'] = 'None'
matplotlib.rc('axes', edgecolor="#0aff00")

# Variables
t = Tests()
ard = Arduino()

green1 = "#034d00"
green2 = "#0aff00"
red = "#FF0000"

r_max = 100.0
dpi = 150
a = []

angles = np.arange(0, 181, 1)
theta = angles * (np.pi / 180.0)
dists = np.ones((len(angles),))

font = {"color": "#0aff00", "size": 10}

# Setting up objects
fig = plt.figure("Arduino Sonar", facecolor=green1)
ax = fig.add_subplot(111, polar=True, facecolor=green1)
plot_res = fig.get_window_extent().bounds

# figure presentation adjustments
plt.rcParams.update({'text.color': green2})
fig.set_dpi(dpi)
ax.set_position([-0.05, -0.05, 1.1, 1.05])

# Config grid
ax.set_ylim([0.0, r_max])
ax.set_xlim([0.0, np.pi])
ax.tick_params(axis='both', colors=green2)
ax.grid(color=green2, alpha=1)
ax.set_rticks(np.linspace(0.0, r_max, 5))
ax.set_thetagrids(np.linspace(0.0, 180.0, 10))


class Sonar:
    def __init__(self):
        pass

    def close(self, event):
        plt.close("all")

    def connect(self):
        global a
        print("Finding Arduino...")
        while len(a) == 0:
            a = ard.arduino_connect()
        print("Receiving data...")

    def sonar(self):
        while True:
            ang, dit = ard.get_data()
            if dit > r_max:
                dit = 0

            dists[int(ang)] = dit
            pols.set_data(theta, dists)
            ax.draw_artist(pols)

            line1.set_data(np.repeat((ang * (np.pi / 180.0)), 2), np.linspace(0.0, r_max, 2))
            ax.draw_artist(line1)

            text.set_text(f"Angulo: {ang}\nDistancia: {dit}")
            ax.draw_artist(text)

            fig.canvas.blit(ax.bbox)
            fig.canvas.flush_events()


s = Sonar()

pols, = ax.plot([], linestyle='', marker='.', markerfacecolor=red, markeredgecolor=red, markeredgewidth=0.2,
                alpha=0.9)
line1, = ax.plot([], color=green2, linewidth=1.0)
text = plt.text(0.73 * np.pi, 170, "", fontdict=font)

stopbutton_ax = fig.add_axes([0.85, 0.025, 0.125, 0.05])
stopbutton = Button(stopbutton_ax, 'Stop Sonar', color=green1)
stopbutton.on_clicked(s.close)

fig.canvas.draw()
fig.show()

plt.ion()
