import numpy as np
import matplotlib.pyplot as plt

# Load the data in
cal_data = np.genfromtxt('balance_cal.csv', delimiter=',',skip_header=True)

# Extract the loads and the voltages
H = cal_data[:,:6]
R = cal_data[:,6:]

# Create the elongated R matrix
Rp = np.append(R,R*R,axis=1)
Rp = np.append(Rp,np.repeat(R[:,0][:,np.newaxis],5,axis=1)*R[:,1:],axis=1)
Rp = np.append(Rp,np.repeat(R[:,1][:,np.newaxis],4,axis=1)*R[:,2:],axis=1)
Rp = np.append(Rp,np.repeat(R[:,2][:,np.newaxis],3,axis=1)*R[:,3:],axis=1)
Rp = np.append(Rp,np.repeat(R[:,3][:,np.newaxis],2,axis=1)*R[:,4:],axis=1)
Rp = np.append(Rp,(R[:,4]*R[:,5])[:,np.newaxis],axis=1)

# Compute the coefficient matrix
H2 = np.matmul(H.transpose(),H)
H2inv = np.linalg.inv(H2)
Hinv = np.matmul(H2inv,H.transpose())
C = np.matmul(Hinv,R)

# Write out the coefficient matrix
np.savetxt("coef.csv", C, delimiter=",")

# Get the modelled loads
Hp = np.matmul(C,R.transpose()).transpose()

np.savetxt("H.csv", H, delimiter=",")
np.savetxt("Hp.csv", Hp, delimiter=",")

# Plot the results
spv = [321, 322, 323, 324, 325, 326]
ttv = ["Fx","Fy","Fz","Mx","My","Mz"]
for i, ind in enumerate(spv):
    plt.subplot(ind)
    plt.scatter(H[:12,i], Hp[:12,i])
    plt.title(ttv[i])
    plt.grid()
    plt.xlabel("Model")
    plt.ylabel("Original")
plt.tight_layout()
plt.show()
