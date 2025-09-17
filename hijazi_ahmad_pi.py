import matplotlib.pyplot as plt
import numpy as np
import random

#Generating graph with all wanted features.
figure, axes = plt.subplots()
draw_circle = plt.Circle((0, 0), 1, fill=False)
axes.set_aspect(1)
axes.add_artist(draw_circle)
plt.title("Circle")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
#Optionally used to set the ticks for both axes to go by .1 instead of .2 for readability
plt.xticks(np.arange(0, 1.1, 0.1))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid(True)


def estimate_pi(n):
    point_within = 0
    point_outside = 0

    for i in range(n):
        x_coord = random.random()
        y_coord = random.random()
        # To determine if a point is between 0 and pi/2, we do distance formula from origin
        # If less than one, we the point is within the circle.
        distance = np.sqrt(x_coord ** 2 + y_coord ** 2)
        if distance < 1:
            point_within += 1
            plt.plot(x_coord, y_coord, '.', color='red')
        else:
            point_outside += 1
            plt.plot(x_coord, y_coord, '.', color='blue')
    print("Total number of points:", n)
    print("Points Within:", point_within)
    print("Applying Monte Carlo Method to approximate Pi:...")

    plt.show()

def main():
    estimate_pi(10000)

if __name__ == '__main__':
    main()

