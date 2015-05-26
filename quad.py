import scipy
import numpy as np
from scipy import integrate

#parameter values and initial conditions
X=-400.
Y = 0.
Z = 44.
x = -400.
Bx = 0.
avgBx=0.
avgBy=0.
avgBz=0.
By = 0.
Bz = 0.
D = -1

#from random import randint
import random
#random.seed([23])
rr=random.uniform(0,10)
print(rr)

#define fringe field integrands
def bx(y,z):
    return (x-X)/pow((x-X)**2+(y-Y)**2+(z-Z)**2,1.5)
def by(y,z):
    return (y-Y)/pow((x-X)**2+(y-Y)**2+(z-Z)**2,1.5)
def bz(y,z):
    return (z-Z)/pow((x-X)**2+(y-Y)**2+(z-Z)**2,1.5)
    
for i in [1,2,3,4,5]: 
    while x <= 400.:  #integrate each x-slice (e.g. y-z plane)_
        Ix = integrate.nquad(bx, [[-5000., 5000.],[0., 24.]]) #2d numerical integration
        Bx += D*Ix[0]
        Iy = integrate.nquad(by, [[-5000., 5000.],[0., 24.]])
        By += D*Iy[0]
        Iz = integrate.nquad(bz, [[-5000., 5000.],[0., 24.]])
        Bz += D*Iz[0]
        #print(Bx, By, Bz, x)
        x+=80   #go to next slice/plane
        D =-1*D #sign of effective magnetic charge density alternates on each plane
    avgBx += Bx
    avgBy += By
    avgBz += Bz
    
print(-1000.*6*pow(10.,5.)*pow(10.,-7.)*Bx, -1000.*6*pow(10.,5.)*pow(10.,-7.)*By, -1000.*6*pow(10.,5.)*pow(10.,-7.)*Bz)
