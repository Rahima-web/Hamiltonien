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

# Sequence of actions 
A=np.zeros((T,1))
#print(A)
#print(A.shape)


""" QUESTION 1 : Implement the Bang Bang Controller """

## Bang Bang Controller

def BangBang_Controller():
    rho=1 # ro T-1
    RHO=[rho]
    A[0]=1 #a (T-1) =1
    for i in range (1,T):
        if r>= 1/rho:
            rho=(1+r) * rho
            RHO.append(rho)
            A[i]=0
        if r< 1/rho:
            rho = 1 + rho
            RHO.append(rho)
            A[i]=1
    RHO.reverse() # la dernière valeur de RO doit être 1, on reorganise donc la liste
    A[:] = A[::-1] # on reorganise aussi A 
    return RHO,A

print("\n")
print ("--------------- THE SEQUENCE OF ACTIONS a --------------------")
B=BangBang_Controller()
#print(b[0])
print(B[1])
print("\n")

## The cumulative reward 

def plant_equation(A):
    X_invest= [X_0]
    for i in range (1,T):
        X_invest.append( X_invest[i-1] + r*X_invest[i-1]*(1-A[i-1]))
    return X_invest


X = plant_equation(B[1])

print ("--------------- EVOLUTION OF THE INVESTED CAPITAL--------------------")
print("\n")
print(X)
    
time=[i for i in range(0,T)]

plt.plot(time,X,color = 'red')
plt.title('INVESTED CAPITAL EVOLUTION')
plt.ylabel('invested capital')
plt.xlabel('Time')
plt.show()


    
""" QUESTION 2 : Compute the corresponding total consumption and 
find the sequence of optimal actions.
"""

def consumption(A):
    X_consum=[0]
    S=0
    for i in range (1,T):
        X_consum.append(r*X[i-1]*A[i-1])
        S+=X_consum[i-1]
    return X_consum,S

print ("--------------- CONSUMPTION ARRAY--------------------")
print("\n")
C=consumption(B[1])
print(C[0])
print("\n")

# The total consumption
print ("--------------- TOTAL CONSUMPTION --------------------")
print("\n")
print(C[1])
print("\n")

#
#plt.plot(time,B[1])
#plt.show()
#plt.plot(time,C[0])
#plt.show()

##
#def optimize2(A):
#    S=consumption(A)[1]
#    return -S
#
#bnds=[(0,1) for i in range (0,T)]
#res2= minimize(optimize2,A,method='SLSQP',bounds=bnds)
#
#A2=res2.x
#A2[-1]=1
##print(A)
#X2=consumption(A2)[0]
#print(X2)
#plt.plot(time,X2)
#plt.show()
    
""" QUESTION 3 : Plot the consumption as a function of time
"""

print ("--------------- EVOLUTION OF CONSUMPTION --------------------")
print("\n")

plt.plot(time,C[0],color= 'green')
plt.title('CONSUMPTION EVOLUTION')
plt.ylabel('consumption')
plt.xlabel('Time')
plt.show()

#
#time=[i for i in range(0,T)]
#
#plt.plot(time,X2)
#plt.show()

""" QUESTION 4 : Plot the action sequence as a function of time.
"""

print ("--------------- EVOLUTION OF ACTIONS --------------------")
print("\n")
plt.plot(time,B[1],color = 'purple')
plt.title('PROPORTION (a) EVOLUTION')
plt.ylabel('proportion a')
plt.xlabel('Time')
plt.show()

gama = np.zeros((T,1))
rho= BangBang_Controller()[0]

def gamma():
    
    for i in range(1,T):
        gama[i-1] =  (1+r) * rho[i] + (1+r*rho[i])*A[i-1]
    
    return gama

Y1 = []
Y2 = []
for i in range (0,T):
    Y1.append (1+rho[i]) #a=1
 
for i in range (0,T):
    Y2.append ((1 + r)*rho[i]) #a=0
   
print ("--------------- CONSUME AND SAVE --------------------")
print("\n")
G = gamma()
plt.plot(rho,Y1,label = 'Y1',color = 'blue')
plt.plot(rho,Y2, label = 'Y2', color ='magenta')
#plt.plot(rho,G)
plt.legend()
plt.show()


#time=[i for i in range(0,T)]
#
#plt.plot(time,A2)
#plt.show()
#
#
#gama = np.zeros((T,1))
#rho,W= BangBang_Controller()
#
#def gamma():
#    
#    for i in range(1,T):
#        gama[i-1] =  (1+r) * rho[i] + (1+r*rho[i])*A1[i-1]
#    
#    return gama
#
#Y1 = []
#Y2 = []
#for i in range (0,T):
#    Y1.append (1+rho[i])
# 
#for i in range (0,T):
#    Y2.append ((1 + r)*rho[i])
#    
#G = gamma()
#plt.plot(rho,Y1)
#plt.plot(rho,Y2)
#plt.plot(rho,G)
#plt.legend()
#plt.show()
#


""" QUESTION 5 : Choose a couple of other strategies (controllers) to compare their respective total consumption to that obtained using the bang-bang approach.
"""




