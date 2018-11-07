import numpy as np
import matplotlib.pyplot as plt

# Load the data in
CpX_data = np.genfromtxt('CpX.csv', delimiter=',',skip_header=True)

# Split coordinate data with thresholds
Y = CpX_data[:,1] < 0.75225
# X = CpX_data[:,0]

# Z = CpX_data[:,2] > 0.289125
CpX = CpX_data[Y,0:4]

print(CpX)
# start with a y threshold

# yNew = CpX_data[Y,1]
# zNew = CpX_data[Z,1]

saveData = np.savetxt("check.csv", CpX, delimiter=",")