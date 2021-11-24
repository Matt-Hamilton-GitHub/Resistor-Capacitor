import numpy as np 
import pandas 
 
dataframe=pandas.read_csv("cap_discharge.txt") 
dataframe

dataframe.update(dataframe['time'].sub(1000)) 
dataframe.head() 

dataframe.update(dataframe['time'].div(1000)) 
dataframe.head() 

import matplotlib.pyplot as plt 
 
plt.plot(dataframe['time'], dataframe['voltage'], label='Capacitor Voltage (V)') 
plt.xlabel("time(s") 
plt.ylabel("Voltage (V)") 
 
plt.legend() 
plt.show() 

# Import curve fitting package from scipy 
from scipy.optimize import curve_fit 
 
# create the function to fit to the curve 
 
def exponential(x, a, b): 
  return a*np.exp(x*b) 
 
pars, cov = curve_fit(f=exponential, xdata=dataframe['time'], ydata=dataframe['voltage']) 

# print the fit results 
print(pars) 
 
 
# print the uncertainties in  the fit parameters 
print(np.sqrt(np.diag(cov))) 

dataframe['model']=4.957*np.exp(-0.0990*dataframe['time']) 
 
dataframe.head() 

import matplotlib.pyplot as plt 
 
plt.plot(dataframe['time'], dataframe['voltage'], label='Capacitor Voltage (V)') 
plt.xlabel("time(s)") 
plt.ylabel("Voltage (V)") 
 
plt.plot(dataframe['time'],dataframe['model'], label='Model') 
 
plt.legend() 
plt.show() 