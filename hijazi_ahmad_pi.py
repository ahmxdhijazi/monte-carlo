import matplotlib.pyplot as plt
import numpy as np

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
    #n values
    n_values = [10**3, 10**4, 10**5]
    # number of repetitions
    R = 500

    for n in n_values:
        print(f"Running {R} Monte Carlo estimates for n = {n} ...")
        estimates = []
        for i in range(R):
            #so there isnt 500 different scatterplots
            points = np.random.rand(n, 2)  # shape (n, 2)
            distances = np.sqrt(points[:, 0] ** 2 + points[:, 1] ** 2)
            inside = distances < 1
            estimates.append(4 * np.sum(inside) / n)

        # single histogram for the R estimates, should be gaussian, and it is (:
        plt.figure()
        plt.hist(estimates, bins=30, density=True, alpha=0.7)
        #Plot the line for pi so we can see where the gaussian distribution should align with
        plt.axvline(np.pi, color='red', linestyle='-.', label="True π")
        #{CHATGPT: to do std dev and mean just for to see}
        mean_est = np.mean(estimates)
        std_est = np.std(estimates)
        plt.axvline(mean_est, color='blue', linestyle='--', label=f"Mean = {mean_est:.5f}")
        plt.text(0.97, 0.95,
                 f"Mean = {mean_est:.5f}\nStd Dev = {std_est:.5f}",
                 ha='right', va='top', transform=plt.gca().transAxes,
                 bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7))
        #{END}
        plt.title(f"Distribution of π Estimates (n={n}, R={R})")
        plt.xlabel("Estimated π")
        plt.ylabel("Density")
        plt.legend()
        plt.show()

if __name__ == '__main__':
    main()
