import numpy as np
import matplotlib.pyplot as plt


from Shin_BirdBathFunction_423_v420 import BirdbathFunc423
from Adams_BirdBathFunction_452_v420 import BirdbathFunc452

def axially_aligned_gradient_descent():
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
    return best_fract

def best_value():
    a =[]
    b = -1
    for i in range(-45, 45):
        for j in range(-45, 45):
            for k in range(-45, 45):
                c = BirdbathFunc423(i, j, k)
                if b == -1 or b < c:
                    b = c
    return b
if __name__ == '__main__' :
    # a = best_value()
    b = axially_aligned_gradient_descent()
    # print(a) # 0.4981701057062594
    print(b) # 0.4977630741037475
