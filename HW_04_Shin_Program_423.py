import numpy as np
import matplotlib.pyplot as plt

from Shin_BirdBathFunction_423_v420 import BirdbathFunc423

def axially_aligned_gradient_descent():
    """
    finds the best value of the function
    function_type: there are function type 452 and 423.
    easy way to switch between the two.
    """
    min__parms = [-45.0, -45.0, -45.0]
    max__parms = [45.0, 45.0, 45.0]
    best_fract = -1
    best_parms = [0.0, 0.0, 0.0]
    N_STEPS_AWAY = 5  # THIS IS A DESIGN DECISION!!
    full_degree_change = max__parms[0] - min__parms[0]
    deg_inc = full_degree_change / (2 * N_STEPS_AWAY + 1)

    change_in_degree = 0.25
    while deg_inc > change_in_degree:
        number_of_parameters = 3
        for index in range(number_of_parameters):
            old_best_val = best_parms[index]
            min_param_val = old_best_val - (N_STEPS_AWAY * deg_inc)
            max_param_val = old_best_val + (N_STEPS_AWAY * deg_inc)
            for param_value in np.arange(min_param_val, max_param_val, deg_inc):
                old_parameter = best_parms[index]
                old_value = BirdbathFunc423(best_parms[0], best_parms[1], best_parms[2])
                best_parms[index] = param_value
                new_value = BirdbathFunc423(best_parms[0], best_parms[1], best_parms[2])
                if new_value <= old_value:
                    best_parms[index] = old_parameter  # reset to old parameter
                    best_fract = old_value
                else:
                    best_fract = new_value

        learning_rate = 63 / 64
        deg_inc = deg_inc * learning_rate  # learning rate decay

    print("Max value: {0}".format(best_fract))
    print("The parameters for max value")
    print("roll: {0} tilt: {1} twist: {2}".format(best_parms[0], best_parms[1], best_parms[2]))

def plot_rosenbrock():
    """
    plots the rosenbrock graph
    """
    x = np.arange(start=-2, stop=2, step=0.15)
    y = np.arange(start=-1, stop=3, step=0.15)
    x, y = np.meshgrid(x, y)

    rosenbrock = lambda x, y: (1 - x) ** 2 + 100 * ((y - x ** 2) ** 2)
    z = rosenbrock(x, y)
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
    plt.title('Rosenbrock’s Banana')
    plt.show()

    return [x, y, z]

if __name__ == '__main__' :
    axially_aligned_gradient_descent()
    plot_rosenbrock()
