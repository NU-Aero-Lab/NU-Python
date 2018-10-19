import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Load the data in
cp_data = np.genfromtxt('2CarPlatoon-Leader_0.5L.csv', delimiter=',',skip_header=True)

# Variables
Area = 0.0885*0.11167 
CD_F = 0.094935
CD_R = 0.0571517

# Extract and Split Cp 
front = cp_data[:,0] < -2 
CpFront = cp_data[front,3]
CpRear = cp_data[~front,3]

# Populate initial coefficients
#coefs0 = np.ones((np.size(CpFront)+np.size(CpRear),1)).flatten()
coefs0 = np.ones((np.size(CpFront),1)).flatten()

# Functions 
def ForceF(Coefs, CpF, Area): return np.sum(CpF*Coefs*Area)
#def ForceR(Coefs, CpF, CpR, Area): return sum(CpF.iterable*Coefs*Area)

def Fitness(Coefs, CpF, Area, knownF):
    return (knownF-ForceF(Coefs, CpF, Area))**2

# Fitness function
#FitnessFunction = (@coefs ((CD_F-ForceF(coefs0,CpFront,Area))**2))#+(CD_R-ForceR(coefs,CpFront,CpRear,Area))^2)

res = minimize(Fitness, coefs0, method='nelder-mead',options={'xtol' : 1e-8, 'disp' : True}, args=(CpFront,Area,CD_F))

print(res)
