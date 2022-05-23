from scipy import stats as st
from scipy.integrate import quad
from scipy.interpolate import make_interp_spline, BSpline
from scipy.optimize import fsolve
from sympy import symbols, solve 
import numpy as np
import scipy as sp
import sympy as sym
import matplotlib.pyplot as plt
import scipy.constants as cc

Torque_max = 162
theta = np.linspace(90, 160, 200) 
F = Torque_max * 0.8 / (0.55 + 0.35 * np.cos((180-theta)*np.pi/180))

plt.figure(1)
plt.plot(theta,F,'r-',label='Torque = 130 Nm')
plt.xlabel('Knee angle (degree)',fontsize=14,weight='bold')
plt.ylabel('Force (N)',fontsize=14,weight='bold')
plt.title('Force vs. Knee angle (Horizontal)',fontsize=20,weight='bold')
plt.xlim(90,160)
plt.ylim(140,)
plt.legend()
plt.grid()  
plt.savefig('F vs Knee angle(H).png')

Torque_max = 130
theta = np.linspace(90, 160, 200) 
F1 = Torque_max / (0.55 + 0.35 * np.sin((180-theta)*np.pi/180))
plt.figure(2)
plt.plot(theta,F1,'r-',label='Torque = 130 Nm')
plt.xlabel('Knee angle (degree)',fontsize=14,weight='bold')
plt.ylabel('Force (N)',fontsize=14,weight='bold')
plt.title('Force vs. Knee angle (Vertical)',fontsize=20,weight='bold')
plt.xlim(90,160)
plt.ylim(140,)
plt.legend()
plt.grid()  
plt.savefig('F vs Knee angle(V).png')