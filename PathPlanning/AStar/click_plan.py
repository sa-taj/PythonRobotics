"""

Use this file to repeatedly plan between two clicked points on the map

"""
from enum import Enum
import matplotlib.pyplot as plt
from a_star import AStarPlanner

grid_size = 2.0  # [m]
robot_radius = 1.0  # [m]

# set obstable positions
ox, oy = [], []
for i in range(-10, 60):
    ox.append(i)
    oy.append(-10.0)
for i in range(-10, 60):
    ox.append(60.0)
    oy.append(i)
for i in range(-10, 61):
    ox.append(i)
    oy.append(60.0)
for i in range(-10, 61):
    ox.append(-10.0)
    oy.append(i)
for i in range(-10, 40):
    ox.append(20.0)
    oy.append(i)
for i in range(0, 40):
    ox.append(40.0)
    oy.append(60.0 - i)

show_animation = True
start_rcvd = False
a_star = AStarPlanner(ox, oy, grid_size, robot_radius)
sx = 0.0
sy = 0.0
fig, ax = plt.subplots()

def drawMap():
    global ax, fig, ox, oy
    ax.plot(ox, oy, ".k")
    ax.grid(True)
    ax.axis("equal")

def onclick(event):
    global sx, sy, start_rcvd, a_star, fig, ax
    if start_rcvd == False:
        print(f'Start: x = {event.xdata}, y = {event.ydata}')
        sx = event.xdata
        sy = event.ydata
        ax.cla()
        drawMap()
        fig.canvas.draw()
        start_rcvd = True
    else:
        start_rcvd = False
        print(f'Goal: x = {event.xdata}, y = {event.ydata}')
        rx, ry = a_star.planning(int(sx), int(sy), int(event.xdata), int(event.ydata))
        ax.plot(rx, ry, "-r")
        fig.canvas.draw()

def main():
    print(__file__ + " started!!")
    drawMap()
    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()

if __name__ == "__main__":
    main()
