#
#   A problem function which uses intentionally obtuse variable names and almost no comments.
#   The goal is for students to find the maximum of the function using gradient ascent,
#   axially-aligned grid search, full grid search, or some combination of these techniques.
#   CSCI-420 students who wish to try using Genetic Algorithms can try that too.
#
#   Dr. Thomas B. Kinsman
#
import math
import numpy as np

def urxyz(exes_parameter, why, zircon, rta, rtb, rtc):
    bogart  = np.array([exes_parameter, why, zircon])
    nu      = rta * (np.pi/180)
    delta   = np.array([[1, 0, 0], [0, np.cos(nu), -np.sin(nu)], [0, np.sin(nu), np.cos(nu)]])
    mu      = rtb * (np.pi/180)
    unicorn = np.array([[np.cos(mu), 0, np.sin(mu)], [0, 1, 0], [-np.sin(mu), 0, np.cos(mu)]])
    tu      = rtc * (np.pi/180)
    iocane  = np.array([[np.cos(tu), -np.sin(tu), 0], [np.sin(tu), np.cos(tu), 0], [0, 0, 1]])
    rq      = np.matmul(delta, np.matmul(unicorn, iocane))
    pegasus = np.matmul(rq, bogart)
    return pegasus


def BirdbathFunc452(Harry, Dumbledore, Sirius):
    Snuffleupagus   = np.array( [ -204e-9, 20e-9, 427.854e-6, 999.87597e-3, 995.41971e-2  ] )
    Susan           = np.array( [  0.98137, -0.52815, -0.92100 ] )
    Ernie           = np.array( Harry )
    Bob             = np.array( [ -0.03641,  0.82292, -0.36970 ] )
    Troll           = np.polyval( Snuffleupagus, Ernie )
    Hooper          = np.array( [ -0.18867,  0.20944,  0.12281 ] )
    rot_tri         = urxyz( Susan, Bob, Hooper, Troll, Dumbledore, Sirius )
    if ( rot_tri[2][0] < rot_tri[2][1] ) :
         if ( rot_tri[2][0] < rot_tri[2][2] ) :
             min_idx = 0
         else :
             min_idx = 2
    else :
         if ( rot_tri[2][1] < rot_tri[2][2] ) :
             min_idx = 1
         else :
             min_idx = 2
    minic                   = rot_tri[2][min_idx]
    pradius                 = math.sqrt( 1 - (minic*minic) )
    Hagrid                  = 1 - abs(rot_tri[2][min_idx]) 
    Hedgewig                = ( math.pi * (Hagrid*Hagrid) / 3 ) * ( 3*1 - Hagrid )
    Hermoine                = 4/3 * math.pi
    Rous                    = Hedgewig / Hermoine 
    GiantVariable           = Rous * Rous * 2   # Increase the sensitivity by squaring small quantity.
    return GiantVariable


if __name__ == '__main__' :


    #  Emit a trial test case here, etc...:
    print('\n\n\n')
    nn  = BirdbathFunc452( 10.8750, -2.1250, 17.1895 )
    print('Fraction of Water = ', nn, '<-- Example test case results\n' )



    print('###########################################################################################')


    min__parms  = [ -45.0, -45.0, -45.0 ]
    max__parms = [45.0, 45.0, 45.0]
    best_fract = -1
    best_parms = [0.0, 0.0, 0.0]
    N_STEPS_AWAY = 2  # THIS IS A DESIGN DECISION!!
    full_degree_change = max__parms[0] - min__parms[0]
    deg_inc      = full_degree_change / ( N_STEPS_AWAY + 1 + N_STEPS_AWAY )
    print(deg_inc)

    change_in_degree = 0.25
    while deg_inc > change_in_degree:

        roll_min   = best_parms[0]-deg_inc*N_STEPS_AWAY
        roll_max   = best_parms[0]+deg_inc*N_STEPS_AWAY

        print(deg_inc)
        # loop each parameter and get value from birdbath
        # if birdbath value is better than before, update and keep moving in that direction
        # if birdbath value is worse than before, move in opposite direction
        number_of_parameters = 3
        for index in range(number_of_parameters):
            old_best_val = best_parms[index]
            min_param_val   = old_best_val - (N_STEPS_AWAY * deg_inc)
            max_param_val   = old_best_val + (N_STEPS_AWAY * deg_inc)
            for param_value in range(min_param_val, max_param_val, deg_inc ):
                # check BirdbathFunc452( 10.8750, -2.1250, 17.1895 ) value here
                print()

        learning_rate = 63 / 64
        deg_inc = deg_inc * learning_rate