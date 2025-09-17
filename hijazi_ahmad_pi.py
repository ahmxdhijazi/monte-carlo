import matplotlib.pyplot as plt
import numpy as np
import random

figure, axes = plt.subplots()
draw_circle = plt.Circle((0, 0), 1, fill=False)
axes.set_aspect(1)
axes.add_artist(draw_circle)


point_within = 0
point_outside = 0

for i in range(2000):
    x_coord = random.random()
    y_coord = random.random()
    # To determine if a point is between 0 and pi/2, we do distance formula from origin
    # If less than one, we the point is within the circle.
    distance = np.sqrt(x_coord ** 2 + y_coord ** 2)
    if distance < 1:
        point_within += 1
    else:
        point_outside += 1
    plt.plot(x_coord, y_coord, 'o', color='black')

print("Total number of points: 2000")
print("Points Within:", point_within)
print("Points Outside:", point_outside)


plt.title("Circle")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)

plt.show()

