import numpy as np
import matplotlib
matplotlib.use( 'tkagg' )
import matplotlib.pyplot as plt
from scipy.integrate import odeint

y0 = [10,1] # [fish, bears] units in hundreds

t = np.linspace(0,50,num=1000)

alpha = 1.1
beta = 0.4
delta = 0.1
gamma = 0.4

params = [alpha, beta, delta, gamma]

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

y = odeint(sim, y0, t, args=(params,))
 

