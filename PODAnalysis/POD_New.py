from __future__ import division
from __future__ import print_function
import numpy as np
import os
from glob import glob
from numpy import linalg as LA
import matplotlib.pyplot as plt
from pylab import *

folder = 'H:\\2d POD\\'
files = os.listdir(folder) # number of files

# velocity mean
mean = np.genfromtxt('H:\\2d POD\\Mean.csv',usecols=(0,1,2,3,4,5,6),skip_header=1,delimiter=',')
u_mean,v_mean = mean[:,1],mean[:,2]

# compose covariance matrix
# def stack(folder,files,u_mean,v_mean):#usecols,skip_header,skip_footer,u_mean,v_mean):
os.chdir(folder)
index=0
for vel_file in range(10):#range(len(files)):
        vel_file = folder+files[vel_file]
        print(vel_file)
        if index==0:
                # data=np.genfromtxt(vel_file,usecols=usecols,skip_header=skip_header,skip_footer=skip_footer)
                data=np.genfromtxt(vel_file,usecols=(0,1,2,3,4,5,6),skip_header=1,delimiter=',')
                x,y,u,v=data[:,4],data[:,5],data[:,1],data[:,2]
                u,v=u-u_mean,v-v_mean
                test = u-u_mean
                U=u
                V=v
                    
        else:
                data=np.genfromtxt(vel_file,usecols=(0,1,2,3,4,5,6),skip_header=1,delimiter=',')
                x,y,u,v=data[:,4],data[:,5],data[:,1],data[:,2]
                # x_i,y_i,x,y,u,v=data[:,0],data[:,1],data[:,2],data[:,3],data[:,4],data[:,5]
                u,v=u-u_mean,v-v_mean
                U=np.vstack((U,u))
                V=np.vstack((V,v))
    
        index+=1  

U=np.hstack((U,V))    
                
    
    # return(U,x_i,y_i,x,y)
    # return(U,x,y)

# eigen decomposition
# def eigen(U):
# C(X,X') = U_T * U - squares the matrix 'C' and correlates U&U U&V V&V
C=np.dot(U,np.transpose(U))

# Compute w=eigenvalues and e_v=eigenvectors 
w,e_v=LA.eig(C)

# Sort in eigenvalues in ascending order
indices=np.argsort(w)

# create a slice for reverse? make a copy??
w=w[indices[::-1]]
index=0

# rearrange eigenvector matrix 
for i in indices:
    if index==0:
            ev=e_v[:,i]
    else:
            ev=np.vstack((ev,e_v[:,i]))
        #print("ind=",i)
    index+=1    
ev=np.transpose(ev)   
ev=np.fliplr(ev)

# return w,ev

# def POD_modes(U,w,ev):
[A,B]=ev.shape

index=0
for b in range(B):
    P=0.0
    for an in range(A):
        # POD Coefficients 
        P+=U[an,:]*ev[an][b]
    if index==0:
        POD=P
    else:
        POD=np.vstack((POD,P))
    index+=1
        
    energy=np.transpose((w))

        # return (POD,energy)
            
# def reconstruction(POD,nmodes,ev,u_mean,v_mean,recon):
    
    #A=np.arange(0,nmodes,1)

aa=ev
[X,Y]=aa.shape
    
U_mean=np.hstack((u_mean,v_mean))
AR=np.arange(0,nmodes,1)
index=0
for m in range(L):
    r=np.zeros(M)
    for l in AR:
        P=POD[l,:]
        Q=np.multiply(P,aa[m][l])
        r=np.add(r,Q)
    if index==0:
        R=r
    else:
        R=np.vstack((R,r))
    index+=1

print("R shape", R.shape)

for r in range(R.shape[0]):
    U2=R[r,:]
    uc,vc=np.hsplit(U2,2)
    os.chdir(recon)
    filename="".join(["POD",str(r).rjust(4,"0"),".dat"])
    write2file=open(filename,"w")
    print("xi, yi, x, y, u, v",file=write2file)
    for i in range(len(uc)):
        print (x_i[i],"\t",y_i[i],"\t",x[i],"\t",y[i],"\t",uc[i],"\t",vc[i],file=write2file)