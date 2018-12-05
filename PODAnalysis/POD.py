import numpy as np
import matplotlib.pyplot as plt

# Load the data in
v_data = np.genfromtxt('C:\\Users\\Hesham\\Desktop\\State 1.csv', delimiter=',',skip_header=True)

# Remove Zero Velocity at Model Surface
zeros = v_data[:,0] == 0
velocityData = v_data[~zeros,:] 

# u components
u_comp = velocityData[:,0]
# v components
v_comp = velocityData[:,1]
