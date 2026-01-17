import numpy as np
import matplotlib
matplotlib.use( 'tkagg' )
import matplotlib.pyplot as plt
from scipy.integrate import odeint



def sim(variables, t, params):
    #fish population level
    x = variables[0]
    
    # bear population level
    y = variables [1]

    alpha = params[0]
    beta = params[1]
    delta = params[2]
    gamma = params[3]

    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y

    return([dxdt, dydt])
 

