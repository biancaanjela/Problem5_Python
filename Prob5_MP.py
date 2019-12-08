import math as m
import matplotlib.pyplot as mp 
import numpy as bi

def problem5(x):
    
    n = bi.linspace(0,199)
    
    if n.any() == 199:
        y = ((1.5)*x) - (2*x*(n - 1)) + ((0.5)*x*(n - 2));

    elif n.any() == 0:
        y = ((-1.5)*x) + (2*x*(n + 1)) + ((0.5)*x*(n + 2));
  
    else:
        y = ((0.5*x*(n + 1)) - (0.5*x*(n - 1)));
    
mp.grid()
mp.plot(x, label = 'x(n)')
mp.plot(y, label = 'y(n)')
mp.legend()
mp.xlabel('n')
mp.ylabel('function with respect to n')
mp.show() 

    
