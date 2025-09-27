import matplotlib.pyplot as plt
import numpy as np
import random
def gen_graph():
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
    gen_graph()
    global pi_estimate
    print("Total number of points:", n)
    point_within = 0
    point_outside = 0
    currentn = 0
    print("Applying Monte Carlo Method to approximate Pi:...")

    for i in range(n):
        x_coord = random.random()
        y_coord = random.random()
        # To determine if a point is between 0 and pi/2, we do distance formula from origin
        # If less than one, we the point is within the circle.
        distance = np.sqrt(x_coord ** 2 + y_coord ** 2)
        if distance < 1:
            point_within += 1
            plt.plot(x_coord, y_coord, '.', markersize = 1, color='red')
        else:
            point_outside += 1
            plt.plot(x_coord, y_coord, '.', markersize = 1, color='blue')
        currentn += 1
    # Ratio of areas is pi/4 so multiply 4*total points within over total points
    pi_estimate = (4 * point_within) / n
    plt.title('Estimate of Pi: {:.4f}'.format(pi_estimate))
    plt.show()
    return pi_estimate

def graph_convergence():
    n_values = [10**3, 10**4, 10**5]
    estimates = [estimate_pi(n) for n in n_values]

    #{CHATGPT CODE: used to display the Convergence Graph for each n}
    plt.figure()
    plt.semilogx(n_values, estimates, 'o-', label="Estimates")
    plt.axhline(y=np.pi, color='r', linestyle='--', label="True π")
    plt.xlabel("Number of points (n)")
    plt.ylabel("Estimated π")
    plt.title("Convergence of Monte Carlo π Estimator")
    plt.legend()
    plt.show()
    #{END}

def main():
    graph_convergence()


if __name__ == '__main__':
    main()

