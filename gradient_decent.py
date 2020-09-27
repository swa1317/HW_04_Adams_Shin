min__parms = [-45.0, -45.0, -45.0]
max__parms = [45.0, 45.0, 45.0]
best_fract = -1
best_parms = [0.0, 0.0, 0.0]
N_STEPS_AWAY = 2  # THIS IS A DESIGN DECISION!!
full_degree_change = max__parms[0] - min__parms[0]
deg_inc = full_degree_change / (2 * N_STEPS_AWAY + 1)

change_in_degree = 0.25
lst_of_values = np.array([])
while deg_inc > change_in_degree:
    # print("CHANGE IN DEGREE: {0} ====================================".format(deg_inc))
    number_of_parameters = 3
    for index in range(number_of_parameters):
        # print("INDEX: {0} ====================================".format(index))
        old_best_val = best_parms[index]
        min_param_val = old_best_val - (N_STEPS_AWAY * deg_inc)
        max_param_val = old_best_val + (N_STEPS_AWAY * deg_inc)
        for param_value in np.arange(min_param_val, max_param_val, deg_inc):
            old_parameter = best_parms[index]
            old_value = BirdbathFunc452(best_parms[0], best_parms[1], best_parms[2])
            best_parms[index] = param_value
            new_value = BirdbathFunc452(best_parms[0], best_parms[1], best_parms[2])
            if new_value <= old_value:
                best_parms[index] = old_parameter  # reset to old parameter
            np.append(lst_of_values, BirdbathFunc452(best_parms[0], best_parms[1], best_parms[2]))

    learning_rate = 63 / 64
    deg_inc = deg_inc * learning_rate  # learning rate decay

plt.plot(lst_of_values)
plt.show()