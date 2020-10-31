#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 18:33:37 2020

@author: rahimamohamed
"""

"""
PROBLEM :
An investor has a fund. It has 1 million euros at time zero. 
It pays 5% interest per year for T=50 years. 
The investor cannot withdraw the invested money. 
But, (s)he consumes a proportion (at) of the interest at time t and 
reinvests the rest. 
What should the investor do to maximize the consumption before T?

"""

import numpy as np
import pandas as pd
from scipy.optimize import minimize
import matplotlib.pyplot as plt

" VARIABLE DECLARATION " 

# Interest rate
r = 0.05 

# Maturity
T = 50 

# fund at t=0
X_0 = 1000000 

# Invested Capital
X_invest = [] 

# Consumed Capital
X_consum = [] 

# Cumulative Reward
W = [] 

# Sequence of actions (50 values between 0 & 1)
A=np.arange(0,1,1/49)
print(A)
print(A.shape)

Ro = [] # Cumulative reward

""" QUESTION 1 : Implement the Bang Bang Controller """

### First, we implement the plant equation

def plant_equation():
    X_invest= [X_0]
    for i in range (1,T):
        X_invest.append( X_invest[i-1] + r*X_invest[i-1]*(1-A[i-1]))
    return X_invest

### Then, we implement the optimization of A
    
def optimize1(A):
    S=0
    X=plant_equation()
    for i in range(0,T):
        S+= r* X[i]* A[i]
    return -S

bnds=((0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),)

res= minimize(optimize1,A,method='SLSQP',bounds=bnds)

A1=res.x
A1[-1]=1
#print(A1)
X=plant_equation()
#print(X)

### Finaly, we implement the Bang Bang controller

def BangBang_Controller():
    ro=1 # ro T-1
    RO=[ro]
    for i in range (T,0,-1):
        if r>= 1/ro:
            ro=(1+r) * ro
            RO.append(ro)
        if r< 1/ro:
            ro = 1 + ro
            RO.append(ro)
    RO.reverse() # la dernière valeur de RO doit être 1, on reorganise donc la liste
    for i in range (0,T):
        W.append(r * X[i] * RO[i])
    return RO, W


#b=BangBang_Controller()
#print(b)

#x = BangBang_Controller()
#print(x)
    
""" QUESTION 2 : Compute the corresponding total consumption and 
find the sequence of optimal actions.
"""

def consumption(A):
    X_consum=[]
    S=0
    for i in range (1,T+1):
        X_consum.append(r*X[i-1]*A[i-1])
        S+=X_consum[i-1]
    return X_consum,S

c=consumption(A)
print(c[1])

def optimize2(A):
    S=consumption(A)[1]
    return -S

bnds=((0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),(0,1),)

res2= minimize(optimize2,A,method='SLSQP',bounds=bnds)

A2=res2.x
A2[-1]=1
#print(A)
X2=consumption(A2)[0]
print(X2)
    
""" QUESTION 3 : Plot the consumption as a function of time
"""

time=[i for i in range(0,T)]

plt.plot(time,X2)
plt.show()

""" QUESTION 4 : Plot the action sequence as a function of time.
"""


time=[i for i in range(0,T)]

plt.plot(time,A2)
plt.show()


""" QUESTION 5 : Choose a couple of other strategies (controllers) to compare their respective total consumption to that obtained using the bang-bang approach.
"""




