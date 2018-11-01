import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.optimize import Bounds
from scipy.optimize import LinearConstraint

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
coefs0 = np.ones((np.size(CpFront)+np.size(CpRear),1)).flatten()

# Functions 
def ForceF(Coefs, CpF, Area): 
    CoefsF = Coefs[0:np.size(CpF)].flatten() 
    return np.sum(CpF*CoefsF*Area)

def ForceR(Coefs, CpF, CpR, Area): 
    CoefsR = Coefs[np.size(CpF):np.size(Coefs)].flatten()
    return np.sum(CpR*CoefsR*Area)

def Fitness(Coefs, CpF, CpR, Area, knownF, knownR):
    return ((knownF-ForceF(Coefs, CpF, Area))**2)+((knownR-ForceR(Coefs, CpF, CpR, Area))**2)

# Solution bounds
ub = np.full((1,np.size(coefs0)), 1.2).flatten() 
lb = np.full((1,np.size(coefs0)), -1.2).flatten()
bounds = Bounds(lb,ub)

res = minimize(Fitness, coefs0, method='TNC',options={'xtol' : 1e-8, 'disp' : True}, args=(CpFront,CpRear,Area,CD_F,CD_R), bounds=bounds)
print('ForceF= ', ForceF(res.x, CpFront, Area))
print('ForceR= ', ForceR(res.x, CpFront, CpRear, Area))

plt.plot(res.x, 'o', markersize=4, label='coefs')
plt.xlabel("Coefficient No.")
plt.ylabel("Scaling")
# plt.legend(loc='lower right')
plt.show()

# saveData = np.savetxt("test.csv", res.x, delimiter=",")

