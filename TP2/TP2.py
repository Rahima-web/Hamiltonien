#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 14:13:01 2020

@author: rahimamohamed
"""

"""
GROUPE : Rahima Mohamed, Mahisha Uruthirasigamani, Danush Chandrarajah  

PROBLEM :
    
You need to sell a car. At every time t = 0, · · · , T − 1, you set a price pt
, and a customer then views the car. 
The probability that the customer buys a car at price p is D(p). 
If the car is not sold at time T, then it is sold for a fixed price WT , WT < 1.
Maximize the reward from selling the car and find the recursion for the optimal 
reward, when D(p) = (1 − p)+.
"""

import numpy as np
import matplotlib.pyplot as plt

" VARIABLE DECLARATION " 

# Maturity
T = 500 

# State
#X = [] 

# if the car is not sell until T

W_T = 0.998

# Cumulative Reward/Total consumption

W=np.zeros((T,1))

# Sequence of actions 
#A=np.zeros((T,1))

#Price matrix
P = np.zeros((T,1))

#The real price

P_R = 30000
time=[i for i in range(0,T)]
""" QUESTION 1 : Find the optimal strategy and the wealth 
i.e., the optimal expected cumulative reward) over time using 
the Bellman equation. 

"""

def Wealth():
    #W_T is fixed and W_0 is equal to zeros
    W[T-1]=W_T
    for i in range (T-1,0,-1):
        W[i-1]= ((1+W[i])/2.0)**2
    return W

W=Wealth()
def Price(W):
    P[T-1]=W_T
    for i in range (T-1,0,-1):
        P[i-1]= (1+W[i])/2.0    
    return P
P=Price(W)


""" QUESTION 2 : Plot the resulting optimal strategy and the wealth over time. """

plt.plot(time,W)
plt.title('EVOLUTION OF WEALTH')
plt.ylabel('W')
plt.xlabel('Time')
plt.show()

plt.plot(time,P)
plt.title('EVOLUTION OF PRICE')
plt.ylabel('P')
plt.xlabel('Time')
plt.show()

""" QUESTION 3 : Choose a couple of other strategies and see the corresponding revenues. """

def Wealth1(P):
    W=P**2
    return W

# 1st Strategy: P is constant
    
P1 = np.array([0.5 for i in range(0,T)])

W1=Wealth1(P1)

plt.plot(time,W1)
plt.title('EVOLUTION OF WEALTH')
plt.ylabel('W')
plt.xlabel('Time')
plt.show()

plt.plot(time,P1)
plt.title('EVOLUTION OF PRICE')
plt.ylabel('P')
plt.xlabel('Time')
plt.show()
    
