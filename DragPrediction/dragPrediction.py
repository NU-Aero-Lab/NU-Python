import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.optimize import Bounds
from scipy.optimize import differential_evolution

# Load the data in
cp_data = np.genfromtxt('2CarPlatoon-Leader_0.5L.csv', delimiter=',',skip_header=True)

# Variables
Area = 0.0885*0.11167 
CD_F = 0.06807
CD_R = 0.0582

# Extract and Split Cp 
front = cp_data[:,0] < -2 
CpFront = cp_data[front,3]
CpRear = cp_data[~front,3]
normalFront = cp_data[front,4]
normalRear = cp_data[~front,4]

# Populate initial coefficients
coefs0 = np.ones((np.size(CpFront)+np.size(CpRear),1)).flatten()

# Functions 
def ForceF(Coefs, CpF, Area, NF): 
    CoefsF = Coefs[0:np.size(CpF)].flatten() 
    
    return np.sum(CpF*CoefsF*Area*NF)

def ForceR(Coefs, CpF, CpR, Area, NR): 
    CoefsR = Coefs[np.size(CpF):np.size(Coefs)].flatten()
    return np.sum(CpR*CoefsR*Area*NR)

def Fitness(Coefs, CpF, CpR, Area, NF, NR, knownF, knownR):
    return ((knownF-ForceF(Coefs, CpF, Area, NF))**2)+((knownR-ForceR(Coefs, CpF, CpR, Area, NR))**2)

def upperLim(ub):
    return 1.2

def lowerLim(lb):
    return -1.2

# Solution bounds
ub = np.full((1,np.size(coefs0)), 1.2).flatten() 
lb = np.full((1,np.size(coefs0)), -1.2).flatten()
bounds = Bounds(lb,ub)

boundaries = ((1.2,-1.2),)*(len(coefs0))

# minimise function
res = minimize(Fitness, coefs0, method='TNC', options={'accuracy' : 1e-5, 'xtol' : 1e-10,'ftol' : 1e-10, 'disp' : True}, args=(CpFront,CpRear,Area,normalFront,normalRear,CD_F,CD_R), bounds=bounds)

# genetic algorithm (differential evolution)
# res = differential_evolution(Fitness, bounds=boundaries, args=(CpFront,CpRear,Area,normalFront,normalRear,CD_F,CD_R), strategy='best1bin', maxiter=10, popsize=15, tol=0.5, mutation=(0.5,1),
#                             recombination= 0.7, disp=True)

# print result
print('ForceF= ', ForceF(res.x, CpFront, Area, normalFront), '  Difference=', CD_F-ForceF(res.x, CpFront, Area, normalFront))
print('ForceR= ', ForceR(res.x, CpFront, CpRear, Area, normalRear), '  Difference=', CD_R-ForceR(res.x, CpFront, CpRear, Area, normalRear))

# plots
x1 = np.linspace(0, np.size(CpFront), num=np.size(CpFront))
plt.subplot(221)
plt.plot(x1, CpFront*normalFront*coefs0[0:np.size(CpFront)].flatten() , '-', label='Ref', linewidth=2, color='r')
plt.plot(x1, CpFront*normalFront*res.x[0:np.size(CpFront)].flatten() , '-')
plt.xlabel("Point Number")
plt.ylabel("Cp")
plt.legend()

x2 = np.linspace(0, np.size(CpRear), num=np.size(CpRear))
plt.subplot(222)
plt.plot(x2, CpRear*normalRear*coefs0[0:np.size(CpRear)].flatten(), '-', label='Ref', linewidth=2, color='r')
plt.plot(x2, CpRear*normalRear*res.x[np.size(CpFront):np.size(coefs0)].flatten() , '-')
plt.xlabel("Point Number")
plt.ylabel("Cp")
plt.legend()

plt.subplot(212)
plt.plot(res.x, 'o', markersize=4, label='coefs')
plt.xlabel("Coefficient No.")
plt.ylabel("Scaling")
plt.show()

# saveData = np.savetxt("test.csv", res.x, delimiter=",")

