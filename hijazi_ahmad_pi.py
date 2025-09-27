import matplotlib.pyplot as plt
import numpy as np
import random

def gen_graph():
    # Generating graph with all wanted features.
    figure, axes = plt.subplots()
    draw_circle = plt.Circle((0, 0), 1, fill=False)
    axes.set_aspect(1)
    axes.add_artist(draw_circle)
    plt.title("Circle")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    # Optionally used to set the ticks for both axes to go by .1 instead of .2 for readability
    plt.xticks(np.arange(0, 1.1, 0.1))
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.grid(True)

def estimate_pi(n):
    gen_graph()
    global pi_estimate
    print("Total number of points:", n)
    print("Applying Monte Carlo Method to approximate Pi...")
    # Generate n points at once
    #Numpy Vectorization to speed up the process
    #For loop to generate each random point was very very very slow for anything over 10^3
    #Wow I am shocked, this was instantaneous... all the way up to 10^8
    points = np.random.rand(n, 2)  # shape (n, 2)
    distances = np.sqrt(points[:, 0] ** 2 + points[:, 1] ** 2)
    #Count points inside the circle of radius 1
    inside = distances < 1
    pi_estimate = 4 * np.sum(inside) / n
    #plotting points

    plt.scatter(points[inside, 0], points[inside, 1], color="blue", s=2, label="Inside circle")
    plt.scatter(points[~inside, 0], points[~inside, 1], color="red", s=2, label="Outside circle")
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
    # {END}

def main():
    graph_convergence()

if __name__ == '__main__':
    main()
